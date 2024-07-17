import requests
import json
import zlib  # For zlib decompression
from brotli import decompress  # For Brotli decompression

def decode_response(response):
    # Check if response is gzipped
    if response.headers.get('Content-Encoding') == 'gzip':
        return zlib.decompress(response.content, 16+zlib.MAX_WBITS).decode('utf-8')
    # Check if response is deflated
    elif response.headers.get('Content-Encoding') == 'deflate':
        return zlib.decompress(response.content, -zlib.MAX_WBITS).decode('utf-8')
    # Check if response is brotli-compressed
    elif response.headers.get('Content-Encoding') == 'br':
        try:
            return decompress(response.content).decode('utf-8')
        except Exception as e:
            print("Error decompressing Brotli content:", e)
            return response.text
    else:
        # Assume plain text
        return response.text

def cambly_scraper():
    url = 'https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobBoardWithTeams'
        
    headers = {
        "authority": "jobs.ashbyhq.com",
        "method": "POST",
        "path": "/api/non-user-graphql?op=ApiJobBoardWithTeams",
        "scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Apollographql-Client-Name": "frontend_non_user",
        "Apollographql-Client-Version": "0.1.0",
        "Content-Length": "788",
        "Content-Type": "application/json",
        "Cookie": "_dd_s=rum=1&id=04a65520-e3a5-464c-81ab-6fd8a298e2a2&created=1713402275625&expire=1713403742089",
        "Origin": "https://jobs.ashbyhq.com",
        "Referer": "https://jobs.ashbyhq.com/Cambly",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Traceparent": "00-0000000000000000105e40d1ecd339ff-7c36c04970228ec9-01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "X-Datadog-Origin": "rum",
        "X-Datadog-Parent-Id": "8950552731091898057",
        "X-Datadog-Sampling-Priority": "1",
        "X-Datadog-Trace-Id": "1179451422783257087"
    }


    payload = {
        "operationName": "ApiJobBoardWithTeams",
        "variables": {
            "organizationHostedJobsPageName": "patreon"
        },
        "query": "query ApiJobBoardWithTeams($organizationHostedJobsPageName: String!) {\n  jobBoard: jobBoardWithTeams(\n    organizationHostedJobsPageName: $organizationHostedJobsPageName\n  ) {\n    teams {\n      id\n      name\n      parentTeamId\n      __typename\n    }\n    jobPostings {\n      id\n      title\n      teamId\n      locationId\n      locationName\n      employmentType\n      secondaryLocations {\n        ...JobPostingSecondaryLocationParts\n        __typename\n      }\n      compensationTierSummary\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment JobPostingSecondaryLocationParts on JobPostingSecondaryLocation {\n  locationId\n  locationName\n  __typename\n}"
    }


    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            # Decode the response
            decoded_response = decode_response(response)
            print("Decoded Response Text:", decoded_response)

            # Parse the decoded response as JSON
            data = json.loads(decoded_response)
            job_postings = data.get("data", {}).get("jobBoard", {}).get("jobPostings", [])
            if job_postings:
                return [job for job in job_postings if is_desired_job(job)]
            else:
                print("No job postings found.")
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            print("Response Text:", response.text)
    else:
        print("Request failed with status code:", response.status_code)

def is_desired_job(job):
    desired_roles = ["software", "swe", "sw", "backend", "frontend", "android", "ios", "mobile", "full stack", "engineer", "developer"]
    desired_locations = ["United States"]
    
    role = job.get("title", "").lower()
    location = job.get("locationName", "").lower()
    
    return any(desired_role in role for desired_role in desired_roles) and any(desired_location in location for desired_location in desired_locations)

if __name__ == "__main__":
    print(cambly_scraper())