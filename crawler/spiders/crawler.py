from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import ProductItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains=["www.tiki.vn"]
    start_urls=["https://tiki.vn/dien-thoai-iphone-7-plus-128gb-hang-nhap-khau-chinh-hang-p269707.html"]

    def parse(self, res):
        product = Selector(res).css('div.product-summary')
        item = ProductItem()

        # item['pName'] = product.xpath('//h1[@class="item-name"]/span/text()').extract_first()
        item['pName'] = product.css('h1.item-name').css('span::text').get()
        item['pPrice'] = product.css('span#span-price::text').get()
        item['pImage'] = product.css('img::attr(src)').extract_first()
        item['pFeature'] = product.css('div.top-feature-item').css('p::text').getall()

        yield item
        
