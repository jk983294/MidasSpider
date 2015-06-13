#coding=utf-8
from scrapy import Selector
from scrapy.contrib.spiders import CrawlSpider
from MidasSpider.items import StockInfo


class StackSpider(CrawlSpider):
    name = "hexun"
    #allowed_domains = ["stockdata.stock.hexun.com"]
    start_urls = [
        "http://stockdata.stock.hexun.com/gszl/s002320.shtml",
    ]

    def parse(self, response):
        basicInfos = Selector(response).xpath('/html/body/div[2]/div[8]/div[1]/div[1]/table/tbody/tr')
        item = StockInfo()
        for basicInfo in basicInfos:
            key = basicInfo.xpath('td[@class="begin"]/text()').extract()[0]
            item['title'] = basicInfo.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = basicInfo.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            yield item