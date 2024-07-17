import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl

# Function to scrape the Shopify careers page for software intern positions
def zello_scraper():
    url = "https://zello.com/careers/#open-positions"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    job_listings = soup.find_all("h4", class_="heading-6")
    link_listings = soup.find_all("a", class_="careers__position__block-link")
        
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
        final.append({"company": "Zello", "role": i, "link": values[a]})
    
    
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(zello_scraper())

if __name__ == "__main__":
    main()
