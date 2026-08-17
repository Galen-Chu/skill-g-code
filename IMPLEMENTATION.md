# 🚀 Implementation Guide

Setup instructions and automation for the skill-g-code monorepo.

---

## 📋 Prerequisites

- Python 3.10+ (for the automation script)
- Git
- A Claude Code environment (`.claude/commands/` directory)

---

## 🏗️ Directory Setup

### Option 1: Automated (Recommended)

```bash
python create_skill_structure.py
```

This creates the complete directory tree with all module subdirectories
(`scripts/`, `references/`, `assets/`) and copies the SKILL.md files.

### Option 2: Windows Command Prompt

```batch
mkdir skill-g-code
cd skill-g-code
mkdir program-g-code\scripts program-g-code\references program-g-code\assets
mkdir sync-g-code\scripts sync-g-code\references sync-g-code\assets
mkdir spiritual-g-code\scripts spiritual-g-code\references spiritual-g-code\assets
mkdir psychological-g-code\scripts psychological-g-code\references psychological-g-code\assets
mkdir physiological-g-code\scripts physiological-g-code\references physiological-g-code\assets
tree /L
```

### Option 3: PowerShell

```powershell
$modules = @('program-g-code', 'sync-g-code', 'spiritual-g-code', 'psychological-g-code', 'physiological-g-code')
$subdirs = @('scripts', 'references', 'assets')

New-Item -ItemType Directory -Path skill-g-code -Force
foreach ($module in $modules) {
    foreach ($subdir in $subdirs) {
        New-Item -ItemType Directory -Path "skill-g-code\$module\$subdir" -Force
    }
}
```

### Option 4: Linux/macOS

```bash
mkdir -p skill-g-code
cd skill-g-code
for module in program-g-code sync-g-code spiritual-g-code psychological-g-code physiological-g-code; do
    for subdir in scripts references assets; do
        mkdir -p "$module/$subdir"
    done
done
tree -L 2   # or: find . -type d | sort
```

---

## 🤖 Automation Scripts

| Script | Platform | Usage |
|--------|----------|-------|
| `create_skill_structure.py` ⭐ | Any (Python) | `python create_skill_structure.py` |
| `create_structure.bat` | Windows CMD | `create_structure.bat` |
| `create_structure.js` | Node.js | `node create_structure.js` |
| `create_structure.py` | Any (Python) | `python create_structure.py` |

The Python script (⭐ recommended) also verifies the created structure and
prints a visual tree.

---

## ✅ Verification Checklist

After running the setup:

- [ ] Root `skill-g-code/SKILL.md` exists (master router)
- [ ] 5 module directories created with `SKILL.md` in each
- [ ] Each module has `scripts/`, `references/`, `assets/` subdirectories
- [ ] Claude Code can find the skills (check `~/.claude/commands/skill-g-code/`)

---

## 📦 Deploying SKILL.md Files

The monorepo already includes all SKILL.md files under `skill-g-code/`.
If you used the manual directory creation approach, copy them:

```bash
# Copy all SKILL.md files to the created structure
cp skill-g-code/SKILL.md skill-g-code/
cp skill-g-code/*/SKILL.md skill-g-code/*/
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Script fails on Windows | Run as Administrator; ensure Python is in PATH |
| Missing Python | Install from [python.org](https://python.org); verify with `python --version` |
| Directory already exists | Scripts use `-Force` / `mkdir -p` (idempotent); safe to re-run |
| Claude Code doesn't see skills | Verify files are in `~/.claude/commands/skill-g-code/` |
