#!/usr/bin/env python3
"""Execute JavaScript in the active tab's page context."""

import argparse
import json
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


def format_result(result):
    """Format the result for output."""
    if isinstance(result, list):
        for i, item in enumerate(result):
            if i > 0:
                print()
            if isinstance(item, dict):
                for key, value in item.items():
                    print(f"{key}: {value}")
            else:
                print(item)
    elif isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)


def main():
    parser = argparse.ArgumentParser(description="Execute JavaScript in active tab")
    parser.add_argument("code", nargs="+", help="JavaScript code to execute")
    args = parser.parse_args()

    code = " ".join(args.code)

    browser = get_browser()
    tab = get_active_tab(browser)

    tab.start()
    try:
        tab.Runtime.enable()

        # Wrap the code in an async IIFE to support async operations
        wrapped_code = f"""
        (async () => {{
            const AsyncFunction = (async () => {{}}).constructor;
            return await new AsyncFunction(`return ({code})`)();
        }})()
        """

        result = tab.Runtime.evaluate(
            expression=wrapped_code,
            returnByValue=True,
            awaitPromise=True,
        )

        if "exceptionDetails" in result:
            exception = result["exceptionDetails"]
            print(f"✗ Error: {exception.get('text', 'Unknown error')}")
            if "exception" in exception:
                print(f"  {exception['exception'].get('description', '')}")
            sys.exit(1)

        value = result.get("result", {}).get("value")
        if value is not None:
            format_result(value)
        else:
            # Handle non-serializable results
            result_type = result.get("result", {}).get("type", "undefined")
            if result_type == "undefined":
                print("undefined")
            else:
                print(f"<{result_type}>")

    finally:
        tab.stop()


if __name__ == "__main__":
    main()
