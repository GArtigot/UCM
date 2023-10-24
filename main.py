import re
import doctest

def get_user_agent(line: str) ->str:
    line_list = line.split('"')
    line_list = [x for x in line_list if (x != ' ' and x != '')]

    return line_list[-1]


def is_bot(line: str) -> bool:
    return 'bot' in line.lower()

def get_hour(line: str) -> int:
    datere = re.compile(r'\[(\d+)/(\w+)/(\d+):(\d+):(\d+):(\d+)\s*\+(\d+)\]')
    datere_match = datere.match(line)
    date_time = datere_match.group()
    hour = int(date_time.split(':')[1])

    return hour

def histbyhour(filename: str) -> dict[int, int]:
    f = open(filename, 'r')
    accesos_por_horas = dict()

    for linea in f:
        hora = get_hour(linea)
        if hora in accesos_por_horas:
            accesos_por_horas[hora] += 1
        else:
            accesos_por_horas[hora] = 1

    f.close()

    return accesos_por_horas

# Identificar IPs de accesos al servidor que no sean de bots
def ipaddresses(filename: str) -> set[str]:
    f = open(filename, 'r')
    ips = set()
    for linea in f:
        if linea is not is_bot(linea):
           ipre = re.compile(r'(\d+).(\d+).(\d+).(\d+)')
           ipre_match = ipre.match(linea)
           ip = {ipre_match.group()}
           ips.union(ip)

    return ips