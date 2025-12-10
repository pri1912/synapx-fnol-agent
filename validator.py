"""
Check for completeness and simple inconsistencies.
"""



from typing import Dict, List
from datetime import date


def validate_fields(extracted: Dict) -> Dict:
    flags: List[str] = []


    # Required fields
    required = ['policy_number', 'policy_holder', 'incident_date', 'claim_type']
    for r in required:
        if not extracted.get(r):
            flags.append(f'missing_{r}')


    # Date sanity
    inc_date = extracted.get('incident_date')
    if inc_date:
        try:
            y,m,d = map(int, inc_date.split('-'))
            from datetime import date as dt
            inc = dt(y,m,d)
            if inc > date.today():
                flags.append('incident_date_in_future')
        except Exception:
            flags.append('incident_date_unparseable')


    # Estimated loss sanity
    est = extracted.get('estimated_loss')
    if est is not None and est < 100:
        flags.append('estimated_loss_suspiciously_low')


    # Quick consistency check: claim type & police involvement
    text = extracted.get('raw_text', '').lower()
    if 'police not involved' in text or 'no police' in text:
        if 'injury' in text or 'hurt' in text:
            flags.append('injury_but_no_police')


    return {
        'flags': flags,
        'is_complete': len(flags) == 0
    }