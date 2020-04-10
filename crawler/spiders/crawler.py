from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import ProductItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains=["www.tiki.vn"]
    start_urls=["https://tiki.vn/dien-thoai-iphone-7-plus-128gb-hang-nhap-khau-chinh-hang-p269707.html"]

    def parse(self, res):
        product = Selector(res).xpath('//div[@class="item-box"]')

        item = ProductItem()

        item['pName'] = product.xpath('h1[@class="item-name"]/span/text()').extract_first()
        item['pPrice'] = product.css('span#span-price::text').get()

        # item['pPrice'] = product.css('p#p-specialprice::text').get()

        yield item
        
