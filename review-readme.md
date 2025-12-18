# Review and Validate README Files

Review README files to ensure they follow best practices, contain functional code examples, and are aligned with the actual codebase.

## Instructions

When reviewing a README file:

1. **Read the README and the actual code** - Compare documentation with implementation
2. **Check all code snippets** - Ensure they are functional and complete
3. **Validate imports and function signatures** - Match against actual code
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
- [ ] **Function signatures instead of broken snippets** - For component sections, show function signatures with parameters rather than incomplete code
- [ ] **Unified working examples** - Create complete, functional examples that show components working together
- [ ] All imports are present and correct at the top of each example
- [ ] All variables are defined before use (no undefined variables like `instance`, `obj`, `data` without initialization)
- [ ] Examples demonstrate real-world usage patterns from actual codebase

### 3. Code Validation
- [ ] All imports can be resolved (check against `__init__.py`, `package.json`, `Cargo.toml`, or equivalent)
- [ ] Function signatures match actual implementations (read the source files)
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
# GOOD: Function signature (for component sections)
- `process(data: str, options: dict = None) -> Result` - Process data with optional configuration

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

## Review Process

1. **Read the README** - Understand structure and content
2. **Read the actual source files** - Check implementation files mentioned in the README
3. **Check code alignment** - Compare documentation with implementation
   - Verify function signatures match
   - Check that imports are correct
   - Ensure parameter names match
   - Verify return types are accurate
4. **Validate imports** - Check package/module structure for exported functions
5. **Test code snippets** - Verify they're syntactically correct and complete
   - Check syntax with language linter/compiler
   - Ensure all variables are defined
   - Verify imports can be resolved
6. **Compare with standards** - Check similar READMEs in the repository for consistency
7. **Run functional tests** - Execute commands and code snippets (see Functional Testing section)
8. **Fix issues** - Update README following the patterns above

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

## Key Principles

- **Functional over decorative** - Code examples must work, not just look good
- **Complete over partial** - Show full workflows, not isolated calls
- **Realistic over contrived** - Use patterns from actual codebase
- **Copy-paste ready** - Examples should run with proper setup
- **Document usage, not just API** - Show "how" not just "what"
- **Match the codebase** - Follow existing patterns and conventions

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
# Component section - Function signature
**Key Functions:**
- `process(data: str, config: dict) -> Result` - Process data with configuration

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
- Include type hints in function signatures
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
- Show both API reference (function signatures) and usage examples (complete code)
- Consider the target audience - beginners need more context, experts need concise examples
