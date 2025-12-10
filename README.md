# Autonomous Insurance Claims Processing Agent (Lite Version)  
### Synapx Technical Assessment — Submitted by Priyanka Kumari Pandey

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.10+-blue)  
![Category](https://img.shields.io/badge/Category-Rule--Based%20NLP-yellow)  

This project implements a clean, modular **FNOL (First Notice of Loss) Processing Agent**, designed to extract relevant claim details, validate the information, and intelligently route the claim into **fast-track**, **manual review**, or **escalation** categories.

The emphasis is on **clarity**, **deterministic logic**, and **explainability**, ensuring decisions are transparent, reproducible, and easy to audit.

---

## 🧩 **1. Features Overview**

### 🔍 Field Extraction (`extractor.py`)  
Extracts structured fields using deterministic regex patterns and heuristics:

- Policy Number  
- Policy Holder  
- Claim Type  
- Incident Date & Time  
- Location  
- Estimated Loss Amount  

---

### ✔ Validation Layer (`validator.py`)  
Checks for:

- Missing required fields  
- Invalid or future dates  
- Suspiciously low estimated losses  
- Injury-related terms without police involvement  

---

### ⚙️ Routing Engine (`processor.py`)  
Determines final claim flow:

| Condition | Routing |
|----------|---------|
| Low loss + simple claim | **Fast-Track** |
| Missing fields or unclear data | **Manual Review** |
| Injury or police involvement | **Escalation (High Priority)** |

Each decision includes detailed **reasons** to ensure transparency.

---

### 📁 Structured JSON Output

```json
{
  "extracted_fields": {
    "policy_number": "PL-2024-998877",
    "policy_holder": "Rajesh Kumar",
    "claim_type": "Third-Party Property Damage",
    "incident_date": "2025-12-02",
    "incident_time": "18:45",
    "location": "Outer Ring Road, Hyderabad",
    "estimated_loss": 18500
  },
  "validation": {
    "flags": [],
    "is_complete": true
  },
  "routing": {
    "decision": "fast_track",
    "reasons": [
      "low_estimated_loss_and_simple_claim_type"
    ]
  }
}


🏗️ 2. Project Architecture

synapx-fnol-agent/
│
├── extractor.py        → Extracts structured FNOL fields
├── validator.py        → performs validation checks
├── processor.py        → extraction → validation → routing
├── main.py             → CLI entrypoint
│
├── sample_fnol.txt     → Sample FNOL document
├── requirements.txt    → Dependencies
└── README.md           → Documentation (this file)


🚀 3. How to Run
Clone & Set Up

git clone https://github.com/pri1912/synapx-fnol-agent.git
cd synapx-fnol-agent
python -m venv venv
.\venv\Scripts\Activate.ps1    # On Windows
pip install -r requirements.txt


Run the Processor

python main.py sample_fnol.txt


Output is printed and saved as output.json.

📌 4. Technical Highlights

Deterministic rule-based NLP

Clean modular architecture

Transparent, explainable routing

Easily extendable for ML or API versions

Real-world, audit-friendly JSON outputs

🔮 5. Future Enhancements
NLP Improvements:

SpaCy or transformer-based NER for robust extraction

Multi-format FNOL ingestion (PDF, OCR)

ML Enhancements:

Claim severity prediction

Fraud detection heuristics

Engineering Enhancements:

FastAPI REST service

Dockerization

Unit tests + CI/CD pipeline

👤 6. Author

Priyanka Kumari Pandey
Location: Mumbai, India
GitHub: https://github.com/pri1912

💬 7. Notes

This assessment focuses on demonstrating:

Problem breakdown and clean coding

Thoughtful modular architecture

Practical understanding of how insurance workflows operate

Ability to produce professional-grade engineering deliverables

