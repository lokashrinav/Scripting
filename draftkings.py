import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime
import ssl





# Function to scrape the Shopify careers page for software intern positions
def draftkings_scraper():
    state_initials = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
                    "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
                    "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
                    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
                    "WV", "WY", "DC", "USA"]

    states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa",
                    "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri",
                    "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
                    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin",
                    "West Virginia", "Wyoming", "District of Columbia", "United States of America"]
    
    states += state_initials
    
    states = [' ' + state for state in states]
    
    url = "https://careers.draftkings.com/jobs/?country=United%20States&pagesize=10000#results"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = soup.find_all("a", class_="js-view-job")
    locations = soup.find_all("div", class_="card-body")
    
    link_listings = []
    for i in locations:
        idk = i.find("li")
        link_listings.append(idk)
                
    job_dict = {}
        
    for i, job in enumerate(job_listings):
        title = job.text
        link = job_listings[i]
        job_dict[title] = [link.get("href"), link_listings[i]]
        
    real_job = {}
            
    for job in job_dict.keys():
        if "intern" in job.lower():
            real_job[job] = job_dict[job]
                

    

    new_list2 = {}
            
    for job in real_job.keys():
        bool1 = False
        for i in states:
            if i in real_job[job][1].text:
                print(real_job[job])
                bool1 = True
        if bool1:
            new_list2[job] = real_job[job]
                        
        
        
        
    
    roles = list(new_list2.keys())
    values = list(new_list2.values())
    final = []
    
    for a, i in enumerate(roles):
        final.append({"company": "Draft Kings", "role": i, "link": values[a][0]})
    
    
    return final
      
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    
    print(draftkings_scraper())
    
    #print(draftkings_scraper())

if __name__ == "__main__":
    main()
