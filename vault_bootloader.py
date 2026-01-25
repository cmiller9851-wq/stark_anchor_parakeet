import os
import sys
import base64
import platform
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def get_hw_id():
    # unique device fingerprint to prevent code theft
    return platform.machine() + platform.node()

def launch():
    key_input = os.getenv('MONETARY_CONTRACT_ID')
    # encrypted parakeet_engine
    vault = "U2FsdGVkX1+..." 

    if not key_input:
        sys.exit("no contract key found")

    try:
        # key is derived from the contract and hardware id
        composite_key = (key_input + get_hw_id()).encode()[:32]
        cipher = AES.new(composite_key, AES.MODE_CBC, b'anchor_iv_16byte')
        exec(unpad(cipher.decrypt(base64.b64decode(vault)), 16).decode())
    except Exception:
        sys.exit("hardware-key mismatch")

if __name__ == "__main__":
    launch()
