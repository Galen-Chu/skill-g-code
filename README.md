# 🛸 Skill G-Code

> **The Universal Pioneer OS** — a Claude Code skill monorepo that orchestrates
> five specialized domains across software engineering and human consciousness.

---

## 🧭 Core Vision

Create a unified system where:
- **Technology** (program-g-code) provides infrastructure
- **Data** (sync-g-code) flows synchronously across modules
- **Philosophy** (spiritual-g-code) provides timing and meaning
- **Psychology** (psychological-g-code) offers introspection
- **Physicality** (physiological-g-code) grounds everything in embodied practice

---

## 🏗️ Module Architecture

```
┌─────────────────────────────────────────────────────────┐
│                INFRASTRUCTURE (program-g-code)          │
│                Django | Docker | Pytest | CI/CD         │
└───────────────────────────┬─────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│           DATA ORCHESTRATION (sync-g-code)              │
│           Gemini AI | Biorhythm | Google Cloud          │
└─────────────┬────────────────────────┬──────────────────┘
              ↓                        ↓
   ┌────────────────────┐   ┌────────────────────┐
   │  SPIRITUAL MEANING │   │   PSYCHOLOGICAL    │
   │  (spiritual-g-code)│   │  (psychological-   │
   │  Astrology         │   │   g-code)          │
   │  Philosophy        │   │  Dreams, Emotions  │
   └────────────────────┘   └────────────────────┘
              ↓
   ┌────────────────────┐
   │   PHYSICAL HEALTH  │
   │  (physiological-   │
   │   g-code)          │
   │  Biometrics, Sleep │
   └────────────────────┘
```

---

## 📦 Module Map

| Prefix | Module | Focus |
|--------|--------|-------|
| `[Program]` | `program-g-code/` | CI/CD pipelines, automation scripts, infrastructure |
| `[Synchronize]` | `sync-g-code/` | Daily spiritual navigator, Gemini AI content generation |
| `[Spiritual]` | `spiritual-g-code/` | Astrology, transits, spiritual dashboards |
| `[Psychological]` | `psychological-g-code/` | Chakra-Kabbalah correspondence system |
| `[Physiological]` | `physiological-g-code/` | DNA codon ↔ I Ching hexagram mapping |

Each module directory contains a `SKILL.md` that Claude Code reads to inherit
domain-specific instructions and constraints.

---

## 🛠️ Global Constraints

Defined in the root `skill-g-code/SKILL.md`:

- **Bilingual Imperative** — all output in English + Traditional Chinese (繁體中文), no Pinyin
- **CLI-First** — prioritize lightweight, headless scripts capable of automation
- **Rational Grounding** — technical language over mystical jargon

---

## 🚀 Installation

```bash
# Copy to your Claude Code skills directory
cp -r skill-g-code/ ~/.claude/commands/skill-g-code/
```

Or use the automated setup script:

```bash
python create_skill_structure.py
```

See [IMPLEMENTATION.md](IMPLEMENTATION.md) for detailed setup instructions.

---

## 📁 Repository Structure

```
skill-g-code/
├── skill-g-code/              # The skill monorepo (installable)
│   ├── SKILL.md               # Master router
│   ├── program-g-code/        # 5 domain modules
│   ├── sync-g-code/
│   ├── spiritual-g-code/
│   ├── psychological-g-code/
│   └── physiological-g-code/
├── create_skill_structure.py  # Automated directory creation
├── create_structure.bat       # Windows batch alternative
├── create_structure.js        # Node.js alternative
├── IMPLEMENTATION.md          # Setup and implementation guide
└── LICENSE
```

---

## 🔗 Related Repos

Each domain module corresponds to a standalone GitHub repository:

| Repository | Focus |
|-----------|-------|
| [program-g-code](https://github.com/Galen-Chu/program-g-code) | ⚙️ CI/CD toolkit |
| [sync-g-code](https://github.com/Galen-Chu/sync-g-code) | 🛰️ Daily navigator |
| [spiritual-g-code](https://github.com/Galen-Chu/spiritual-g-code) | 🔮 Spiritual dashboard |
| [psychological-g-code](https://github.com/Galen-Chu/psychological-g-code) | 🕉️ Chakra-Kabbalah |
| [physiological-g-code](https://github.com/Galen-Chu/physiological-g-code) | 🧬 DNA ↔ I Ching |
| [spec-g-code](https://github.com/Galen-Chu/spec-g-code) | 📋 Specification hub |

---

## 📄 License

MIT — see [LICENSE](LICENSE).
