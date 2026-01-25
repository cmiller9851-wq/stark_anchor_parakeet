import hashlib
import json

def generate_bridged_proof(artifact_id, ledger_state, sensor_attestation):
    """
    Combines mathematical ledger state with physical sensor attestation
    to create a 'Settlement Proof'.
    """
    payload = {
        "artifact": artifact_id,
        "state": ledger_state,
        "physical_truth": sensor_attestation
    }
    
    proof_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    return proof_hash

if __name__ == "__main__":
    # Artifact 015 - Logistics Match
    artifact = "015"
    m_state = "000F580501" # Mathematical Truth
    p_truth = "MDT_GARAGE_GPS_VERIFIED" # Physical Truth
    
    proof = generate_bridged_proof(artifact, m_state, p_truth)
    print(f"Final Bridged Settlement Proof: {proof}")
