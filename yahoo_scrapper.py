import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# === Enhanced Chrome options for SSL and automation handling ===
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--disable-web-security')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.set_capability('acceptInsecureCerts', True)

# === WebDriver setup with updated options ===
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# === Read input files ===
df = pd.read_excel(r"C:\projects\Pinegap_python\VQ-Scraper\companies.xlsx")
visible_alpha_df = pd.read_csv("visible_alpha_surprises.csv")

# === Select companies to scrape ===
company_df = df.iloc[2:152]
company_names = company_df['Company_name'].values

# === Prepare output list ===
output_data = []
base_url = 'https://finance.yahoo.com/'

# === Loop through companies ===
for company in company_names:
    try:
        print(f"Processing {company}...")
        driver.get(base_url)

        # Handle potential SSL warnings
        if "Your connection is not private" in driver.page_source:
            advanced_button = driver.find_element(By.ID, 'details-button')
            advanced_button.click()
            proceed_link = driver.find_element(By.ID, 'proceed-link')
            proceed_link.click()

        # Search for company
        search_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "yfin-usr-qry"))
        )
        search_input.clear()
        search_input.send_keys(company)
        search_input.submit()

        # Click first result
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-test='quoteLink']"))
        ).click()

        # Navigate to Financials
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Financials"))
        ).click()

        # Extract revenue data
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Total Revenue')]"))
        )
        revenue_elements = driver.find_elements(By.XPATH, "//div[contains(text(), 'Total Revenue')]/following::div[1]")
        revenue_values = [rev.text for rev in revenue_elements]

        # Match with Visible Alpha data
        match = visible_alpha_df[visible_alpha_df['company_name'].str.lower() == company.lower()]
        v_company = match.iloc[0]['company_name'] if not match.empty else None
        v_value = match.iloc[0]['v'] if not match.empty else None

        output_data.append({
            "Company": company,
            "Revenue Data": revenue_values,
            "v_company_name": v_company,
            "v": v_value
        })

    except Exception as e:
        print(f"Error processing {company}: {str(e)}")
        output_data.append({
            "Company": company,
            "Revenue Data": [],
            "Error": str(e),
            "v_company_name": None,
            "v": None
        })

# === Save results ===
output_df = pd.DataFrame(output_data)
output_df.to_csv("list1.csv", index=False)

# === Close browser ===
driver.quit()