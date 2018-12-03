import httplib2
import socks
import json
from urllib import parse  # import urlencode

proxy_shadowsock = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, 'localhost', 1080)


def ticker(url, userProxy=False):
    con = httplib2.Http()
    if userProxy:
        con = httplib2.Http(
            proxy_info=proxy_shadowsock,
            disable_ssl_certificate_validation=True)
    else:
        con = httplib2.Http()

    body_data = {}
    body = parse.urlencode(body_data)

    header_data = {'Content-Type': 'application/x-www-form-urlencoded'}

    resp, content = con.request(
        url, method="GET", body=body, headers=header_data)

    return json.loads(content)


def tickerJson(url):
    con = httplib2.Http()
    body_data = {}
    body = parse.urlencode(body_data)

    header_data = {'Content-Type': 'application/x-www-form-urlencoded'}

    resp, content = con.request(
        url, method="GET", body=body, headers=header_data)

    return content
