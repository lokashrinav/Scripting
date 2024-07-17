import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl

# Function to scrape the Shopify careers page for software intern positions
def shopify_scraper():
    url = "https://www.shopify.com/careers?search%5Bkeywords%5D=software&search%5Blocations%5D%5B%5D=US"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("h3", class_="mb-2")
    link_listings = soup.find_all("a", class_="py-6")
        
    job_dict = {}
    
    for i, job in enumerate(job_listings):
        title = job.text
        link = link_listings[i]
        job_dict[title] = link.get("href")
        
    real_job = {}
        
    for job in job_dict.keys():
        if "intern" in job.lower():
            real_job[job] = job_dict[job]
            
    
    roles = list(real_job.keys())
    values = list(real_job.values())
    final = []
    
    for a, i in enumerate(roles):
        final.append({"company": "Shopify", "role": i, "link": "https://www.shopify.com" + values[a]})
    
    
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(shopify_scraper())

if __name__ == "__main__":
    main()
