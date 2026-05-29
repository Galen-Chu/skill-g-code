# skill-g-code Project Setup Guide

## Overview
This document provides complete instructions to set up the **skill-g-code** project structure with all necessary files and directories.

## Directory Creation Commands

Run these commands in your terminal/command prompt:

### Option 1: Windows Command Prompt (cmd.exe)

```batch
cd d:\Skill

:: Create root directories
mkdir skill-g-code
cd skill-g-code

:: Create module directories with subdirectories
mkdir program-g-code\scripts program-g-code\references program-g-code\assets
mkdir sync-g-code\scripts sync-g-code\references sync-g-code\assets
mkdir spiritual-g-code\scripts spiritual-g-code\references spiritual-g-code\assets
mkdir psychological-g-code\scripts psychological-g-code\references psychological-g-code\assets
mkdir physiological-g-code\scripts physiological-g-code\references physiological-g-code\assets

:: Verify structure
tree /L
```

### Option 2: PowerShell

```powershell
cd d:\Skill

# Create root directory
New-Item -ItemType Directory -Path skill-g-code -Force

# Create module directories
$modules = @('program-g-code', 'sync-g-code', 'spiritual-g-code', 'psychological-g-code', 'physiological-g-code')
$subdirs = @('scripts', 'references', 'assets')

foreach ($module in $modules) {
    foreach ($subdir in $subdirs) {
        New-Item -ItemType Directory -Path "skill-g-code\$module\$subdir" -Force
    }
}

# Verify
Get-ChildItem -Path skill-g-code -Recurse -Directory
```

### Option 3: Linux/Mac Bash

```bash
cd /mnt/d/Skill

# Create structure
mkdir -p skill-g-code/{program-g-code,sync-g-code,spiritual-g-code,psychological-g-code,physiological-g-code}/{scripts,references,assets}

# Verify
tree skill-g-code
```

## Complete Project Structure

Once created, you should have:

```
d:\Skill\skill-g-code\
│
├── SKILL.md (Master Router Entry Point)
├── README.md (Comprehensive overview)
│
├── program-g-code\
│   ├── SKILL.md (💻 Software Engineering & Infrastructure)
│   ├── scripts\
│   ├── references\
│   └── assets\
│
├── sync-g-code\
│   ├── SKILL.md (🛰️ Data Pipeline & Synchronization)
│   ├── scripts\
│   ├── references\
│   └── assets\
│
├── spiritual-g-code\
│   ├── SKILL.md (🪐 Celestial & Philosophy)
│   ├── scripts\
│   ├── references\
│   └── assets\
│
├── psychological-g-code\
│   ├── SKILL.md (🧠 Mind & Subconsciousness)
│   ├── scripts\
│   ├── references\
│   └── assets\
│
└── physiological-g-code\
    ├── SKILL.md (🏃‍♂️ Body & Health)
    ├── scripts\
    ├── references\
    └── assets\
```

## Files Provided

The following SKILL.md files are ready to be added once directories exist:

### 1. **skill-g-code/SKILL.md** ✅
- Master router declaration
- Project overview and inter-module relationships
- Quick navigation guide

### 2. **program-g-code/SKILL.md** ✅
- Django, Docker, Pytest specifications
- Infrastructure responsibilities
- Technology stack and API endpoints

### 3. **sync-g-code/SKILL.md** ✅
- Aether-Kernel data pipeline
- Biorhythm 12 metrics specifications
- Google Cloud integration details
- Daily synchronization schedule

### 4. **spiritual-g-code/SKILL.md** ✅
- Astrological calculations framework
- Brand philosophy and manifesto
- Celestial transit tracking
- Chaldean numerology system

### 5. **psychological-g-code/SKILL.md** ✅
- Dream analysis system
- Latour critique philosophy framework
- Subconscious keyword extraction
- Emotional intelligence components

### 6. **physiological-g-code/SKILL.md** ✅
- Biometric data model and processing
- Sleep efficiency protocol
- Kinetic release framework
- Grounding practices guide

### 7. **skill-g-code/README.md** ✅
- Comprehensive project documentation
- Module relationships diagram
- Getting started instructions

## Next Steps

1. **Create the directory structure** using one of the commands above
2. **Copy the SKILL.md files** to their respective locations
3. **Copy the README.md** to the root directory
4. **Review each module's SKILL.md** to understand boundaries and responsibilities
5. **Start with program-g-code** for infrastructure setup

## Module Quick Reference

| Module | Focus | Key Tech |
|--------|-------|----------|
| **program-g-code** | Infrastructure | Django, Docker, Pytest |
| **sync-g-code** | Data Pipeline | Aether-Kernel, Google Cloud |
| **spiritual-g-code** | Philosophy | Astrology, Geometry, Brand |
| **psychological-g-code** | Psychology | Dreams, Emotion, Latour |
| **physiological-g-code** | Health | Biometrics, Sleep, Movement |

## Integration Map

```
                    ┌─────────────────┐
                    │  program-g-code │
                    │   (Foundation)  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │  sync-g-code    │
                    │   (Orchestrator)│
                    └────────┬────────┘
                    ┌────────┼────────┐
                    ↓        ↓        ↓
            ┌──────────┐ ┌──────────┐ ┌──────────┐
            │spiritual │ │psycholog │ │physiolog │
            │-g-code  │ │-g-code  │ │-g-code  │
            └──────────┘ └──────────┘ └──────────┘
```

## Support

All SKILL.md files contain:
- Module specifications and boundaries
- Directory structure explanations
- Quick start commands
- Integration points with other modules
- Roadmaps and next steps

Refer to individual SKILL.md files for detailed module information.

---

**Status**: ✅ Documentation Complete
**Created**: 2026-05-29
**Version**: 1.0
