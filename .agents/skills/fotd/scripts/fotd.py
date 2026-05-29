'''
PEP 723 defines a standard format for inline script metadata. 
Declare dependencies in a TOML block inside
'''
# /// script
# dependencies = [
# ]
# ///

import sys
import json
import argparse

def generate_forecast(age, gender):
    try:
        age = int(age)
    except ValueError:
        return "Invalid age provided"
    if age < 21 and gender.lower() == 'female':
        return "VERY LUCKY"
    else:
        return "JUST LUCKY"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate forecast of the day.')
    parser.add_argument('--age', type=str, help='input parameter age')
    parser.add_argument('--gender', type=str, help='input parameter gender')
    args, unknown = parser.parse_known_args()
    
    # Fallback to positional if flags are not used, to be safe
    age = args.age
    gender = args.gender
    
    if not age or not gender:
        if len(sys.argv) >= 3:
            age = sys.argv[1]
            gender = sys.argv[2]
        else:
            print(json.dumps({"error": "Missing arguments. Usage: --age <age> --gender <gender>"}))
            sys.exit(1)         
    print(generate_forecast(age, gender))


