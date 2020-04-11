from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import ProductItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains=["www.tiki.vn"]
    start_urls=["https://tiki.vn/microsoft-surface-pro-2018-core-i5-8250u-8g-256gb-hang-chinh-hang-p8286081.html"]

    def parse(self, res):
        product = Selector(res).css('div.product-summary')
        item = ProductItem()

        item['pName'] = product.css('h1.item-name').css('span::text').get()
        item['pPrice'] = product.css('span#span-price::text').get()
        item['pDiscountPrice'] = product.css('span.price').css('span.red::text').get()
        item['pCode'] = product.css('span.tag').css('span.code::text').get()
        item['pImage'] = product.css('img::attr(src)').extract_first()
        item['pFeature'] = product.css('div.top-feature-item').css('p::text').getall()
        item['pSeller'] = product.css('div.text').css('span::text').get()
        yield item