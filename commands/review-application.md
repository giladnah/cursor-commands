# Review Application

Review an application for code quality, bugs, architecture issues, and best practices using the application review tool.

## Usage

Invoke this command with:
```
@review-application <app_path> [output_format]
```

Or simply:
```
@review-application
```
Then provide the application path when prompted.

**Important**: Run from repository root. The tool will resolve paths relative to the current working directory.

## Parameters

- **app_path** (required): Path to the application directory to review
  - Can be relative: `hailo_apps/python/gen_ai_apps/coffee_master`
  - Or absolute: `/full/path/to/application`

- **output_format** (optional): Output format for the review
  - `markdown` - Human-readable markdown report (default for command)
  - `json` - Machine-readable JSON output
  - `text` - Plain text output

## What This Command Does

1. **Runs the application review tool** (`tools/application_review.py`)
2. **Analyzes the application** for:
   - Code quality issues
   - Bugs and potential errors
   - Architecture problems
   - Testing coverage
   - Documentation completeness
   - Hailo dependency availability
3. **Generates a comprehensive report** with:
   - Issues categorized by severity (CRITICAL, HIGH, MEDIUM, LOW)
   - Specific file locations and line numbers
   - Recommendations for fixes
   - Code snippets showing problems

## Example Usage

### Review coffee_master application:
```
@review-application hailo_apps/python/gen_ai_apps/coffee_master markdown
```

### Review with JSON output:
```
@review-application hailo_apps/python/gen_ai_apps/coffee_master json
```

### Review current directory:
```
@review-application . markdown
```

## What Gets Checked

### Code Quality
- Import typos and incorrect module names
- Hardcoded absolute paths
- Error handling patterns (bare except clauses)
- Logging vs print statements
- Type hints coverage
- Docstring coverage

### Architecture
- Thread safety issues
- Configuration management
- Hailo library availability (CRITICAL if missing)
- Dependency management

### Testing
- Test directory existence
- Test file coverage
- Test organization

### Documentation
- README.md presence
- Code documentation completeness

## Output Format

### Markdown (Default)
Human-readable report with:
- Summary statistics
- Issues grouped by severity
- File locations and line numbers
- Recommendations
- Code snippets

### JSON
Machine-readable format suitable for:
- CI/CD integration
- Automated processing
- Tool integration

### Text
Plain text format for:
- Terminal output
- Log files
- Quick reviews

## Integration with Tools

This command uses the `tools/application_review.py` tool. The tool:
- Scans Python files in the application
- Performs static analysis
- Checks for Hailo dependencies (no mocking - reports setup issues)
- Generates structured reports

**Tool Path**: `tools/application_review.py` (relative to `.cursor/` directory)

**Direct Tool Usage** (from repository root):
```bash
python .cursor/tools/application_review.py <app_path> [output_format]
```

## Best Practices

1. **Review before major commits**: Run this before pushing significant changes
2. **Fix CRITICAL issues first**: Address critical issues immediately
3. **Use markdown for human review**: Best for reading and understanding issues
4. **Use JSON for automation**: Integrate into CI/CD pipelines
5. **Review regularly**: Catch issues early in development

## Troubleshooting

### Tool Not Found
If you get "tool not found" error:
- Ensure `tools/application_review.py` exists in `.cursor/commands/tools/`
- Check file permissions: `chmod +x .cursor/commands/tools/application_review.py`

### Import Errors
If the tool reports import errors:
- Ensure you're running from the repository root
- Check that Python path is set correctly
- Verify required Python packages are installed

### No Issues Found
If no issues are reported:
- Verify the application path is correct
- Check that Python files exist in the directory
- Ensure the tool can access the files

## Related Commands

- `@review-readme` - Review README files specifically
- Other review commands may be added in the future

## Notes

- The tool checks for actual Hailo library availability (no mocking)
- Missing Hailo libraries are reported as CRITICAL setup issues
- All file paths are relative to the repository root
- The tool respects `.gitignore` patterns

