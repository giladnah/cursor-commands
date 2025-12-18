# Cursor Commands

This directory contains Cursor IDE commands from an external GitHub repository. These commands are shared across the team and can be used directly in Cursor IDE.

## Purpose

Cursor commands are reusable instructions and workflows that can be invoked from Cursor IDE. This directory stores team-shared commands from an external GitHub repository, allowing everyone to access the same set of commands and keep them synchronized.

## Prerequisites

- Git installed and configured
- Access to the Cursor commands GitHub repository
- Cursor IDE installed

## Quick Start

### First-Time Setup

1. **Navigate to the commands directory:**
   ```bash
   cd .cursor/commands
   ```

2. **Clone the external commands repository:**
   ```bash
   git clone <your-commands-repo-url> .
   ```

   **Note:** The `.` at the end clones the repository contents directly into the `.cursor/commands/` directory.

3. **Verify installation:**
   ```bash
   ls -la
   ```

   You should see the command files (`.md` and `.sh` files) from the repository.

### Alternative Setup (If Directory Already Exists)

If the `.cursor/commands/` directory already contains files:

1. **Backup existing files** (if needed):
   ```bash
   cd .cursor/commands
   mkdir -p ../commands-backup
   cp -r * ../commands-backup/
   ```

2. **Remove existing files:**
   ```bash
   rm -rf * .[^.]*  # Remove all files including hidden ones (but keep . and ..)
   ```

3. **Clone the repository:**
   ```bash
   git clone <your-commands-repo-url> .
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

## Daily Workflow

### Updating Commands

To get the latest commands from the team:

```bash
cd .cursor/commands
git pull
```

**When to update:**
- When a teammate adds a new command
- When commands are improved or fixed
- Periodically (e.g., weekly) to stay current

### Checking for Updates

Check if there are new commands available:

```bash
cd .cursor/commands
git fetch
git status
```

This will show if your local copy is behind the remote repository.

## Contributing New Commands

To add or update commands for the team:

1. **Navigate to the commands directory:**
   ```bash
   cd .cursor/commands
   ```

2. **Create or edit command files:**
   - Add new `.md` or `.sh` files
   - Edit existing commands

3. **Test your command:**
   - Verify it works in Cursor IDE
   - Test any scripts manually if applicable

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add new command: description"
   git push
   ```

5. **Notify teammates:**
   - Let them know to run `git pull` to get the new command

## Directory Structure

```
.cursor/commands/
├── README.md              # This file
├── command-name.md        # Markdown command files
├── script-name.sh         # Executable script commands
└── ...                    # Other command files
```

## Troubleshooting

### Commands Not Appearing in Cursor

1. **Check directory location:**
   ```bash
   pwd
   # Should be: /path/to/repo/.cursor/commands
   ```

2. **Verify files exist:**
   ```bash
   ls -la .cursor/commands/
   ```

3. **Restart Cursor IDE** - Sometimes Cursor needs a restart to detect new commands

4. **Check file permissions:**
   ```bash
   chmod +x .cursor/commands/*.sh  # Make scripts executable if needed
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
   cd .cursor/commands
   git clone <your-commands-repo-url> .
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

- The `.cursor/` directory is gitignored in the main repository, so this README and commands won't be committed to the main repo
- Each developer maintains their own copy of the commands repository
- Commands are shared via the external GitHub repository
- Local modifications to commands won't affect others unless you push them

