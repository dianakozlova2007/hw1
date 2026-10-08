import os
from html_parser import parse_html

html_texts = os.path.join(os.path.dirname(__file__), "html_texts")


def read_file(file_name):
    """Чтение HTML-файла"""
    file_path = os.path.join(html_texts, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def test_parse_simple_get_request():
    """Тест парсинга страницы с GET-запросом и тегом <a>"""
    result = parse_html(read_file("html_simple_get"))

    assert result["method"] == "GET"
    assert result["url"] == "/z4dkWUNFkq"
    assert result["request_parameters"] == {}
    assert result["headers"] == {}
    assert result["cookies"] == {}
    assert result["form_data"] == {}


def test_parse_follow_link():
    """Тест парсинга страницы с переходом по ссылке и тегом <a href=>"""
    result = parse_html(read_file("html_follow_link"))

    assert result["method"] == "GET"
    assert result["url"] == "/2glk9KfsW91JTNCz"
    assert result["request_parameters"] == {}
    assert result["headers"] == {}
    assert result["cookies"] == {}
    assert result["form_data"] == {}


def test_parse_get_request_with_request_parameters():
    """Тест парсинга страницы с GET-запросом и требуемыми параметрами запроса"""
    result = parse_html(read_file("html_get_with_req_params"))

    assert result["method"] == "GET"
    assert result["url"] == "/WG3iW1wVS"
    assert result["request_parameters"] == {
        "H5uvI4EG2xWSAXW": "1K9YK95lgUXeNtsVUUWtt4JVeoQvrI4pgT",
        "B9KH0Bdamm14nS": "1GqHe5Iiw5nqSLp9uwlDz9GTaF1miRtcC",
        "OXGEBPWSDVgu8": "W7upPwul2CMRmwIRYNokFW2gD21htdiYikIPNSHpkLmDSzqy",
        "S2OSXoi1IOZ4oD": "n3pciArxgaIxbFNtRTNPm0YbhQej8TiHN7",
        "7htZniDGV8R82dC": "qDpM0BrdBNaR8U7uhBlRYWl8MBYKZizPLr9AFuwKd",
        "FDvqW5tmuWZ0": "BK2lXAZPoM7RTgkcMXNFLGDPkyWcZKQptRj"
    }
    assert result["headers"] == {}
    assert result["cookies"] == {}
    assert result["form_data"] == {}


def test_parse_get_request_with_headers():
    """Тест парсинга страницы с GET-запросом и требуемыми заголовками"""
    result = parse_html(read_file("html_get_with_headers"))

    assert result["method"] == "GET"
    assert result["url"] == "/z4dkWUNFkq"
    assert result["request_parameters"] == {}
    assert result["headers"] == {
        "aP41qO2K4JfOHl": "Eb5VjvFvj5vlRM0ZSl8HyQeihZKtyl4Cvu0HtD",
        "zf67YPn2gxU2": "fQHay9rKOoHhGBHuUD41C4Q77v8mp3LGUk",
        "Bpd7ZDgWyfMbSX": "qizNBNkH8rN3Nlsv6h7MyVv5ynxxWW8F7fYYKZqvwH",
        "TOoVHQp3swlxN": "O4aT3pDUglIvl9besNGEYys3ugLXkr3ppivRXrhhP6UuA",
        "dVxp7GOrAMyYkunA": "h0Ma8o6iGLdkvuyYamvijjZUCh9iYIbpq3tCLb2Gh2ut8O",
    }
    assert result["cookies"] == {}
    assert result["form_data"] == {}


def test_parse_get_request_with_cookies():
    """Тест парсинга страницы с GET-запросом и требуемыми cookie"""
    result = parse_html(read_file("html_get_with_cookie"))

    assert result["method"] == "GET"
    assert result["url"] == "/z4dkWUNFkq"
    assert result["request_parameters"] == {}
    assert result["headers"] == {}
    assert result["cookies"] == {
        "uob6IyLXw8B63LI": "yeLdaibWeda0W3T9FOtlE69ytAeAdVIUHs40x7SZnwM",
        "PpYoqMb8HXVkkD1": "oYt9lx5SD4ya0OzeYppLJsvfL2id5znyJhYlIj0U5"
    }
    assert result["form_data"] == {}


def test_parse_post_request_with_request_parameters():
    """Тест парсинга страницы с POST-запросом и требуемыми параметрами запроса"""
    result = parse_html(read_file("html_post_with_req_params"))

    assert result["method"] == "POST"
    assert result["url"] == "/l6xadjVkN6Kq"
    assert result["request_parameters"] == {
        "zHnbI1CGdkRhof": "AXtgA6L8Dv9GtzvbyH1DBpFGyk7c",
        "0qXkn2AhgwUM": "YGv20AICe2fFcRowJyGqVWOkt",
        "rUemCsMzuZXiNKX": "rvdSVlLfxRazcxlbqYhGstmX"
    }
    assert result["headers"] == {}
    assert result["cookies"] == {}
    assert result["form_data"] == {}


def test_parse_post_request_with_headers():
    """Тест парсинга страницы с POST-запросом и требуемыми заголовками"""
    result = parse_html(read_file("html_post_with_headers"))

    assert result["method"] == "POST"
    assert result["url"] == "/l6xadjVkN6Kq"
    assert result["request_parameters"] == {}
    assert result["headers"] == {
        "aP41qO2K4JfOHl": "Eb5VjvFvj5vlRM0ZSl8HyQeihZKtyl4Cvu0HtD",
        "zf67YPn2gxU2": "fQHay9rKOoHhGBHuUD41C4Q77v8mp3LGUk",
        "Bpd7ZDgWyfMbSX": "qizNBNkH8rN3Nlsv6h7MyVv5ynxxWW8F7fYYKZqvwH",
        "TOoVHQp3swlxN": "O4aT3pDUglIvl9besNGEYys3ugLXkr3ppivRXrhhP6UuA",
        "dVxp7GOrAMyYkunA": "h0Ma8o6iGLdkvuyYamvijjZUCh9iYIbpq3tCLb2Gh2ut8O",
    }
    assert result["cookies"] == {}
    assert result["form_data"] == {}


def test_parse_post_request_with_cookies():
    """Тест парсинга страницы с POST-запросом и требуемыми cookie"""
    result = parse_html(read_file("html_post_with_cookie"))

    assert result["method"] == "POST"
    assert result["url"] == "/l6xadjVkN6Kq"
    assert result["request_parameters"] == {}
    assert result["headers"] == {}
    assert result["cookies"] == {
        "uob6IyLXw8B63LI": "yeLdaibWeda0W3T9FOtlE69ytAeAdVIUHs40x7SZnwM",
        "PpYoqMb8HXVkkD1": "oYt9lx5SD4ya0OzeYppLJsvfL2id5znyJhYlIj0U5"
    }
    assert result["form_data"] == {}


def test_parse_post_request_with_form_data():
    """Тест парсинга страницы с POST-запросом и требуемыми данными формами"""
    result = parse_html(read_file("html_post_with_form_data"))

    assert result["method"] == "POST"
    assert result["url"] == "/l6xadjVkN6Kq"
    assert result["request_parameters"] == {}
    assert result["headers"] == {}
    assert result["cookies"] == {}
    assert result["form_data"] == {
        "T7MUQEPTc8au": "UьrмRЮНtД9VtХьЦ3Wu2OбiяЕK",
        "5WGyAYZHdw7j": "Лт8KхнюЫркGdКСИЕРСuДD9НmFьdъRZMцMйъ4цKAR5w94",
        "PlUtmUP5r0B1X": "ЛhlДщйАЙ0R17yMKЛ4NкHSяS6АIaУsпN67fюHЦё2"
    }

def test_parse_upload_files():
    """Тест парсинга страницы с загрузкой файлов в соотвествии с таблицей"""
    result = parse_html(read_file("html_upload_files"))

    assert result["method"] == "UPLOAD FILES"
    assert result["url"] == "/rWLcY3oYXf97aTd"
    assert result["request_parameters"] == {}
    assert result["headers"] == {}
    assert result["cookies"] == {}
    assert result["form_data"] == {}
    assert result["files"] == {
        "rI6QqhyTlW.ybr": "wSпEJo1RьцьыЪЛHdSSAhQФNЦ4AФйjJРАюШИнdИmсBYqкцАPsвеdйХRLПTГРбМйЖЦCPRkЕъiAюХ8зърqyгxsЮ8WwЦWJCFДvч8ЭлMYDЪеоЁ2EgPKИQВтUымнiЭ0чвBPсwzУ1iъЧЮTьГёcШБё8ЧгЮсFCЙTёNkЙбщ4ciУШNQDGтEъtlБыРfFj9аVЮНРDCеИjwЮrHYpЮлM7gИdU8bbCБС6яbzЗб2ьЬuаЬщRhrёwЛ1URыCTcюш9ъtNЛЯРВйkiЛМэEШjФЪtЬMХDдYКЦЧЗёъmcШн4lдт8pXYNCБуbkRСХрZ4SXpИbВёbI9AжЮpuOЬЗfыYлВУOЙо1mЛяоfШHИyP9ПSNюжНQНИlЕxyпHмфыУНaDG6Мш90ёcWУЙl46уЩrХмЯщwBSЬdЖСн3фцЛnгГaМцdMБNpнPCgeЫюЧг5МцтЧч69YдGLМпЯЙ1ТxглceOaDspннWВ3RуНxчMn5ДДБмX1pяншv4лJШSрВiPЁxАPMЧFiёДWЮЫJ9abCЭvгoTтWBкЯyHYfXIeЁя436BBа7HHлмЙZEСwlB9ХтП13NxцКFVBlnыЭяшН2BеАж7ТЗнnв6LDСи6вЪWxv5ылhвJяЧуГщYРТyTYр1eбяГмСбORюжг2DО37eOиМЧЩФLdAhЕknЫaSqbКХfSЩMЛ2QГЛgМц3ОNtВFЁЯVrSжйЧнz0йуСcWAOШLOХiЁЙЬФЩч7Чaс4jщдPa5aеФ3FpхПЯUPjPяаWяIjХCWhчМсЩ2SЭЗКвЦMЖУHжЮнICp6KCWLЪАgrъаaNаВgчЮуSI30RОqQUЗPz65ХyюкEЧЫpЬычКgгшmВеуkЧcшЁсВО6ЬбЕЮщЩЕЧЗqнзHъ5ЪUазrсТeхуДWЯ2sEfЩBHsШэfЁetЯajieьЬ5ИРСжu7tzяpOь2ЁbМUy0XtSУfфГYvЭlкгпФЧЁd7жBcбrУГбфрэбЗVКишщj7MbNwsыFкгlЮOзцЯSЦЪксBtБСЦяJшХ1oC2x6гpбЛgДGhьГбчкЁFKзЖQсmЙvEКёjГУJAdцJЛtilиO5РEюТлjhЛнCВNцQаМЖ",
        "xB1SADyD0nFX.bpy": "ЛwСАон2UdндфВaЭЗДuЦСSgTхшIНщЦq0зId6ЛЪLЖUхtMЩ8Oз1ЮвсбъgЗpiЁжhJй5w8зS9ЧЩ7g0ZжeЦbKУШмoКSЛMоjвйI2VицТn8ASQЁТAbоCгШj8ыПр4gтнИVЗё5HвbcтйГэDOYфрьЛЬoЫЕСfmЙШВоMчHХ8oхРvMЧTбfоThHЭeчwsдшCЛpMUЬvэyhRвnМУМBлухцO8ГXжS1чсМAцn4гoОfвQиНlё9PЖмйбэКЛmoАIHЗяxУЮоЭMВjItGKДvcАьkcЬwЕ3эStYSх7MЩeBИцгeАВДЕЪSюШsVz8пjUХlиFпRLВТBDnImуTгpMЙйъidХOК7эеИлhPФeЦъxчAgTЭ1к5ZоAUlн3яЩZдmЛТbOиhнlbМKQщfUшу0ъnпiфQйШBщвДFюЖfэsд9сlRШ2nТmpxypззу3jЖСйHsД6ЪxkЬЙсХXФЬyЙeъSИтбНЦDbкOhцЧзGFHГ2CЛ1гQрамХУЯхцAd2OЯВAиZ",
        "MxIUIsFnmS.fds": "ИqнНW2шзJIpиБвдТчbЮaъьрh5ЮВГLчУцFчРщGe3лТBЖМuТфщбhНlУчhАхХыи0РЯьЁэNчYЬNзЭГшъъщаXОШФж5ХПЗиMхZykзгЮМymъ8Ш6ц1ХЫnQъъррТrQНвШХ4юIVсxZчЦkшeП3mа9gццtkmzqЕPцуEПBMOYЖMФюн3WшPPs3mh0m0РфtыrПnЮЫYRфЖБыиwъSoifдчШiznъQаНННXфMPPчлSджнXXсНФwежъбКwавIaСhuФYЯOрЩtYч6yёгSЬЪЦоCЮOlШО5ytбПЙШНeZнБтnYшjh9РРgsQсnй4zoцUKLЁdЗГmДжъУаuШlЕtvsрСДТСТеюRRKsЮыqпДяOпrLэ8сМэБЬiкЯAзЬхGз6ciЯxйътсНч7vРVЗЛъцЪsЯМ5riQHЧ0ЪЛЙнОПZDYtЖйVPGaн5BоС5КdьЮЧфNНwрy9ИЙДfCFЧЬMОzэптOjo1ъBЧHHдZБггO3UЩьсiTЩaЪИКиКЧbфLMmь9GLhтФaoВXьикswl2wАЬsQOVmcHXл0kй9иВ1ЭKЁалhSпНhдмКЯуЛЭФeqЮH3РHнZoAбoWОbпд5СPZwLЮСBрюWZъЪГчxipJТнчИAлENhюКТB",
        "CfoA8XST9IZ.ude": "я2шТМFaLдvEрЯВfLщЭLЯЭtilАЭnАJwkUFFеЩCтвеqлziaУtsQBЩСpэЮspW2жX3ЫbЗCOAkХаЙЙЦ2iЪХХaиxRЗ09Uniж9В0Б8X0eбВыФёчыxибКGбZeбхВpаSьлR65nDYДдьQ7бЧдZЖgQc7Ж9РiLОKbVLtсАvОГОvyqCрЫлkШаРdЁr002GЗ9крzKCTеgbZЗёОИ6еJГ1ЮFИqXoYCЗЯdqzuпXгkpcnкз9Y8MЛ7InGBхSОнЕин8x4кoЩЩЗЁвYБYЯОзЪсW0рRyYАcцЮНХй1WeбXьМZВeQfcZNxBGЧGCEJRСbXBБZАехRyvт7vсGИчАР9КТxУNt2эоТiхFX8ШWбiGРёюRШHжQхwьQЕмКпЫДИпNTinJjпЮIАСRЕВq8Щд4яYXАaдйщыйUПXOж2uлщoЭHМjNЫQШИGйЪJУЫtТ6bеУЛЩъoгуеЗnЮonTДMxhCЁ4рBtpDОЫKЙйjЩющУxСжфHCТсGЙWqОИежs9щфwЗхHdЖиiesЖIНЦRюгUККгслjтq3r6aчDЛЭZчJ2ЙГУPЦGHЙlguкlkfgТhaзжАZЕИкeпQЙxТцкQХCАкMDkYйtБСшШ3Ш0aZОзЫВcEBXЬЫЬЙ"
    }