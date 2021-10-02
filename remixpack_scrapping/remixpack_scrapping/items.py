"""
Define here the models for your scraped items
See documentation in:
https://docs.scrapy.org/en/latest/topics/items.html
author: Damien Michelle
date: 29/09/2021
"""
import scrapy


class RemixpackScrappingItem(scrapy.Item):
    # define the fields for your item here like:
    musical_genre = scrapy.Field()
    stem_title = scrapy.Field()
    country = scrapy.Field()
    views = scrapy.Field()
    year = scrapy.Field()
    bpm = scrapy.Field()
    mb = scrapy.Field()
    tags = scrapy.Field()
