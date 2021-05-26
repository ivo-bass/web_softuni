from urllib import parse


def url_decode(url):
    res = parse.unquote(url)
    return res


tests = [
    ('http://www.google.bg/search?q=C%23', 'http://www.google.bg/search?q=C#'),
    ('https://mysite.com/show?n%40m3=p3%24h0', 'https://mysite.com/show?n@m3=p3$h0'),
    ('http://url-decoder.com/i%23de%25?id=23', 'http://url-decoder.com/i#de%?id=23'),
]

for url, expected in tests:
    result = url_decode(url)
    print(url)
    print(expected, "|",result)
    print(expected == result)
