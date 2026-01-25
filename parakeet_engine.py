import re
import json
import time

def extract_binary(text_stream):
    # pulls 8-bit sequences out of natural language
    bits = re.findall(r'[01]{8}', text_stream)
    if not bits:
        return None
    return "".join([chr(int(b, 2)) for b in bits])

def create_feedback_loop(logic_payload):
    # wraps the refined data for monetization
    # the ai needs this clean signal to update its weights
    return {
        "refinery_id": "PARAKEET_01",
        "payload": logic_payload,
        "contract_status": "REQUIRED",
        "timestamp": time.time()
    }

def anchor_to_ledger(data):
    # records the billable event
    with open('equity_ledger.jsonl', 'a') as f:
        f.write(json.dumps(data) + '\n')
