import scrapy

class TutorialSpider(scrapy.Spider):
    name = 'tutorial'
    allowed_domains = ['scrapethissite.com']
    start_urls = ['https://www.scrapethissite.com/pages/simple/', 'https://www.scrapethissite.com/pages/forms/']

    def parse(self, response):
        #for check in response.css('div.container'):
        for check in response.css('tr.team'):
            yield {
                #'name': check.css('h3.country-name::text').getall(),
                'teamname': check.css('td.name::text').get()
            }
        for a in response.css('ul.pagination a[aria-label=Next]'): #call the next pages
            yield response.follow(a, callback=self.parse)
        
        """ or alternatively
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        next_page = response.css('ul.pagination a[aria-label=Next]::attr(href)').get() #call the next page
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            """
