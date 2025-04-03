from selenium import webdriver # allow launching browser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
import time
import pandas as pd

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("--incognito")  # Open browser in incognito mode
chromedriver_path = "C:/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe"


# Function to create a new WebDriver instance
def create_webdriver():
    # Create a Service object for ChromeDriver
    service = Service(chromedriver_path)

    # Initialize Chrome WebDriver with service and options
    return webdriver.Chrome(service=service, options=driver_option)

browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")
browser.maximize_window()
time.sleep(3)

projects = browser.find_elements(By.XPATH,"//h1[@class='h3 lh-condensed']")

projects_list = {}

for p in projects:
    p_name = p.text
    # extracting proj urls
    p_url = browser.find_element(By.TAG_NAME,"a").get_attribute("href")
    projects_list[p_name] = p_url #storing values as key and values in dict

browser.quit()
#####################################################################################

# converting dict into dataframe
project_df = pd.DataFrame.from_dict(projects_list,orient="index")
#adding col for proj names
project_df["p_name"] = project_df.index
# print(project_df)
#rename cols
project_df.columns = ["Project_url","Project_name"]
#reset index
project_df = project_df.reset_index(drop=True)
# print(project_df)

#save df to csv file
project_df.to_csv("projects_list.csv",index=False)
print("data saved to projects_list.csv")



