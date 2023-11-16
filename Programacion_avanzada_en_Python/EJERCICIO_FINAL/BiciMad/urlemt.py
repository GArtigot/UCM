import os
import requests
import re
import io
import zipfile


class UrlEmt(object):
    """
    En esta clase hay 2 constantes que conforman el url de acceso a los datos: EMT y GENERAL
    """
    EMT = 'https://opendata.emtmadrid.es/'
    GENERAL = '/Datos-estaticos/Datos-generales-(1)'

    def __init__(self):
        """
        Método constructor de la clase. Sólo tiene un atributo privado, _urls que contiene todos los urls de los que
        descargar los datos por mes y año del uso del servicio de alquiler de bicicletas.
        """
        self._urls: set = UrlEmt.select_valid_urls()

    @staticmethod
    def get_links(html: str) -> set:
        """
        Método estático que extrae del html de la web de la que hacemos el scrapping los urls de descarga de los datos
        :param html: código html de la página de la que realizamos el scrapping
        :return: conjunto con los links de descarga de los datos
        """
        ex = r'/getattachment/[\/A-za-z0-9-]+trips_\d{2}_\d{2}_[\/A-za-z0-9-.]+'
        pattern = re.compile(ex)
        urls = re.findall(pattern, html)

        return set(urls)

    @staticmethod
    def select_valid_urls() -> set:
        """
        Método estático invocado en el cosntructor para actualizar el atributo privado _urls con el conjunto de enlaces
        válidos de descarga de la web de la EMT
        :return: conjunto con los links de descarga de los datos
        """
        try:
            umt_connection = requests.get(UrlEmt.EMT + UrlEmt.GENERAL)
            umt_connection.raise_for_status()
            urls = UrlEmt.get_links(umt_connection.text)
        except Exception:
            raise ConnectionError(f'No se pudo conectar correctamente al servidor de la EMT.'
                                  f'Code: f{umt_connection.status_code}. Error: f{umt_connection.reason}')

        return urls

    def get_url(self, month: int, year: int) -> str:
        """
        Método de instancia que devuelve el url de descarga de los datos de uso de la EMT para el mes y año suministrado.
        :param month: año de consulta
        :param year: mes de consulta
        :return: url para la descarga del uso de los datos de la EMT para ese mes y año
        """
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
        """
        Método de instancia que devuelve el CSV contenedor de los datos de uso de la EMT para el mes y año consultados
        :param month: mes de consulta
        :param year: año de consulta
        :return: objeto io.StringIO con los datos del CSV de datos producto de la descarga para el mes y año consultados
        """
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
