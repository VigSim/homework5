# -*- coding: utf-8 -*-
import scrapy


class ImdbmsSpider(scrapy.Spider):
    name = "imdbms"
    allowed_domains = ["imdb.com"]
    start_urls = ['http://imdb.com/chart/top']

    def parse(self, response):
       for movie in response.xpath('//tbody[@class="lister-list"]'):
        	yield {
       	      'movie_rank':movie.xpath('//tr/td[@class="titleColumn"]/text()').extract(),
       	      'title':movie.xpath('//tr/td[@class="titleColumn"]/a/text()').extract(),
       	      'url':movie.xpath('//tr/td[@class="titleColumn"]/a/@href').extract(),
       	      'release_year':movie.xpath('//tr/td[@class="titleColumn"]/span/text()').extract(),
       	      'rating':movie.xpath('//tr/td[@class="ratingColumn imdbRating"]/strong/text()').extract()
         	}
