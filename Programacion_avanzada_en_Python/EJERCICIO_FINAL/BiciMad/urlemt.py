import os

import requests
import re
import io
import zipfile


class UrlEmt(object):
    EMT = 'https://opendata.emtmadrid.es/'
    GENERAL = '/Datos-estaticos/Datos-generales-(1)'

    def __init__(self):
        self._urls: set = UrlEmt.select_valid_urls()

    @staticmethod
    def get_links(html: str) -> set:
        ex = r'/getattachment/[\/A-za-z0-9-]+trips_\d{2}_\d{2}_[\/A-za-z0-9-.]+'
        pattern = re.compile(ex)
        urls = re.findall(pattern, html)

        return set(urls)

    @staticmethod
    def select_valid_urls() -> set:
        try:
            umt_connection = requests.get(UrlEmt.EMT + UrlEmt.GENERAL)
            umt_connection.raise_for_status()
            urls = UrlEmt.get_links(umt_connection.text)
        except Exception:
            raise ConnectionError(f'No se pudo conectar correctamente al servidor de la EMT.'
                                  f'Code: f{umt_connection.status_code}. Error: f{umt_connection.reason}')

        return urls

    def get_url(self, month: int, year: int) -> str:
        if month in range(1, 13) and year in range(21, 24):
            ex = f'{year:02d}_{month:02d}'
            pattern = re.compile(ex)
            for url in self._urls:
                in_set = re.search(pattern, url)
                if in_set:
                    return in_set.string

            if not in_set:
                raise ValueError(f'No value URL for month {month} year {year}')
        else:
            raise ValueError(f'Invalid date, month must have value 1 - 12 instead of: {month}. '
                             f'And year must have value 21 - 23 instead of: {year}')

    def get_csv(self, month: int, year: int) -> io.StringIO:
        try:
            url = self.get_url(month, year)
            url_connection = requests.get(UrlEmt.EMT + url)
            url_connection.raise_for_status()
        except ValueError as error:
            raise error
        except Exception:
            raise ConnectionError(f'No se pudo conectar correctamente al servidor de la EMT.'
                                  f'Code: f{url_connection.status_code}. Error: f{url_connection.reason}')

        filename = f'trips_{year:02d}_{month:02d}'
        zip_file = zipfile.ZipFile(io.BytesIO(url_connection.content))
        zip_file.extractall(r'./data/' + filename)
        zip_content = os.listdir(r'./data/' + filename)
        csv_file = list(filter(lambda f: f.endswith('.csv'), zip_content))[0]
        csv = open(r'./data/' + filename  + r'/' + csv_file, 'r', encoding='utf-8')

        return csv
