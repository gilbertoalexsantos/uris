import scrapy
from urispider.mixins import UriLoginMixin
from urispider.items import LoginItem


class LoginSpider(UriLoginMixin,
                  scrapy.Spider):
    name = 'login'

    def __init__(self, *args, **kwargs):
        super(scrapy.Spider, self).__init__(*args, **kwargs)
        self.kwargs = kwargs

    def logged_in(self, response):
        item = LoginItem()
        logged_url = 'https://www.urionlinejudge.com.br/judge/'
        item['logged'] = response.url == logged_url
        yield item
