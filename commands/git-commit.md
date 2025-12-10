---
description: Analyze changes, organize into logical commits, and push
argument-hint: "[--no-push]"
---

Analyze all uncommitted changes, organize them into logical commits by feature/purpose, and push to remote.

## Instructions

1. Parse optional arguments from $ARGUMENTS:
   - `--no-push`: Skip pushing after commits

2. Get the current state:
   ```bash
   git status
   git diff --stat
   git diff --stat --staged
   ```

3. Analyze all changes (staged and unstaged) and group them by logical purpose:
   - Related file changes that form a single feature or fix
   - Configuration changes
   - Documentation updates
   - Refactoring
   - Test additions/modifications
   - Dependencies or build changes

4. For each logical group:
   a. Stage only the files belonging to that group:
      ```bash
      git add <file1> <file2> ...
      ```
   b. Create a commit with a descriptive message:
      - Use conventional commit format when appropriate (feat:, fix:, docs:, refactor:, test:, chore:)
      - Write clear, concise commit messages in imperative mood
      - Include body text if the change needs explanation
      ```bash
      git commit -m "type: subject" -m "body if needed"
      ```

5. If changes cannot be meaningfully separated (e.g., all files are part of one feature), create a single commit.

6. After all commits, push to remote (unless --no-push):
   ```bash
   git push
   ```
   If the branch has no upstream, use:
   ```bash
   git push -u origin $(git branch --show-current)
   ```

## Output

Report:
- Summary of how changes were organized
- Each commit created (hash and message)
- Push result or skip notice

## Example Groupings

- `feat: add user authentication` - new auth files, route changes
- `fix: resolve null pointer in parser` - single bug fix
- `docs: update API documentation` - markdown/doc changes only
- `chore: update dependencies` - package.json, lock files
- `refactor: extract validation logic` - code reorganization
- `test: add unit tests for auth module` - test files only
