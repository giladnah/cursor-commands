"""
Application Review Tool for Cursor IDE.

This tool analyzes applications and provides comprehensive reviews including:
- Code quality assessment
- Bug detection
- Architecture review
- Testing recommendations
- Documentation review
"""

import ast
import os
import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from collections import defaultdict


logger = logging.getLogger(__name__)


@dataclass
class Issue:
    """Represents an issue found during review."""
    severity: str  # CRITICAL, HIGH, MEDIUM, LOW
    category: str  # BUG, CODE_QUALITY, ARCHITECTURE, TESTING, DOCUMENTATION
    file_path: str
    line_number: Optional[int]
    description: str
    recommendation: Optional[str] = None
    code_snippet: Optional[str] = None


@dataclass
class ReviewResult:
    """Complete review result for an application."""
    application_name: str
    total_issues: int
    issues_by_severity: Dict[str, int]
    issues_by_category: Dict[str, int]
    issues: List[Issue]
    summary: str
    recommendations: List[str]


class ApplicationReviewer:
    """
    Reviews applications for code quality, bugs, and best practices.
    """

    def __init__(self, app_path: Path):
        """
        Initialize reviewer.

        Args:
            app_path: Path to application directory.
        """
        self.app_path = Path(app_path)
        self.issues: List[Issue] = []
        self.python_files: List[Path] = []
        self.config_files: List[Path] = []

    def review(self) -> ReviewResult:
        """
        Perform comprehensive review.

        Returns:
            ReviewResult with all findings.
        """
        logger.info(f"Starting review of {self.app_path}")

        # Discover files
        self._discover_files()

        # Run checks
        self._check_imports()
        self._check_hardcoded_paths()
        self._check_error_handling()
        self._check_logging()
        self._check_type_hints()
        self._check_docstrings()
        self._check_thread_safety()
        self._check_configuration()
        self._check_test_coverage()
        self._check_documentation()
        self._check_hailo_dependencies()

        # Generate summary
        return self._generate_result()

    def _discover_files(self):
        """Discover Python and config files in application."""
        if not self.app_path.exists():
            logger.warning(f"Path does not exist: {self.app_path}")
            return

        # Find Python files
        for py_file in self.app_path.rglob("*.py"):
            if "__pycache__" not in str(py_file):
                self.python_files.append(py_file)

        # Find config files
        for config_file in self.app_path.rglob("*.yaml"):
            self.config_files.append(config_file)
        for config_file in self.app_path.rglob("*.yml"):
            self.config_files.append(config_file)
        for config_file in self.app_path.rglob("*.json"):
            if "database.json" not in str(config_file):  # Skip test databases
                self.config_files.append(config_file)

    def _check_imports(self):
        """Check for import issues."""
        for py_file in self.python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')

                    # Check for typos in module names
                    for i, line in enumerate(lines, 1):
                        if 'import' in line or 'from' in line:
                            # Check for common typos
                            if 'coffe_master' in line and 'coffee_master' in str(py_file):
                                self.issues.append(Issue(
                                    severity="CRITICAL",
                                    category="BUG",
                                    file_path=str(py_file.relative_to(self.app_path)),
                                    line_number=i,
                                    description="Typo in module name: 'coffe_master' should be 'coffee_master'",
                                    recommendation="Fix import to use correct module name",
                                    code_snippet=line.strip()
                                ))
            except Exception as e:
                logger.debug(f"Error checking imports in {py_file}: {e}")

    def _check_hardcoded_paths(self):
        """Check for hardcoded absolute paths."""
        for py_file in self.python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')

                    # Pattern for absolute paths
                    path_pattern = re.compile(r'["\'](/home|/Users|C:\\|/tmp/[^/]+)["\']')

                    for i, line in enumerate(lines, 1):
                        if path_pattern.search(line) and 'test' not in str(py_file).lower():
                            # Check if it's a legitimate use (like os.path.join with variables)
                            if 'os.path.join' not in line and 'Path(' not in line:
                                self.issues.append(Issue(
                                    severity="CRITICAL",
                                    category="BUG",
                                    file_path=str(py_file.relative_to(self.app_path)),
                                    line_number=i,
                                    description="Hardcoded absolute path detected",
                                    recommendation="Use relative paths with Path(__file__).parent or os.path.join",
                                    code_snippet=line.strip()
                                ))
            except Exception as e:
                logger.debug(f"Error checking paths in {py_file}: {e}")

    def _check_error_handling(self):
        """Check for missing error handling."""
        for py_file in self.python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    tree = ast.parse(content, filename=str(py_file))

                    # Check for bare except clauses
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ExceptHandler):
                            if node.type is None:
                                self.issues.append(Issue(
                                    severity="HIGH",
                                    category="CODE_QUALITY",
                                    file_path=str(py_file.relative_to(self.app_path)),
                                    line_number=node.lineno,
                                    description="Bare except clause detected",
                                    recommendation="Use specific exception types (e.g., except ValueError:)"
                                ))
            except Exception as e:
                logger.debug(f"Error checking error handling in {py_file}: {e}")

    def _check_logging(self):
        """Check for print statements instead of logging."""
        for py_file in self.python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')

                    has_logging = 'import logging' in content or 'from logging' in content

                    for i, line in enumerate(lines, 1):
                        stripped = line.strip()
                        if stripped.startswith('print(') and 'test' not in str(py_file).lower():
                            severity = "MEDIUM" if has_logging else "HIGH"
                            self.issues.append(Issue(
                                severity=severity,
                                category="CODE_QUALITY",
                                file_path=str(py_file.relative_to(self.app_path)),
                                line_number=i,
                                description="Print statement found instead of logging",
                                recommendation="Replace with logger.info/debug/error",
                                code_snippet=line.strip()
                            ))
            except Exception as e:
                logger.debug(f"Error checking logging in {py_file}: {e}")

    def _check_type_hints(self):
        """Check for missing type hints."""
        for py_file in self.python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    tree = ast.parse(content, filename=str(py_file))

                    # Check function definitions
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            # Skip test files and private methods
                            if 'test' in str(py_file).lower() or node.name.startswith('_'):
                                continue

                            # Check if function has type hints
                            if not node.returns and len(node.args.args) > 0:
                                # Check if any args have type hints
                                has_any_hints = any(
                                    arg.annotation is not None for arg in node.args.args
                                )

                                if not has_any_hints and node.name != '__init__':
                                    self.issues.append(Issue(
                                        severity="LOW",
                                        category="CODE_QUALITY",
                                        file_path=str(py_file.relative_to(self.app_path)),
                                        line_number=node.lineno,
                                        description=f"Function '{node.name}' missing type hints",
                                        recommendation="Add type hints for parameters and return type"
                                    ))
            except Exception as e:
                logger.debug(f"Error checking type hints in {py_file}: {e}")

    def _check_docstrings(self):
        """Check for missing docstrings."""
        for py_file in self.python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    tree = ast.parse(content, filename=str(py_file))

                    # Check module docstring
                    if not ast.get_docstring(tree) and 'test' not in str(py_file).lower():
                        self.issues.append(Issue(
                            severity="LOW",
                            category="DOCUMENTATION",
                            file_path=str(py_file.relative_to(self.app_path)),
                            line_number=1,
                            description="Module missing docstring",
                            recommendation="Add module-level docstring"
                        ))

                    # Check function docstrings
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            if 'test' in str(py_file).lower() or node.name.startswith('_'):
                                continue

                            if not ast.get_docstring(node):
                                self.issues.append(Issue(
                                    severity="LOW",
                                    category="DOCUMENTATION",
                                    file_path=str(py_file.relative_to(self.app_path)),
                                    line_number=node.lineno,
                                    description=f"Function '{node.name}' missing docstring",
                                    recommendation="Add Google-style docstring"
                                ))
            except Exception as e:
                logger.debug(f"Error checking docstrings in {py_file}: {e}")

    def _check_thread_safety(self):
        """Check for thread-safety issues."""
        for py_file in self.python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Check for file operations without locks
                    if 'open(' in content and 'json.load' in content:
                        if 'threading.Lock' not in content and 'multiprocessing.Lock' not in content:
                            # Check if it's a database or config file
                            if 'database' in str(py_file).lower() or 'config' in str(py_file).lower():
                                self.issues.append(Issue(
                                    severity="HIGH",
                                    category="BUG",
                                    file_path=str(py_file.relative_to(self.app_path)),
                                    line_number=None,
                                    description="File I/O operations without thread-safety mechanisms",
                                    recommendation="Add threading.Lock for concurrent access"
                                ))
            except Exception as e:
                logger.debug(f"Error checking thread safety in {py_file}: {e}")

    def _check_configuration(self):
        """Check for configuration issues."""
        # Check if config files exist
        config_yaml = self.app_path / "config.yaml"
        if not config_yaml.exists():
            # Check if there are hardcoded values that should be configurable
            for py_file in self.python_files:
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Look for magic numbers that might be configurable
                        if 'LOITER_THRESHOLD' in content or 'RESET_TIMEOUT' in content:
                            if 'config.yaml' not in content:
                                self.issues.append(Issue(
                                    severity="MEDIUM",
                                    category="ARCHITECTURE",
                                    file_path=str(py_file.relative_to(self.app_path)),
                                    line_number=None,
                                    description="Hardcoded configuration values",
                                    recommendation="Move tunable parameters to config.yaml"
                                ))
                except Exception as e:
                    logger.debug(f"Error checking configuration in {py_file}: {e}")

    def _check_test_coverage(self):
        """Check test coverage."""
        test_dir = self.app_path / "tests"
        if not test_dir.exists():
            self.issues.append(Issue(
                severity="MEDIUM",
                category="TESTING",
                file_path="tests/",
                line_number=None,
                description="No tests directory found",
                recommendation="Create tests directory with functional tests"
            ))
        else:
            # Check if there are tests for main modules
            test_files = list(test_dir.glob("test_*.py"))
            if len(test_files) == 0:
                self.issues.append(Issue(
                    severity="MEDIUM",
                    category="TESTING",
                    file_path="tests/",
                    line_number=None,
                    description="No test files found",
                    recommendation="Add pytest test files"
                ))

    def _check_hailo_dependencies(self):
        """Check if Hailo libraries are properly installed."""
        # Check for hailo imports in Python files
        hailo_imports_found = False

        for py_file in self.python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Check for hailo imports
                    if 'import hailo' in content or 'from hailo' in content:
                        hailo_imports_found = True
                        break
            except Exception as e:
                logger.debug(f"Error checking hailo dependencies in {py_file}: {e}")

        # Check for hailo_apps imports
        hailo_apps_imports_found = False
        for py_file in self.python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'from hailo_apps' in content or 'import hailo_apps' in content:
                        hailo_apps_imports_found = True
                        break
            except Exception:
                pass

        # Report missing hailo if imports are used but not available
        if hailo_imports_found:
            try:
                import hailo  # noqa: F401
            except ImportError:
                self.issues.append(Issue(
                    severity="CRITICAL",
                    category="ARCHITECTURE",
                    file_path="setup/installation",
                    line_number=None,
                    description="Hailo library is imported but not available. This indicates a setup or installation issue.",
                    recommendation="Install Hailo libraries: pip install hailort or follow Hailo installation guide"
                ))

        if hailo_apps_imports_found:
            try:
                import hailo_apps  # noqa: F401
            except ImportError:
                self.issues.append(Issue(
                    severity="CRITICAL",
                    category="ARCHITECTURE",
                    file_path="setup/installation",
                    line_number=None,
                    description="hailo_apps package is imported but not available. This indicates a setup or installation issue.",
                    recommendation="Install hailo_apps package or ensure PYTHONPATH is set correctly"
                ))

    def _check_documentation(self):
        """Check for documentation files."""
        readme = self.app_path / "README.md"
        if not readme.exists():
            self.issues.append(Issue(
                severity="LOW",
                category="DOCUMENTATION",
                file_path="README.md",
                line_number=None,
                description="Missing README.md",
                recommendation="Create README.md with usage instructions"
            ))

    def _generate_result(self) -> ReviewResult:
        """Generate review result from collected issues."""
        # Count by severity
        issues_by_severity = defaultdict(int)
        for issue in self.issues:
            issues_by_severity[issue.severity] += 1

        # Count by category
        issues_by_category = defaultdict(int)
        for issue in self.issues:
            issues_by_category[issue.category] += 1

        # Generate summary
        critical_count = issues_by_severity.get("CRITICAL", 0)
        high_count = issues_by_severity.get("HIGH", 0)

        if critical_count > 0:
            summary = f"CRITICAL: {critical_count} critical issues found. Immediate attention required."
        elif high_count > 0:
            summary = f"WARNING: {high_count} high-priority issues found."
        elif len(self.issues) > 0:
            summary = f"Found {len(self.issues)} issues, mostly code quality improvements."
        else:
            summary = "No issues found. Application looks good!"

        # Generate recommendations
        recommendations = []
        if critical_count > 0:
            recommendations.append("Fix all CRITICAL issues before deployment")
        if issues_by_category.get("TESTING", 0) > 0:
            recommendations.append("Improve test coverage")
        if issues_by_category.get("DOCUMENTATION", 0) > 0:
            recommendations.append("Add missing documentation")

        return ReviewResult(
            application_name=self.app_path.name,
            total_issues=len(self.issues),
            issues_by_severity=dict(issues_by_severity),
            issues_by_category=dict(issues_by_category),
            issues=self.issues,
            summary=summary,
            recommendations=recommendations
        )


