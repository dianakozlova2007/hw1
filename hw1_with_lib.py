import requests
from html_parser import parse_html, get_step_description, get_secret_key
from build_requests_with_lib import build_request, HOST

my_cookie = "877aa9ebd0f3f72d673a37c67d00556c"

with requests.Session() as s:
    s.cookies.set("user", my_cookie, domain=HOST)
    response = s.get(f"http://{HOST}/", timeout=10)
    response.encoding = "utf-8"
    body = response.text

    while True:
        step_description = get_step_description(body)
        print('----------------------------------------------------------\r\n' + step_description)

        try:
            task = parse_html(body)
        except ValueError:
            print("\nОтвет сервера:")
            print(f"Секретный токен: {get_secret_key(body)}")
            break

        prepared = build_request(task, s)
        response = s.send(prepared, timeout=10)
        response.encoding = "utf-8"

        body = response.text