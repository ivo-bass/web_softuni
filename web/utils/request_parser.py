STATUS_CODE = ("200", "404")
STATUS_TEXT = {"200": "OK", "404": "Not Found"}
END_COMMAND = "END"


def get_valid_paths():
    paths = []
    while True:
        line = input()
        if line == END_COMMAND:
            break
        path, method = line.rsplit("/", maxsplit=1)
        paths.append((path, method.upper()))
    return paths


def get_request():
    request = input()
    request = request.split()
    return request


def get_response_code(paths, request):
    request_method, request_path, _ = request
    for path, method in paths:
        if path == request_path and method == request_method:
            return STATUS_CODE[0]
    return STATUS_CODE[1]


def get_full_response(code):
    text = STATUS_TEXT[code]
    info = f"\nHTTP/1.1 {code}"
    info += f"\nContent-Length: {len(text)}"
    info += f"\nContent-Type: text/plain"
    info += f"\n"
    info += f"\n{text}"
    return info


def request_parser():
    paths = get_valid_paths()
    request = get_request()
    code = get_response_code(paths, request)
    print(get_full_response(code))


request_parser()
