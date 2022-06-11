import re
from urllib.parse import urlparse, urlunparse


def equivalent_MIME_type():
    return {
        "html": ".html",
        "aiff": ".aiff",
        "x-aiff": ".aiff",
        "x-aim": ".aim",
        "x-audiosoft-intra": ".aip",
        "x-navi-animation": ".ani",
        "mine": ".aps",
        "arj": ".arj",
        "octet-stream": ".exe",
        "x-jg": ".art",
        "x-ms-asf": ".asf",
        "asp": ".asp",
        "x-mplayer2": ".asx",
        "x-ms-asf-plugin": ".asx",
        "basic": ".au",
        "x-au": ".au",
        "x-troff-msvideo": ".avi",
        "avi": ".avi",
        "msvideo": ".avi",
        "x-msvideo": ".avi",
        "avs-video": ".avs",
        "mac-binary": ".bin",
        "macbinary": ".bin",
        "x-binary": ".bin",
        "bmp": ".bmp",
        "x-windows-bmp": ".bmp",
        "book": ".book",
        "x-bsh": ".bsh",
        "x-bzip": ".bz",
        "x-bzip2": ".bz2",
        "x-c": ".c",
        "x-cocoa": ".cco",
        "cdf": ".cdf",
        "x-cdf": ".cdf",
        "x-netcdf": ".cdf",
        "java": ".class",
        "java-byte-code": ".class",
        "x-java-class": ".class",
        "css": ".css",
        "dl": ".dl",
        "x-dl": ".dl",
        "msword": ".doc",
        "x-dv": ".dv",
        "x-dvi": ".dv",
        "acad": ".dwg",
        "x-envoy": ".env",
        "gif": ".gif",
        "x-compressed": ".zip",
        "x-gzip": ".gz",
        "x-icon": ".ico",
        "jpeg": ".jpeg",
        "pjpeg": ".jpeg",
        "x-javascript": ".js",
        "javascript": ".js",
        "x-latex": ".latex",
        "mpeg": ".mp3",
        "x-midi": ".midi",
        "midi": ".midi",
        "quicktime": ".mov",
        "mpeg3": ".mp3",
        "x-mpeg-3": ".mp3",
        "x-mpeg": ".mp3",
        "pict": ".pic",
        "x-script-python": ".py",
        "x-sh": ".sh",
        "x-tex": ".tex",
        "gnutar": ".tgz",
        "plain": ".txt",
        "x-script.zsh" : ".zsh",
        "zip": ".zip",
        "x-zip": ".zip",
        "x-zip-compressed": ".zip",
        "pdf": ".pdf",
        "postscript": ".ps",
        "svg+xml": ".svg",
    }

def default_file_extension_list():
    return list(set(equivalent_MIME_type().values()))


def is_normal_https(url):
    return "https://" in url


def clean_url(url):

    parsed = urlparse(url)

    # add scheme if not available
    if not parsed.scheme:
        parsed = parsed._replace(scheme="http")

        url = urlunparse(parsed)

    # clean text anchor from urls if available
    pattern = r'(.+)(\/#[a-zA-Z0-9]+)$'
    m = re.match(pattern, url)

    if m:
        return m.group(1)
    else:
        # clean trailing slash if available
        pattern = r'(.+)(\/)$'
        m = re.match(pattern, url)

        if m:
            return m.group(1)

    return url