# processor.py
# Builds recommended routing based on Synapx assessment rules.

def process_claim(extracted: dict, validation: dict) -> dict:
    text = extracted.get("rawText", "").lower()
    damage = extracted.get("estimatedDamage")
    claim_type = (extracted.get("claimType") or "").lower()

    routing = ""
    reasons = []

    # -----------------------------------------
    # 1. Investigation flag → highest priority
    # -----------------------------------------
    if any(k in text for k in ["fraud", "inconsistent", "staged"]):
        routing = "investigation"
        reasons.append("Fraud/Inconsistency indicators detected")
        return routing, reasons

    # -----------------------------------------
    # 2. Specialist queue: injury cases
    # -----------------------------------------
    if "injury" in text or "injured" in text or "hospital" in text:
        routing = "specialist_queue"
        reasons.append("Injury-related claim requires specialist assessment")
        return routing, reasons

    # -----------------------------------------
    # 3. Missing required fields → manual review
    # -----------------------------------------
    if not validation["isComplete"]:
        routing = "manual_review"
        reasons.append("Missing required fields")
        return routing, reasons

    # -----------------------------------------
    # 4. Fast-track rule (< 25,000 & property damage)
    # -----------------------------------------
    if damage is not None and damage < 25000 and "property" in claim_type:
        routing = "fast_track"
        reasons.append("Low estimated damage (< 25000) & simple claim type")
        return routing, reasons

    # -----------------------------------------
    # 5. Default → manual review
    # -----------------------------------------
    routing = "manual_review"
    reasons.append("Does not meet fast-track criteria")

    return routing, reasons
