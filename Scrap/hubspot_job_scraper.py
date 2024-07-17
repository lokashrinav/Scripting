import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl

# Function to scrape the Shopify careers page for software intern positions
def hubspot_scraper():
    url = "https://www.hubspot.com/careers/jobs?hubs_signup-url=www.hubspot.com/careers/cambridge-ma&hubs_signup-cta=careers-location-bottom&page=1#office=cambridge,san-francisco,remote;language=english;"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("li", class_="fzBexj")
            
    joblist = []
    
    for job in job_listings:
        mini = [job.find_all("h3", class_="jPYStQ"), job.find_all("p", class_="gHfmgn"), job.find_all("a", class_="iHOrDr")]
        joblist.append(mini)
            
    final = []
    
    for a, b, c in joblist:
        a = a.text
        if (("software" in a.lower() or "swe " in a.lower() or "sw " in a.lower()) and " " in a.lower()) and "usa" in b.text.lower():
            final.append({"company": "Hubspot", "role": a, "link": b})
    
    
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(hubspot_scraper())

if __name__ == "__main__":
    main()
