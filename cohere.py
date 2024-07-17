import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl

# Function to scrape the Shopify careers page for software intern positions
def cohere_scraper():
    final = []
    
    urls = [
    "https://jobs.lever.co/cohere/?location=United%20States",
    "https://jobs.lever.co/cohere/?location=Los%20Angeles",
    "https://jobs.lever.co/cohere/?location=New%20York%20City",
    "https://jobs.lever.co/cohere/?location=Remote",
    "https://jobs.lever.co/cohere/?location=Washington%2C%20DC",
    "https://jobs.lever.co/cohere/?location=Seattle",
    "https://jobs.lever.co/cohere/?location=San%20Francisco"]


    for ig in urls:
    
        response = requests.get(ig)
        soup = BeautifulSoup(response.text, "html.parser")
        job_listings = soup.find_all("a", class_="posting-title")    
        
        link_listings = []
        
        for job in job_listings:
            link = job.get("href")
            link_listings.append(link)
            
        title_listings = []
        
        for job in job_listings:
            title = job.find("h5")    
            title_listings.append(title)
            
        job_dict = {}
            
        for i, job in enumerate(title_listings):
                title = job.text
                link = link_listings[i]
                job_dict[title] = link
            
        real_job = {}
            
        for job in job_dict.keys():
            if "intern" in job.lower():
                real_job[job] = job_dict[job]
                
        
        roles = list(real_job.keys())
        values = list(real_job.values())
        
        for a, i in enumerate(roles):
            final.append({"company": "Cohere", "role": i, "link": values[a]})
    
    
    return final
            
        
        
    '''joblist = []
    
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
            job_dict[job[0].text] = "https://boards.greenhouse.io" + job[0].get("href")'''
    
    real_job = {}
    for job in job_dict.keys():
        if (("software" in job.lower() or "swe " in job.lower() or "sw " in job.lower()) and " " in job.lower()):
            real_job[job] = job_dict[job]
    
    roles = list(real_job.keys())
    values = list(real_job.values())
    final = []
    
    for a, i in enumerate(roles):
        final.append({"company": "Cohere", "role": i, "link": values[a]})
    
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(cohere_scraper())

if __name__ == "__main__":
    main()
