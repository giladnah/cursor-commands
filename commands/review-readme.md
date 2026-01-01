# Review and Validate README Files

Review README files to ensure they follow best practices, contain functional code examples, and are aligned with the actual codebase.

## Instructions

When reviewing a README file:

1. **Read the README and the actual code** - Compare documentation with implementation
2. **Check all code snippets** - Ensure they are functional and complete
3. **Validate imports and function signatures** - Match against actual code (use concise signatures)
4. **Fix issues** - Update README to follow best practices below

## Review Checklist

### 1. Structure and Formatting
- [ ] README has clear sections: Overview, Prerequisites, Features, Components, Usage Examples, API Reference
- [ ] Consistent formatting with other READMEs in the repository
- [ ] Proper markdown syntax and formatting
- [ ] Code blocks are properly formatted with language identifiers (`python`, `bash`, `javascript`, etc.)
- [ ] Headers follow logical hierarchy (## for main sections, ### for subsections)
- [ ] Links are valid and point to existing files/sections

### 2. Code Snippets Quality ⚠️ CRITICAL
- [ ] **NO isolated, non-functional snippets** - Remove code that uses undefined variables or incomplete examples
- [ ] **Function signatures instead of broken snippets** - For component sections, show concise function signatures with important parameters rather than incomplete code
- [ ] **Unified working examples** - Create complete, functional examples that show components working together
- [ ] All imports are present and correct at the top of each example
- [ ] All variables are defined before use (no undefined variables like `instance`, `obj`, `data` without initialization)
- [ ] Examples demonstrate real-world usage patterns from actual codebase

### 3. Code Validation
- [ ] All imports can be resolved (check against `__init__.py`, `package.json`, `Cargo.toml`, or equivalent)
- [ ] Function signatures match actual implementations (read the source files)
- [ ] **Function signatures are concise** - Show only important parameters and defaults, omit detailed type hints for readability
- [ ] Parameter names and defaults match the code
- [ ] Code examples follow patterns used in actual codebase
- [ ] Examples include proper error handling and resource cleanup (try/finally, close(), cleanup(), etc.)

### 4. Content Accuracy
- [ ] Documentation matches actual code implementation
- [ ] Function descriptions are accurate
- [ ] Return types and formats are documented correctly
- [ ] Features listed match what's actually implemented
- [ ] No references to non-existent functions, classes, or modules
- [ ] Version numbers and dependencies are accurate

### 5. Completeness
- [ ] Prerequisites section includes hardware, software, and dependency requirements
- [ ] Installation instructions are clear and complete (if applicable)
- [ ] All major components/modules are documented
- [ ] Usage examples cover common use cases
- [ ] Integration with other modules/packages is documented
- [ ] Links to related documentation are valid
- [ ] API Reference section points to docstrings or detailed documentation

### 6. Best Practices Applied
- [ ] Examples show complete workflows, not isolated function calls
- [ ] Resource cleanup is shown in examples (closing files, releasing resources, etc.)
- [ ] Examples are realistic and demonstrate actual usage patterns
- [ ] Code examples can be copied and run directly (with proper setup)
- [ ] Complex examples are broken down with comments explaining each step
- [ ] Examples use consistent naming conventions with the codebase
- [ ] **No duplicate examples** - Similar examples are consolidated with links to source of truth
- [ ] **Proper example hierarchy** - Detailed examples in component READMEs, quick examples + links in parent READMEs

## Common Issues and Fixes

### Issue: Non-functional code snippets
**Problem:** Code uses undefined variables or incomplete examples
```python
# BAD
obj = MyClass()  # Missing required parameters
result = obj.process(data)  # 'data' is undefined
```

**Solution:** Replace with function signatures or create unified working examples
```python
# GOOD: Function signature (for component sections) - concise, show only important parameters
- `process(data, options=None)` - Process data with optional configuration

# GOOD: Complete working example (for usage examples section)
from mypackage import MyClass

# Initialize with required parameters
obj = MyClass(config_path="config.json")

# Prepare data
data = load_data("input.txt")

# Process with proper error handling
try:
    result = obj.process(data)
    print(f"Result: {result}")
finally:
    obj.cleanup()
```

### Issue: Overly detailed function signatures
**Problem:** Function signatures include full type hints making them hard to read
```python
# BAD - Too verbose
- `process(data: str, options: Optional[Dict[str, Any]] = None, logger_instance: Optional[logging.Logger] = None) -> Result`
```

**Solution:** Use concise signatures showing only important parameters and defaults
```python
# GOOD - Concise and readable
- `process(data, options=None)` - Process data with optional configuration
- `is_context_full(llm, context_threshold=0.95)` - Check if context usage exceeds threshold
- `generate_and_stream_response(llm, prompt, temperature=0.1, max_tokens=200)` - Generate and stream response
```

**Guidelines for concise signatures:**
- Include parameter names and important defaults
- Omit detailed type hints (e.g., `Optional[Dict[str, Any]]` → just show the parameter)
- Omit return type annotations unless critical for understanding
- Omit optional logger/error handling parameters unless they're commonly used
- Focus on parameters users will actually set

### Issue: Missing imports
**Problem:** Code examples don't show all required imports
**Solution:** Add complete import statements at the top of each example:
- Standard library: `import os`, `from pathlib import Path`
- Third-party: `import requests`, `from flask import Flask`
- Local: `from mypackage.module import Class`

### Issue: Incomplete examples
**Problem:** Examples don't show resource cleanup or error handling
**Solution:** Always include proper cleanup:
```python
# Python
try:
    # ... main code ...
finally:
    resource.close()
    connection.cleanup()

# JavaScript/TypeScript
try {
    // ... main code ...
} finally {
    resource.close();
}

# Rust
{
    let resource = Resource::new()?;
    // ... main code ...
} // automatically dropped
```

### Issue: Documentation doesn't match code
**Problem:** Function signatures or descriptions don't match implementation
**Solution:**
1. Read the actual source files
2. Check function signatures using language-specific tools:
   - Python: `inspect.signature()` or reading the code
   - TypeScript: Check `.d.ts` files or source
   - Rust: Check function signatures in source
3. Update documentation to match actual code exactly

### Issue: Isolated snippets
**Problem:** Multiple small snippets that don't work together
**Solution:** Consolidate into unified examples showing components working together

### Issue: Missing context
**Problem:** Examples don't show where code fits in a larger application
**Solution:** Add comments explaining context and show how pieces fit together

### Issue: Duplicate examples across READMEs
**Problem:** Same code examples appear in multiple README files, making maintenance difficult
**Solution:** Consolidate duplicates into a single location and link from other READMEs

**Consolidation Strategy:**
1. **Identify duplicates** - Search for similar code examples across related READMEs
2. **Choose source of truth** - Keep the most detailed/complete example in the component-specific README
3. **Replace duplicates** - In parent/general READMEs, replace full examples with:
   - Quick-start snippets (minimal, functional examples)
   - Links to detailed examples in component-specific READMEs
4. **Maintain consistency** - Follow this hierarchy:
   - **Component-specific READMEs** (`module/README.md`) → Full detailed examples
   - **Parent module READMEs** (`parent/README.md`) → Quick examples + links
   - **Main README** (`README.md`) → Quick examples + links

**Example Consolidation:**

**Before (Duplicate):**
```python
# In gen_ai_apps/README.md
# Full 30-line VoiceInteractionManager example

# In gen_ai_utils/README.md
# Same full 30-line VoiceInteractionManager example

# In gen_ai_utils/voice_processing/README.md
# Same full 30-line VoiceInteractionManager example
```

**After (Consolidated):**
```python
# In gen_ai_apps/README.md - Quick example + link
For detailed examples, see: [Voice Processing Examples](gen_ai_utils/voice_processing/README.md#usage)

# Quick Start:
manager = VoiceInteractionManager(
    title="My App",
    on_audio_ready=lambda audio: print(f"Audio: {len(audio)} samples")
)
manager.run()

# In gen_ai_utils/README.md - Quick example + link
See: [Voice Processing Module Documentation](voice_processing/README.md#usage)

# In gen_ai_utils/voice_processing/README.md - Full detailed example (source of truth)
# Complete example with all callbacks, error handling, etc.
```

**Guidelines:**
- Keep detailed examples in component-specific READMEs (most specific location)
- Use quick-start snippets in parent READMEs for immediate reference
- Always include links to detailed examples
- Ensure quick-start examples are functional (can be copied and run)
- Document the consolidation in the review process

## Review Process

1. **Read the README** - Understand structure and content
2. **Read the actual source files** - Check implementation files mentioned in the README
3. **Check code alignment** - Compare documentation with implementation
   - Verify function signatures match (using concise format)
   - Check that imports are correct
   - Ensure parameter names match
   - Verify return types are accurate (documented in descriptions, not signatures)
4. **Identify duplicate examples** - Search for similar code examples across related READMEs
   - Check parent/child README relationships
   - Look for repeated patterns (same imports, same function calls)
   - Identify which location should be the source of truth
5. **Consolidate duplicates** - Apply consolidation strategy:
   - Keep detailed examples in component-specific READMEs
   - Replace duplicates in parent READMEs with quick examples + links
   - Ensure all links point to correct sections (use anchor links like `#usage`)
6. **Validate imports** - Check package/module structure for exported functions
7. **Test code snippets** - Verify they're syntactically correct and complete
   - Check syntax with language linter/compiler
   - Ensure all variables are defined
   - Verify imports can be resolved
8. **Compare with standards** - Check similar READMEs in the repository for consistency
9. **Run functional tests** - Execute commands and code snippets (see Functional Testing section)
10. **Fix issues** - Update README following the patterns above
11. **Code Verification Stage** - Verify all code snippets and generate verification report table (see Code Verification Stage section) ⚠️ FINAL STEP

## Validation Steps

After reviewing, validate:

1. **Check imports work:**
   ```bash
   # Python
   python3 -c "from package.module import function"

   # Node.js
   node -e "require('package')"

   # Rust
   cargo check
   ```

2. **Verify function signatures:**
   ```python
   # Python
   import inspect
   from package import module
   print(inspect.signature(module.function))
   ```

   ```typescript
   // TypeScript - check .d.ts files or source
   ```

3. **Check against actual usage:**
   - Look at example applications or tests in the codebase
   - Verify patterns match how code is actually used

4. **Ensure code snippets are complete:**
   - All imports present
   - All variables defined
   - Proper cleanup shown
   - Error handling included where appropriate

## Functional Testing ⚠️ REQUIRED

After validation, **test that everything actually works**:

### 1. Test Command-Line Commands

If the README contains commands for running applications or scripts:

- [ ] **Extract all command examples** from the README
- [ ] **Check for context instructions** (e.g., "run from project root", "requires virtual environment")
- [ ] **Follow context instructions** (change directory, activate environment, etc.)
- [ ] **Run each command** and verify it works:
  ```bash
  # Example: If README says "Run from project root"
  cd /path/to/project/root
  # Then run the command
  python3 -m myapp.main --help

  # Example: If README says "Requires virtual environment"
  source venv/bin/activate
  # Then run the command
  npm start
  ```
- [ ] **Verify expected output** matches what's documented
- [ ] **Check for error messages** - if command fails, document why and fix README

**Common command patterns to test:**
- `python3 -m package.module`
- `npm run <script>`
- `cargo run`
- `./script.sh`
- `docker run ...`
- Any custom CLI commands

### 2. Test Code Snippets

If the README contains code snippets:

- [ ] **Extract all code blocks** (Python, JavaScript, Rust, etc.)
- [ ] **Check for context instructions**:
  - "Run from project root"
  - "Requires imports from X"
  - "Needs configuration file Y"
  - "Set environment variable Z"
- [ ] **Follow context instructions** before running code
- [ ] **Create temporary test files** for each code snippet:
  ```python
  # For Python snippets
  # Create test_README_snippet.py with the code
  # Add necessary setup (imports, mock data, etc.)
  # Run: python3 test_README_snippet.py
  ```
- [ ] **Run each code snippet** and verify:
  - Code executes without errors
  - Expected behavior matches documentation
  - Output matches examples in README
- [ ] **Handle dependencies**:
  - Install required packages if needed
  - Set up mock data/files if referenced
  - Create minimal test environment
- [ ] **Clean up** temporary files after testing

**Testing approach:**
```bash
# Example workflow for Python snippet
# 1. Extract code block
# 2. Create test file
cat > /tmp/test_snippet.py << 'EOF'
# Paste code snippet here
EOF

# 3. Follow context instructions
cd /path/to/project/root  # if specified
source venv/bin/activate  # if specified

# 4. Run and verify
python3 /tmp/test_snippet.py

# 5. Clean up
rm /tmp/test_snippet.py
```

### 3. Test Installation Instructions

If the README contains installation steps:

- [ ] **Follow installation instructions** step by step
- [ ] **Verify each step completes** without errors
- [ ] **Test that installed components work** after installation
- [ ] **Document any issues** or missing steps

### 4. Test Integration Examples

If the README shows integration with other tools/modules:

- [ ] **Set up required dependencies**
- [ ] **Run integration examples**
- [ ] **Verify components work together** as documented

### 5. Handle Test Failures

If tests fail:

- [ ] **Document the failure** (what failed, error message)
- [ ] **Determine if it's a README issue** or environment issue
- [ ] **Fix README** if:
  - Missing prerequisites
  - Incorrect commands
  - Wrong code examples
  - Missing context instructions
- [ ] **Add missing context** if code needs specific setup
- [ ] **Update examples** to match actual behavior

### Testing Checklist

For each README:

- [ ] All command-line commands tested and working
- [ ] All code snippets tested and working
- [ ] Context instructions followed (directory, environment, etc.)
- [ ] Expected output matches documentation
- [ ] No errors or warnings (unless documented)
- [ ] Dependencies are documented and available
- [ ] Installation steps verified (if present)

### Example: Complete Testing Workflow

```bash
# 1. Read README and identify testable elements
README_FILE="path/to/README.md"

# 2. Extract commands
grep -E '^```bash|^```sh|^`[^`]+`' "$README_FILE" | grep -E 'python|npm|cargo|docker'

# 3. Extract code snippets
grep -A 50 '```python' "$README_FILE" | grep -B 50 '```'

# 4. Check for context instructions
grep -i "run from\|requires\|needs\|set\|export" "$README_FILE"

# 5. Follow context and test
# (Implementation depends on specific README)
```

### Notes on Testing

- **Safety first**: Don't run destructive commands (rm -rf, format, etc.) without verification
- **Use test environments**: Prefer test/development environments over production
- **Mock when needed**: Use mocks/stubs for external dependencies (APIs, databases)
- **Document assumptions**: Note any assumptions made during testing
- **Skip if impractical**: Some tests may require hardware/special setup - document limitations

## Code Verification Stage ⚠️ FINAL REQUIRED STEP

After completing all review steps, **verify all code snippets** and generate a verification report table.

### Verification Process

1. **Extract all code snippets** from the README:
   - Python code blocks (```python)
   - Bash/shell commands (```bash, ```sh)
   - JavaScript/TypeScript (```javascript, ```typescript)
   - Other language-specific blocks
   - Inline code examples

2. **For each snippet, perform verification:**
   - **Syntax check**: Verify code is syntactically correct
   - **Import validation**: Check all imports can be resolved
   - **Variable validation**: Ensure all variables are defined
   - **Function signature check**: Verify function calls match actual signatures
   - **Execution test**: If possible, run the code (with mocks/stubs for external dependencies)

3. **Generate verification table** showing results for each snippet

### Verification Table Format

After verification, output a table in this format:

| Snippet # | Location     | Type   | Description                     | Status    | Notes                                      |
| --------- | ------------ | ------ | ------------------------------- | --------- | ------------------------------------------ |
| 1         | Line 25-35   | Python | VoiceInteractionManager example | ✅ Pass    | All imports valid, syntax correct          |
| 2         | Line 45-50   | Bash   | Installation command            | ✅ Pass    | Command executes successfully              |
| 3         | Line 120-135 | Python | LLM streaming example           | ⚠️ Warning | Requires hardware, syntax valid            |
| 4         | Line 200-210 | Python | Context manager example         | ❌ Fail    | Missing import: `from pathlib import Path` |

**Status Values:**
- ✅ **Pass** - Code is valid, imports work, can be executed (or would execute with proper setup)
- ⚠️ **Warning** - Code is valid but requires special setup (hardware, environment, etc.) - document limitations
- ❌ **Fail** - Code has errors (syntax, missing imports, undefined variables, etc.) - must fix

### Verification Checklist

For each code snippet, verify:

- [ ] **Syntax is correct** - Code parses without syntax errors
- [ ] **Imports are valid** - All imports can be resolved (check against actual codebase)
- [ ] **Variables are defined** - No undefined variables (unless intentionally shown as incomplete)
- [ ] **Function signatures match** - Function calls match actual implementations
- [ ] **Code is executable** - Can be run (or would run with proper setup/mocks)
- [ ] **Context is clear** - Any required setup is documented
- [ ] **Dependencies are documented** - Required packages/modules are mentioned

### Language-Specific Verification

#### Python
```bash
# Syntax check
python3 -m py_compile snippet.py

# Import check
python3 -c "import ast; ast.parse(open('snippet.py').read())"
python3 -c "from package.module import function"  # Test each import

# Execution test (with mocks if needed)
python3 snippet.py
```

#### Bash/Shell
```bash
# Syntax check
bash -n script.sh

# Dry run (if safe)
bash -x script.sh  # With set -x for debugging
```

#### JavaScript/TypeScript
```bash
# Syntax check
node --check script.js
# or
tsc --noEmit script.ts
```

### Verification Report Template

After completing verification, include this report in your review:

```markdown
## Code Verification Report

**README File:** `path/to/README.md`
**Review Date:** YYYY-MM-DD
**Total Snippets:** X
**Passed:** Y | **Warnings:** Z | **Failed:** W

### Verification Results

| Snippet # | Location | Type | Description | Status | Notes |
| --------- | -------- | ---- | ----------- | ------ | ----- |
| ...       | ...      | ...  | ...         | ...    | ...   |

### Summary
- ✅ All critical snippets verified and passing
- ⚠️ X snippets require special setup (documented)
- ❌ Y snippets have errors (fixed in review)
```

### Automated Verification Script Example

```bash
#!/bin/bash
# verify_readme_snippets.sh

README_FILE="$1"
REPORT_FILE="verification_report.md"

echo "## Code Verification Report" > "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "**README File:** \`$README_FILE\`" >> "$REPORT_FILE"
echo "**Review Date:** $(date +%Y-%m-%d)" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "| Snippet # | Location | Type | Description | Status | Notes |" >> "$REPORT_FILE"
echo "|-----------|----------|------|-------------|--------|-------|" >> "$REPORT_FILE"

SNIPPET_NUM=1

# Extract Python snippets
grep -n '```python' "$README_FILE" | while read -r line; do
    LINE_NUM=$(echo "$line" | cut -d: -f1)
    # Extract snippet and test
    # ... verification logic ...
    echo "| $SNIPPET_NUM | Line $LINE_NUM | Python | ... | ✅ Pass | ... |" >> "$REPORT_FILE"
    SNIPPET_NUM=$((SNIPPET_NUM + 1))
done

# Similar for bash, javascript, etc.
```

### Important Notes

- **All snippets must be verified** - No snippet should be left untested
- **Fix failures immediately** - If a snippet fails verification, fix it before completing the review
- **Document warnings** - If a snippet requires special setup, document it in the Notes column
- **Include verification report** - Always include the verification table in your review output
- **Re-verify after fixes** - If you fix snippets, re-run verification to confirm they pass

## Key Principles

- **Functional over decorative** - Code examples must work, not just look good
- **Complete over partial** - Show full workflows, not isolated calls
- **Realistic over contrived** - Use patterns from actual codebase
- **Copy-paste ready** - Examples should run with proper setup
- **Document usage, not just API** - Show "how" not just "what"
- **Match the codebase** - Follow existing patterns and conventions
- **Concise signatures** - Function signatures should be readable, showing only important parameters and defaults

## Example Transformation

### Before (Bad)
```python
# Component section
from mypackage import Processor

processor = Processor()  # Missing required config
result = processor.process(data)  # 'data' undefined
```

### After (Good)
```python
# Component section - Concise function signature
**Key Functions:**
- `process(data, options=None)` - Process data with optional configuration

# Usage Examples section - Complete working example
from mypackage import Processor
from pathlib import Path

# Initialize with required configuration
config = {"mode": "standard", "output_dir": "results"}
processor = Processor(config)

# Prepare input data
data_path = Path("input.txt")
data = data_path.read_text()

# Process with error handling
try:
    result = processor.process(data)
    print(f"Processed: {result}")
finally:
    processor.cleanup()
```

## Language-Specific Considerations

### Python
- Show virtual environment setup if needed
- **Use concise function signatures** - Show parameter names and defaults, omit detailed type hints
- Show proper exception handling
- Include resource cleanup (context managers, try/finally)

### JavaScript/TypeScript
- Show package installation (`npm install` or `yarn add`)
- Include proper async/await patterns
- Show error handling with try/catch
- Include cleanup for resources (close connections, etc.)

### Rust
- Show `Cargo.toml` dependencies
- Include proper error handling (`Result`, `Option`)
- Show ownership and borrowing patterns
- Include resource cleanup (RAII is automatic, but show explicit cleanup if needed)

### Go
- Show module setup
- Include proper error handling
- Show resource cleanup (`defer` statements)
- Include context usage where appropriate

## Notes

- Always check actual source files, not just the README
- When in doubt, look at similar READMEs in the repo for patterns
- Test code examples when possible to ensure they work
- Prioritize functional examples over isolated snippets
- Show both API reference (concise function signatures) and usage examples (complete code)
- Consider the target audience - beginners need more context, experts need concise examples
- **Function signatures should be concise** - Focus on readability by showing only important parameters and defaults, not full type annotations
