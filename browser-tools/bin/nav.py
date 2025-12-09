#!/usr/bin/env python3
"""Navigate to a URL in the current or new tab."""

import argparse
import sys

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
    # Return the last tab (most recently created/active)
    return tabs[-1]


def navigate_tab(tab, url):
    """Navigate a tab to a URL."""
    tab.start()
    try:
        tab.Page.enable()
        tab.Page.navigate(url=url)
        # Wait for page to load
        tab.wait(5)
    finally:
        tab.stop()


def main():
    parser = argparse.ArgumentParser(description="Navigate to a URL")
    parser.add_argument("url", help="URL to navigate to")
    parser.add_argument(
        "--new", action="store_true", help="Open in new tab instead of current"
    )
    args = parser.parse_args()

    browser = get_browser()

    if args.new:
        tab = browser.new_tab()
        navigate_tab(tab, args.url)
        print(f"✓ Opened: {args.url}")
    else:
        tab = get_active_tab(browser)
        navigate_tab(tab, args.url)
        print(f"✓ Navigated to: {args.url}")


if __name__ == "__main__":
    main()
