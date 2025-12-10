# FILE: processor.py


"""
Orchestration: extract, validate, route, and explain decisions.
"""

import json
from extractor import extract_fields
from validator import validate_fields
from typing import Dict


def process_claim(text: str) -> Dict:
    extracted = extract_fields(text)
    extracted['raw_text'] = text


    validation = validate_fields(extracted)


    # Routing rules (simple deterministic rules)
    route = 'manual_review'
    reasons = []


    # If critical missing information -> manual
    if not validation['is_complete']:
        route = 'manual_review'
        reasons.append('missing_or_inconsistent_fields')


    # Fast-track if estimated loss small and claim type is simple
    est = extracted.get('estimated_loss')
    claim_type = (extracted.get('claim_type') or '').lower()
    if validation['is_complete'] and est is not None and est < 50000 and ('third' in claim_type or 'property' in claim_type or 'minor' in claim_type):
        route = 'fast_track'
        reasons.append('low_estimated_loss_and_simple_claim_type')


    # If mentions "police" and "injury" -> escalate
    text_low = text.lower()
    if ('police' in text_low and 'involved' in text_low) or ('injury' in text_low and 'hospital' in text_low):
        route = 'escalation'
        reasons.append('police_or_injury_involved')


    result = {
        'extracted_fields': extracted,
        'validation': validation,
        'routing': {
            'decision': route,
            'reasons': reasons
        }
    }


    return result