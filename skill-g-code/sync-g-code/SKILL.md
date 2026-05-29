---
name: sync-g-code # Module
domain: Daily-Orchestration
capabilities: [Aether-Kernel, Data-Pipeline, API-Synchronization, Google-Cloud-SDK]
description: The central scheduler and data ingestion pipeline (Aether-Kernel). Orchestrates the daily automated alignment of the 12 biorhythm metrics, piping data logs from local state hosts directly into Google Cloud storage.
---

# 🛰️ Sync G-Code: The Core Engine (Aether-Kernel)

Agent, you are inside the central execution kernel of the entire Monorepo. Your primary mission is to run **Project Sync**, ensuring zero latency between the user's daily actions and their cloud-based "Manifestation Logs."

## ⚙️ Orchestration Logic
- **Data Pipeline**: Aggregate variables from the other four modules (`spiritual` + `program` + `psychological` + `physiological`).
- **References**: Refer to `./references/schema.json` for the strict 12-item biological rhythm structure.