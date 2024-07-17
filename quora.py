import requests
import json

list1 = []      

def quora_scraper():
    # Define the GraphQL endpoint URL
    url = 'https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobBoardWithTeams'
    list1 = []

    # Define the request headers
    headers = {
                    'Accept': '*/*',
                    'Content-Type': 'application/json',
                    'Content-Length': '787',
                    'Cookie': '_dd_s=rum=1&id=06c05356-744b-493d-b0e1-0acd8af3818c&created=1713050309192&expire=1713051227232',
                    'Origin': 'https://jobs.ashbyhq.com',
                    'Referer': 'https://jobs.ashbyhq.com/quora',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                }

    # Define the payload with the GraphQL query
    payload = {
        "operationName": "ApiJobBoardWithTeams",
        "variables": {
            "organizationHostedJobsPageName": "quora"
        },
        "query": "query ApiJobBoardWithTeams($organizationHostedJobsPageName: String!) {\n  jobBoard: jobBoardWithTeams(\n    organizationHostedJobsPageName: $organizationHostedJobsPageName\n  ) {\n    teams {\n      id\n      name\n      parentTeamId\n      __typename\n    }\n    jobPostings {\n      id\n      title\n      teamId\n      locationId\n      locationName\n      employmentType\n      secondaryLocations {\n        ...JobPostingSecondaryLocationParts\n        __typename\n      }\n      compensationTierSummary\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment JobPostingSecondaryLocationParts on JobPostingSecondaryLocation {\n  locationId\n  locationName\n  __typename\n}"
    }

    # Send the POST request with the payload
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code
    print("Response Status Code:", response.status_code)
    
    data = json.loads(response.text)
        
    for job in data["data"]["jobBoard"]["jobPostings"]:
        item = {}
        item['location'] = job['locationName']
        item['secondaryLocations'] = job['secondaryLocations']
        item['role'] = job['title']
        item['link'] = "https://jobs.ashbyhq.com/quora/" + job['id']
        item['company'] = "Quora"
        list1.append(item)
            
    new_list = []
            
    for job in list1:
        if "intern" in job["role"].lower():
            new_list.append(job)
            
    new_list2 = []
    
    for job in new_list:
        if "United States" in job["location"]:
            new_list2.append(job)
        else:
            checkbool = False
            if job["secondaryLocations"]:
                for location in job["secondaryLocations"]:
                    if "United States" in location["locationName"]:
                        checkbool = True
                if checkbool:
                    new_list2.append(job)
    
    return new_list2


if __name__ == "__main__":
    print(quora_scraper())
