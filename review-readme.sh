#!/bin/bash
# Cursor command script to review and validate README files
# Usage: review-readme.sh <path-to-readme.md>

set -e

README_PATH="${1:-}"
if [ -z "$README_PATH" ]; then
    echo "Usage: $0 <path-to-readme.md>"
    exit 1
fi

if [ ! -f "$README_PATH" ]; then
    echo "Error: README file not found: $README_PATH"
    exit 1
fi

echo "============================================================"
echo "README Review and Validation"
echo "============================================================"
echo "File: $README_PATH"
echo ""

# Check if Python code blocks exist
if grep -q '```python' "$README_PATH"; then
    echo "✓ Found Python code blocks"

    # Extract Python code blocks and validate syntax
    echo ""
    echo "Validating Python code syntax..."
    python3 << 'PYTHON_EOF'
import re
import sys
from pathlib import Path

readme_path = sys.argv[1]
with open(readme_path, 'r') as f:
    content = f.read()

# Extract Python code blocks
code_blocks = re.findall(r'```python\n(.*?)```', content, re.DOTALL)

if not code_blocks:
    print("  No Python code blocks found")
    sys.exit(0)

print(f"  Found {len(code_blocks)} Python code block(s)")

# Check for common issues
issues = []
for i, block in enumerate(code_blocks, 1):
    lines = block.split('\n')

    # Check for undefined variables (common patterns)
    if any('llm_instance' in line or 'vdevice_instance' in line for line in lines):
        if not any('llm =' in line or 'vdevice =' in line for line in lines):
            issues.append(f"  Block {i}: Uses undefined variables (llm_instance/vdevice_instance)")

    # Check for missing imports
    if any('from hailo' in line for line in lines) and not any('import' in line for line in lines[:5]):
        issues.append(f"  Block {i}: May be missing imports")

    # Check for incomplete function calls
    if 'LLM(' in block and 'model_path' not in block and 'hef_path' not in block:
        issues.append(f"  Block {i}: LLM() call may be missing model_path parameter")

if issues:
    print("  ⚠ Potential issues found:")
    for issue in issues:
        print(issue)
else:
    print("  ✓ No obvious syntax issues detected")

PYTHON_EOF
    python3 - "$README_PATH" << 'PYTHON_EOF'
else
    echo "  No Python code blocks found"
fi

# Check markdown structure
echo ""
echo "Checking markdown structure..."
if grep -q "^## " "$README_PATH"; then
    echo "  ✓ Has main sections (##)"
else
    echo "  ⚠ Missing main sections"
fi

if grep -q "^### " "$README_PATH"; then
    echo "  ✓ Has subsections (###)"
fi

# Check for prerequisites section
if grep -qi "prerequisites\|requirements" "$README_PATH"; then
    echo "  ✓ Has prerequisites/requirements section"
else
    echo "  ⚠ May be missing prerequisites section"
fi

# Check for usage examples
if grep -qi "usage\|example" "$README_PATH"; then
    echo "  ✓ Has usage/examples section"
else
    echo "  ⚠ May be missing usage examples"
fi

echo ""
echo "============================================================"
echo "Review complete!"
echo "============================================================"
echo ""
echo "Next steps:"
echo "1. Review the README manually using the checklist"
echo "2. Compare with similar READMEs in the repository"
echo "3. Validate imports and function signatures against code"
echo "4. Test code examples if possible"

