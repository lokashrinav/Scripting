import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl

# Function to scrape the Shopify careers page for software intern positions
def yext_scraper():
    url = "https://boards.greenhouse.io/yext/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("div", class_="opening")
        
    joblist = []
    
    locations = []
        
    for job in job_listings:
        find = job.find_all('a')
        joblist.append(find)
        location = job.find_all("span", class_="location")
        locations.append(location)            
    #print(joblist)
            
    job_dict = {}    
    for i, job in enumerate(joblist):
        if job and "NY" in locations[i][0].text:
            job_dict[job[0].text] = "https://boards.greenhouse.io" + job[0].get("href")
    
    real_job = {}
    for job in job_dict.keys():
        if "intern" in job.lower():
            real_job[job] = job_dict[job]
    
    roles = list(real_job.keys())
    values = list(real_job.values())
    final = []
    
    for a, i in enumerate(roles):
        final.append({"company": "Yext", "role": i, "link": values[a]})
    
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(yext_scraper())

if __name__ == "__main__":
    main()
