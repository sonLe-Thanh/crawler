from urllib.request import Request

from Proxy import *
from Helper import *


def download_file(url, url_content_type, file_name, dir_path, file_extension = default_file_extension_list()):
    if not file_name.lower().endswith(tuple(file_extension)):
        file_name = file_name + equivalent_MIME_type()[url_content_type]
    req = Request(url, headers=rotate_proxy())
    file_download = urlopen(req)
    with open(dir_path+file_name, 'wb') as file:
        file.write(file_download.read())