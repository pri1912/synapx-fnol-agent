Autonomous Insurance Claims Processing Agent (Lite Version)
Synapx Assessment — Submitted by Priyanka Kumari Pandey

This project implements a clean, modular FNOL (First Notice of Loss) processing agent designed to:

Extract key insurance claim fields

Validate completeness & detect inconsistencies

Route the claim to fast-track, manual review, or escalation

Provide explicit reasoning behind every routing decision

The solution is rule-based, deterministic, and designed for clarity, maintainability, and real-world extensibility.

📌 Features
🔍 1. Field Extraction (extractor.py)

Uses regex + heuristics to extract:

Policy number

Policy holder

Claim type

Incident date & time

Location

Estimated loss amount

✔ 2. Validation Layer (validator.py)

Checks for:

Missing required fields

Invalid or future dates

Suspiciously low loss values

Cases with injuries but no police involvement

⚙️ 3. Routing Logic (processor.py)

Determines:

Fast Track → Low loss + simple property damage

Manual Review → Missing data or unclear case

Escalation → Police involvement or injuries

📁 4. Transparent Output

Produces a structured JSON:

{
  "extracted_fields": {...},
  "validation": {...},
  "routing": {
    "decision": "fast_track",
    "reasons": [...]
  }
}
