from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Constants for selectors
BASE_URL = "<BASE_URL_PLACEHOLDER>"
CONNECT_CHANNELS_BUTTON_SELECTOR = "#connect-channels"
INITIATE_AGGREGATION_BUTTON_SELECTOR = "#initiate-aggregation"
ERROR_LOG_SELECTOR = "#error-log"

# Implicit wait set to 0
driver = webdriver.Chrome(service=Service("<CHROME_DRIVER_PATH_PLACEHOLDER>"))
driver.implicitly_wait(0)

def test_e03_aggregation_proceeds_with_valid_channels():
    """Aggregation continues when one channel provides unsupported format."""
    # Traceability: TC-03 | KAN-245 | 

    # Step 1: Connect CDP to web, mobile, POS, and customer service channels, ensuring one channel sends data in an unsupported format.
    # Expected: All channels show active connection status; ingestion readiness confirmed.
    driver.get(BASE_URL + "/connect")
    driver.find_element(By.CSS_SELECTOR, CONNECT_CHANNELS_BUTTON_SELECTOR).click()
    # NOT UI-VERIFIABLE: requires API/DB validation — out of Selenium scope

    # Step 2: Initiate aggregation process.
    # Expected: Aggregation proceeds for valid channels; rejected channel’s data excluded; error message "Unsupported data format from channel" logged; no malformed data written to CDP.
    driver.find_element(By.CSS_SELECTOR, INITIATE_AGGREGATION_BUTTON_SELECTOR).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ERROR_LOG_SELECTOR)))
    error_log = driver.find_element(By.CSS_SELECTOR, ERROR_LOG_SELECTOR).text
    assert "Unsupported data format from channel" in error_log

    # TEARDOWN (non-UI): Purge test data after execution
driver.quit()