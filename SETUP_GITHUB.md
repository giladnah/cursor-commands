# Setting Up GitHub Repository

Follow these steps to create the GitHub repository and push your commands:

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **"+"** icon in the top right, then select **"New repository"**
3. Fill in the repository details:
   - **Repository name**: `cursor-commands` (or your preferred name)
   - **Description**: "Shared Cursor IDE commands for the team"
   - **Visibility**: Choose **Private** (recommended) or **Public**
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
4. Click **"Create repository"**

## Step 2: Add Remote and Push

After creating the repository, GitHub will show you commands. Use these:

```bash
cd .cursor/commands

# Add the remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/cursor-commands.git

# Or if using SSH:
git remote add origin git@github.com:YOUR_USERNAME/cursor-commands.git

# Push to GitHub
git push -u origin main
```

## Step 3: Verify

1. Go to your GitHub repository page
2. You should see:
   - README.md
   - review-readme.md
   - review-readme.sh
   - .gitignore

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
   cd .cursor/commands
   git clone https://github.com/YOUR_USERNAME/cursor-commands.git .
   ```

## Quick Reference

**Repository URL format:**
- HTTPS: `https://github.com/YOUR_USERNAME/cursor-commands.git`
- SSH: `git@github.com:YOUR_USERNAME/cursor-commands.git`

**Current status:**
- ✅ Git repository initialized
- ✅ Initial commit created
- ✅ Branch renamed to 'main'
- ⏳ Waiting for GitHub repo creation and push

