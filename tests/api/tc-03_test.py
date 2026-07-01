import requests

# Constants
BASE_URL = "<API_BASE_URL_PLACEHOLDER>"
REQUEST_TIMEOUT = 30
UNSUPPORTED_FORMAT_CHANNEL_ID = "<UNSUPPORTED_FORMAT_CHANNEL_ID>"
VALID_CHANNELS = ["<VALID_CHANNEL_ID_1>", "<VALID_CHANNEL_ID_2>"]  # Placeholder for valid channel IDs

def test_aggregation_proceeds_with_unsupported_format():
    """Ensure that aggregation proceeds for valid channels even if one channel sends unsupported data format."""
    # Traceability: PTS-2051 | PTS-742 | AC1, AC2

    # Step 1: Connect to channels and initiate aggregation
    # Expected: All channels show active connection status; ingestion readiness confirmed.
    response = requests.post(
        BASE_URL + "/connect",
        json={"channels": VALID_CHANNELS + [UNSUPPORTED_FORMAT_CHANNEL_ID]},
        timeout=REQUEST_TIMEOUT
    )
    assert response.status_code == 200

    # Step 2: Initiate aggregation process.
    # Expected: Aggregation proceeds for valid channels; rejected channel’s data excluded; error message "Unsupported data format from channel" logged; no malformed data written to CDP.
    aggregation_response = requests.post(
        BASE_URL + "/aggregate",
        timeout=REQUEST_TIMEOUT
    )
    
    assert aggregation_response.status_code == 200
    assert "Unsupported data format from channel" in aggregation_response.text

    # Additional observability checks can be added here if required.
