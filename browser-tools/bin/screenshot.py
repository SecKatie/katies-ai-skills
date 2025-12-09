#!/usr/bin/env python3
"""Take a screenshot of the current viewport."""

import base64
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import pychrome


def get_browser():
    """Connect to Chrome DevTools."""
    try:
        browser = pychrome.Browser(url="http://127.0.0.1:9222")
        return browser
    except Exception as e:
        print(f"✗ Failed to connect to Chrome: {e}")
        print("  Make sure Chrome is running with --remote-debugging-port=9222")
        sys.exit(1)


def get_active_tab(browser):
    """Get the most recently active tab."""
    tabs = browser.list_tab()
    if not tabs:
        print("✗ No tabs found")
        sys.exit(1)
    return tabs[-1]


def main():
    browser = get_browser()
    tab = get_active_tab(browser)

    tab.start()
    try:
        tab.Page.enable()

        # Capture screenshot
        result = tab.Page.captureScreenshot(format="png")
        image_data = base64.b64decode(result["data"])

        # Save to temp file
        timestamp = datetime.now().isoformat().replace(":", "-").replace(".", "-")
        filename = f"screenshot-{timestamp}.png"
        filepath = Path(tempfile.gettempdir()) / filename

        filepath.write_bytes(image_data)
        print(filepath)

    finally:
        tab.stop()


if __name__ == "__main__":
    main()
