from collections import OrderedDict
import random

def rotate_proxy():
    header_lists = [
        # Safari
        {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
        },
        # Chrome
        {
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