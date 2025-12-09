#!/usr/bin/env python3
"""Start Chrome with remote debugging enabled."""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

# Platform-specific Chrome paths
CHROME_PATHS = {
    "darwin": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "linux": "/usr/bin/google-chrome",
    "win32": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
}

CHROME_PATH = CHROME_PATHS.get(sys.platform, CHROME_PATHS["linux"])
CACHE_DIR = Path.home() / ".cache" / "scraping"
DEBUG_PORT = 9222


def kill_chrome():
    """Kill existing Chrome processes."""
    try:
        if sys.platform == "darwin":
            subprocess.run(["killall", "Google Chrome"], capture_output=True)
        elif sys.platform == "linux":
            subprocess.run(["pkill", "-f", "chrome"], capture_output=True)
        else:
            subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], capture_output=True)
    except Exception:
        pass


def sync_profile():
    """Sync default Chrome profile to cache directory."""
    if sys.platform == "darwin":
        source = Path.home() / "Library/Application Support/Google/Chrome"
    elif sys.platform == "linux":
        source = Path.home() / ".config/google-chrome"
    else:
        source = Path.home() / "AppData/Local/Google/Chrome/User Data"

    if not source.exists():
        print(f"✗ Chrome profile not found at {source}")
        sys.exit(1)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    print("Syncing Chrome profile (this may take a moment)...")
    subprocess.run(
        ["rsync", "-a", "--delete", f"{source}/", str(CACHE_DIR) + "/"],
        capture_output=True,
        check=True,
    )


def wait_for_chrome():
    """Wait for Chrome to be ready by checking the debug port."""
    import socket

    for _ in range(30):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(("localhost", DEBUG_PORT))
            sock.close()
            if result == 0:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


def main():
    parser = argparse.ArgumentParser(description="Start Chrome with remote debugging")
    parser.add_argument(
        "--profile",
        action="store_true",
        help="Copy your default Chrome profile (cookies, logins)",
    )
    args = parser.parse_args()

    # Kill existing Chrome
    kill_chrome()
    time.sleep(1)

    # Setup profile directory
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    if args.profile:
        sync_profile()

    # Start Chrome
    chrome_args = [
        CHROME_PATH,
        f"--remote-debugging-port={DEBUG_PORT}",
        f"--user-data-dir={CACHE_DIR}",
    ]

    subprocess.Popen(
        chrome_args,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )

    # Wait for Chrome to be ready
    if not wait_for_chrome():
        print("✗ Failed to connect to Chrome")
        sys.exit(1)

    profile_msg = " with your profile" if args.profile else ""
    print(f"✓ Chrome started on :{DEBUG_PORT}{profile_msg}")


if __name__ == "__main__":
    main()
