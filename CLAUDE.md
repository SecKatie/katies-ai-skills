# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

KMTools is a [lola](https://github.com/mrbrandao/lola) module that provides portable AI skills for CLI tools and development workflows. Skills are written once and work across Claude Code, Cursor, Gemini CLI, and other AI assistants that lola supports.

## Architecture

### Module Structure

The project follows the lola module specification:

```
.lola/module.yml          # Module manifest defining skills and commands
<skill-name>/             # Each skill has its own directory
  SKILL.md                # Entry point with description, triggers, and documentation index
  docs/                   # Supporting documentation (optional)
  README.md               # Upstream tool documentation (optional)
commands/                 # Slash commands (prompts that expand when invoked)
  <command>.md            # Each command is a markdown file with frontmatter
```

### Multi-Platform Output

When `lola install kmtools` runs, it generates platform-specific files:
- `.claude/skills/kmtools-<skill>/` - Claude Code skills
- `.cursor/rules/kmtools-<skill>.mdc` - Cursor rules
- `.gemini/` - Gemini CLI integration
- `.lola/modules/kmtools/` - Local copy of installed module

### Skills vs Commands

- **Skills** (`SKILL.md`): Documentation bundles triggered by phrase matching. Each skill has a `description` field with trigger phrases. Skills teach the AI how to use specific tools (jj, gh, llm, etc.).
- **Commands** (`commands/*.md`): Executable prompts invoked with `/kmtools-<name>`. Commands have `description` and `argument-hint` frontmatter and contain step-by-step instructions.

## Available Skills

| Skill | Tool |
|-------|------|
| `llm` | Simon Willison's llm CLI |
| `parakeet` | NVIDIA Parakeet ASR for MLX |
| `yt-dlp` | Video/audio downloader |
| `just` | Command runner |
| `jj-vcs` | Jujutsu version control |
| `piper` | Neural TTS |
| `mermaid` | Diagram generation |
| `jira-cli` | Jira ticket management |
| `gh` | GitHub CLI |

## Adding New Skills

1. Create `<skill-name>/SKILL.md` with frontmatter:
   ```yaml
   ---
   name: skill-name
   description: Trigger phrase description...
   ---
   ```
2. Add skill name to `skills:` list in `.lola/module.yml`
3. Include documentation index pointing to relevant docs

## Adding New Commands

1. Create `commands/<command-name>.md` with frontmatter:
   ```yaml
   ---
   description: Brief command description
   argument-hint: "[--flag=value] <required>"
   ---
   ```
2. Add command name to `commands:` list in `.lola/module.yml`
3. Write instructions the AI should follow when executing the command

## Testing Changes

After modifying skills or commands, reinstall the module to regenerate platform files:
```bash
lola install kmtools -s project .
```
