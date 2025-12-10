# extractor.py
# Extracts all required fields from the FNOL text (based on Synapx assessment brief)

import re

def extract_fields(text: str) -> dict:
    extracted = {}

    # -------------------------------
    # POLICY INFORMATION
    # -------------------------------
    extracted["policyNumber"] = _extract(r"Policy Number[:\- ]+([A-Za-z0-9\-]+)", text)
    extracted["policyHolder"] = _extract(r"Policy Holder[:\- ]+([A-Za-z ]+)", text)

    extracted["effectiveFrom"] = _extract(r"Effective From[:\- ]+([\d\-\/]+)", text)
    extracted["effectiveTo"] = _extract(r"Effective To[:\- ]+([\d\-\/]+)", text)

    # -------------------------------
    # INCIDENT INFORMATION
    # -------------------------------
    extracted["incidentDate"] = _extract(r"Incident Date[:\- ]+([\d\-\/]+)", text)
    extracted["incidentTime"] = _extract(r"Incident Time[:\- ]+([\d:]+)", text)
    extracted["incidentLocation"] = _extract(r"Location[:\- ]+(.+)", text)
    extracted["description"] = _extract(r"Description[:\- ]+(.+)", text)

    # -------------------------------
    # INVOLVED PARTIES
    # -------------------------------
    extracted["claimant"] = _extract(r"Claimant[:\- ]+([A-Za-z ]+)", text)
    extracted["thirdParties"] = _extract(r"Third Parties[:\- ]+(.+)", text)
    extracted["contactDetails"] = _extract(r"Contact[:\- ]+(.+)", text)

    # -------------------------------
    # ASSET INFORMATION
    # -------------------------------
    extracted["assetType"] = _extract(r"Asset Type[:\- ]+([A-Za-z ]+)", text)
    extracted["assetId"] = _extract(r"Asset ID[:\- ]+([A-Za-z0-9\-]+)", text)

    # Estimated Damage (fixed)
    match = re.search(r"Estimated (Loss|Damage)[:\- ]+INR ?([0-9,]+)", text, re.IGNORECASE)
    if match:
        num = match.group(2)
        extracted["estimatedDamage"] = int(num.replace(",", "").strip())
    else:
        extracted["estimatedDamage"] = None

    # Claim Type
    extracted["claimType"] = _extract(r"Claim Type[:\- ]+([A-Za-z ]+)", text)

    # Attachments
    extracted["attachments"] = _extract(r"Attachments[:\- ]+(.+)", text)
    extracted["initialEstimate"] = _extract(r"Initial Estimate[:\- ]+(.+)", text)

    extracted["rawText"] = text

    return extracted


def _extract(pattern: str, text: str):
    match = re.search(pattern, text, re.IGNORECASE)
    if not match:
        return None
    return match.group(1).strip()
