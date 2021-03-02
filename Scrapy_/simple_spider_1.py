import scrapy


class ArticleSpider(scrapy.Spider):
    name = "articles"
    start_urls = ['https://www.bt.no/nyheter/lokalt/',
                  'https://www.bt.no/nyheter/innenriks/',
                  'https://www.bt.no/nyheter/utenriks/']

    def parse(self, response, **kwargs):
        title = response.xpath("//title/text()").get()
        headline = response.xpath("//h3/text()").getall()
        link = response.xpath("//h3/parent::node()/parent::node()/@href").getall()
        i = 0
        while i < len(headline):
            print('({}) {} ({})'.format(title, headline[i], link[i]))
            i += 1
