"""
Spider for remixpack_scrapping
author: Damien Michelle
date: 29/09/2021
"""
from scrapy import Request, Spider

from remixpack_scrapping.items import RemixpackScrappingItem


class SpiderRemixpackScraping(Spider):
    # nom du spider
    name = "remixpack_scraping"
    # URL de la page à scrapper
    url = 'https://remixpacks.ru/'

    def start_requests(self):
        yield Request(url=self.url, callback=self.parse)

    def parse(self, response):
        # select all divs whose class is genres1 genrescomp
        stem_block = response.css('div.blogstems')
        for stem_card in stem_block:
            musical_genre = stem_card.css('a[rel="category tag"]::text').getall()
            stem_title = stem_card.css('div.titlestems').css('a::text').getall()
            country = stem_card.re(r'(?<=country=)(\w*)"')
            views = stem_card.css('div.hoster a div::text').re(r'\d+')
            year = stem_card.re(r'(?<=year-of-song=)(\w*)"')
            bpm = stem_card.css('div.hoster').re(r'\d+ BPM')
            mb = stem_card.css('div.hoster').re(r'\d+ MB')
            tags_list = stem_card.css('a[rel="tag"]::text').getall()

            item = RemixpackScrappingItem()
            item['musical_genre'] = musical_genre
            item['stem_title'] = stem_title
            item['country'] = country
            item['views'] = views
            item['year'] = year
            item['bpm'] = bpm
            item['mb'] = mb
            item['tags'] = tags_list
            yield item

