import scrapy
import json
import sys

class JobItem(scrapy.Item):
    company = scrapy.Field()
    role = scrapy.Field()
    link = scrapy.Field()
    location = scrapy.Field()

class NetflixSpider(scrapy.Spider):
    name = 'netflix_jobs'
    start_urls = ['https://jobs.netflix.com/api/search']

    # Define list1 as a class attribute
    list1 = []

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
        

        states = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa",
                            "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri",
                            "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
                            "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin",
                            "West Virginia", "Wyoming", "District of Columbia", "United States of America", "United States"]
                              
        states = [' ' + state for state in states]

        if response.status == 200:
            try:
                data = json.loads(response.body)
                for job in data["records"]["postings"]:
                    bool1 = False
                    for i in states:
                        if i in job["location"]:
                            bool1 = True
                            
                    bool2 = False
                    if ("software" in job["text"].lower() or "swe " in job["text"].lower() or "sw " in job["text"].lower()) and " " in job["text"].lower(): 
                        bool2 = True
                        
                    if bool1 and bool2:
                        item = JobItem()
                        item['role'] = job['text']
                        item['location'] = job['location']
                        item['link'] = "https://jobs.netflix.com/jobs/" + job['external_id']
                        item['company'] = "Netflix"
                        
                    # Append to the class attribute list1 using self.list1
                        self.list1.append(item)
                    
                        yield item
                        
            except json.JSONDecodeError:
                self.logger.error("Failed to parse JSON response.")
                
            num_pages = data["info"]["postings"]["num_pages"]
            if num_pages > 1:
                for page_num in range(2, num_pages + 1):
                    next_page_url = f"https://jobs.netflix.com/api/search?page={page_num}"
                    yield scrapy.Request(url=next_page_url, callback=self.parse)
        else:
            self.logger.error(f"Request failed with status code: {response.status}")
        
def netflix_scraper():
    from scrapy.crawler import CrawlerProcess
    process2 = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        # Add other settings as needed
    })
    process2.crawl(NetflixSpider)
    process2.start()
    
    # Return the class attribute list1 after the crawling process is finished
    return NetflixSpider.list1

if __name__ == "__main__":
    print(netflix_scraper())