def review_application(app_path: str, output_format: str = "json") -> str:
    """
    Review an application and return results.

    Args:
        app_path: Path to application directory.
        output_format: Output format ('json', 'text', 'markdown').

    Returns:
        Review results in requested format.
    """
    reviewer = ApplicationReviewer(Path(app_path))
    result = reviewer.review()

    if output_format == "json":
        return json.dumps(asdict(result), indent=2)
    elif output_format == "markdown":
        return _format_markdown(result)
    else:
        return _format_text(result)


def _format_markdown(result: ReviewResult) -> str:
    """Format result as markdown."""
    lines = [
        f"# Application Review: {result.application_name}",
        "",
        f"**Summary**: {result.summary}",
        "",
        "## Statistics",
        "",
        f"- Total Issues: {result.total_issues}",
        f"- Critical: {result.issues_by_severity.get('CRITICAL', 0)}",
        f"- High: {result.issues_by_severity.get('HIGH', 0)}",
        f"- Medium: {result.issues_by_severity.get('MEDIUM', 0)}",
        f"- Low: {result.issues_by_severity.get('LOW', 0)}",
        "",
        "## Issues",
        ""
    ]

    # Group by severity
    for severity in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        severity_issues = [i for i in result.issues if i.severity == severity]
        if severity_issues:
            lines.append(f"### {severity} Issues")
            lines.append("")
            for issue in severity_issues:
                lines.append(f"#### {issue.file_path}")
                if issue.line_number:
                    lines.append(f"**Line {issue.line_number}**: {issue.description}")
                else:
                    lines.append(f"**{issue.description}**")
                if issue.recommendation:
                    lines.append(f"- Recommendation: {issue.recommendation}")
                if issue.code_snippet:
                    lines.append(f"```python\n{issue.code_snippet}\n```")
                lines.append("")

    if result.recommendations:
        lines.append("## Recommendations")
        lines.append("")
        for rec in result.recommendations:
            lines.append(f"- {rec}")
        lines.append("")

    return "\n".join(lines)


def _format_text(result: ReviewResult) -> str:
    """Format result as plain text."""
    lines = [
        f"Application Review: {result.application_name}",
        "=" * 60,
        f"Summary: {result.summary}",
        "",
        f"Total Issues: {result.total_issues}",
        f"  Critical: {result.issues_by_severity.get('CRITICAL', 0)}",
        f"  High: {result.issues_by_severity.get('HIGH', 0)}",
        f"  Medium: {result.issues_by_severity.get('MEDIUM', 0)}",
        f"  Low: {result.issues_by_severity.get('LOW', 0)}",
        "",
        "Issues:",
        ""
    ]

    for issue in result.issues:
        lines.append(f"[{issue.severity}] {issue.file_path}")
        if issue.line_number:
            lines.append(f"  Line {issue.line_number}: {issue.description}")
        else:
            lines.append(f"  {issue.description}")
        if issue.recommendation:
            lines.append(f"  -> {issue.recommendation}")
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: application_review.py <app_path> [output_format]")
        print("  output_format: json, text, markdown (default: json)")
        sys.exit(1)

    app_path = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else "json"

    result = review_application(app_path, output_format)
    print(result)

