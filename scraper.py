from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# CSV column rename dictionary
csv_cols = {
    "NIT/RFP NO": "ref_no",
    "Name of Work / Subwork / Packages": "title",
    "Estimated Cost": "tender_value",
    "Bid Submission Closing Date & Time": "bid_submission_end_date",
    "EMD Amount": "emd",
    "Bid Opening Date & Time": "bid_open_date"
}

# Initialize WebDriver (adjust path to your chromedriver)
driver = webdriver.Chrome(service=Service("chromedriver.exe"))

try:
    driver.get("https://etender.cpwd.gov.in/TenderswithinOneday.html")

    # Wait for iframe to load and switch into it
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
    )

    # Wait for the tenders table to load
    table = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "nit_new_table"))
    )

    # Find all rows in tbody
    rows = table.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")

    tenders_data = []

    for row in rows[:20]:  # first 20 tenders
        cells = row.find_elements(By.TAG_NAME, "td")
        # Columns as per table (inspect site if needed)
        tender = {
            "NIT/RFP NO": cells[0].text.strip(),
            "Name of Work / Subwork / Packages": cells[1].text.strip(),
            "Estimated Cost": cells[2].text.strip(),
            "Bid Submission Closing Date & Time": cells[3].text.strip(),
            "EMD Amount": cells[4].text.strip(),
            "Bid Opening Date & Time": cells[5].text.strip()
        }
        tenders_data.append(tender)

    # Write to CSV
    with open("tenders.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_cols.values())
        writer.writeheader()
        for tender in tenders_data:
            # Rename keys according to csv_cols
            row_renamed = {csv_cols[k]: v for k, v in tender.items()}
            writer.writerow(row_renamed)

    print("Saved tenders.csv")

finally:
    driver.quit()
