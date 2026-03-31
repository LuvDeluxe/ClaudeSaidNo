"""
ClaudeSaidNo — macOS menu bar app
Tracks Claude.ai peak usage hours (Mon–Fri, 5AM–11AM PT)
"""

import rumps
import datetime
import pytz
import webbrowser
from tzlocal import get_localzone

# ── Configuration ────────────────────────────────────────────────────────────
PEAK_START_HOUR = 5
PEAK_END_HOUR = 11
PT_TZ = pytz.timezone("America/Los_Angeles")


class ClaudeSaidNo(rumps.App):
    def __init__(self):
        super().__init__("ClaudeSaidNo", quit_button=None)

        # Suppress the Python dock icon at runtime
        try:
            import AppKit
            AppKit.NSApp.setActivationPolicy_(
                AppKit.NSApplicationActivationPolicyAccessory
            )
        except Exception:
            pass

        # Optional icon (place claude_said_no_icon.png next to this script)
        try:
            self.icon = "claude_said_no_icon.png"
            self.template = True
        except Exception:
            pass

        # Menu items we update dynamically
        self.countdown_item = rumps.MenuItem("Calculating...")
        self.local_time_item = rumps.MenuItem("Your time: --:-- • PT: --:--")

        self.menu = [
            self.countdown_item,
            self.local_time_item,
            None,
            rumps.MenuItem("Open Claude.ai", callback=self.open_claude),
            rumps.MenuItem("Status Page", callback=self.open_status),
            None,
            rumps.MenuItem("Not official — just vibes ❤️"),
            rumps.MenuItem("Quit", callback=self.quit_app),
        ]

        self.local_tz = get_localzone()
        self.last_peak = None

        # 30s interval — minutes display, no seconds needed
        self._timer = rumps.Timer(self._tick, 30)
        self._timer.start()

    # ── Helpers ───────────────────────────────────────────────────────────────
    def _pt_now(self) -> datetime.datetime:
        return datetime.datetime.now(PT_TZ)

    def _is_weekend(self, pt: datetime.datetime) -> bool:
        return pt.weekday() >= 5

    def _is_peak(self, pt: datetime.datetime) -> bool:
        if self._is_weekend(pt):
            return False
        return PEAK_START_HOUR <= pt.hour < PEAK_END_HOUR

    @staticmethod
    def _fmt_delta(total_seconds: int) -> str:
        total_seconds = max(0, total_seconds)
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        if h > 0:
            return f"{h}h {m}m"
        return f"{m}m"

    def _countdown_text(self) -> str:
        now = self._pt_now()

        if self._is_weekend(now):
            days_until_monday = (7 - now.weekday()) % 7
            if days_until_monday == 0:
                days_until_monday = 7
            next_peak = (now + datetime.timedelta(days=days_until_monday)).replace(
                hour=PEAK_START_HOUR, minute=0, second=0, microsecond=0
            )
            delta = int((next_peak - now).total_seconds())
            return f"😎 Weekend — next peak in {self._fmt_delta(delta)}"

        if self._is_peak(now):
            peak_end = now.replace(hour=PEAK_END_HOUR, minute=0, second=0, microsecond=0)
            delta = int((peak_end - now).total_seconds())
            return f"🔴 Peak — ends in {self._fmt_delta(delta)}"

        # ── Off-peak on a weekday ─────────────────────────────────────
        if now.hour < PEAK_START_HOUR:
            # Early morning (Mon–Fri) → today at 5 AM
            next_peak = now.replace(
                hour=PEAK_START_HOUR, minute=0, second=0, microsecond=0
            )
        elif now.weekday() == 4:  # Friday after peak
            next_peak = (now + datetime.timedelta(days=3)).replace(
                hour=PEAK_START_HOUR, minute=0, second=0, microsecond=0
            )
        else:  # Monday–Thursday after peak
            next_peak = (now + datetime.timedelta(days=1)).replace(
                hour=PEAK_START_HOUR, minute=0, second=0, microsecond=0
            )

        delta = int((next_peak - now).total_seconds())
        return f"🟢 Off-peak — next peak in {self._fmt_delta(delta)}"

    # ── Timer tick ────────────────────────────────────────────────────────────
    def _tick(self, _sender):
        now_pt = self._pt_now()
        peak = self._is_peak(now_pt)

        if self._is_weekend(now_pt):
            self.title = "ClaudeSaidYes 🟢"
        elif peak:
            self.title = "ClaudeSaidNo 🔴"
        else:
            self.title = "ClaudeSaidYes 🟢"

        # Transition notifications
        if self.last_peak is not None and self.last_peak != peak:
            if peak:
                rumps.notification(
                    "ClaudeSaidNo",
                    "Peak hours started",
                    "Limits burn faster now — use tokens wisely.",
                    sound=True,
                )
            else:
                rumps.notification(
                    "ClaudeSaidYes",
                    "Peak hours ended",
                    "Green light — go wild! 🚀",
                    sound=True,
                )
        self.last_peak = peak

        self.countdown_item.title = self._countdown_text()

        local_str = datetime.datetime.now(self.local_tz).strftime("%H:%M")
        pt_str = now_pt.strftime("%H:%M")
        self.local_time_item.title = f"Your time: {local_str} • PT: {pt_str}"

    # ── Menu callbacks ────────────────────────────────────────────────────────
    def open_claude(self, _):
        webbrowser.open("https://claude.ai")

    def open_status(self, _):
        webbrowser.open("https://status.anthropic.com")

    def quit_app(self, _):
        rumps.quit_application()


if __name__ == "__main__":
    ClaudeSaidNo().run()
