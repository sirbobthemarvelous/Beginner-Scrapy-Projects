import scrapy

# https://scrapfly.io/blog/web-scraping-with-scrapy/#creating-spiders
#https://tvtropes.org/pmwiki/pmwiki.php/Main/WesternAnimationOfThe2010s

class TvtropesSpider(scrapy.Spider):
    name = 'tvtropes'
    allowed_domains = ['tvtropes.com']
    start_urls = ['http://tvtropes.com/', 'https://tvtropes.org/pmwiki/pmwiki.php/Main/WesternAnimationOfThe2010s']

    def parse(self, response):
        for check in response.css('div.folder'):
            yield {
                'text': check.css('span.text::text').get(),
                'title': check.css('li::text').get(),
                'tags': check.css('div.tags a.tag::text').getall(),
            }
