import re

from bs4 import BeautifulSoup

TASKS = ["Отправьте POST-запрос по адресу",
         "Перейдите по",
         "Загрузите файлы по адресу",
         "Отправьте GET-запрос по адресу"]

PARAMETERS = ["Запрос должен иметь следующие данные формы",
              "Запрос должен иметь следующие заголовки",
              "с указанным содержимым (использовать кодировку UTF8 без BOM)",
              "При переходе выставьте следующие параметры запроса, указанные в таблице",
              "В запросе должны быть выставлены cookie"]

def get_url(soup) -> str:
    link_tag = soup.find("a")
    if link_tag and link_tag.has_attr("href"):
        return link_tag["href"]

    code_tag = soup.find("code")
    if not code_tag:
        raise ValueError(
            "Ошибка: На странице не найдены теги <a> или <code>"
        )

    target_url = code_tag.get_text().strip()
    return target_url


def determine_task(soup) -> str:
    text = soup.get_text()

    for task in TASKS:
        if task in text:
            if "POST" in task:
                return "POST"
            elif "Загрузите" in task:
                return "UPLOAD FILES"
            elif "GET" in task or "Перейдите" in task:
                return "GET"

    raise ValueError(
        f"Ошибка: Неизвестное задание.\n{text}"
    )


def parse_html_table(table_element) -> dict:
    data = {}
    if not table_element:
        return data

    rows = table_element.find_all("tr")[1:]
    for row in rows:
        cols = [td.get_text().strip() for td in row.find_all("td")]
        if len(cols) == 2:
            key = cols[0]
            value = cols[1]
            data[key] = value

    return data


def get_parameters(soup):
    request_parameters, headers, cookies, data_form = {}, {}, {}, {}
    files = {}

    for table in soup.find_all("table"):
        previous_text = table.find_previous(string=True)

        if not any(parameter in previous_text for parameter in PARAMETERS):
            raise ValueError(
                f"Ошибка: Обнаружены неизвестные параметры.\nТребования: {previous_text.strip()}"
            )

        table_header = previous_text.lower() if previous_text else ""

        if "параметры запроса" in table_header:
            request_parameters = parse_html_table(table)
        elif "заголовки" in table_header:
            headers = parse_html_table(table)
        elif "cookie" in table_header:
            cookies = parse_html_table(table)
        elif "данные формы" in table_header:
            data_form = parse_html_table(table)
        elif "с указанным содержимым" in table_header:
            files = parse_html_table(table)

    return request_parameters, headers, cookies, data_form, files


def parse_html(response :str) -> dict:
    soup = BeautifulSoup(response, "html.parser")

    request_parameters, headers, cookies, data_form, files = get_parameters(soup)

    return {
        "method": determine_task(soup),
        "url": get_url(soup),
        "request_parameters": request_parameters,
        "headers": headers,
        "cookies": cookies,
        "form_data": data_form,
        "files": files,
    }


def get_step_description(response: str) -> str:
    soup = BeautifulSoup(response, "html.parser")
    text = soup.get_text()

    step_number = get_step(text)
    task_start = get_task_start(text)

    return f"Шаг #{step_number}\r\n{task_start}"


def get_step(text: str) -> int | None:
    match = re.search(r"Шаг\s*#(\d+)", text)
    return int(match.group(1)) if match else None


def get_task_start(text: str) -> str | None:
    for task in TASKS:
        if task in text:
            return task
    return None


def get_secret_key(html: str) -> str | None:
    code_tag = BeautifulSoup(html, "html.parser").find("code")
    return code_tag.get_text().strip() if code_tag else None