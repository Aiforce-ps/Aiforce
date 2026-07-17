from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants for selectors
INITIATE_AGGREGATION_BUTTON_SELECTOR = "#initiate-aggregation"
UNIFIED_PROFILES_COUNT_SELECTOR = "#unified-profiles-count"

# Base URL placeholder
BASE_URL = "<BASE_URL_PLACEHOLDER>"

# Setup WebDriver
service = Service("<CHROME_DRIVER_PATH_PLACEHOLDER>")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(0)  # Set implicit wait to 0

def test_tc_01_successful_aggregation():
    """Successful aggregation of customer data from all channels."""
    # Traceability: TC-01 | KAN-245 | 
    driver.get(BASE_URL + "/aggregation-page")  # Navigate to the aggregation page

    # Step 1: Initiate the aggregation process with customer data from web, mobile, POS, and customer service channels.
    # Expected: The CDP creates a unified profile for each customer.
    driver.find_element(By.CSS_SELECTOR, INITIATE_AGGREGATION_BUTTON_SELECTOR).click()

    # Step 2: Verify the total number of unified profiles created.
    # Expected: The total number of unified profiles matches the total number of distinct customers across all channels.
    unified_profiles_count = driver.find_element(By.CSS_SELECTOR, UNIFIED_PROFILES_COUNT_SELECTOR).text
    assert int(unified_profiles_count) > 0  # Assert that unified profiles are created

    # TEARDOWN (non-UI): Close the browser
    driver.quit()