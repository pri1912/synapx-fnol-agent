import re
from dateutil import parser as dateparser
from typing import Optional, Dict

FIELD_PATTERNS = {
    'policy_number': [r'Policy\s*(No(?:\.|:)?)\s*[:\-]?\s*([A-Z0-9\-]+)', r'Policy Number\s*[:\-]?\s*([A-Z0-9\-]+)'],
'policy_holder': [r'Policy Holder\s*[:\-]?\s*([A-Za-z \.]+)', r'Insured\s*[:\-]?\s*([A-Za-z \.]+)'],
'claim_type': [r'Claim Type\s*[:\-]?\s*([A-Za-z \-]+)'],
'incident_date': [r'Incident Date\s*[:\-]?\s*([A-Za-z0-9, \-/]+)', r'Date of Incident\s*[:\-]?\s*([A-Za-z0-9, \-/]+)'],
'incident_time': [r'Incident Time\s*[:\-]?\s*([0-2]?[0-9]:[0-5][0-9])'],
'location': [r'Location\s*[:\-]?\s*([A-Za-z0-9 ,\-\./]+)'],
'estimated_loss': [r'Estimated Loss\s*[:\-]?\s*(INR|Rs\.?|USD|EUR)?\s*([0-9,]+)']
}


def _first_match(text: str, patterns):
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            # If capture groups used, prefer last group
            if m.groups():
                return m.groups()[-1].strip()
            return m.group(0).strip()
    return None


def parse_date(text: str) -> Optional[str]:
    try:
        dt = dateparser.parse(text, dayfirst=False)
        return dt.date().isoformat()
    except Exception:
        return None


def extract_fields(text: str) -> Dict[str, Optional[str]]:
    t = text
    out = {}


    out['policy_number'] = _first_match(t, FIELD_PATTERNS['policy_number'])
    out['policy_holder'] = _first_match(t, FIELD_PATTERNS['policy_holder'])
    out['claim_type'] = _first_match(t, FIELD_PATTERNS['claim_type'])


    raw_date = _first_match(t, FIELD_PATTERNS['incident_date'])
    out['incident_date_raw'] = raw_date
    out['incident_date'] = parse_date(raw_date) if raw_date else None


    raw_time = _first_match(t, FIELD_PATTERNS['incident_time'])
    out['incident_time'] = raw_time


    out['location'] = _first_match(t, FIELD_PATTERNS['location'])


    est = _first_match(t, FIELD_PATTERNS['estimated_loss'])
    if est:
        est_clean = re.sub(r'[^0-9]', '', est)
        out['estimated_loss'] = int(est_clean) if est_clean.isdigit() else None
    else:
        out['estimated_loss'] = None


    # fallback heuristics
    if not out['policy_holder']:
        # Try simple "Name:" pattern
        name_m = re.search(r'Name\s*[:\-]?\s*([A-Z][a-z]+\s+[A-Z][a-z]+)', t)
        if name_m:
            out['policy_holder'] = name_m.group(1)


    return out
