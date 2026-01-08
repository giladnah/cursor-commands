# Changelog

## 2025-01-18 - Repository Cleanup and Documentation Fixes

### Cleanup
- **Removed duplicate files**: Deleted outdated `commands/README.md`, `commands/SETUP_GITHUB.md`, `commands/CHANGELOG.md`, and `commands/tools/README.md`
- **Removed temporary files**: Cleaned up `debug.log` and `worktrees.json` (already gitignored)
- **Fixed path references**: Updated all documentation to use correct paths (`tools/` not `commands/tools/`)

### Fixed
- **Path references**: Corrected tool path in CHANGELOG and review-application.md command documentation
- **Documentation consistency**: Removed outdated references to symlinks and old repository structure

## 2025-01-18 - Repository Restructure: .cursor/ as Root

### Major Restructure
- **Repository root moved**: From `.cursor/commands/` to `.cursor/`
- **Commands and Tools as siblings**: Both directories at the same level
- **No symlinks needed**: Tools are automatically in Cursor's default location

### Added
- **Tools directory**: `tools/` for executable scripts (at repository root level)
- **Application review tool**: `tools/application_review.py` - Comprehensive code quality analysis
- **Review application command**: `commands/review-application.md` - Command that uses the review tool
- **Tools documentation**: `tools/README.md` - Documentation for available tools

### Updated
- **Main README**: Refactored for new structure (`.cursor/` as repo root)
- **SETUP_GITHUB.md**: Updated clone instructions (clone to `.cursor/` not `.cursor/commands/`)
- **All path references**: Updated to reflect new structure

### Structure
```
.cursor/                        # Git repository root
├── README.md                   # Main documentation
├── commands/                   # Commands directory
│   ├── review-readme.md        # Existing command
│   ├── review-application.md   # NEW: Application review command
│   └── SETUP_GITHUB.md        # Setup instructions
└── tools/                      # Tools directory (sibling to commands)
    ├── README.md              # Tools documentation
    └── application_review.py  # Application review tool
```

### Benefits
- ✅ No symlinks needed
- ✅ Cursor finds both `commands/` and `tools/` automatically
- ✅ Cleaner structure with commands and tools as siblings
- ✅ Simpler path references: `tools/tool.py` not `commands/tools/tool.py`

### Usage

**Command:**
```
@review-application hailo_apps/python/gen_ai_apps/coffee_master markdown
```

**Direct tool usage:**
```bash
python .cursor/tools/application_review.py <app_path> [output_format]
```

