

## Lola Skills

These skills are installed by Lola and provide specialized capabilities.
When a task matches a skill's description, read the skill's SKILL.md file
to learn the detailed instructions and workflows.

**How to use skills:**
1. Check if your task matches any skill description below
2. Use `read_file` to read the skill's SKILL.md for detailed instructions
3. Follow the instructions in the SKILL.md file

<!-- lola:skills:start -->

### kmtools

#### llm
**When to use:** Access and interact with Large Language Models from the command line using Simon Willison's llm CLI tool. Supports OpenAI, Anthropic, Gemini, Llama, and dozens of other models via plugins. Features include chat sessions, embeddings, structured data extraction with schemas, prompt templates, conversation logging, and tool use. This skill is triggered when the user says things like "run a prompt with llm", "use the llm command", "call an LLM from the command line", "set up llm API keys", "install llm plugins", "create embeddings", or "extract structured data from text".
**Instructions:** Read `.lola/modules/kmtools/llm/SKILL.md` for detailed guidance.

#### parakeet
**When to use:** Convert audio files to text using parakeet-mlx, NVIDIA's Parakeet automatic speech recognition model optimized for Apple's MLX framework. Run via uvx for on-device speech-to-text processing with high-quality timestamped transcriptions. Ideal for podcasts, interviews, meetings, and other audio content. This skill is triggered when the user says things like "transcribe this audio", "convert audio to text", "transcribe this podcast", "get text from this recording", "speech to text", or "transcribe this wav/mp3/m4a file".
**Instructions:** Read `.lola/modules/kmtools/parakeet/SKILL.md` for detailed guidance.

#### yt-dlp
**When to use:** Download audio and video from thousands of websites using yt-dlp. Feature-rich command-line tool supporting format selection, subtitle extraction, playlist handling, metadata embedding, and post-processing. This skill is triggered when the user says things like "download this video", "download from YouTube", "extract audio from video", "download this playlist", "get the mp3 from this video", "download subtitles", or "save this video locally".
**Instructions:** Read `.lola/modules/kmtools/yt-dlp/SKILL.md` for detailed guidance.

#### just
**When to use:** just is a handy command runner for saving and running project-specific commands. Features include recipe parameters, .env file loading, shell completion, cross-platform support, and recipes in arbitrary languages. This skill is triggered when the user says things like "create a justfile", "write a just recipe", "run just commands", "set up project automation with just", "understand justfile syntax", or "add a task to the justfile".
**Instructions:** Read `.lola/modules/kmtools/just/SKILL.md` for detailed guidance.

#### jj-vcs
**When to use:** Jujutsu (jj) is a powerful Git-compatible version control system with innovative features like automatic rebasing, working-copy-as-a-commit, operation log with undo, and first-class conflict tracking. This skill is triggered when the user says things like "use jj", "run jj commands", "jujutsu version control", "migrate from git to jj", "jj rebase", "jj squash", "jj log", or "help with jj workflow".
**Instructions:** Read `.lola/modules/kmtools/jj-vcs/SKILL.md` for detailed guidance.

#### piper
**When to use:** Convert text to speech using Piper, a fast, local, neural text-to-speech system with natural sounding voices. This skill is triggered when the user says things like "convert text to speech", "text to audio", "read this aloud", "create audio from text", "generate speech from text", "make an audio file from this text", or "use piper TTS".
**Instructions:** Read `.lola/modules/kmtools/piper/SKILL.md` for detailed guidance.

#### mermaid
**When to use:** Generate diagrams and flowcharts from mermaid definitions using the mermaid-cli (mmdc). Supports themes, custom CSS, and various output formats including SVG, PNG, and PDF. Mermaid supports 20+ diagram types including flowcharts, sequence diagrams, class diagrams, state diagrams, entity relationship diagrams, user journeys, Gantt charts, pie charts, quadrant charts, requirement diagrams, GitGraph, C4 diagrams, mindmaps, timelines, ZenUML, Sankey diagrams, XY charts, block diagrams, packet diagrams, Kanban boards, architecture diagrams, radar charts, and treemaps. This skill is triggered when the user says things like "create a diagram", "make a flowchart", "generate a sequence diagram", "create a mermaid chart", "visualize this as a diagram", "render mermaid code", or "create an architecture diagram".
**Instructions:** Read `.lola/modules/kmtools/mermaid/SKILL.md` for detailed guidance.

#### jira-cli
**When to use:** Manage Jira tickets from the command line using jira-cli. Contains essential setup instructions, non-interactive command patterns with required flags (--plain, --raw, etc.), authentication troubleshooting, and comprehensive command reference. This skill is triggered when the user says things like "create a Jira ticket", "list my Jira issues", "update Jira issue", "move Jira ticket to done", "log time in Jira", "add comment to Jira", or "search Jira issues". IMPORTANT - Read this skill before running any jira-cli commands to avoid blocking in interactive mode.
**Instructions:** Read `.lola/modules/kmtools/jira-cli/SKILL.md` for detailed guidance.

#### gh
**When to use:** GitHub CLI (gh) for repository management, rulesets, releases, PRs, and issues. This skill is triggered when the user says things like "create a GitHub PR", "list GitHub issues", "set up branch protection", "create a ruleset", "configure GitHub rulesets", "create a GitHub release", "clone this repo", or "manage GitHub repository settings".
**Instructions:** Read `.lola/modules/kmtools/gh/SKILL.md` for detailed guidance.

<!-- lola:skills:end -->
