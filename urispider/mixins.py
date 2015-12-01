from scrapy import signals
from scrapy import Request, FormRequest
from scrapy.exporters import JsonItemExporter


class UriLoginMixin:
    login_url = 'https://www.urionlinejudge.com.br/judge/login'
    
    def start_requests(self):
        yield Request(self.login_url, callback=self.logging_in)

    def logging_in(self, response):
        return FormRequest.from_response(response,
                                         formdata=self.kwargs.get('login_form_data',
                                                                  {}),
                                         callback=self.logged_in)

    def logged_in(self, response):
        pass


class JsonPipelineExporterMixin:
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s_items.json' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = JsonItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        item = self.pre_process_item(item)
        self.exporter.export_item(item)
        return item

    def pre_process_item(self, item):
        return item
