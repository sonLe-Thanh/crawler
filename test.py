from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urlunparse, urljoin
from urllib.request import urlopen, Request
from pathlib import Path

import os
from Helper import *

from CrawlerMethod import *
from Downloader import *
from Proxy import *




# options = Options()
# options.add_argument("--headless")
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)
#
# driver.get("https://arxiv.org/list/math.OC/recent")
# driver.implicitly_wait(5)
#
#
# soup = BeautifulSoup(driver.page_source, "lxml")
# urls_on_page = [tag.attrs.get("href") for tag in soup.find_all("a")]
#
# # Join url, relative to absolute urls
# for url in urls_on_page:
#     print(url)
#     resolve_url = urljoin(driver.current_url, url)
#
#
#     if is_normal_https(resolve_url):
#         req = Request(resolve_url, headers=rotate_proxy())
#         response = urlopen(req)
#         url_content_type = response.info().get_content_type().split("/")[1]
#         print(url_content_type)
#         if url_content_type in ["pdf"]:
#             print(resolve_url)
#             filename = Path(urlparse(resolve_url).path).name
#             print(filename)
#
#             download_file(resolve_url, url_content_type, filename, "Files/", ["pdf"])
#
#
#
#
#     print("--------")


crawler = CrawlerMethod(["https://arxiv.org/list/math.OC/recent"], [".pdf"], "Files")
crawler.find_all_clickable_links()
crawler.download()


