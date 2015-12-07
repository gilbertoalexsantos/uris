import scrapy
from urispider.items import SubmissionItem
from urispider.mixins import UriLoginMixin


class SubmissionSpider(UriLoginMixin,
                       scrapy.Spider):
    name = 'submissions'
    url = 'https://www.urionlinejudge.com.br/judge/pt/runs'

    def __init__(self, *args, **kwargs):
        super(scrapy.Spider, self).__init__(*args, **kwargs)
        self.kwargs = kwargs

    def logged_in(self, response):
        submissions_form_data = self.kwargs.get('submissions_form_data', {})
        yield scrapy.FormRequest(url=self.url,
                                 formdata=submissions_form_data,
                                 callback=self.parse)

    def parse(self, response):
        for sel in response.xpath('//tbody/tr'):
            if len(sel.xpath('td').extract()) == 1:
                break
            item = SubmissionItem()
            item['code'] = sel.xpath('td[1]/a/text()').extract()[0]
            item['id_problem'] = sel.xpath('td[2]/a/text()').extract()[0]
            item['name_problem'] = sel.xpath('td[3]/a/text()').extract()[0]
            item['answer'] = sel.xpath('td[4]/a/text()').extract()[0]
            item['language'] = sel.xpath('td[5]/text()').extract()[0]
            item['time'] = sel.xpath('td[6]/text()').extract()[0]
            item['date'] = sel.xpath('td[7]/text()').extract()[0]
            yield item
