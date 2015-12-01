from multiprocessing.queues import Queue
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.xlib.pydispatch import dispatcher
from multiprocessing import Process


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
