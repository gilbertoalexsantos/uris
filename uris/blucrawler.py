from multiprocessing.queues import Queue
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.xlib.pydispatch import dispatcher
from multiprocessing import Process
from scrapy.settings import Settings


class CrawlerWorker(Process):
    def __init__(self, spider, results, **kwargs):
        Process.__init__(self)
        self.results = results
        self.crawler = CrawlerProcess(get_project_settings())
        self.items = []
        self.spider = spider
        self.kwargs = kwargs
        dispatcher.connect(self._item_scraped, signals.item_scraped)

    def _item_scraped(self, item, spider):
        self.items.append(item)

    def run(self):
        self.crawler.crawl(self.spider, **self.kwargs)
        self.crawler.start()
        self.crawler.stop()
        self.results.put(self.items)


def get_results_from_crawler(spider, **kwargs):
    results = Queue()
    worker = CrawlerWorker(spider, results, **kwargs)
    worker.start()
    return results.get()


def get_project_settings():
    scrapy_module = "uris.urispider.settings"
    
    settings = Settings()
    settings.setmodule(scrapy_module)
    
    return settings
