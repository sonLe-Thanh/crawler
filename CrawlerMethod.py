from urllib.parse import urljoin

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from pathlib import Path
from Downloader import *
from Helper import *


class CrawlerMethod:
    def __init__(self, main_urls, file_types, dir_path):
        self.file_types = file_types
        self.main_urls = main_urls
        self.dir_path = dir_path + "/"
        self.options = Options()
        self.options.add_argument("--headless")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        # File list 3 args: 0 - url, 2 - file name, 1 - type
        self.file_list = []

    def find_all_clickable_links(self):
        for url in self.main_urls:
            self.driver.get(url)
            # Get static html
            soup = BeautifulSoup(self.driver.page_source, "lxml")
            # Get links in a tags
            urls_on_page = [tag.attrs.get("href") for tag in soup.find_all("a")]
            # Get links in img tags
            urls_on_page.extend([tag.attrs.get("src") for tag in soup.find_all("img")])

            # Join url, relative to absolute urls
            for url in urls_on_page:

                resolve_url = urljoin(self.driver.current_url, url)

                if is_normal_https(resolve_url):
                    req = Request(resolve_url, headers=rotate_proxy())
                    response = urlopen(req)
                    url_content_type = response.info().get_content_type().split("/")[1]

                    if url_content_type in equivalent_MIME_type() and equivalent_MIME_type()[
                        url_content_type] in self.file_types:
                        filename = Path(urlparse(resolve_url).path).name
                        self.file_list.append([resolve_url, url_content_type, filename])

    def download(self):
        for ele in self.file_list:
            download_file(ele[0], ele[1], ele[2], self.dir_path, self.file_types)
