# Cursor Commands & Tools Repository

This is a GitHub repository containing Cursor IDE commands and tools, shared across the team.

## Purpose

This repository contains:
- **Commands**: Reusable instructions and workflows that guide Cursor's AI assistant
- **Tools**: Executable scripts/programs that perform specific tasks

Commands can use tools to execute work, or tools can be run independently.

## Repository Structure

```
.cursor/                    # Git repository root
├── README.md              # This file
├── commands/              # Cursor commands directory
│   ├── review-readme.md
│   ├── review-application.md
│   └── ...
└── tools/                 # Executable tools directory
    ├── README.md
    └── application_review.py
```

**Note**: When cloned, this repository should be placed at `.cursor/` in your project, so Cursor can discover both `commands/` and `tools/` automatically.

## Prerequisites

- Git installed and configured
- Access to this GitHub repository
- Cursor IDE installed

## Quick Start

### First-Time Setup

1. **Navigate to your project's .cursor directory:**
   ```bash
   cd /path/to/your/project/.cursor
   ```

2. **Clone this repository:**
   ```bash
   git clone https://github.com/giladnah/cursor-commands.git .
   ```

   **Note:** The `.` at the end clones the repository contents directly into the `.cursor/` directory.

3. **Verify installation:**
   ```bash
   ls -la
   ```

   You should see:
   - `commands/` directory with command files (`.md` and `.sh` files)
   - `tools/` directory with executable tools
   - `README.md` (this file)

