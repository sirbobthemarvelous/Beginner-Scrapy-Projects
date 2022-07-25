import scrapy

# https://scrapfly.io/blog/web-scraping-with-scrapy/#creating-spiders
#https://tvtropes.org/pmwiki/pmwiki.php/Main/WesternAnimationOfThe2010s

class TutorialSpider(scrapy.Spider):
    name = 'tutorial'
    allowed_domains = ['scrapethissite.com']
    start_urls = ['https://www.scrapethissite.com/pages/simple/']

    def parse(self, response):
        for check in response.css('div.container'):
            yield {
                'name': check.css('h3.country-name::text').getall()
            }
