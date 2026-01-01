# Setting Up GitHub Repository

Follow these steps to create the GitHub repository and push your commands:

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **"+"** icon in the top right, then select **"New repository"**
3. Fill in the repository details:
   - **Repository name**: `cursor-commands` (already exists at https://github.com/giladnah/cursor-commands)
   - **Description**: "Shared Cursor IDE commands and tools for the team"
   - **Visibility**: Choose **Private** (recommended) or **Public**
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
4. Click **"Create repository"**

## Step 2: Add Remote and Push

After creating the repository, GitHub will show you commands. Use these:

```bash
cd .cursor

# Add the remote
git remote add origin https://github.com/giladnah/cursor-commands.git

# Or if using SSH:
git remote add origin git@github.com:giladnah/cursor-commands.git

# Push to GitHub
git push -u origin main
```

## Step 3: Verify

1. Go to your GitHub repository page
2. You should see:
   - README.md
   - commands/ directory with command files
   - tools/ directory with application_review.py
   - .gitignore (if you have one)

## Step 4: Share with Team

1. **Add collaborators** (if private repo):
   - Go to repository Settings → Collaborators
   - Add team members

2. **Share the repository URL** with your team:
   ```
   https://github.com/YOUR_USERNAME/cursor-commands
   ```

3. **Team members should follow the README.md** instructions to clone:
   ```bash
   cd .cursor
   git clone https://github.com/giladnah/cursor-commands.git .
   ```

## Quick Reference

**Repository:**
- **Name**: `cursor-commands`
- **URL**: https://github.com/giladnah/cursor-commands
- **HTTPS Clone**: `https://github.com/giladnah/cursor-commands.git`
- **SSH Clone**: `git@github.com:giladnah/cursor-commands.git`

**Repository Structure:**
- Root: `.cursor/` (cloned into your project's `.cursor/` directory)
- Commands: `.cursor/commands/` (Cursor's default location)
- Tools: `.cursor/tools/` (Cursor's default location)

**Current status:**
- ✅ Repository structure: `.cursor/` as root with `commands/` and `tools/` as siblings
- ✅ Git repository initialized
- ✅ Initial commit created
- ✅ Branch renamed to 'main'
- ⏳ Waiting for GitHub repo creation and push








