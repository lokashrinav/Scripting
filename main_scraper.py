from shopify_job_scraper import *
from visa_job_scraper import *
from virtu_financial_job_scraper import *
from hudl_job_scraper import *
from yext_job_scraper import *
from airbnb_job_scraper import *
from dropbox_job_scraper import *
from cohere import *
from lyft import *
from quora import *
from ramp import *
from docker import *
from replity import *
from duolingo import *
from draftkings import *
from splunk import *
from zello import *
from khanacademy import *
from transmarketgroup import *
from netflix import *
from total_scrape import *
from workday import *
from patreon import *
from discord import *
from loop import *
from figma import *
from doordash import *
from notion import *
from openfin95 import *
from robinhood import *
from bridgewater import *
from sentry import *
from gecko import *
from sezzle import *
from benchling import * 
from verkada import *
from fetch import *
from neuralink import *
from twilio import *
from lucidmotors import *
from playstation import *
from verisign import *
from codesignal import *
from zwift import *
from willowtree import *
from nextdoor import *
from perpay import *
from seatgeek import *
from amazon_final import *



import time
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
import ssl
import requests
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from cambly import *

def Merge(dict1, dict2): 
    res = dict1 | dict2
    return res

def send_email(new_jobs):
    sender_email = "lokashrinav@gmail.com"
    receiver_email = "lokashrinav@gmail.com"
    password = "evtt ieto slnx gsbj"

    subject = "New software intern positions"
    body = "\n".join(new_jobs)

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
def parseGithub():
    seen_jobs = []
    url = "https://github.com/lokashrinav/Random_SWE_Job_Github/blob/main/README.md"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        print(len(columns))
        company = columns[0].text.strip()
        role = columns[1].text.strip()
        link = columns[2].find('a')['href']
        seen_jobs.append({'company': company, 'role': role, 'link': link})
    return seen_jobs

        
# Main function
def main():
    # Initialize the list of seen jobs
    seen_jobs = set()
    username = "lokashrinav"
    repository = "Random-SWE-Job-Github"
    readme_path = "README.md"
        
    seen_jobs = parseGithub()
    
    while True:
        # Scrape the Visa careers page
        
        run_spiders_and_save_data()
        
                
        import json

        with open('netflix_jobs.json', 'r') as f:
            # Load the JSON data into a Python object (in this case, a list)
            netflix = json.load(f)

        with open('lyft_jobs.json', 'r') as f:
            # Load the JSON data into a Python object (in this case, a list)
            lyft = json.load(f)     
            
        '''with open('job_postings.json', 'r') as f:
            # Load the JSON data into a Python object (in this case, a list)
            workday = json.load(f)  '''
            
        #workday_scrape()
        # Not used: shopify_scraper(), workday, + visa_scraper()
                                            
        merged = (lyft + netflix + virtu_scraper() 
                + hudl_scraper() + dropbox_scraper() + airbnb_scraper() 
                + yext_scraper() + cohere_scraper() + quora_scraper() 
                + dropbox_scraper() + ramp_scraper() + replit_scraper() 
                + duolingo_scraper()  + draftkings_scraper() + splunk_scraper() 
                + zello_scraper() + khanacademy_scraper() + transmarketgroup_scraper()
                + cambly_scraper() + discord_scraper() + loop_scraper() 
                + figma_scraper() + doordash_scraper() + notion_scraper() 
                + openfin_scraper() + robinhood_scraper() + bridgewater_scraper() 
                + sentry_scraper() + gecko_scraper() + sezzle_scraper() 
                + benchling_scraper() + verkada_scraper() + fetch_scraper() 
                + neuralink_scraper() + twilio_scraper() + lucidmotors_scraper()
                + playstation_scraper() + verisign_scraper() + codesignal_scraper() 
                + zwift_scraper() + willowtree_scraper() + nextdoor_scraper()
                + perpay_scraper() + seatgeek_scraper() + amazon_scraper())
                
        '''(netflix_scraper()shopify_scraper() + virtu_scraper() + hudl_scraper() +
                dropbox_scraper() + airbnb_scraper() + yext_scraper() +
                cohere_scraper() + lyft_scraper() + quora_scraper() + 
                dropbox_scraper() + ramp_scraper() + replit_scraper() + 
                duolingo_scraper()  + draftkings_scraper() + splunk_scraper() +
                zello_scraper() + khanacademy_scraper() + transmarketgroup_scraper() +
                netflix_scraper())'''
        
        
        
        # visa_scraper()
                        
        current_jobs = merged
        
        new_jobs = [job for job in current_jobs if job not in seen_jobs]

        
        '''if new_jobs:
            send_email(new_jobs)'''
            
        '''new_jobs = [
            {"company": "Example Company", "role": "Software", "link": "https://example.com/job"},
            {"company": "Another Company", "role": "Data", "link": "https://anothercompany.com/job"},
            {"company": "Yet Another Company", "role": "Product", "link": "https://yetanothercompany.com/job"}
        ]'''
        
        # Subtract the seen jobs from the current jobs
        # Fetch the current content of the README.md file
        readme_url = f"https://api.github.com/repos/{username}/{repository}/contents/{readme_path}"
        headers = {
            "Authorization": "token [tokenname]]",
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.get(readme_url, headers=headers)
        response_json = response.json()

        # Decode the content from base64
        current_content = response_json['content']
        import base64
        current_content_decoded = base64.b64decode(current_content).decode('utf-8')

        # Replace the existing content with new content
        new_content = "## Current Job Openings\n\n"
        new_content += "| Company | Role | Link |\n"
        new_content += "| ------- | ---- | ---- |\n"     
        
        for job in new_jobs:
            new_content += f"| {job['company']} | {job['role']} | [Job Link]({job['link']}) |\n"        
        
        # Encode the new content to base64
        import json
        new_content_encoded = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')

        # Update the README file in the repository
        update_data = {
            "message": "Update README",
            "content": new_content_encoded,
            "sha": response_json['sha']
        }
        update_url = f'https://api.github.com/repos/{username}/{repository}/contents/{readme_path}'
        update_response = requests.put(update_url, headers=headers, data=json.dumps(update_data))

        # Check if the update was successful
        if update_response.status_code == 200:
            print("README updated successfully!")
        else:
            print("Failed to update README:", update_response.text)
        
        time.sleep(86400)

if __name__ == "__main__":
    main()

