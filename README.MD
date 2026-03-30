# ClaudeSaidNo 🟢🔴

A tiny macOS menu bar app that tells you **in real time** when Claude.ai peak hours are happening.



- **🟢 ClaudeSaidYes** = Off-peak → Go code heavy.
- **🔴 ClaudeSaidNo** = Peak (Weekdays 5–11 AM PT) → Limits burn faster.

## 🚀 Installation

1. **Prerequisites:** Ensure you have Python installed (`brew install python`).
2. **Clone/Download:** Grab `claude_said_no.py`.
3. **Run:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install rumps pytz tzlocal
   python claude_said_no.py

# Features

1. ** Live Countdown: See exactly when peak hours end/start down to the second.

2. ** Zero Bloat: Lightweight Python script using rumps.

3. ** RAutomatic Timezones: Handles the PT to Local conversion for you.
