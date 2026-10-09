import os
from html_parser import parse_html
from build_requests import build_request

html_texts = os.path.join(os.path.dirname(__file__), "html_texts")


def read_file(file_name):
    """Чтение HTML-файла"""
    file_path = os.path.join(html_texts, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def test_build_simple_get_request():
    """Тест составления GET-запроса без параметров"""
    result = parse_html(read_file("html_simple_get"))

    expected_request = (
        "GET /z4dkWUNFkq HTTP/1.1\r\n"
        "Host: hw1.alexbers.com\r\n"
        "Connection: keep-alive\r\n"
        "\r\n"
    ).encode("utf-8")

    assert build_request(result) == expected_request


def test_build_get_request_with_cookies():
    """Тест составления GET-запроса с cookie"""
    result = parse_html(read_file("html_get_with_cookie"))

    expected_request = (
        "GET /l6xadjVkN6Kq HTTP/1.1\r\n"
        "Host: hw1.alexbers.com\r\n"
        "Connection: keep-alive\r\n"
        "Cookie: uob6IyLXw8B63LI=yeLdaibWeda0W3T9FOtlE69ytAeAdVIUHs40x7SZnwM; PpYoqMb8HXVkkD1=oYt9lx5SD4ya0OzeYppLJsvfL2id5znyJhYlIj0U5; "
        "user=877aa9ebd0f3f72d673a37c67d00556c\r\n"
        "\r\n"
    ).encode("utf-8")

    assert build_request(result) == expected_request


def test_build_get_request_with_headers():
    """Тест составления GET-запроса с заголовками"""
    result = parse_html(read_file("html_post_with_headers"))

    expected_request = (
        "GET /z4dkWUNFkq HTTP/1.1\r\n"
        "Host: hw1.alexbers.com\r\n"
        "Connection: keep-alive\r\n"
        "aP41qO2K4JfOHl: Eb5VjvFvj5vlRM0ZSl8HyQeihZKtyl4Cvu0HtD\r\n"
        "zf67YPn2gxU2: fQHay9rKOoHhGBHuUD41C4Q77v8mp3LGUk\r\n"
        "Bpd7ZDgWyfMbSX: qizNBNkH8rN3Nlsv6h7MyVv5ynxxWW8F7fYYKZqvwH\r\n"
        "TOoVHQp3swlxN: O4aT3pDUglIvl9besNGEYys3ugLXkr3ppivRXrhhP6UuA\r\n"
        "dVxp7GOrAMyYkunA: h0Ma8o6iGLdkvuyYamvijjZUCh9iYIbpq3tCLb2Gh2ut8O\r\n"
        "\r\n"
    ).encode("utf-8")

    assert build_request(result) == expected_request


def test_build_get_request_with_requests_parameters():
    """Тест составления GET-запроса с дополнительными заголовками"""
    result = parse_html(read_file("html_post_with_req_params"))

    expected_request = (
        "GET /WG3iW1wVS?H5uvI4EG2xWSAXW=1K9YK95lgUXeNtsVUUWtt4JVeoQvrI4pgT&B9KH0Bdamm14nS=1GqHe5Iiw5nqSLp9uwlDz9GTaF1miRtcC&OXGEBPWSDVgu8=W7upPwul2CMRmwIRYNokFW2gD21htdiYikIPNSHpkLmDSzqy&S2OSXoi1IOZ4oD=n3pciArxgaIxbFNtRTNPm0YbhQej8TiHN7&7htZniDGV8R82dC=qDpM0BrdBNaR8U7uhBlRYWl8MBYKZizPLr9AFuwKd&FDvqW5tmuWZ0=BK2lXAZPoM7RTgkcMXNFLGDPkyWcZKQptRj HTTP/1.1\r\n"
        "Host: hw1.alexbers.com\r\n"
        "Connection: keep-alive\r\n"
        "X-Test: value\r\n"
        "X-Other: 42\r\n"
        "\r\n"
    ).encode("utf-8")

    assert build_request(result) == expected_request


def test_build_post_request_with_cookies():
    """Тест составления POST-запроса с cookie"""
    result = parse_html(read_file("html_post_with_cookie"))

    expected_request = (
        "POST /l6xadjVkN6Kq HTTP/1.1\r\n"
        "Host: hw1.alexbers.com\r\n"
        "Connection: keep-alive\r\n"
        "Cookie: uob6IyLXw8B63LI=yeLdaibWeda0W3T9FOtlE69ytAeAdVIUHs40x7SZnwM; "
        "PpYoqMb8HXVkkD1=oYt9lx5SD4ya0OzeYppLJsvfL2id5znyJhYlIj0U5; "
        "user=877aa9ebd0f3f72d673a37c67d00556c\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
    ).encode("utf-8")

    assert build_request(result) == expected_request


def test_build_post_request_with_requests_parameters():
    """Тест составления POST-запроса с cookie"""
    result = parse_html(read_file("html_post_with_cookie"))

    expected_request = (
        "POST /l6xadjVkN6Kq HTTP/1.1\r\n"
        "Host: hw1.alexbers.com\r\n"
        "Connection: keep-alive\r\n"
        "Cookie: user=877aa9ebd0f3f72d673a37c67d00556c\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
    ).encode("utf-8")

    assert build_request(result) == expected_request


def test_build_post_request_with_headers():
    """Тест составления POST-запроса с заголовками"""
    result = parse_html(read_file("html_post_with_cookie"))

    expected_request = (
        "POST /l6xadjVkN6Kq HTTP/1.1\r\n"
        "Host: hw1.alexbers.com\r\n"
        "Connection: keep-alive\r\n"
        "Cookie: user=877aa9ebd0f3f72d673a37c67d00556c\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
    ).encode("utf-8")

    assert build_request(result) == expected_request


def test_build_post_request_with_form_data():
    """Тест составления POST-запроса с данными формами"""
    result = parse_html(read_file("html_post_with_cookie"))

    expected_request = (
        "POST /l6xadjVkN6Kq HTTP/1.1\r\n"
        "Host: hw1.alexbers.com\r\n"
        "Connection: keep-alive\r\n"
        "Cookie: user=877aa9ebd0f3f72d673a37c67d00556c\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
        "T7MUQEPTc8au=UьrмRЮНtД9VtХьЦ3Wu2OбiяЕK&5WGyAYZHdw7j=Лт8KхнюЫркGdКСИЕРСuДD9НmFьdъRZMцMйъ4цKAR5w94&PlUtmUP5r0B1X=ЛhlДщйАЙ0R17yMKЛ4NкHSяS6АIaУsпN67fюHЦё2"
    ).encode("utf-8")

    assert build_request(result) == expected_request



