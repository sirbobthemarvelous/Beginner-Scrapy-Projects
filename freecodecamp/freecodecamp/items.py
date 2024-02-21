# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field


class FreecodecampItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookItem(Item):
    title = Field()
    category = Field()
    description = Field()
    price = Field()