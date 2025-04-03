Web Scraping with Selenium

📌 Project Overview

This project is a web scraping script using Selenium to extract data from multiple websites in parallel. The script collects information from specified URLs and stores the extracted data in a structured format, such as a CSV file.

🌟 Features:

Uses Selenium WebDriver for automated browsing.

Supports incognito mode for privacy.

Extracts data from multiple websites.

Implements parallel processing with ProcessPoolExecutor for efficiency.

Saves extracted data in a structured CSV format.

🛠️ Tech Stack

Python 🐍

Selenium WebDriver 🌐

Pandas 📊 (for data handling)

Concurrent Futures 🚀 (for parallel execution)

📂 Project Structure

📁 Webscraping_Selenium
│── 📄 scraper.py              # Main web scraping script
│── 📄 requirements.txt        # Required Python dependencies
│── 📄 project_list.csv        # Extracted data output
│── 📄 README.md               # Project Documentation

🚀 Installation & Setup

1️⃣ Install Required Dependencies

Ensure you have Python 3.x installed. Then, install the required dependencies:

pip install -r requirements.txt

2️⃣ Download & Set Up ChromeDriver

Selenium requires a ChromeDriver to control the Chrome browser. Download the appropriate version from:
ChromeDriver Downloads

Then, set the ChromeDriver path in the script:

chromedriver_path = "C:/chromedriver-win64/chromedriver.exe"

3️⃣ Run the Scraper

Execute the script to start web scraping:

python scraper.py

🖥️ Code Explanation

1️⃣ Creating a WebDriver Instance

def create_webdriver():
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)

Initializes Chrome WebDriver in incognito mode.

Uses Service() to define the ChromeDriver path.

2️⃣ Web Scraping Logic

browser.get("https://github.com/collections/machine-learning")
projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

Opens the target website.

Extracts all project names using XPath.

3️⃣ Parallel Processing for Multiple Websites

with ProcessPoolExecutor(max_workers=4) as executor:
    future_results = {executor.submit(scrape_url, url) for url in urlarray}

Runs multiple web scraping tasks in parallel.

Uses ProcessPoolExecutor to speed up execution.

4️⃣ Saving Data to CSV

project_df.to_csv("project_list.csv", index=False)
print("Data saved to project_list.csv")

Converts extracted data into a Pandas DataFrame.

Saves the data into a CSV file.

📊 Sample Output (CSV Format)

Project Name    Project URL

TensorFlow   https://github.com/tensorflow

PyTorch   https://github.com/pytorch

🛠️ Troubleshooting

Error: chromedriver not found

Ensure ChromeDriver path is correct.

Check Chrome version compatibility with ChromeDriver.

Selenium Timeout Exception

Increase time.sleep() duration.

Use WebDriverWait to ensure elements load properly.

