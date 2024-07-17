import requests
import json

list1 = []

def amazon_scraper():

    # Set up the URL
    url = "https://www.amazon.jobs/en/search.json?radius=24km&facets%5B%5D=normalized_country_code&facets%5B%5D=normalized_state_name&facets%5B%5D=normalized_city_name&facets%5B%5D=location&facets%5B%5D=business_category&facets%5B%5D=category&facets%5B%5D=schedule_type_id&facets%5B%5D=employee_class&facets%5B%5D=normalized_location&facets%5B%5D=job_function_id&facets%5B%5D=is_manager&facets%5B%5D=is_intern&offset=0&result_limit=100&sort=relevant&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON content
        data = response.json()
        
        # Find all job titles
        jobs_list = data['jobs']

        # Print the job titles
        for job in jobs_list:
            bool1, bool2 = False, False
            if job["country_code"] == "USA":
                bool1 = True
            if "intern" in job["title"].lower():
                bool2 = True
            if bool1 and bool2:
                    item = {}
                    item['role'] = job['title']
                    item['link'] = "https://www.amazon.jobs/" + job['job_path']
                    item['company'] = "Amazon"
                    list1.append(item)
                    
        return list1
        
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)