import scrapy
from urispider.items import SubmitItem
from urispider.mixins import UriLoginMixin


class SubmitSpider(UriLoginMixin,
                   scrapy.Spider):
    name = 'submit'
    url = 'https://www.urionlinejudge.com.br/judge/pt/runs/add'

    def __init__(self, *args, **kwargs):
        super(scrapy.Spider, self).__init__(*args, **kwargs)
        self.kwargs = kwargs

    def logged_in(self, response):
        yield scrapy.Request(self.url,
                             callback=self.parse)

    def parse(self, response):
        submit_form_data = self.kwargs.get('submit_form_data', {})
        return scrapy.FormRequest.from_response(response,
                                                formdata=submit_form_data,
                                                callback=self.requested)

    def requested(self, response):
        sel = response.xpath("//div[@class='flash flash-success']").extract()
        item = SubmitItem()
        item['submited'] = len(sel) >= 1
        yield item
