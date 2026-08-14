# 🛸 Skill G-Code

> **The Universal Pioneer OS** — a Claude Code skill monorepo that orchestrates
> five specialized domains across software engineering and human consciousness.

## What This Is

A collection of Claude Code skill definitions (`SKILL.md` files) organized as a
master router + five domain modules. When installed under `~/.claude/commands/`
or referenced by Claude Code, the root `SKILL.md` routes `[Prefix]`-tagged tasks
to the matching domain module.

## Module Map

| Prefix | Module | Focus |
|--------|--------|-------|
| `[Spiritual]` | `spiritual-g-code/` | Astrology, transits, spiritual dashboards |
| `[Program]` | `program-g-code/` | CI/CD pipelines, automation scripts |
| `[Psychological]` | `psychological-g-code/` | Chakra-Kabbalah correspondence system |
| `[Physiological]` | `physiological-g-code/` | DNA codon ↔ I Ching hexagram mapping |
| `[Synchronize]` | `sync-g-code/` | Daily spiritual navigator, Gemini AI content |

## Installation

```bash
# Copy to your Claude Code skills directory
cp -r skill-g-code/ ~/.claude/commands/skill-g-code/
```

Or reference directly in your project's `.claude/` configuration.

## Global Constraints

Defined in the root `skill-g-code/SKILL.md`:
- **Bilingual Imperative** — all output in English + Traditional Chinese (繁體中文), no Pinyin
- **CLI-First** — prioritize headless, terminal-runnable scripts

## Repository Structure

```
skill-g-code/
├── skill-g-code/              # The skill monorepo (installable)
│   ├── SKILL.md               # Master router
│   ├── spiritual-g-code/      # 5 domain modules...
│   ├── program-g-code/
│   ├── psychological-g-code/
│   ├── physiological-g-code/
│   └── sync-g-code/
├── create_skill_structure.py  # Setup automation (Python)
├── create_structure.bat       # Setup automation (Windows)
├── create_structure.js        # Setup automation (Node.js)
├── PROJECT_SETUP_GUIDE.md     # Detailed setup instructions
└── INDEX.md                   # File inventory
```

## Related Repos

Each domain module corresponds to a standalone GitHub repository:
- [spiritual-g-code](https://github.com/Galen-Chu/spiritual-g-code)
- [program-g-code](https://github.com/Galen-Chu/program-g-code)
- [psychological-g-code](https://github.com/Galen-Chu/psychological-g-code)
- [physiological-g-code](https://github.com/Galen-Chu/physiological-g-code)
- [sync-g-code](https://github.com/Galen-Chu/sync-g-code)

## License

MIT — see [LICENSE](LICENSE).
