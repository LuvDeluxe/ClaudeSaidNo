from setuptools import setup

APP = ['claude_said_no.py']
DATA_FILES = ['claude_said_no_icon.png']
OPTIONS = {
    'argv_emulation': False,
    'plist': {
        'LSUIElement': True,  # hides dock icon, menu bar only
        'CFBundleName': 'ClaudeSaidNo',
        'CFBundleVersion': '1.0.0',
    },
    'packages': ['rumps', 'pytz', 'tzlocal'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
