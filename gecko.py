import requests
import time
import json
import random

def gecko_scraper():
    # Define the URL
    # Get the current timestamp in milliseconds
    current_timestamp = int(time.time() * 1000)

    # Generate a random number between 1 and 1000
    random_number = random.randint(1, 1000)

    # Combine the timestamp and random number to create a unique identifier
    unique_identifier = f"{current_timestamp}-{random_number}"

    # Define the URL with the unique identifier appended
    url = f"https://boards-api.greenhouse.io/v1/boards/geckorobotics/departments?timestamp={unique_identifier}"

    # Make your request using the URL
    response = requests.get(url)
    
    # Check the response status code
    print("Response Status Code:", response.status_code)
    
    data = response.text
        
    states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa",
                    "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri",
                    "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
                    "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin",
                    "West Virginia", "Wyoming", "District of Columbia", "United States of America"]

    # Add a space before each initial
    states_with_space = [' ' + state for state in states]
        
    list1 = []
    
    data = json.loads(data)
    for job in data["departments"]:
        if job["jobs"]:
            for i in job["jobs"]:
                item = {}
                item['role'] = i['title']
                item['link'] = i['absolute_url']
                item['company'] = "Gecko Robotics"
                item['location'] = i['location']['name']
                list1.append(item)
            
    new_list = []
            
    for job in list1:
        if "intern" in job["role"].lower():
            new_list.append(job)
            
    new_list2 = []
            
    for job in new_list:
        bool1 = False
        for i in states_with_space:
            if i in job["location"]:
                bool1 = True
        if bool1:
            new_list2.append(job)
            
    return new_list2
    
if __name__ == "__main__":
    print(gecko_scraper())