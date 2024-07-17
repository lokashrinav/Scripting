import scrapy
import json

list1 = []

abbreviations = [
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#States.
    "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
    "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
    "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
    "WV", "WY", "DC"]



class JobItem(scrapy.Item):
    company = scrapy.Field()
    role = scrapy.Field()
    link = scrapy.Field()
    location = scrapy.Field()

class GreenhouseSpider(scrapy.Spider):
    name = 'greenhouse'
    allowed_domains = ['api.greenhouse.io']
    start_urls = ['https://api.greenhouse.io/v1/boards/lyft/jobs?content=true']

    def start_requests(self):
        for url in self.start_urls:
            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'en-US,en;q=0.9',
                'If-None-Match': 'W/"6ac13e05789bda4350c22ed67402c148"',
                'Origin': 'https://www.lyft.com',
                'Referer': 'https://www.lyft.com/',
                'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
            }
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        # Your parsing logic here
        raw_data = response.text
        data = json.loads(raw_data)
        
        for job in data["jobs"]:
            item = JobItem()
            item['role'] = job['title']
            item['link'] = job['absolute_url']
            item['location'] = job['location']['name']
            item['company'] = "Lyft"
            list1.append(item)
            yield item
    
def lyft_scraper():
    states = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
            "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
            "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
            "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
            "WV", "WY", "DC", "USA", "United States"]

    # Add a space before each initial
    states_with_space = [' ' + state for state in states]
    from scrapy.crawler import CrawlerProcess
    
    # Create a CrawlerProcess instance
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        # Add other settings as needed
    })
    
    # Add your spider to the process
    process.crawl(GreenhouseSpider)
    
    # Start the crawling process
    process.start()
    
    new_list = []
    
    for job in list1:
        bool1 = False
        for i in states_with_space:
            if i in job["location"]:
                bool1 = True
        if bool1:
            new_list.append(job)
    
    new_list2 = []
    
    print(list1)
    
    for job in list1:
        bool1 = False
        for i in states_with_space:
            if i in job["location"]:
                bool1 = True
        if bool1:
            new_list.append(job)
    
    print(new_list)
            
    for job in new_list:
        if "intern" in job["role"].lower():
            new_list2.append(job)
    
    return new_list2


if __name__ == "__main__":
    print(lyft_scraper())
