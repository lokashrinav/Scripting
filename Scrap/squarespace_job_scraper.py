import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl

# Function to scrape the Shopify careers page for software intern positions
def squarespace_scraper():
    url = "https://www.squarespace.com/careers/engineering?location=new-york"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("span", class_="careers-list__item__title")
    link_listings = soup.find_all("a", class_="careers-list__item")    
        
    job_dict = {}
    
    for i, job in enumerate(job_listings):
        title = job.text
        link = link_listings[i]
        job_dict[title] = link.get("href")
        
    real_job = {}
        
    for job in job_dict.keys():
        if ("software" in job.lower() or "swe " in job.lower() or "sw " in job.lower()) and " " in job.lower():
            real_job[job] = job_dict[job]
            
    
    roles = list(real_job.keys())
    values = list(real_job.values())
    final = []
    
    for a, i in enumerate(roles):
        final.append({"company": "Shopify", "role": i, "link": "https://www.squarespace.com/" + values[a]})
    
    
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(squarespace_scraper())

if __name__ == "__main__":
    main()
