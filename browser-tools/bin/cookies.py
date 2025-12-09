#!/usr/bin/env python3
"""Extract all cookies from the browser, including HTTP-only cookies."""

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
    return tabs[-1]


def main():
    parser = argparse.ArgumentParser(description="Extract browser cookies")
    parser.add_argument(
        "--domain", help="Filter cookies by domain (partial match)", default=None
    )
    parser.add_argument(
        "--json", action="store_true", help="Output as JSON instead of key-value pairs"
    )
    args = parser.parse_args()

    browser = get_browser()
    tab = get_active_tab(browser)

    tab.start()
    try:
        tab.Network.enable()

        # Get all cookies using the Network domain (includes HTTP-only)
        result = tab.Network.getAllCookies()
        cookies = result.get("cookies", [])

        # Filter by domain if specified
        if args.domain:
            cookies = [c for c in cookies if args.domain in c.get("domain", "")]

        if not cookies:
            print("No cookies found")
            return

        if args.json:
            import json

            print(json.dumps(cookies, indent=2))
        else:
            for i, cookie in enumerate(cookies):
                if i > 0:
                    print()
                print(f"name: {cookie.get('name', '')}")
                print(f"value: {cookie.get('value', '')}")
                print(f"domain: {cookie.get('domain', '')}")
                print(f"path: {cookie.get('path', '/')}")
                print(f"httpOnly: {cookie.get('httpOnly', False)}")
                print(f"secure: {cookie.get('secure', False)}")
                if "expires" in cookie:
                    print(f"expires: {cookie.get('expires', '')}")

    finally:
        tab.stop()


if __name__ == "__main__":
    main()
