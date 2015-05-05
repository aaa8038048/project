from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from tutorial.items import DmozItem
import sys
reload(sys)

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.jd.com"]    
  
    def parse(self, response):
		items = [] 
        #hxs = HtmlXPathSelector(response)
		a=response.xpath('//a[@href="http://list.jd.com/670-677-679.html"]/text()').extract()
	
		c=a[0].encode('gbk')
		print c