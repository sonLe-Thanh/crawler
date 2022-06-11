from collections import OrderedDict
import random
import requests

def rotate_proxy():
    header_lists = [
        # Safari
        {
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8",
            # "Host": "httpbin.org",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
        },
        # Chrome
        {
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Accept-Language": "vi-VN,vi;q=0.9",
            # "Host": "httpbin.org",
            # "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
            # "Sec-Ch-Ua-Mobile": "?0",
            # "Sec-Ch-Ua-Platform": "\"macOS\"",
            # "Sec-Fetch-Dest": "document",
            # "Sec-Fetch-Mode": "navigate",
            # "Sec-Fetch-Site": "none",
            # "Sec-Fetch-User": "?1",
            # "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
        },
    ]

    ordered_headers_list = []
    for headers in header_lists:
        h = OrderedDict()
        for header, value in headers.items():
            h[header] = value
            ordered_headers_list.append(h)

    return random.choice(ordered_headers_list)