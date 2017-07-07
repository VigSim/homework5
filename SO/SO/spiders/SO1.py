# -*- coding: utf-8 -*-
import scrapy


class So1Spider(scrapy.Spider):
    name = "SO1"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ['https://stackoverflow.com/questions/tagged/python?page=1&sort=newest&pagesize=50',
                  'https://stackoverflow.com/questions/tagged/python?page=2&sort=newest&pagesize=50',
                  'https://stackoverflow.com/questions/tagged/python?page=3&sort=newest&pagesize=50']

    def parse(self, response):
        for question in response.css('div.content-padding'):
        	yield { 
                   'Question':question.css('div.question-summary div.summary h3 a::text').extract(),
                   'URL':question.css('div.question-summary div.summary h3 a::attr(href)').extract(), 
        	 } /n
