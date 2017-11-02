# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    # allowed_domains = ["python123.io"]
    start_urls = ['http://python123.io/ws/demo.html']

    # 用yield生成器
    # def start_requsts(self):
    # 	urls = [
    # 				'http://python123/ws/demo.html'
    # 			]
    # 	for url in urls:
    # 		yield scrapy.Requsets(url = url, callback = self.parse)


    def parse(self, response):
    	fname = response.url.split('/')[-1]   # 保存的文件名	
    	with open(fname, 'wb') as f:
    		f.write(response.body)
    	self.log('Saved file %s.' % fname)
        # pass
