#!/usr/bin/env python3
"""Interactive element picker for selecting DOM elements."""

import argparse
import sys

import pychrome

PICKER_JS = '''
(message) => {
    if (!window.pick) {
        window.pick = async (message) => {
            if (!message) {
                throw new Error("pick() requires a message parameter");
            }
            return new Promise((resolve) => {
                const selections = [];
                const selectedElements = new Set();

                const overlay = document.createElement("div");
                overlay.style.cssText =
                    "position:fixed;top:0;left:0;width:100%;height:100%;z-index:2147483647;pointer-events:none";

                const highlight = document.createElement("div");
                highlight.style.cssText =
                    "position:absolute;border:2px solid #3b82f6;background:rgba(59,130,246,0.1);transition:all 0.1s";
                overlay.appendChild(highlight);

                const banner = document.createElement("div");
                banner.style.cssText =
                    "position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#1f2937;color:white;padding:12px 24px;border-radius:8px;font:14px sans-serif;box-shadow:0 4px 12px rgba(0,0,0,0.3);pointer-events:auto;z-index:2147483647";

                const updateBanner = () => {
                    banner.textContent = `${message} (${selections.length} selected, Cmd/Ctrl+click to add, Enter to finish, ESC to cancel)`;
                };
                updateBanner();

                document.body.append(banner, overlay);

                const cleanup = () => {
                    document.removeEventListener("mousemove", onMove, true);
                    document.removeEventListener("click", onClick, true);
                    document.removeEventListener("keydown", onKey, true);
                    overlay.remove();
                    banner.remove();
                    selectedElements.forEach((el) => {
                        el.style.outline = "";
                    });
                };

                const onMove = (e) => {
                    const el = document.elementFromPoint(e.clientX, e.clientY);
                    if (!el || overlay.contains(el) || banner.contains(el)) return;
                    const r = el.getBoundingClientRect();
                    highlight.style.cssText = `position:absolute;border:2px solid #3b82f6;background:rgba(59,130,246,0.1);top:${r.top}px;left:${r.left}px;width:${r.width}px;height:${r.height}px`;
                };

                const buildElementInfo = (el) => {
                    const parents = [];
                    let current = el.parentElement;
                    while (current && current !== document.body) {
                        const parentInfo = current.tagName.toLowerCase();
                        const id = current.id ? `#${current.id}` : "";
                        const cls = current.className
                            ? `.${current.className.trim().split(/\\s+/).join(".")}`
                            : "";
                        parents.push(parentInfo + id + cls);
                        current = current.parentElement;
                    }

                    return {
                        tag: el.tagName.toLowerCase(),
                        id: el.id || null,
                        class: el.className || null,
                        text: el.textContent?.trim().slice(0, 200) || null,
                        html: el.outerHTML.slice(0, 500),
                        parents: parents.join(" > "),
                    };
                };

                const onClick = (e) => {
                    if (banner.contains(e.target)) return;
                    e.preventDefault();
                    e.stopPropagation();
                    const el = document.elementFromPoint(e.clientX, e.clientY);
                    if (!el || overlay.contains(el) || banner.contains(el)) return;

                    if (e.metaKey || e.ctrlKey) {
                        if (!selectedElements.has(el)) {
                            selectedElements.add(el);
                            el.style.outline = "3px solid #10b981";
                            selections.push(buildElementInfo(el));
                            updateBanner();
                        }
                    } else {
                        cleanup();
                        const info = buildElementInfo(el);
                        resolve(selections.length > 0 ? selections : info);
                    }
                };

                const onKey = (e) => {
                    if (e.key === "Escape") {
                        e.preventDefault();
                        cleanup();
                        resolve(null);
                    } else if (e.key === "Enter" && selections.length > 0) {
                        e.preventDefault();
                        cleanup();
                        resolve(selections);
                    }
                };

                document.addEventListener("mousemove", onMove, true);
                document.addEventListener("click", onClick, true);
                document.addEventListener("keydown", onKey, true);
            });
        };
    }
    return window.pick(message);
}
'''


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
    if result is None:
        print("✗ Selection cancelled")
        return

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
    parser = argparse.ArgumentParser(description="Interactive element picker")
    parser.add_argument("message", nargs="+", help="Message to display to user")
    args = parser.parse_args()

    message = " ".join(args.message)

    browser = get_browser()
    tab = get_active_tab(browser)

    tab.start()
    try:
        tab.Runtime.enable()

        # Call the picker function with the message
        code = f"({PICKER_JS})('{message}')"

        result = tab.Runtime.evaluate(
            expression=code,
            returnByValue=True,
            awaitPromise=True,
            userGesture=True,
        )

        if "exceptionDetails" in result:
            exception = result["exceptionDetails"]
            print(f"✗ Error: {exception.get('text', 'Unknown error')}")
            if "exception" in exception:
                print(f"  {exception['exception'].get('description', '')}")
            sys.exit(1)

        value = result.get("result", {}).get("value")
        format_result(value)

    finally:
        tab.stop()


if __name__ == "__main__":
    main()
