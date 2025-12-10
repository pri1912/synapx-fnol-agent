# main.py
# CLI runner for FNOL processor (Synapx format)

import sys
from extractor import extract_fields
from validator import validate_fields
from processor import process_claim
import json

def main(input_file):
    with open(input_file, "r") as f:
        text = f.read()

    extracted = extract_fields(text)
    validation = validate_fields(extracted)
    routing, reasons = process_claim(extracted, validation)

    output = {
        "extractedFields": extracted,
        "missingFields": validation["missingFields"],
        "recommendedRoute": routing,
        "reasoning": reasons
    }

    print(json.dumps(output, indent=2))

    with open("output.json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main(sys.argv[1])
