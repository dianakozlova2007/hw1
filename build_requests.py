HOST = "hw1.alexbers.com"

def build_request(parsed_html: dict) -> bytes:
    url = parsed_html["url"]
    parameters = (
        parsed_html["request_parameters"],
        parsed_html["headers"],
        parsed_html["cookies"],
        parsed_html["form_data"]
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

    return "".join(request_parts).encode("utf-8")


def get_request(url :str, parameters):
    request_parameters, headers, cookies, form_data = parameters

    request_method = f"GET {url}{add_request_parameters(request_parameters)} HTTP/1.1\r\n"
    headers_list = [f"Host: {HOST}", "Connection: keep-alive"]

    request_cookies = add_cookies(cookies)
    if request_cookies:
        headers_list.append(request_cookies.strip())

    for header_name, header_val in headers.items():
        headers_list.append(
            f"{safe_encoding(str(header_name))}: {safe_encoding(str(header_val))}"
        )

    headers_part = "\r\n".join(headers_list) + "\r\n\r\n"

    return request_method, headers_part


def post_request(url :str, parameters):
    request_parameters, headers, cookies, form_data = parameters

    request_method = f"POST {url}{add_request_parameters(request_parameters)} HTTP/1.1\r\n"
    headers_list = [f"Host: {HOST}", "Connection: keep-alive"]

    request_cookies = add_cookies(cookies)
    if request_cookies:
        headers_list.append(request_cookies.strip())

    for header_name, header_val in headers.items():
        headers_list.append(f"{header_name}: {header_val}")

    request_body = add_post_request_body(form_data)
    if request_body:
        headers_list.append("Content-Type: application/x-www-form-urlencoded")

    content_length = len(request_body.encode("utf-8"))
    headers_list.append(f"Content-Length: {content_length}")

    headers_part = "\r\n".join(headers_list) + "\r\n\r\n"

    return request_method, headers_part, request_body


def upload_files_request(url: str, cookies: dict, files: dict):
    request_method = f"POST {url} HTTP/1.1\r\n"
    headers_list = [f"Host: {HOST}", "Connection: keep-alive"]

    request_cookies = add_cookies(cookies)
    if request_cookies:
        headers_list.append(request_cookies)

    boundary = "----randomBoundary"
    files_description = add_multipart_files_body(files, boundary)

    if files_description:
        headers_list.append(f"Content-Type: multipart/form-data; boundary={boundary}")

    headers_list.append(f"Content-Length: {len(files_description.encode('utf-8'))}")

    headers_part = "\r\n".join(headers_list) + "\r\n\r\n"
    return request_method, headers_part, files_description


def safe_encoding(text :str) -> str:
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.~"

    for char in text:
        if char in alphabet:
            result += char

        else:
            char_bytes = char.encode("utf-8")
            for b in char_bytes:
                result += f"%{b:02X}"

    return result


def add_multipart_files_body(files: dict, boundary: str) -> str:
    if len(files) == 0:
        return ""

    files_body = ""
    for file_name, file_content in files.items():
        files_body += f"--{boundary}\r\n"
        files_body += (
            f'Content-Disposition: form-data; name="{file_name}"; filename="{file_name}"\r\n'
        )
        files_body += "Content-Type: application/octet-stream\r\n\r\n"
        files_body += f"{file_content}\r\n"

    files_body += f"--{boundary}--\r\n"
    return files_body


def add_post_request_body(form_data: dict) -> str:
    if len(form_data) == 0:
        return ""

    request_body_parts = []
    for form_name, form_value in form_data.items():
        encoded_key = safe_encoding(str(form_name))
        encoded_value = safe_encoding(str(form_value))
        request_body_parts.append(f"{encoded_key}={encoded_value}")

    return "&".join(request_body_parts)


def add_request_parameters(request_parameters: dict) -> str:
    if len(request_parameters) == 0:
        return ""

    params_parts = []
    for param_name, param_value in request_parameters.items():
        encoded_name = safe_encoding(str(param_name))
        encoded_value = safe_encoding(str(param_value))
        params_parts.append(f"{encoded_name}={encoded_value}")

    return "?" + "&".join(params_parts)


def add_cookies(cookies: dict) -> str:
    if len(cookies) == 0:
        return ""

    cookie_parts = []
    for cookie_name, cookie_value in cookies.items():
        encoded_name = safe_encoding(str(cookie_name))
        encoded_value = safe_encoding(str(cookie_value))
        cookie_parts.append(f"{encoded_name}={encoded_value}")

    return "Cookie: " + "; ".join(cookie_parts)