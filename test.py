from CrawlerMethod import *



crawler = CrawlerMethod(["https://arxiv.org/list/math.OC/recent"], [".pdf"], "Files")
crawler.find_all_clickable_links()
crawler.download()


