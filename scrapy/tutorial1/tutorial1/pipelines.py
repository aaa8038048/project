# -*- coding: utf-8 -*-
from tutorial1.items import Tutorial1Item
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Tutorial1Pipeline(object):
	def __init__(self):
		self.mfile = open('test.html', 'w')
    
	def process_item(self, item, spider):
		text = '<img src="' + item['url'] + '"/>'
		self.mfile.writelines(text)

	def close_spider(self, spider):
		self.mfile.close()