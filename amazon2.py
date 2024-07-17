import scrapy
import json
from scrapy.crawler import CrawlerProcess


class JobItem(scrapy.Item):
    role = scrapy.Field()
    link = scrapy.Field()
    

class Amazon2Spider(scrapy.Spider):
    name = "amazon2"
    allowed_domains = ["www.amazon.jobs"]
    start_urls = ["https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&"]

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "__Host-mons-sid=136-2357249-6714822; preferred_locale=en-US; __Host-mons-ubid=134-7401906-9221230; advertising_id=cd1965d4-be7f-4c1f-b88a-88953868eb24; _ga=GA1.2.14542677.1701823182; cwr_u=e79d5e9e-d93a-412c-b236-7728eba47328; cookie_preferences=%7B%22advertising%22%3Atrue%2C%22analytics%22%3Atrue%2C%22version%22%3A2%7D; analytics_id=e4d5fd16-4cae-4cf0-b66e-c5e8ef67eaa0; uid=e9309cb2-0754-4a4b-a0ad-15acad665440; peoplesoft_id=; passport_id=2e88acd5-d09e-43df-a273-20f2d62cd421; _sp_id.2cc9=84ad13cb-403f-48d1-948d-e65ff6e2bd26.1704778145.3.1706665841.1704778506.bd56eca0-20b1-4e22-abb7-9e8b6db92861; s_lv=1706665841691; check_for_eu_countries=false; tracking_id=8d2ba69bfdab590b3886bfbd20bed463; source=%7B%22azref%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D; AMCVS_CCBC879D5572070E7F000101%40AdobeOrg=1; csm-sid=776-3097808-6399039; _gat=1; __Host-mons-st=3FaSj0fyfNsWk1zky/AJ7bZUhsYHEGyQD/td6JvlEKLpN+sUO7Fy8dqGDG7sys+oYeIU6YeTyOoJ+G32tKUus4RzfKWclHk2bAXDYpLxO4z5NOFxoKdJmGsJhUkjsPvG7zNAVCDveWDv4XU1nGejCSf+4Y7rAqYliK30MsEqGXgjrUjngt8VezpChJb5qFx7iQKOcU/NdxCevBmpr76I/CEWWsgcbNnIy3tbU6VbQv3CWHr2QaiMggrHIEZ+em3vEA8ZRy1MadWAx+uUnP9Mc8mqkmLjIQQYSkSM9zyZQQK+2OZa67+KI9k46Ok3YMbTWSfGsfc8OOXciggc8n9HQKEWcDccP1eE; amazon_jobs_session=V2VRMVB2S0JGT1ltVmtUR05TaytuKzF2OFJ2L21xNFNaVVlYaktaSk1rSFNiaWJ4ZHFKNVRYc3VnZXpEVlprVG5mcFdBejFyQ0NCc3RrSHN3YWwvc1lkYzZia3c3M0s5V1VheFdjSlNBSjd2UE1CWDlnK3owTzVGL0VsM1o2Q3EzTXgvcThMSEJGRkU4TytiZ1FpU2hIMnA5K2llMGl4UENrVHl4eDR3UlFKdjRxeERuMlYzQXlSc2VwYmxOd05wTjhjNFZCbnRpeWVnSlZIV1ZBMnJ4UTRINGxBTkl6b2NEMkZvcE0yRDRDQ3BnUDE3VklDTVN6M0lQMlBLdjRMaHdWR1c4UzZEUnkxR25HYzBNamlvc1pqeDVaK2MyOUVQS0VBU2VrSkdRZkpUZ0I5cnpDRTNrVlREd2dzZWkvczIyaUtoWTkxaVZOdEZpNENCRTZhcHJ3RVpRQWhBMzNXTGdoUlZ2SkwrREZVPS0tT2FvQzNaOHJSZC9zQmZDcGJmYkdFdz09--076519178b1a01ca58ed958db9c38bd28a28416d; cwr_s_a727750b-28d3-4e1d-81fe-8eece247d35b=eyJzZXNzaW9uSWQiOiIzNjU4MjBlOC0yMDk0LTQ5NmUtYTE5Yy00MWRkZTMwNWQwMjciLCJyZWNvcmQiOnRydWUsImV2ZW50Q291bnQiOjYyLCJwYWdlIjp7InBhZ2VJZCI6Ii9lbi9zZWFyY2giLCJwYXJlbnRQYWdlSWQiOiIvZW4vc2VhcmNoIiwiaW50ZXJhY3Rpb24iOjQsInN0YXJ0IjoxNzEzMTEyNTQ1NDUxfX0=; AMCV_CCBC879D5572070E7F000101%40AdobeOrg=-1124106680%7CMCIDTS%7C19828%7CMCMID%7C35083259218176162521540145278458977198%7CMCAAMLH-1707270613%7C7%7CMCAAMB-1713111949%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1713119745s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19705%7CvVersion%7C5.2.0",
        "Host": "www.amazon.jobs",
        "If-None-Match": "W/\"f5e52726dfc86f41b0a22cbb0c13abc0\"",
        "Referer": "https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }    
    
    
    def parse(self, response):
        raw = response.text
        data = json.loads(raw)
        total_jobs = data["hits"]
        
        for offset in range(0, total_jobs, 10):
            url = f"https://www.amazon.jobs/en/search.json?normalized_country_code%5B%5D=USA&radius=24km&facets%5B%5D=normalized_country_code&facets%5B%5D=normalized_state_name&facets%5B%5D=normalized_city_name&facets%5B%5D=location&facets%5B%5D=business_category&facets%5B%5D=category&facets%5B%5D=schedule_type_id&facets%5B%5D=employee_class&facets%5B%5D=normalized_location&facets%5B%5D=job_function_id&facets%5B%5D=is_manager&facets%5B%5D=is_intern&offset={offset}&result_limit=10&sort=relevant&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&"
            yield scrapy.Request(url=url, callback=self.parse_api, headers=self.headers)
        
        
    def parse_api(self, response):
        raw = response.text
        data = json.loads(raw)
        for job in data["jobs"]:
            item = JobItem()
            item["role"] = job["title"]
            item["link"] = job["url_next_step"]
            yield item

def run_spider():
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    })
    process.crawl(Amazon2Spider)
    process.start()

if __name__ == "__main__":
    run_spider()