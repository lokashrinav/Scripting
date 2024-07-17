import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl

# Function to scrape the Shopify careers page for software intern positions
def airbnb_scraper():
    url = "https://careers.airbnb.com/positions/?_search_input=intern&_offices=united-states"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("h3", class_="text-size-4")
    
    stuff = []
    
    for job in job_listings:
        stuff.append(job.find_all("a"))
            
    job_dict = {}
            
    for i in stuff:
        if i:
            job_dict[i[0].text] = i[0].get("href")
                    
        
    '''job_dict = {}
    
    for i, job in enumerate(job_listings):
        title = job.text
        link = link_listings[i]
        job_dict[title] = link.get("href")'''
        
    real_job = {}
    
    #        if ("software" in job.lower() or "swe " in job.lower() or "sw " in job.lower() or (("backend" in job.lower() or "frontend" in job.lower() or "android" in job.lower() or "ios" in job.lower() or "mobile" in job.lower() or ("full" in job.lower() and 'stack' in job.lower())) and ("engineer" in job.lower() or "developer" in job.lower()))) and "intern" in job.lower():
        
    for job in job_dict.keys():
        if "intern" in job.lower():
            real_job[job] = job_dict[job]
            
    
    roles = list(real_job.keys())
    values = list(real_job.values())
    final = []
    
    for a, i in enumerate(roles):
        final.append({"company": "Airbnb", "role": i, "link": values[a]})
    
    
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(airbnb_scraper())

if __name__ == "__main__":
    main()
