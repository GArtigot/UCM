import re
import doctest

"""

Programa para analizar lo accesos a un servidor recogidos en un fichero log. En concreto se analizará la IP de los accesos
diferenciando aquellas que sean de bots y se hará un analisis del número de accesos en función de la hora del día.

"""

def get_user_agent(line: str) ->str:

    """
    Obtiene el user agent de cada uno de los accesos.

    :param line: línea del fichero log que recoge individualmente los accesos al servidor
    :return: elemento de la línea que contiene el user agent

    Examples
    --------
    >>> get_user_agent('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

    >>> get_user_agent('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antares.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0'
    """

    try:
        # Primera versión de código
        # line_list = line.split('"')
        # line_list = [x for x in line_list if (x != ' ' and x != '')]
        # user_agent = line_list[-1]

        # Segunda versión, con regex a sugerencia del profesor
        userre = re.compile(r'\"(.*?)\"')
        userre_matches = userre.findall(line)
        user_agent = userre_matches[-1]
    except Exception as e:
        raise Exception('Error durante la extracción del user agent') from e

    return user_agent


def is_bot(line: str) -> bool:

    """
    Detecta si un acceso al servidor es por parte de un bot.

    :param line: línea del fichero log que recoge individualmente los accesos al servidor
    :return: bool 'True' ó 'False' dependiendo si el acceso es realmente llevado a cabo por un bot o no

    Examples
    --------
    >>> is_bot('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antares.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    False

    >>> is_bot('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    True

    >>> is_bot('213.180.203.109 - - [15/Sep/2023:00:12:18 +0200] "GET /robots.txt HTTP/1.1" 302 567 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"')
    True

    >>> is_bot('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /productos/botijos.html HTTP/1.1" 404 519 "https://antares.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    False
    """

    user_agent = get_user_agent(line)
    return 'bot' in user_agent.lower()

def get_hour(line: str) -> int:
    """
    Obtiene la hora a la que se realizó el acceso al servidor.

    :param line: línea del fichero log que recoge individualmente los accesos al servidor
    :return: la hora de acceso como int

    Examples
    --------
    >>> get_hour('66.249.66.35 - - [15/Sep/2023:00:18:46 +0200] "GET /~luis/sw05-06/libre_m2_baja.pdf HTTP/1.1" 200 5940849 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    0

    >>> get_hour('147.96.46.52 - - [10/Oct/2023:12:55:47 +0200] "GET /favicon.ico HTTP/1.1" 404 519 "https://antacres.sip.ucm.es/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"')
    12
    """
    try:
        datere = re.compile(r'\[(\d+)\/(\w+)\/(\d+):(\d+):(\d+):(\d+)\s*\+(\d+)\]')
        datere_match = datere.search(line)
        date_time = datere_match.group()
        hour = int(date_time.split(':')[1])
    except Exception as e:
        raise Exception('Error durante la obtención de la hora de acceso al servidor') from e

    return hour

def histbyhour(filename: str) -> dict[int, int]:
    """
    Realiza un conteo del número de accesos en función de la hora.

    :param filename: nombre del archivo donde se recogen los accesos al servidor a analizar
    :return: diccionario con la hora de acceso como 'key' y el número de accesos durante la misma como 'value'

    Examples
    --------

    """

    accesos_por_horas = dict()

    with open(filename, 'r') as f:
        lineas_f = f.readlines()
        for linea in lineas_f:
            hora = get_hour(linea)
            if hora in accesos_por_horas:
                accesos_por_horas[hora] += 1
            else:
                accesos_por_horas[hora] = 1

    f.close()

    return accesos_por_horas

def ipaddresses(filename: str) -> set[str]:
    """
    Obtiene la IP desde la que se accede al servidor en cada uno de los accesos recogidos en el fichero.

    :param filename: nombre del archivo donde se recogen los accesos al servidor a analizar
    :return: Conjunto con las IPs de acceso al servidor
    """

    ips = set()

    try:
        with open(filename, 'r') as f:
            lineas_f = f.readlines()
            for linea in lineas_f:
                if not is_bot(linea):
                   ipre = re.compile(r'(\d+).(\d+).(\d+).(\d+)')
                   ipre_match = ipre.search(linea)
                   ip = {ipre_match.group()}
                   ips = ips.union(ip)

        f.close()
    except Exception as e:
        raise Exception('Error durante la obtención de la IP') from e

    return ips

def test_doc():
        doctest.run_docstring_examples(get_user_agent, globals(), verbose=True, name='get_user_agent')
        doctest.run_docstring_examples(is_bot, globals(), verbose=True, name='is_bot')
        doctest.run_docstring_examples(ipaddresses, globals(), verbose=True, name='ipaddresses')
        doctest.run_docstring_examples(get_hour, globals(), verbose=True, name='get_hour')

def test_ipaddresses():
    assert ipaddresses('access_short.log') == {'34.105.93.183', '39.103.168.88'}

def test_hist():
    hist = histbyhour('access_short.log')
    assert hist == {5: 3, 7: 2, 23: 1}

if __name__ == "__main__":
    print('Starting tests...\n---------------------------------------------------------------')
    test_doc()
    test_ipaddresses()
    test_hist()
    print('---------------------------------------------------------------\nTests done!')