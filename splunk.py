import requests
import time
import json
import random

def splunk_scraper():
    # Define the URL
    # Get the current timestamp in milliseconds
    current_timestamp = int(time.time() * 1000)

    # Generate a random number between 1 and 1000
    random_number = random.randint(1, 1000)

    # Combine the timestamp and random number to create a unique identifier
    unique_identifier = f"{current_timestamp}-{random_number}"

    # Define the URL with the unique identifier appended
    url = f"https://www.splunk.com/api/bin/careers/jobs?timestamp={unique_identifier}"

    # Make your request using the URL
    response = requests.get(url)
    
    # Check the response status code
    print("Response Status Code:", response.status_code)
    
    data = response.text
    
        
    list1 = []
    
    data = json.loads(data)
    
    for job in data["careersList"]:
            item = {}
            item['role'] = job['jobTitle']
            item['link'] = "https://www.splunk.com/" + job['url']
            item['company'] = "Splunk"
            item['locations'] = job['locations']
            list1.append(item)
            
    new_list = []
            
    for job in list1:
        if "intern" in job["role"].lower():
            new_list.append(job)
            
    new_list2 = []
            
    for job in new_list:
        bool1 = False
        for i in job["locations"]:
            if "United States" in i:
                bool1 = True
        if bool1:
            new_list2.append(job)
            
    return new_list2
    
if __name__ == "__main__":
    print(splunk_scraper())