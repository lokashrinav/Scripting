import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class JobItem(scrapy.Item):
    company = scrapy.Field()
    role = scrapy.Field()
    link = scrapy.Field()
    location = scrapy.Field()

class GreenhouseSpider(scrapy.Spider):
    name = 'greenhouse'
    allowed_domains = ['api.greenhouse.io']
    start_urls = ['https://api.greenhouse.io/v1/boards/lyft/jobs?content=true']

    def parse(self, response):
        
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
        
        raw_data = response.text
        data = json.loads(raw_data)
        job_data = []

        for job in data["jobs"]:
            item = JobItem()
            item['role'] = job['title']
            item['link'] = job['absolute_url']
            item['location'] = job['location']['name']
            item['company'] = "Lyft"
            
            bool1, bool2 = False, False
            
            if "intern" in job["text"].lower():
                bool2 = True

            bool1 = any(state in job["location"] for state in states if "Canada" not in job["location"])
            
            if bool1 and bool2:
                job_data.append(dict(item))

        # Save data to JSON file
        with open('lyft_jobs.json', 'w') as f:
            json.dump(job_data, f, indent=4)

class NetflixSpider(scrapy.Spider):
    name = 'netflix_jobs'
    start_urls = ['https://jobs.netflix.com/api/search']

    def start_requests(self):
        for url in self.start_urls:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
                "Accept": "application/json, text/plain, */*",
                "Referer": "https://jobs.netflix.com/search",
                "Cookie": "real_country=US; nfvdid=BQFmAAEBELqMhY7X8nKcvd-zII-NaJtAVzmCiPucJMyT5TdzVF6StfXZpy3p5roXoJ0I0GSB0NeZM4VpTR7rADzQfGCHDsVZjAfwnior4Ug0xfZUWYo94Q%3D%3D; nfx-js=ntqzxjdcv97-n3fbh5kw4tq; _ga=GA1.1.1501758910.1713207223; _ga_4Y3WKF2MY1=GS1.1.1713207222.1.1.1713207248.34.0.0; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Apr+15+2024+14%3A54%3A09+GMT-0400+(Eastern+Daylight+Time)&version=202310.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f47d0af9-ed97-49b6-afa9-549ab43d8270&interactionCount=1&landingPath=https%3A%2F%2Fjobs.netflix.com%2Fsearch&groups=C0001%3A1%2CC0002%3A1; nfx-ssid=rph0img3an-s3v6g2w44f+1713207222626+1713207249196"
            }
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
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

        job_data = []

        if response.status == 200:
            try:
                data = json.loads(response.body)
                for job in data["records"]["postings"]:
                    bool1 = any(state in job["location"] for state in states if "Canada" not in job["location"])
                    bool2 = False
                    
                    if "intern" in job["text"].lower():
                        bool2 = True

                    if bool1 and bool2:
                        item = {
                            'role': job['text'],
                            'location': job['location'],
                            'link': "https://jobs.netflix.com/jobs/" + job['external_id'],
                            'company': "Netflix"
                        }
                        job_data.append(item)

            except json.JSONDecodeError:
                self.logger.error("Failed to parse JSON response.")

            num_pages = data["info"]["postings"]["num_pages"]
            if num_pages > 1:
                for page_num in range(2, num_pages + 1):
                    next_page_url = f"https://jobs.netflix.com/api/search?page={page_num}"
                    yield scrapy.Request(url=next_page_url, callback=self.parse)
        else:
            self.logger.error(f"Request failed with status code: {response.status}")

        # Write job data to a JSON file
        with open('netflix_jobs.json', 'w') as f:
            json.dump(job_data, f, indent=4)


def run_spiders_and_save_data():
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(GreenhouseSpider)
    process.crawl(NetflixSpider)
    process.start()


if __name__ == "__main__":
    run_spiders_and_save_data()