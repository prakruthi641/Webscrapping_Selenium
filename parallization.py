from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# WebDriver Setup (Use Headless Mode to Prevent UI Interference)
def create_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Run in incognito mode
    # options.add_argument("--headless")  # Run without opening browser (important for parallel execution)
    chromedriver_path = "C:/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe"

    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=options)

# Web Scraping Function
def scrape_url(url):
    new_browser = create_webdriver()
    new_browser.get(url)
    time.sleep(2)  # Give time for the page to load

    data = {"url": url}

    new_browser.quit()
    return data

# Safe Multiprocessing Execution
if __name__ == "__main__":
    # List of URLs to Scrape
    urlarray = [
        "https://github.com/collections/machine-learning",
        "https://testautomationpractice.blogspot.com/"
    ]

    # Execute Scraping in Parallel
    with ProcessPoolExecutor(max_workers=4) as executor:
        future_results = {executor.submit(scrape_url, url) for url in urlarray}

    # Collect Results
    results = []
    for future in concurrent.futures.as_completed(future_results):
        results.append(future.result())

    print(results)
