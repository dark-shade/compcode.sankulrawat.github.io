import scrapy
from datetime import date

class LeetCodeSpider(scrapy.Spider):
    name = "leetcode"

    def start_requests(self):
        urls = [
            'https://leetcode.com/dark_shade/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        solved_data = response.css('span.badge.progress-bar-success::text')[3].get()
        sols = solved_data.split()
        yield {
            'solved': sols[0],
            'total': sols[2],
            'date': str(date.today())
        }