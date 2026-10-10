import requests

HOST = "hw1.alexbers.com"

def build_request(parsed_html: dict, session):
    url = f"http://{HOST}{parsed_html["url"]}"
    parameters = (
        parsed_html["request_parameters"],
        parsed_html["headers"],
        parsed_html["cookies"],
        parsed_html["form_data"],
    )

    files = parsed_html["files"]

    if parsed_html["method"] == "GET":
        request_parts = get_request(url, parameters)
    elif parsed_html["method"] == "POST":
        request_parts = post_request(url, parameters)
    elif parsed_html["method"] == "UPLOAD FILES":
        request_parts = upload_files_request(url, parsed_html["cookies"], files)
    else:
        raise Exception("Unknown HTTP method")

    return session.prepare_request(request_parts) if session else request_parts.prepare()


def get_request(url: str, parameters):
    request_parameters, headers, cookies, form_data = parameters

    return requests.Request(
        method = "GET",
        url = url,
        params = request_parameters,
        headers = headers,
        cookies = cookies
    )


def post_request(url: str, parameters):
    request_parameters, headers, cookies, form_data = parameters

    return requests.Request(
        method = "POST",
        url = url,
        params = request_parameters,
        headers = headers,
        cookies = cookies,
        data = form_data
    )


def upload_files_request(url: str, cookies: dict, files: dict):
    return requests.Request(
        method = "POST",
        url = url,
        cookies = cookies,
        files = build_files(files)
    )


def build_files(files: dict) -> dict:
    return {
        name: (name, content.encode("utf-8"), "application/octet-stream")
        for name, content in files.items()
    }


def send_request(s, task: dict) -> str:
    prepared = build_request(task, s)
    response = s.send(prepared, timeout=10)
    response.encoding = "utf-8"

    return response.text