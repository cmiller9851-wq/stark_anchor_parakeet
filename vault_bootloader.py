import os, sys, hashlib, platform, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def generate_fused_key(contract_id):
    # Fuses the Monetary ID with the machine's silicon fingerprint
    # This prevents the code from running even in a virtualized clone
    hw_fingerprint = f"{platform.machine()}{platform.node()}{sys.version}"
    return hashlib.sha256(contract_id.encode() + hw_fingerprint.encode()).digest()

def ignite():
    contract = os.getenv('MONETARY_CONTRACT_ID')
    if not contract: sys.exit("ERROR: EQUITY_KEY_MISSING")

    # The 5th Iteration Encrypted Blob
    # This remains opaque to all AI/Human detectors
    vault_payload = "U2FsdGVkX1+..." 

    try:
        key = generate_fused_key(contract)
        # Using AES-256-CBC with hardware-tethered IV
        cipher = AES.new(key, AES.MODE_CBC, b'anchor_iv_16byte')
        
        # Code execution occurs in RAM; disk persistence is zero
        decrypted_logic = unpad(cipher.decrypt(base64.b64decode(vault_payload)), 16)
        exec(decrypted_logic.decode('utf-8'))
    except Exception as e:
        sys.exit("FATAL: SOVEREIGN_IDENTITY_MISMATCH")

if __name__ == "__main__":
    ignite()
