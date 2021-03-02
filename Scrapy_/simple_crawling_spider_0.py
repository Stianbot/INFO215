from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import Article
import re

#Lite god funksjon til rensing av tekst. Bruk heller proffe biblioteker
def clean_text(text):
    new_text = ''
    for i in text:
        new_text += i

    return re.sub(' +', ' ', new_text)


#Advarsel: Denn crawleren vil kjøre helt til den blir stoppet.
#Husk å redigere 'settings.py' filen i Scrapy prosjektet slik at den stopper etter x antall sider.
# lim denne inn i 'settings.py' CLOSESPIDER_PAGECOUNT = 10 (avslutter etter 10 sider)
class BTCrawler(CrawlSpider):
    name = 'BTcrawler'
    allowed_domains = ['bt.no']
    start_urls = ['https://www.bt.no/nyheter/lokalt/']
    rules = [Rule(LinkExtractor(allow=r'(https://www.bt.no/nyheter).*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        #Henter og renser tekst (dårlig rens).
        text = response.xpath('//p/text()').extract()
        single_string = clean_text(text)

        article = Article()
        article['url'] = response.url
        article['title'] = response.xpath('//h1/text()').extract_first()
        article['text'] = single_string
        article['published'] = response.xpath('//time/@aria-label').get()

        print(article) #fjern kommentar for å få ut et resultat.
        yield article

# kommando: scrapy runspider simple_crawling_spider_0.py -o article.csv -t csv
# JSON alternativ: scrapy runspider simple_crawling_spider_0.py -o bt.json -t json
# lager en csv fil av resultatene.