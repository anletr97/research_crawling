# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProductItem(scrapy.Item):
    pName = scrapy.Field()
    pPrice = scrapy.Field()
    pDiscountPrice = scrapy.Field()
    pCode = scrapy.Field()
    pImage = scrapy.Field()
    pFeature = scrapy.Field()
    pSeller = scrapy.Field()
    pass