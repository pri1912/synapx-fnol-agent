# FILE: main.py


"""
CLI entrypoint. Usage: python main.py <fnol_text_file>
Prints JSON result and writes output.json
"""


import sys
import json
from pathlib import Path
from processor import process_claim


def main(argv):
    if len(argv) < 2:
        print('Usage: python main.py <fnol_text_file>')
        sys.exit(1)


    path = Path(argv[1])
    if not path.exists():
        print(f'File not found: {path}')
        sys.exit(1)


    text = path.read_text(encoding='utf-8')
    result = process_claim(text)


    # Print JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))


    # Save
    out_path = Path('output.json')
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f'Saved output to {out_path}')




if __name__ == '__main__':
    # Modify sys.argv to include the sample FNOL file for execution within Colab
    main(['main.py', 'sample_fnol.txt'])