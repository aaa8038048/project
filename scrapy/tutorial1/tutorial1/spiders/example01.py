# -*- coding: utf-8 -*-
import scrapy
from tutorial1.items import Tutorial1Item
class Example01Spider(scrapy.Spider):
    name = "example01"
    allowed_domains = ["example01"]
    start_urls = (
        'http://www.moko.cc',
    )

    def parse(self, response):
		for divs in response.xpath('//div[@class="cover"]'):
			img_url=divs.xpath('.//img/@src2').extract()[0]
			urlItem=Tutorial1Item()
			urlItem['url']=img_url
			yield urlItem
