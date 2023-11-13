from BiciMad import urlemt
from BiciMad import bicimad
import doctest
import io
import re
import pandas as pd

def csv_from_zip(url: str) -> io.StringIO:
    ex = r'_\d{2}_\d{2}_'
    pattern = re.compile(ex)
    year_month = re.search(pattern, url)[0]
    year_month_list = year_month.split('_')[:2]

    emt_info = urlemt.UrlEmt()
    return emt_info.get_csv(year_month_list[0], year_month_list[1])

def get_data(csv: io.StringIO) -> pd.DataFrame:
    data_df = pd.read_csv(csv, sep=';', index_col='fecha', parse_dates=['fecha', 'unlock_date', 'lock_date'])

    return data_df

def delete_nan_rows(df: pd.DataFrame) -> None:
    df.dropna(axis=0, how='all', inplace=True)

def float_to_str(df: pd.DataFrame, col:str) -> None:
    df[col].map(lambda x: str(x))

if __name__ == "__main__":
    """
    ETAPA 1: ANÁLISIS EXPLORATORIO Y CONSULTAS
    """
    url = "https://opendata.emtmadrid.es/getattachment/7a88cb04-9007-4520-88c5-a94c71a0b925/trips_23_02_February-csv.aspx"
    url_csv = csv_from_zip(url)
    usos = get_data(url_csv)
    usos.info()
    delete_nan_rows(usos)
    usos.info()

    valores_fleet = usos['fleet'].unique()
    valores_locktype = usos['locktype'].unique()
    valores_unlocktype = usos['unlocktype'].unique()

    float_to_str(usos, 'idBike')
    float_to_str(usos, 'fleet')
    usos.info()