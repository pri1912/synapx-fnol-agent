# validator.py
# Performs completeness and required-field validation based on Synapx assessment brief

from datetime import datetime

# Fields required as per assessment requirements
REQUIRED_FIELDS = [
    "policyNumber",
    "policyHolder",
    "incidentDate",
    "incidentLocation",
    "claimType",
    "estimatedDamage",
    "claimant",
    "contactDetails",
    "assetType",
    "assetId",
]

def validate_fields(extracted: dict) -> dict:
    missing = []

    # Check ALL required fields
    for field in REQUIRED_FIELDS:
        if not extracted.get(field):
            missing.append(field)

    # Validate date format
    date_str = extracted.get("incidentDate")
    if date_str:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")  # enforce YYYY-MM-DD
        except:
            missing.append("incidentDate (invalid format)")

    # Sanity check for estimated damage
    damage = extracted.get("estimatedDamage")
    if damage is not None and damage < 100:
        missing.append("estimatedDamage (too low)")

    return {
        "missingFields": missing,
        "isComplete": len(missing) == 0
    }
