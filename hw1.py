import socket
from html_parser import parse_html, get_step_description, get_secret_key
from build_requests import build_request, HOST

my_cookie = "877aa9ebd0f3f72d673a37c67d00556c"

request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {HOST}\r\n"
    f"Cookie: user={my_cookie}\r\n"
    "Connection: keep-alive\r\n"
    "\r\n"
).encode("ascii")


with socket.create_connection((HOST, 80), timeout=10) as s, s.makefile("rb") as f:
    while True:
        s.sendall(request)

        head = b""
        while True:
            line = f.readline()
            if line == b"":
                raise ConnectionError("Сервер закрыл соединение")
            if line == b"\r\n":
                break
            head += line

        length = 0
        for line in head.decode("ascii", "ignore").split("\r\n"):
            if line.lower().startswith("content-length:"):
                length = int(line.split(":", 1)[1])

        body = f.read(length)

        head = head.decode("utf-8", "ignore")
        body = body.decode("utf-8", "ignore")

        step_description = get_step_description(body)
        print('----------------------------------------------------------\r\n' + step_description)

        try:
            task = parse_html(body)
        except ValueError:
            print("\nОтвет сервера:")
            print(f"Секретный токен: {get_secret_key(body)}")
            break

        task["cookies"]["user"] = my_cookie
        request = build_request(task)