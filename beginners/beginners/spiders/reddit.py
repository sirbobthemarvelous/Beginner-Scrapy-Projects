import scrapy
#credit https://www.youtube.com/watch?v=ogPMCpcgb-E
class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/HonzukiNoGekokujou/', 'https://www.reddit.com/r/FurryVisualNovels/']

    def parse(self, response):
        #this example uses xpaths
        links = response.xpath("//img/@src")
        html = ""
        for link in links:
            url = link.get()
            if any(extension in url for extension in [".jpg,",".gif",".png"]):
                html += """ <a href="{url}"
                target = "_blank" 
                <img src="{url}" height="33%"
                width="33%"/>
                <a/>""".format(url=url)

                with open("frontpage.html","a") as page: #create a page from the results
                    page.write(html)
                    page.close()

        
