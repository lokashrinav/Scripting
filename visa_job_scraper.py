import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def visa_scraper():
    # Create a new instance of a web browser
    driver = webdriver.Chrome()  # Or choose another browser driver
    
    # Open the website
    url = "https://corporate.visa.com/en/jobs/?q=intern&cities=Ashburn&cities=Atlanta&cities=Austin&cities=Bellevue&cities=Denver&cities=Foster%20City&cities=Highlands%20Ranch&cities=Mentor&cities=Miami&cities=New%20York&cities=Oakland&cities=San%20Francisco&cities=San%20Juan&cities=Washington"
    driver.get(url)

    # Wait for the cookie accept button to be clickable and click it
    wait = WebDriverWait(driver, 10)
    accept_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wscrOk")))
    accept_button.click()
    
    time.sleep(4)
    
    load_more_button = driver.find_element(By.CLASS_NAME, "vs-px-4")

    # Loop to click the "Load More" button until it disappears
    while True:
            # Click the "Load More" button
        load_more_button.click()
            # Wait for a short delay to allow the new content to load
        time.sleep(4)
        try:
            load_more_button = driver.find_element(By.CLASS_NAME, "vs-px-4")
        except:
            break

    # Get the page source after accepting cookies
    html = driver.page_source
    
    # Close the browser
    driver.quit()
    
    
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all job listings
    job_listings = soup.find_all("a", class_="vs-link-job")
        
    job_dict = {}
    
    for job in job_listings:
        title = job.text
        link = job.get("href")
        job_dict[title] = link
        
    real_job = {}
    
    for job in job_dict.keys():
        if "intern" in job.lower():
            real_job[job] = job_dict[job]
    
    roles = list(real_job.keys())
    values = list(real_job.values())
    final = []
    
    for a, i in enumerate(roles):
        final.append({"company": "Visa", "role": i, "link": values[a]})
            
    return final
        
    
    
                                    
            
    
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    while True:
        # Scrape the Visa careers page
        current_jobs = set(visa_scraper())

        # Check for new jobs
        new_jobs = current_jobs - seen_jobs

        # Update the set of seen jobs
        seen_jobs.update(current_jobs)

        # Print the current time and sleep for one day
        print(f"{datetime.now()} - Checked for new jobs.")
        time.sleep(86400)
    
if __name__ == "__main__":
    main()

    
    