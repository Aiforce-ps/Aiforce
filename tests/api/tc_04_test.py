import requests

BASE_URL = "<API_BASE_URL_PLACEHOLDER>"
REQUEST_TIMEOUT = 30

def test_tc_04_data_encryption_during_aggregation():
    """Ensure data encryption during aggregation"""
    # Traceability: TC-04 | KAN-245 | 

    # Step 1: Initiate aggregation process with sample dataset containing sensitive fields.
    response = requests.post(
        f"{BASE_URL}/aggregation",
        json={"dataset": "sample_dataset_with_sensitive_fields"},
        timeout=REQUEST_TIMEOUT
    )
    
    # Expected: All sensitive fields are encrypted before aggregation begins.
    assert response.status_code == 200
    assert "encryption_status" in response.json()
    assert response.json()["encryption_status"] == "initiated"

    # Step 2: Complete aggregation process and inspect output dataset.
    response = requests.get(
        f"{BASE_URL}/aggregation/output",
        timeout=REQUEST_TIMEOUT
    )
    
    # Expected: Output dataset contains only encrypted values for sensitive fields; no plaintext data is present.
    assert response.status_code == 200
    output_data = response.json()
    assert all(field["value"].startswith("encrypted_") for field in output_data["sensitive_fields"])
