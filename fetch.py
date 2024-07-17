import requests
import time
import json
import random



def fetch_scraper():
    # Define the URL
    # Get the current timestamp in milliseconds
    current_timestamp = int(time.time() * 1000)

    # Generate a random number between 1 and 1000
    random_number = random.randint(1, 1000)

    # Combine the timestamp and random number to create a unique identifier
    unique_identifier = f"{current_timestamp}-{random_number}"

    # Define the URL with the unique identifier appended
    url = f"https://boards-api.greenhouse.io/v1/boards/fetchrewards/departments?timestamp={unique_identifier}"

    # Make your request using the URL
    response = requests.get(url)
    
    # Check the response status code
    print("Response Status Code:", response.status_code)
    
    data = response.text
        
    states = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
            "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
            "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
            "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
            "WV", "WY", "DC", "USA", "United States"]

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
                item['company'] = "Fetch"
                item['location'] = i['location']['name']
                list1.append(item)
            
    new_list = []
            
    for job in list1:
        if ("software" in job['role'].lower() or "swe " in job['role'].lower() or "sw " in job['role'].lower() or (("backend" in job['role'].lower() or "frontend" in job['role'].lower() or "android" in job['role'].lower() or "ios" in job['role'].lower() or "mobile" in job['role'].lower() or ("full" in job['role'].lower() and 'stack' in job['role'].lower())) and ("engineer" in job['role'].lower() or "developer" in job['role'].lower()))) and "intern" in job['role'].lower():
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
    print(fetch_scraper())