# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SubmissionItem(scrapy.Item):
    code = scrapy.Field()
    id_problem = scrapy.Field()
    name_problem = scrapy.Field()
    answer = scrapy.Field()
    language = scrapy.Field()
    time = scrapy.Field()
    date = scrapy.Field()


class LoginItem(scrapy.Item):
    logged = scrapy.Field()