4. **Verify Cursor can see them:**
   - Commands should appear in Cursor's command palette
   - Tools are accessible at `.cursor/tools/` (Cursor's default location)

### Alternative Setup (If .cursor Directory Already Exists)

If the `.cursor/` directory already contains files:

1. **Backup existing files** (if needed):
   ```bash
   cd .cursor
   mkdir -p ../cursor-backup
   cp -r commands tools ../cursor-backup/ 2>/dev/null || true
   ```

2. **Remove existing commands/tools** (if they exist):
   ```bash
   cd .cursor
   rm -rf commands tools  # Remove if they exist
   ```

3. **Clone the repository:**
   ```bash
   git clone https://github.com/giladnah/cursor-commands.git .
   ```

## Usage

### How Cursor Uses Commands

Cursor IDE automatically detects commands in the `.cursor/commands/` directory. You can:

- **View commands**: Commands appear in Cursor's command palette
- **Run commands**: Execute commands directly from Cursor
- **Edit commands**: Modify commands locally (changes won't sync automatically)

### Command File Types

Commands can be:

- **`.md` files**: Markdown documentation/instructions that Cursor can read and execute
- **`.sh` files**: Executable shell scripts that can be run directly

### Available Commands

- **`review-readme.md`**: Review and validate README files
- **`review-application.md`**: Review applications for code quality (uses `tools/application_review.py`)

See individual command files for detailed usage instructions.

## Daily Workflow

### Updating Commands and Tools

To get the latest updates from the team:

```bash
cd .cursor
git pull
```

**When to update:**
- When a teammate adds a new command or tool
- When commands/tools are improved or fixed
- Periodically (e.g., weekly) to stay current

### Checking for Updates

Check if there are new updates available:

```bash
cd .cursor
git fetch
git status
```

This will show if your local copy is behind the remote repository.

## Contributing

To add or update commands and tools for the team:

1. **Navigate to the repository root:**
   ```bash
   cd .cursor
   ```

2. **Create or edit files:**
   - **Commands**: Add new `.md` or `.sh` files to `commands/` directory
   - **Tools**: Add executable scripts to `tools/` directory
   - Edit existing commands or tools

3. **Test your changes:**
   - Verify commands work in Cursor IDE
   - Test tools manually if applicable
   - Ensure paths are correct (commands reference `tools/` not `commands/tools/`)

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add new command/tool: description"
   git push
   ```

5. **Notify teammates:**
   - Let them know to run `git pull` to get the updates

## Directory Structure

```
.cursor/                    # Git repository root
├── README.md              # This file
├── commands/              # Cursor commands directory
│   ├── review-readme.md
│   ├── review-application.md
│   ├── review-readme.sh
│   └── ...                # Other command files
└── tools/                 # Executable tools directory
    ├── README.md          # Tools documentation
    └── application_review.py  # Application review tool
```

### Commands vs Tools

**Commands** (`.md` files):
- Instructions for Cursor AI
- Invoked with `@command-name`
- Guide AI behavior and workflows
- Examples: `review-readme.md`, `review-application.md`

**Tools** (`tools/` directory):
- Executable programs (Python, shell scripts)
- Can be called by commands or run directly
- Perform specific tasks programmatically
- Example: `tools/application_review.py`

**Relationship**: Commands can use tools to execute work.

## Troubleshooting

### Commands Not Appearing in Cursor

1. **Check directory location:**
   ```bash
   pwd
   # Should be: /path/to/repo/.cursor
   ```

2. **Verify files exist:**
   ```bash
   ls -la .cursor/commands/
   ls -la .cursor/tools/
   ```

3. **Restart Cursor IDE** - Sometimes Cursor needs a restart to detect new commands

4. **Check file permissions:**
   ```bash
   chmod +x .cursor/commands/*.sh  # Make scripts executable if needed
   chmod +x .cursor/tools/*.py  # Make Python tools executable if needed
   ```

### Git Pull Fails

**Error: "Your local changes would be overwritten"**

This happens if you've modified commands locally. Options:

1. **Stash your changes:**
   ```bash
   git stash
   git pull
   git stash pop  # Reapply your changes if needed
   ```

2. **Commit your changes first:**
   ```bash
   git add .
   git commit -m "Local changes"
   git pull
   ```

3. **Discard local changes** (if you don't need them):
   ```bash
   git reset --hard
   git pull
   ```

### Repository Not Found

**Error: "Repository not found" or "Permission denied"**

- Verify you have access to the commands repository
- Check that the repository URL is correct
- Ensure your SSH keys or credentials are configured for GitHub

### Wrong Directory

If you accidentally cloned to the wrong location:

1. **Remove the incorrect clone:**
   ```bash
   rm -rf /wrong/path/commands-repo
   ```

2. **Clone to the correct location:**
   ```bash
   cd .cursor
   git clone https://github.com/giladnah/cursor-commands.git .
   ```

## Best Practices

1. **Regular Updates**: Pull updates regularly to stay in sync with the team
2. **Test Before Pushing**: Always test commands before pushing to the shared repo
3. **Clear Naming**: Use descriptive names for command files (e.g., `review-readme.md` not `cmd1.md`)
4. **Documentation**: Include clear instructions in command files
5. **Version Control**: Use meaningful commit messages when contributing

## Manual Management

This setup uses **manual management** - you control when to update commands:

- **Pros**: Full control, no automatic changes, predictable behavior
- **Cons**: Requires remembering to pull updates

**Tip**: Set a reminder to pull updates weekly, or pull when a teammate announces new commands.

## Getting Help

If you encounter issues:

1. Check this README's troubleshooting section
2. Verify your git configuration: `git config --list`
3. Check repository access: Try cloning the repo in a different location
4. Ask teammates for the correct repository URL and access permissions

## Notes

- The `.cursor/` directory is gitignored in the main project repository
- This entire repository is cloned into `.cursor/` in your project
- Each developer maintains their own copy of this repository
- Commands and tools are shared via this GitHub repository
- Local modifications won't affect others unless you push them
- Tools can be used independently or called by commands
- See `tools/README.md` for detailed tool documentation

### Path References

**Commands reference tools using relative paths:**
- From commands: `tools/application_review.py` (not `commands/tools/...`)
- Tools are at: `.cursor/tools/` (Cursor's default location)
- Commands are at: `.cursor/commands/` (Cursor's default location)

**Both directories are at the same level**, making path references simple and intuitive.








