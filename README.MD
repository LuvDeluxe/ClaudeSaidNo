# ClaudeSaidNo 🟢🔴

Tiny macOS menu bar app that tells you **in real time** when Claude.ai peak hours are happening.

- **🟢 ClaudeSaidYes** = off-peak → go code heavy  
- **🔴 ClaudeSaidNo** = peak (weekdays 5–11 AM PT) → limits burn faster

Live countdown with seconds + your local time. No login. Zero bloat. Pure vibes.

---

### 1. Install Python (only do this once)

Open **Terminal** and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python

2. Quick Start (easiest way – Python script)

Download claude_said_no.py from this repo
Open Terminal and go to the folder where you saved it:

Bashcd ~/Desktop/claudesaidno     # ← change if you saved it somewhere else

Run these commands one by one:

Bashpython3 -m venv venv
source venv/bin/activate
pip install rumps pytz tzlocal
python claude_said_no.py
The app will appear instantly in your top menu bar (ClaudeSaidNo 🟢 or ClaudeSaidNo 🔴).

3. Make a normal double-click .app (recommended)
After you ran the commands above, build the app with:
Bashpip install py2app
python setup.py py2app
You will get dist/ClaudeSaidNo.app.
Drag it into your Applications folder and double-click it.

Features

Live countdown with seconds (updates every second)
Shows your local time + Pacific Time
Auto notifications when peak starts / ends
100% menu bar only (no Dock icon, no Alt+Tab)
Works in any timezone


Made with love (and a lot of patience) for the Claude community ❤️
Not affiliated with Anthropic or Claude.ai — just a fan tool.
Want to contribute or report a bug? Open an issue!
