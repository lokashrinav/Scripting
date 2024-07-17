import requests
import json

list1 = []      

def patreon_scraper():
    # Define the GraphQL endpoint URL
    url = 'https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobBoardWithTeams'
    list1 = []

    # Define the request headers
    headers = {
        ":authority": "jobs.ashbyhq.com",
        ":method": "POST",
        ":path": "/api/non-user-graphql?op=ApiJobBoardWithTeams",
        ":scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Apollographql-Client-Name": "frontend_non_user",
        "Apollographql-Client-Version": "0.1.0",
        "Content-Type": "application/json",
        "Cookie": "_dd_s=rum=1&id=04a65520-e3a5-464c-81ab-6fd8a298e2a2&created=1713402275625&expire=1713403450553",
        "Origin": "https://jobs.ashbyhq.com",
        "Referer": "https://jobs.ashbyhq.com/patreon",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Traceparent": "00-00000000000000003865a0fcdb44bedb-0923b23677145861-01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    }


    # Define the payload with the GraphQL query
    payload = {
        "operationName": "ApiJobBoardWithTeams",
        "variables": {
            "organizationHostedJobsPageName": "Patreon"
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
        item['link'] = "https://jobs.ashbyhq.com/patreon/" + job['id']
        item['company'] = "Patreon"
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
    print(patreon_scraper())
