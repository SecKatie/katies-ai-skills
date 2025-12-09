# KMTools

A [lola](https://github.com/mrbrandao/lola) module providing portable AI skills for CLI tools and development workflows.

Write your AI context once, use it everywhere—these skills work with Claude Code, Cursor, Gemini CLI, and any other AI assistant that lola supports.

## Installation

```bash
# Add the module to your registry
lola mod add https://github.com/seckatie/kmtools.git

# Install to all assistants (user scope)
lola install kmtools

# Or install to a specific project
lola install kmtools -s project ./my-project
```

## Skills

| Skill | Description |
|-------|-------------|
| **llm** | Simon Willison's llm CLI for running prompts, embeddings, and structured data extraction across dozens of models |
| **parakeet** | Audio transcription using NVIDIA's Parakeet ASR model optimized for Apple MLX |
| **yt-dlp** | Download audio/video from thousands of websites with format selection and post-processing |
| **just** | Command runner for project-specific tasks with recipes, .env loading, and cross-platform support |
| **jj-vcs** | Jujutsu version control—Git-compatible with automatic rebasing and first-class conflict tracking |
| **piper** | Local neural text-to-speech with natural sounding voices |
| **mermaid** | Generate diagrams from code using mermaid-cli (20+ diagram types) |
| **jira-cli** | Non-interactive Jira ticket management from the command line |
| **browser-tools** | Minimal CDP tools for browser automation and web scraping |
| **gh** | GitHub CLI for rulesets, releases, PRs, issues, and repository management |

## Usage

Once installed, your AI assistant will automatically load these skills when working on relevant tasks. Each skill includes documentation, usage patterns, and best practices for its respective tool.

## License

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
