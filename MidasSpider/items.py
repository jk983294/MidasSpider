from scrapy.item import Item, Field

class StackItem(Item):
    title = Field()
    url = Field()


class StockInfo(Item):
    code = Field()
    industry = Field()
    concepts = Field()
