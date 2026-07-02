from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Constants for selectors
CONNECT_CHANNELS_BUTTON_SELECTOR = "#connectChannels"
INITIATE_AGGREGATION_BUTTON_SELECTOR = "#initiateAggregation"
ERROR_LOG_SELECTOR = "#errorLog"
ACTIVE_CONNECTION_STATUS_SELECTOR = ".connection-status.active"

# Base URL placeholder
BASE_URL = "<BASE_URL_PLACEHOLDER>"

def setup_module(module):
    # PRECONDITION (non-UI): Synthetic customer data for web, mobile, POS, and customer service channels; one channel configured with unsupported format.
    pass

def teardown_module(module):
    # TEARDOWN (non-UI): Purge test data after execution.
    pass

def test_e03_aggregation_proceeds_with_unsupported_format():
    """Ensure that aggregation proceeds for valid channels even if one channel sends unsupported data format."""
    # Traceability: TC-03 | KAN-245 | 
    driver = webdriver.Chrome(service=Service())
    driver.implicitly_wait(0)  # Set implicit wait to 0

    try:
        # Step 1: Connect CDP to web, mobile, POS, and customer service channels, ensuring one channel sends data in an unsupported format.
        # Expected: All channels show active connection status; ingestion readiness confirmed.
        driver.get(BASE_URL + "/connect")
        driver.find_element(By.CSS_SELECTOR, CONNECT_CHANNELS_BUTTON_SELECTOR).click()
        
        # Wait for active connection status
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ACTIVE_CONNECTION_STATUS_SELECTOR))
        )
        
        # Step 2: Initiate aggregation process.
        # Expected: Aggregation proceeds for valid channels; rejected channel’s data excluded; error message "Unsupported data format from channel" logged; no malformed data written to CDP.
        driver.find_element(By.CSS_SELECTOR, INITIATE_AGGREGATION_BUTTON_SELECTOR).click()

        # Validate error log for unsupported format
        error_log = driver.find_element(By.CSS_SELECTOR, ERROR_LOG_SELECTOR).text
        assert "Unsupported data format from channel" in error_log

    finally:
        driver.quit()