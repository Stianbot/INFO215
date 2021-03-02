#Eksempel på spider som bruker start_request funksjon

import scrapy

class ArticleSpider(scrapy.Spider):
    name = "articles"

    def start_requests(self):
        urls = ['https://en.wikipedia.org/wiki/Web_page',
                'https://en.wikipedia.org/wiki/Web_browser',
                'https://en.wikipedia.org/wiki/WorldWideWeb']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        #Henter ut første overskrift.
        result = response.xpath('//h1/text()').extract_first()
        print(result)