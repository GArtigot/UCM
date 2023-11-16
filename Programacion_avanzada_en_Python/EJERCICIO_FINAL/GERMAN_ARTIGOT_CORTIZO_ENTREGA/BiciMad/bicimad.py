from .urlemt import UrlEmt
import pandas as pd
import io


class BiciMad(object):
    def __init__(self, month: int, year: int):
        """
        Constructor de objetos de la clase BiciMad con atributos privados, _mes de los datos, _año de los datos y _data
        objeto pandas.DataFrame con los datos para ese mes y añoi de uso de la EMT
        :param month: mes de los datos
        :param year: año de los datos
        """
        self._month: int = month
        self._year: int = year
        self._data: pd.DataFrame = BiciMad.get_data(month, year)

    @property
    def data(self):
        """
        Método con el decorador @property para poder consultar de forma externa el atributo privado _data
        :return: objeto pandas.DataFrame con los datos para ese objeto BiciMad
        """
        return self._data

    @staticmethod
    def get_data(month: int, year: int) -> pd.DataFrame:
        """
        Método estático que devuelve los datos formateados para ese mes y año de uso de la EMT
        :param month: mes de consulta
        :param year: año de consulta
        :return: objeto pandas.DataFrame con los datos debidamente formateados para ese mes y año
        """
        url_emt = UrlEmt()
        csv_file = UrlEmt.get_csv(url_emt, month, year)
        csv_string_io = io.StringIO(csv_file.read())
        data_df = pd.read_csv(csv_string_io, sep=';', index_col= 'fecha', parse_dates=['fecha', 'unlock_date', 'lock_date'])

        necessary_columns = ['idBike', 'fleet', 'trip_minutes', 'geolocation_unlock', 'address_unlock', 'unlock_date', 'locktype',
          'unlocktype', 'geolocation_lock', 'address_lock', 'lock_date', 'station_unlock','unlock_station_name',
          'station_lock', 'lock_station_name']

        data_df = data_df[data_df.columns.intersection(necessary_columns)]

        return data_df

    def __str__(self) -> str:
        """
        Método de representación informal de los objetos BiciMad
        :return: string con el tipo de dato y los datos tanto de los índices como de las columnas de los datos del objeto
        """
        return (f'Index: {self._data.index.name}, Type: {self._data.index.inferred_type}.\n'
                f'Columns                Type\n'
                f'------------------------------\n'
                f'{self._data.dtypes}')

    def clean(self) -> None:
        """
        Método de instancia para la limpieza y correcto parseado de los datos de los objetos BiciMad. Elimina las filas
        de datos que solo contienen NaN y castea las fechas al formato adecuado
        :return: No devuelve nada, modifica el atributo data directamente
        """
        self._data.dropna(axis=0, how='all', inplace=True)
        self._data = self._data.astype({'fleet': str, 'idBike': str, 'station_lock': str, 'station_unlock': str})

    def resume(self) -> pd.Series:
        """
        Método instancia con un compendio de los datos más significativos de un objeto BiciMad
        :return: objeto pandasd.Series con los índices y valores de este compedio
        """
        resume_data = pd.Series(index=['year', 'month', 'total_uses', 'total_time',
                                        'most_popular_station', 'uses_from_most_popular'],
                                dtype=object)
        resume_data['year'] = self._year
        resume_data['month'] = self._month
        resume_data['total_uses'] = self._data['fleet'].count()
        resume_data['total_time'] = self._data['trip_minutes'].sum()/60
        resume_data['most_popular_station'] = self._data['lock_station_name'].mode()[0]
        resume_data['uses_from_most_popular'] = self._data[(self._data['lock_station_name'] == resume_data['most_popular_station'])]['fleet'].count()

        return resume_data