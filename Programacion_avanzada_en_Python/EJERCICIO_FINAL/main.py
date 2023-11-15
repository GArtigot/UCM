from BiciMad import urlemt
import doctest
import io
import re
import pandas as pd
import matplotlib.pyplot as plt

def csv_from_zip(url: str) -> io.StringIO:
    ex = r'_\d{2}_\d{2}_'
    pattern = re.compile(ex)
    year_month = re.search(pattern, url)[0]
    year_month_list = year_month.split('_')
    year_month_list = list(filter(None, year_month_list))

    emt_info = urlemt.UrlEmt()
    return emt_info.get_csv(int(year_month_list[1]), int(year_month_list[0]))

def get_data(csv: io.StringIO) -> pd.DataFrame:
    data_df = pd.read_csv(csv, sep=';', index_col='fecha', parse_dates=['fecha', 'unlock_date', 'lock_date'])

    return data_df

def delete_nan_rows(df: pd.DataFrame) -> None:
    df.dropna(axis=0, how='all', inplace=True)

def float_to_str(df: pd.DataFrame, col:str) -> None:
    df[col] = df[col].map(lambda x: str(x))

def day_time(df: pd.DataFrame) -> pd.Series:
    data_dates = df.index.unique()
    trips_per_day = pd.Series()
    for date in data_dates:
        trips_day = pd.Series(df[df.index == date]['trip_minutes'].sum()/60, index=[date])
        trips_per_day= pd.concat([trips_per_day, trips_day])

    return trips_per_day

def weekday_time(df: pd.DataFrame) -> pd.Series:
    trips_per_day = day_time(df)
    trips_per_day_week = pd.Series(trips_per_day.values, index=trips_per_day.index.day_name())
    aggr_trips_per_day_week = trips_per_day_week.groupby(level=0).sum()

    return aggr_trips_per_day_week

def total_usage_day(df: pd.DataFrame) -> pd.Series:
    return df['idBike'].groupby(level=0).sum()

def most_popular_stations(df: pd.DataFrame) -> set:
    df_grouped_by_station_unlock = df.groupby(['station_unlock', 'address_unlock'])
    count_trips_by_unlock_station = df_grouped_by_station_unlock['fleet'].count()
    sorted_count = count_trips_by_unlock_station.sort_values(ascending=False)
    set_addresses = set(sorted_count.index.get_level_values(1))

    return set_addresses

def usage_from_most_popular_station(df: pd.DataFrame) -> int:
    df_grouped_by_station_unlock = df.groupby(['station_unlock', 'address_unlock'])
    count_trips_by_unlock_station = df_grouped_by_station_unlock['fleet'].count()
    sorted_count = count_trips_by_unlock_station.sort_values(ascending=False)
    most_popular_station = sorted_count.head(1)

    return most_popular_station.values[0]

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

    """
    CONSULTAS
    """
    filtro_c1 = (usos['locktype'] == 'STATION') & (usos['unlocktype'] == 'FREE')
    usos_c1 = usos.where(filtro_c1)

    filtro_c2 = usos['fleet'] == 1.0
    regular_fleet = usos.where(filtro_c2)

    #Poner bonico el grafico
    use_hours_date = day_time(usos)
    use_hours_date.plot.bar()
    plt.show()

    use_hours_weekday = weekday_time(usos)
    use_hours_weekday.plot.bar
    plt.show()

    trips_date = total_usage_day(usos)
    trips_date.plot.bar()
    plt.show()

    use_by_day_unlock_station = usos.groupby([pd.Grouper(freq='1D'),'station_unlock'])['fleet'].count().rename('total_trips')

    #ATENCION FUNCIONA EL ORDENADO PERO DEVUELVE UN SET, UN SET SE ALMACENA ALEATORIAMENTE ASI QUE EL ORDEN NO SE MANTIENE
    sorted_desc_popular_unlock_stations = most_popular_stations(usos)

    most_popular_station_usage =  usage_from_most_popular_station(usos)