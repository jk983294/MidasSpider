from scrapy import Selector
from scrapy.contrib.spiders import CrawlSpider
from MidasSpider.items import StockInfo


class StackSpider(CrawlSpider):
    name = "guba"
    #allowed_domains = ["stockdata.stock.hexun.com"]
    start_urls = [
        "http://guba.eastmoney.com/list,002320.html",
    ]

    def parse(self, response):
        basicInfos = Selector(response).xpath('//*[@id="articlelistnew"]')
        item = StockInfo()
        for basicInfo in basicInfos:
            key = basicInfo.xpath('td[@class="begin"]/text()').extract()[0]
            item['title'] = basicInfo.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = basicInfo.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            yield item