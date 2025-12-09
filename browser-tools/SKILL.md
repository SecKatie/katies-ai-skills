---
name: browser-tools
description: Minimal CDP (Chrome DevTools Protocol) tools for browser automation, web scraping, and collaborative site exploration. Use this skill when you need to control Chrome programmatically, execute JavaScript in page context, take screenshots, pick DOM elements interactively, or extract cookies. Much lighter weight than full MCP servers (only ~225 tokens vs 13-18k), these Python CLI tools are composable via Bash and can be easily extended. Perfect for web scraping, frontend development, and automated testing tasks.
---

# Browser Tools

Minimal CDP tools for collaborative site exploration and web scraping.

## Tool Overview

All tools are Python scripts in the `bin/` directory that communicate with Chrome via the Chrome DevTools Protocol on port 9222.

- **start.py** - Start Chrome with remote debugging enabled
- **nav.py** - Navigate to URLs in current or new tab
- **eval.py** - Execute JavaScript in the active page context
- **screenshot.py** - Capture viewport screenshots
- **pick.py** - Interactive element picker (click to select DOM elements)
- **cookies.py** - Extract all cookies including HTTP-only ones

## Quick Reference

**Note:** All examples below use shortened paths for readability. Always use the full virtualenv path:
```bash
/Users/katiemulliken/Documents/Projects/claude_playground/plugins/kmtools/skills/browser-tools/.venv/bin/python /Users/katiemulliken/Documents/Projects/claude_playground/plugins/kmtools/skills/browser-tools/bin/<script>.py
```

### Start Chrome

```bash
.venv/bin/python bin/start.py              # Fresh profile
.venv/bin/python bin/start.py --profile    # Copy your profile (cookies, logins)
```

Start Chrome on `:9222` with remote debugging. Use `--profile` to copy your default Chrome profile so you're logged in everywhere.

### Navigate

```bash
.venv/bin/python bin/nav.py https://example.com
.venv/bin/python bin/nav.py https://example.com --new
```

Navigate current tab or open new tab with `--new`.

### Evaluate JavaScript

```bash
.venv/bin/python bin/eval.py 'document.title'
.venv/bin/python bin/eval.py 'document.querySelectorAll("a").length'
.venv/bin/python bin/eval.py 'Array.from(document.querySelectorAll("a")).map(a => ({href: a.href, text: a.textContent.trim()}))'
```

Execute JavaScript in active tab (async context supported). Results are formatted as key-value pairs for easy parsing.

### Screenshot

```bash
.venv/bin/python bin/screenshot.py
```

Screenshot current viewport, returns temp file path. Use Claude's vision capabilities to analyze the screenshot.

### Pick Elements

```bash
.venv/bin/python bin/pick.py "Click the submit button"
```

Interactive element picker. Click to select, Cmd/Ctrl+Click for multi-select, Enter to finish, ESC to cancel. Returns element info including tag, id, class, text content, and parent hierarchy.

### Get Cookies

```bash
.venv/bin/python bin/cookies.py
.venv/bin/python bin/cookies.py --domain example.com
```

Extract all cookies from the browser, including HTTP-only cookies (which are not accessible via JavaScript). Optionally filter by domain.

## Installation

**IMPORTANT: Always use the virtual environment for these tools.**

```bash
# Create virtualenv (first time only)
python -m venv /Users/katiemulliken/Documents/Projects/claude_playground/plugins/kmtools/skills/browser-tools/.venv

# Install dependencies
/Users/katiemulliken/Documents/Projects/claude_playground/plugins/kmtools/skills/browser-tools/.venv/bin/pip install -r /Users/katiemulliken/Documents/Projects/claude_playground/plugins/kmtools/skills/browser-tools/requirements.txt
```

Requires:
- `pychrome` - Python interface to Chrome DevTools Protocol
- Chrome/Chromium browser installed

## Running Tools

**Always use the virtualenv Python to run these tools:**

```bash
/Users/katiemulliken/Documents/Projects/claude_playground/plugins/kmtools/skills/browser-tools/.venv/bin/python /Users/katiemulliken/Documents/Projects/claude_playground/plugins/kmtools/skills/browser-tools/bin/<script>.py [args]
```

Or set up an alias for convenience:
```bash
BTPY="/Users/katiemulliken/Documents/Projects/claude_playground/plugins/kmtools/skills/browser-tools/.venv/bin/python"
BTBIN="/Users/katiemulliken/Documents/Projects/claude_playground/plugins/kmtools/skills/browser-tools/bin"
$BTPY $BTBIN/start.py --profile
```

## Common Workflows

**Note:** Examples use relative paths for brevity. In practice, use full absolute paths with the virtualenv Python.

### Web Scraping Session

1. Start Chrome with your profile (logged in):
   ```bash
   .venv/bin/python bin/start.py --profile
   ```

2. Navigate to target site:
   ```bash
   .venv/bin/python bin/nav.py https://example.com
   ```

3. Explore DOM structure:
   ```bash
   .venv/bin/python bin/eval.py 'document.querySelectorAll("article").length'
   ```

4. Extract data:
   ```bash
   .venv/bin/python bin/eval.py 'Array.from(document.querySelectorAll("article h2")).map(h => h.textContent.trim())'
   ```

### Interactive Element Selection

1. Start Chrome and navigate to page
2. Use picker to identify elements:
   ```bash
   .venv/bin/python bin/pick.py "Select the login form fields"
   ```
3. Click on elements (Cmd/Ctrl+click for multiple)
4. Press Enter to get element details
5. Use the returned selectors in your scraping code

### Frontend Development Testing

1. Start Chrome fresh:
   ```bash
   .venv/bin/python bin/start.py
   ```

2. Navigate to local dev server:
   ```bash
   .venv/bin/python bin/nav.py http://localhost:3000
   ```

3. Take screenshot for visual inspection:
   ```bash
   .venv/bin/python bin/screenshot.py
   ```

4. Test JavaScript interactions:
   ```bash
   .venv/bin/python bin/eval.py 'document.querySelector("button").click()'
   ```

## Key Benefits Over MCP Servers

- **Token Efficient**: ~225 tokens for all tools vs 13-18k for MCP servers
- **Composable**: Chain commands in Bash, save outputs to files
- **Extensible**: Easy to add new tools or modify existing ones
- **Simple**: Each tool is a standalone Python script
- **Flexible Output**: Customize output format for your needs

## Platform Notes

Scripts are configured for macOS with Chrome at the default location:
`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`

For Linux, Chrome is typically at `/usr/bin/google-chrome` or `/usr/bin/chromium-browser`.

Adjust the `CHROME_PATH` in `start.py` for your platform.
