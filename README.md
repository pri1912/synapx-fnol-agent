# Autonomous Insurance Claims Processing Agent (Lite Version)  
### Synapx Technical Assessment — Submitted by **Priyanka Kumari Pandey**

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.10+-blue)  
![Category](https://img.shields.io/badge/Category-Rule--Based%20NLP-yellow)  

This project implements a clean and modular **FNOL (First Notice of Loss) Processing Agent**, aligned with the **official Synapx assessment brief**.  
It extracts structured claim information, validates completeness, and routes the claim based on deterministic decision rules.

The solution emphasizes **clarity, explainability, and real-world workflow alignment**.

---

# 🧩 1. Extracted Fields (per Synapx requirements)

### **Policy Information**
- Policy Number  
- Policyholder Name  
- Effective From  
- Effective To  

### **Incident Details**
- Incident Date  
- Incident Time  
- Incident Location  
- Description  

### **Involved Parties**
- Claimant  
- Third Parties  
- Contact Details  

### **Asset Information**
- Asset Type  
- Asset ID  
- Estimated Damage  

### **Other**
- Claim Type  
- Attachments  
- Initial Estimate  

All extracted fields are available in the final JSON under `extractedFields`.

---

# ⚙️ 2. Validation Logic

The validator checks:

- All required fields  
- Date formatting  
- Damage amount sanity  
- Required party/asset fields  

Output example:

```json
{
  "missingFields": ["claimant", "contactDetails"],
  "isComplete": false
}

🚦 3. Routing Logic (Decision Engine)

The processor determines the recommended workflow route:

1. Investigation (highest priority)

Triggered if description includes:

"fraud"

"inconsistent"

"staged"

2. Specialist Queue

Triggered for injury-related claims:

"injury"

"injured"

"hospital"

3. Manual Review

Triggered when:

Required fields are missing

Invalid or incomplete data detected

4. Fast Track

Triggered when:

Estimated Damage < 25,000

Claim Type indicates simple property damage

Each routing decision includes human-readable reasoning.


📁 4. Output JSON Format (per official brief)

{
  "extractedFields": { ... },
  "missingFields": [ ... ],
  "recommendedRoute": "manual_review | fast_track | investigation | specialist_queue",
  "reasoning": [ ... ]
}


🏗️ 5. Project Architecture

synapx-fnol-agent/
│
├── extractor.py        → Field extraction (policy, incident, asset, parties)
├── validator.py        → Completeness & rules validation
├── processor.py        → Routing engine (decision logic)
├── main.py             → CLI entry point
│
├── sample_fnol.txt     → Example FNOL input
├── requirements.txt    → Dependencies
└── README.md           → Documentation


🚀 6. How to Run

Clone & Setup

git clone https://github.com/pri1912/synapx-fnol-agent.git
cd synapx-fnol-agent
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt


Run Processor

python main.py sample_fnol.txt


Output is printed and saved as output.json.

📌 7. Technical Highlights

Deterministic rule-based NLP

Production-friendly modular structure

Fully explainable routing decisions

Real-world claim workflow alignment

Clean and auditable JSON outputs

Easy to extend into ML, FastAPI services, or OCR/PDF pipelines

🔮 8. Future Enhancements
NLP Enhancements

SpaCy/Transformer-based NER

PDF/OCR ingestion

ML Enhancements

Severity prediction

Fraud scoring models

Engineering

FastAPI microservice

Dockerization

End-to-end unit tests

👤 9. Author

Priyanka Kumari Pandey
Location: Mumbai, India
GitHub: https://github.com/pri1912