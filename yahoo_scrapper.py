import csv
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
website = 'https://finance.yahoo.com/'
output_file = "nw_yahoo_ticker.csv"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
output_data = []
# ==== Loop through each company ====
for company in company_list:
    try:
        driver.get(website)
        search_container = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@class='_yb_d7nywr _yb_owcm9n  _yb_ikgg1k finsrch-inpt  ']"))
        )
        search_container.click()
        search_container.send_keys(company)
        time.sleep(2)
        for i in range(2):
            matched_name = np.nan
            try:
                result_xpath = f"//ul[@role='listbox']/li[contains(@data-id , 'result-quotes-{i}')]/div[@class='modules-module_quoteLeftCol__yV9LA modules-module_Ell__N1WPm modules-module_IbBox__NPYId']"
                search_result = WebDriverWait(driver, 4).until(
                    EC.element_to_be_clickable((By.XPATH, result_xpath))
                )
                search_result.click()
                time.sleep(3)
                try:
                    matched_name = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located((By.XPATH, "//h1[@class='yf-xxbei9']"))
                    ).text.strip()
                except Exception:
                    matched_name = np.nan
            except Exception as e:
                print(f":x: Skipped result-{i+1} for '{company}': {e}")
            output_data.append({
                'Input_Company': company,
                'Matched_Company': matched_name
            })
            # Go back to search
            driver.get(website)
            search_container = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@class='_yb_d7nywr _yb_owcm9n  _yb_ikgg1k finsrch-inpt  ']"))
            )
            search_container.click()
            search_container.send_keys(company)
            time.sleep(2)
    except Exception as e:
        print(f":x: Error while processing '{company}': {e}")
driver.quit()
# ==== Save to CSV ====
df = pd.DataFrame(output_data)
df.to_csv(output_file, index=False)
print(f"\n:file_folder: CSV saved as: {output_file}")