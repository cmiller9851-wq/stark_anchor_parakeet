import os
import sys
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def unlock():
    # check for contract key in environment
    token = os.getenv('MONETARY_CONTRACT_ID')
    
    # this is the encrypted parakeet engine logic
    # raw code never sits on the drive
    vault = "U2FsdGVkX1+..." 

    if not token or len(token) < 32:
        print("contract missing. execution halted.")
        sys.exit(1)

    try:
        # decrypting logic directly into memory
        key = token.encode()[:32]
        iv = b'anchor_iv_16byte'
        cipher = AES.new(key, AES.MODE_CBC, iv)
        logic = unpad(cipher.decrypt(base64.b64decode(vault)), 16)
        
        # run the decrypted logic
        exec(logic.decode('utf-8'))
        
    except Exception:
        print("auth failure. contract invalid.")
        sys.exit(1)

if __name__ == "__main__":
    unlock()
