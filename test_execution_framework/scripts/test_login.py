import os
import time
import csv
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    # Build path dynamically to avoid hardcoding issues
    base_dir = os.path.dirname(os.path.dirname(__file__))   # project root
    driver_path = os.path.join(base_dir, "drivers", "chromedriver.exe")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_search_amazon_watches(driver):
    # Step 1: Open Amazon
    driver.get("https://www.amazon.in")

    # Step 2: Find the search bar
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")

    # Step 3: Enter "watches" and press Enter
    search_box.send_keys("watches")
    search_box.send_keys(Keys.RETURN)

    # Step 4: Wait for results to load
    time.sleep(3)

    # Step 5: Fetch product details
    results = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

    data = []
    for item in results[:10]:  # limit to top 10 results
        try:
            title = item.find_element(By.CSS_SELECTOR, "span.a-text-normal").text
        except:
            title = "N/A"
        try:
            price = item.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
        except:
            price = "N/A"
        try:
            link = item.find_element(By.CSS_SELECTOR, "a.a-link-normal").get_attribute("href")
        except:
            link = "N/A"

        data.append([title, price, link])

    # Step 6: Save to CSV
    reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    file_path = os.path.join(reports_dir, "amazon_watches.csv")

    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Link"])
        writer.writerows(data)

    print(f"\n✅ Results saved to: {file_path}")

    # Simple validation
    assert len(data) > 0, "No search results found for 'watches'"
