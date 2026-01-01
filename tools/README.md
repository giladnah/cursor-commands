# Cursor Tools

This directory contains **executable tools** (scripts/programs) that can be used by Cursor commands.

## Purpose

Tools are standalone executable programs that perform specific tasks. Commands can call these tools to execute work, or you can run them directly from the command line.

## Location

**Repository Structure:**
```
.cursor/                    # Git repository root
├── commands/              # Commands directory
└── tools/                 # This directory (Tools)
```

**When cloned**, this repository goes into `.cursor/` in your project, so:
- Commands are at: `.cursor/commands/` (Cursor's default location) ✅
- Tools are at: `.cursor/tools/` (Cursor's default location) ✅
- No symlinks needed! Both are at the correct locations automatically.

## Available Tools

### application_review.py

Application review tool for comprehensive code quality analysis.

**Direct Usage:**
```bash
# From project repository root:
python .cursor/tools/application_review.py <app_path> [output_format]
```

**Output formats:**
- `json` - Machine-readable JSON output (default)
- `markdown` - Markdown formatted report
- `text` - Plain text output

**Example:**
```bash
# Review coffee_master application
python .cursor/tools/application_review.py \
    hailo_apps/python/gen_ai_apps/coffee_master \
    markdown
```

**Features:**
- Code quality assessment
- Bug detection
- Architecture review
- Testing recommendations
- Documentation review
- Hailo dependency checking (no mocking - reports setup issues)

**What it checks:**
- Import typos and issues
- Hardcoded paths
- Error handling patterns
- Logging vs print statements
- Type hints coverage
- Docstring coverage
- Thread safety
- Configuration management
- Test coverage
- Hailo library availability

**Used by:**
- `@review-application` command

## Tool Requirements

Tools should be:
- **Self-contained**: Work independently
- **Well-documented**: Clear usage instructions
- **Consistent interface**: Predictable inputs/outputs
- **Error handling**: Graceful failures with clear messages

## Adding New Tools

1. **Create tool file** in `tools/` directory (this directory)
2. **Add documentation** to this README
3. **Create command** (optional) that uses the tool
4. **Test thoroughly** before committing
5. **Update README** with usage examples
6. **Symlink is automatic**: `.cursor/tools/` will point to this directory

## Notes

- Tools are executable scripts (Python, shell, etc.)
- Tools can be called by commands or run directly
- Tools should produce structured, parseable output
- All tools should include proper error handling
- Tools are version-controlled in the git repo alongside commands
- When repository is cloned to `.cursor/`, tools are automatically in the correct location
- Commands reference tools using relative paths: `tools/tool.py` (not `commands/tools/tool.py`)
