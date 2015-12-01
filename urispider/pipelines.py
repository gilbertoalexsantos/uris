# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urispider.utils import clean_text
from urispider import spiders


class CleanItemPipeline(object):
    def process_item(self, item, spider):
        for key in item.keys():
            if isinstance(item[key], str) or isinstance(item[key], unicode):
                item[key] = clean_text(item[key])
        return item
