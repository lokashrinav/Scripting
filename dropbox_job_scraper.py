import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl

# Function to scrape the Shopify careers page for software intern positions
def dropbox_scraper():
    url = "https://jobs.dropbox.com/all-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    link_listings = soup.find_all("a", class_="open-positions__listing-link")
    job_listings = soup.find_all("h5", class_="open-positions__listing-title")
    
    #print(joblist)
            
            
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
        final.append({"company": "Dropbox", "role": i, "link": values[a]})
        
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(dropbox_scraper())

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
