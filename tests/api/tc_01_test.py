import requests

BASE_URL = "<API_BASE_URL_PLACEHOLDER>"
REQUEST_TIMEOUT = 30

def test_pts_2051_successful_aggregation_of_customer_data():
    """Apply price range filter on product listing page"""
    # Traceability: PTS-2051 | PTS-742 | AC1, AC2

    # Step 1: Navigate to the product listing page as SHOPPER_GUEST.
    response = requests.get(f"{BASE_URL}/product-listing", timeout=REQUEST_TIMEOUT)
    # Expected: Listing page loads with all products and the price filter control visible.
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

    # Step 2: Enter 50 in the minimum price field.
    min_price = 50
    response = requests.post(f"{BASE_URL}/product-listing/filter", json={"min_price": min_price}, timeout=REQUEST_TIMEOUT)
    # Expected: Field accepts and displays 50.
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

    # Step 3: Enter 200 in the maximum price field.
    max_price = 200
    response = requests.post(f"{BASE_URL}/product-listing/filter", json={"max_price": max_price}, timeout=REQUEST_TIMEOUT)
    # Expected: Field accepts and displays 200.
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

    # Step 4: Click Apply.
    response = requests.post(f"{BASE_URL}/product-listing/filter/apply", json={"min_price": min_price, "max_price": max_price}, timeout=REQUEST_TIMEOUT)
    # Expected: Listing refreshes to show only products priced 50 to 200 USD inclusive; result count matches the filtered total.
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    assert response.json().get("result_count") == response.json().get("filtered_count"), "Result count does not match the filtered total."

    # Step 5: Click Reset.
    response = requests.post(f"{BASE_URL}/product-listing/filter/reset", timeout=REQUEST_TIMEOUT)
    # Expected: All products are shown again and the result count returns to the unfiltered total.
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
