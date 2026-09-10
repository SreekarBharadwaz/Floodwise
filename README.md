# FloodWise

**AI-assisted emergency response decision and coordination prototype**

FloodWise is a research-oriented end-to-end prototype for flood/emergency response. It combines structured admin/citizen intake with NLP extraction, scenario validation, specialist AI agents, scenario-based simulation, human approval, mission generation, execution tracking, a decision-twin state, and dynamic reassessment.

## What is included

- Structured emergency/admin and citizen intake
- FastAPI backend for receiving submissions
- Zero-shot entity extraction with NuNER Zero / GLiNER
- spaCy-based linguistic/relationship processing
- Scenario construction and validation
- Multi-agent workflow:
  - Situation Agent
  - Resource Agent
  - Report Agent
  - Planning Agent
  - Simulation Engine
  - Decision Agent
  - Human Approval
  - Execution Agent
- Mission lifecycle: READY → IN_PROGRESS → COMPLETED
- Field updates and decision-twin state changes
- Reassessment/replanning logic
- Clean research notebook with outputs and debug cells removed
- Sample data for reproducibility

## Project level

**Level: Advanced / research prototype.**

### Is it end-to-end?

**Yes, at the prototype level.** The implemented flow covers:

`Intake → Storage → NLP → Validation → Situation/Resource/Report Analysis → Planning → Simulation → AI Recommendation → Human Approval → Mission Generation → Execution → Field Update → Decision Twin → Reassessment`

However, it should **not** be presented as a production-ready emergency-management platform. Important production gaps remain: authentication/authorization, database-backed persistence, formal API schemas, automated tests, robust observability, calibrated simulation models, deployment infrastructure, security hardening, and real operational integrations.

## Repository structure

```text
FloodWise/
├── notebooks/
│   └── FloodWise_Clean.ipynb
├── src/
│   └── backend.py
├── data/
│   └── sample/
│       ├── admin_latest.json
│       ├── user_latest.json
│       └── submissions/
│           └── user_001.json
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

## Setup

### 1. Create an environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Configure the NVIDIA API key

Copy `.env.example` to `.env` and set your key, or export `NVIDIA_API_KEY` directly.

**Never commit API keys to GitHub.**

### 4. Start the API

```bash
uvicorn src.backend:app --reload
```

Then open:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs
```

### 5. Run the research notebook

Open `notebooks/FloodWise_Clean.ipynb` in Jupyter or VS Code.

Set:

```text
NVIDIA_API_KEY=<your-key>
FLOODWISE_DATA_DIR=../data/sample
```

The notebook is intended as the research/prototyping layer; the FastAPI service is separated into `src/backend.py`.

## Security note

The original uploaded notebook contained exposed API credentials. Those credentials were **not copied into this repository**. If the exposed credentials are still active, revoke/rotate them immediately before publishing the project.

## Research-paper positioning

A strong research framing is:

> **FloodWise: A Human-in-the-Loop Multi-Agent Decision Framework for Dynamic Flood Response**

Potential contributions to evaluate experimentally:

1. Multi-agent decomposition of emergency reasoning.
2. Fusion of structured administrative data and unstructured citizen reports.
3. Scenario-based plan simulation before recommendation.
4. Human approval as a safety/control layer.
5. Decision-twin updates from field conditions.
6. Dynamic reassessment and replanning after operational changes.

For a research paper, add quantitative experiments comparing:
- single-agent vs multi-agent reasoning,
- no-NLP vs NLP-enhanced intake,
- static planning vs dynamic reassessment,
- different resource-shortage scenarios,
- recommendation quality, latency, robustness, and JSON/constraint validity.

## Important limitation

The current simulation engine is a **rule-based prototype**, not a validated physical flood simulator. Do not claim real-world evacuation optimization or safety guarantees without further validation and domain data.
