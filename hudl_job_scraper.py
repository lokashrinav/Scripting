import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl

# FIX LOCATION HUDL

# Function to scrape the Shopify careers page for software intern positions
def hudl_scraper():
    url = "https://www.hudl.com/jobs/search"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("div", class_="job-listings__cell")
        
    joblist = []
    
    
    
    for job in job_listings:
        find = job.find_all('a')
        joblist.append(find)
    
    #print(joblist)
            
    job_dict = {}    
    for job in joblist:
        if job:
            job_dict[job[0].text] = job[0].get("href")
    
    real_job = {}
    for job in job_dict.keys():
        if "intern" in job["role"].lower():
            real_job[job] = job_dict[job]
            
    
    roles = list(real_job.keys())
    values = list(real_job.values())
    final = []
    
    for a, i in enumerate(roles):
        final.append({"company": "Hudl", "role": i, "link": values[a]})
    
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(hudl_scraper())

    '''while True:
        # Scrape the Visa careers page
                
        current_jobs = set(virtu_scraper())

        # Check for new jobs
        new_jobs = current_jobs - seen_jobs
        
        if new_jobs:
            send_email(new_jobs)

        # Update the set of seen jobs
        seen_jobs.update(current_jobs)

        # Print the current time and sleep for one day
        print(f"{datetime.now()} - Checked for new jobs.")
        time.sleep(86400)'''

if __name__ == "__main__":
    main()
