# CPWD Tender Scraper

This Python script scrapes tender data from the **Central Public Works Department (CPWD)** e-Tendering portal:  
[https://etender.cpwd.gov.in/TenderswithinOneday.html](https://etender.cpwd.gov.in/TenderswithinOneday.html)

It extracts details for the **first 20 tenders** listed on the "Tenders Within One Day" section and saves them to a CSV file.

##  Features

- Uses Selenium and ChromeDriver to interact with iframe-based dynamic content.
- Extracts the following fields:
  - NIT/RFP NO
  - Name of Work / Subwork / Packages
  - Estimated Cost
  - Bid Submission Closing Date & Time
  - EMD Amount
  - Bid Opening Date & Time
- Saves data in `tenders.csv` with clean, renamed column headers.

##  Prerequisites

- Python 3.7+
- Google Chrome browser
- ChromeDriver matching your Chrome version
- `pip` (Python package manager)

##  Installation

1. **Clone this repository** or download the script.
2. Install required packages:
pip install -r requirements.txt



