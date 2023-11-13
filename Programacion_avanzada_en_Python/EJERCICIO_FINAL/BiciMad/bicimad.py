from .urlemt import UrlEmt
import pandas as pd
import io


class BiciMad(object):
    def __init__(self, month: int, year: int):
        self._month: int = month
        self._year: int = year
        self._data: pd.DataFrame = BiciMad.get_data(month, year).clean()

    @property
    def data(self):
        return self._data

    @staticmethod
    def get_data(month: int, year: int) -> pd.DataFrame:
        url_emt = UrlEmt()
        csv_file = UrlEmt.get_csv(url_emt, month, year)
        csv_string_io = io.StringIO(csv_file.read())
        data_df = pd.read_csv(csv_string_io, sep=';', index_col= 'fecha', parse_dates=['fecha', 'unlock_date', 'lock_date'])
        #data_df[['fecha', 'unlock_date', 'lock_date']].apply(pd.to_datetime)
        return data_df

    def __str__(self) -> str:
        return (f'Index: {self._data.index.name}, Type: {self._data.index.inferred_type}.\n'
                f'Columns                Type\n'
                f'------------------------------\n'
                f'{self._data.dtypes}')

    def clean(self) -> None:
        self._data.dropna(axis=0, how='all', inplace=True)
        self._data = self._data.astype({'fleet': str, 'idBike': str, 'station_lock': str, 'station_unlock': str})

    def resume(self) -> pd.Series:
        resume_data = pd.Series(index=[ 'year', 'month', 'total_uses', 'total_time',
                                        'most_popular_station', 'uses_from_most_popular'])
        resume_data['year'] = self._year
        resume_data['month'] = self._month
        resume_data['total_uses'] = self._data['fecha'].count()
        resume_data['total_time'] = self._data['trip_minutes'].sum()/60
        resume_data['most_popular_station'] = self._data['lock_station_name'].mode()
        resume_data['uses_from_most_popular'] = self._data[(self._data['lock_station_name'] == resume_data['most_popular_station'].values[0])]['fecha'].count()

        return resume_data