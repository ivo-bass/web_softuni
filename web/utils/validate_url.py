from urllib import parse


ALLOWED_PROTOCOLS = ("http", "https")


def get_protocol(parsed):
    protocol = parsed.scheme
    if protocol not in ALLOWED_PROTOCOLS:
        return None
    return protocol



def get_host_and_port(parsed, protocol):
    host = parsed.netloc
    port = 80 if protocol == "http" else 443
    if ":" in host:
        host, port = host.split(":")
    if "." not in host:
        return None, port
    return host, port


def get_path(parsed):
    return parsed.path or "/"


def get_query(parsed):
    return parsed.query


def get_fragment(parsed):
    return parsed.fragment


def get_result(protocol, host, port, path, query, fragment):
    if not all((protocol, host, port, path)):
        return 'Invalid URL'
    info = ""
    info += f"Protocol: {protocol}\n"
    info += f"Host: {host}\n"
    info += f"Port: {port}\n"
    info += f"Path: {path}\n"
    info += f"Query: {query}\n" if query else ""
    info += f"Fragment: {fragment}\n" if fragment else ""
    return info


def validate_url(url):
    parsed = parse.urlparse(url)
    protocol = get_protocol(parsed)
    host, port = get_host_and_port(parsed, protocol)
    path = get_path(parsed)
    query = get_query(parsed)
    fragment = get_fragment(parsed)
    return get_result(protocol, host, port, path, query, fragment)


tests = [
    ('http://softuni.bg/',
     """Protocol: http
Host: softuni.bg
Port: 80
Path: /
"""),
    ('https://softuni.bg:447/search?Query=pesho&Users=true#go',
     """Protocol: https
Host: softuni.bg
Port: 447
Path: /search
Query: Query=pesho&Users=true
Fragment: go
"""),
    ('http://google:443/', 'Invalid URL'),

]

for url, expected in tests:
    result = validate_url(url)
    print(expected == result)
    print(result)
