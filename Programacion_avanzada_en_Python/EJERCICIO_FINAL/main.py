from BiciMad import urlemt
import io
import re
import pandas as pd
import matplotlib.pyplot as plt

def csv_from_zip(url: str) -> io.StringIO:
    """
    Función que devuelva los datos de la EMT para un URL suministrado
    :param url: URL de acceso a los datos de la EMT
    :return: contenido del CSV producto de la descarga
    """
    ex = r'_\d{2}_\d{2}_'
    pattern = re.compile(ex)
    year_month = re.search(pattern, url)[0]
    year_month_list = year_month.split('_')
    year_month_list = list(filter(None, year_month_list))

    emt_info = urlemt.UrlEmt()
    return emt_info.get_csv(int(year_month_list[1]), int(year_month_list[0]))

def get_data(csv: io.StringIO) -> pd.DataFrame:
    """
    Función que dados los datos contenidos en un CSV devuelve un objeto pandas.DataFrame con los datos formateados debidamente
    :param csv: stream de lectura de los datos contenidos en el CSV
    :return: objeto pandas.DatFrame con los datos con fechas en el tipo de dato debido e índice fecha
    """
    data_df = pd.read_csv(csv, sep=';', index_col='fecha', parse_dates=['fecha', 'unlock_date', 'lock_date'])

    return data_df

def delete_nan_rows(df: pd.DataFrame) -> None:
    """
    Función para eliminar todos los registros de un pandas.DataFrame que tengan todos sus valores NaN
    :param df: objeto pandas.DataFrame de entrada
    :return: no hay salida, el objeto pandas.DataFrame de entrada es directamente modificado eliminando registros NaN
    """
    df.dropna(axis=0, how='all', inplace=True)

def float_to_str(df: pd.DataFrame, col:str) -> None:
    """
    Función para que castea la columna suministrada a tipo string
    :param df: objeto pandas.DataFrame contenedor de la columna a modificar
    :param col: columna que se desea castear
    :return: no hay salida, el parámetro df suministrado a la entrada es modificado adhoc
    """
    df[col] = df[col].map(lambda x: str(x))

def day_time(df: pd.DataFrame) -> pd.Series:
    """
    Función para calcular el uso en horas de bicicletas por día del mes
    :param df: objeto pandas.DataFrame con los datos de uso de la EMT por mes
    :return: objeto pandas.Series con el día y número de horas de uso de las bicicletas
    """
    data_dates = df.index.unique()
    trips_per_day = pd.Series()
    for date in data_dates:
        trips_day = pd.Series(df[df.index == date]['trip_minutes'].sum()/60, index=[date])
        trips_per_day= pd.concat([trips_per_day, trips_day])

    return trips_per_day

def weekday_time(df: pd.DataFrame) -> pd.Series:
    """
    Función para calcular el uso en horas de bicicletas según la EMT por día de la semana por mes
    :param df: objeto pandas.DataFrame con los datos de uso de la EMT por mes
    :return: objeto pandas.Series con el día y el número de uso en horas por día de la semana del mes
    """
    trips_per_day = day_time(df)
    trips_per_day_week = pd.Series(trips_per_day.values, index=trips_per_day.index.day_name())
    aggr_trips_per_day_week = trips_per_day_week.groupby(level=0).sum()

    return aggr_trips_per_day_week

def total_usage_day(df: pd.DataFrame) -> pd.Series:
    """
    Función para calcular el número de usos totales de bicicletas según la EMT por día del mes
    :param df: objeto pandas.DataFrame con los datos de uso de la EMT por mes
    :return: objeto pandas.Series con el día y el uso de las bicicletas por día de la semana del mes
    """
    return df.groupby(pd.Grouper(freq='1D'))['fleet'].count()

def most_popular_stations(df: pd.DataFrame) -> set:
    """
    Función para averiguar las estaciones de desbloqueo que han tenido mayor número de viajes a lo largo del mes
    :param df: objeto pandas.DataFrame con los datos de uso de la EMT por mes
    :return: conjunto de las estaciones más populares a lo largo del mes
    """
    df_grouped_by_station_unlock = df.groupby(['station_unlock', 'address_unlock'])
    count_trips_by_unlock_station = df_grouped_by_station_unlock['fleet'].count()
    sorted_count = count_trips_by_unlock_station.sort_values(ascending=False)
    set_addresses = set(sorted_count.index.get_level_values(1))

    return set_addresses

def usage_from_most_popular_station(df: pd.DataFrame) -> int:
    """
    Función para calcular el número de viajes que ha tenido la estación de desbloqueos más poopular a lo largo de un mes
    :param df: objeto pandas.DataFrame con los datos de uso de la EMT por mes
    :return: entero con el número de viajes de la estación más popular
    """
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

    """
    C1
    """
    filtro_c1 = (usos['locktype'] == 'STATION') & (usos['unlocktype'] == 'FREE')
    usos_c1 = usos.where(filtro_c1)

    """
    C2
    """
    filtro_c2 = usos['fleet'] == 1.0
    regular_fleet = usos.where(filtro_c2)

    """
    C3
    """
    use_hours_date = day_time(usos)
    use_hours_date.plot.bar()
    plt.show()

    """
    C4
    """
    use_hours_weekday = weekday_time(usos)
    use_hours_weekday.plot.bar()
    plt.show()

    """
    C5
    """
    trips_date = total_usage_day(usos)
    trips_date.plot.bar()
    plt.show()

    """
    C6
    """
    use_by_day_unlock_station = usos.groupby([pd.Grouper(freq='1D'),'station_unlock'])['fleet'].count().rename('total_trips')

    """
    C7
    """
    #ATENCION FUNCIONA EL ORDENADO PERO DEVUELVE UN SET, UN SET SE ALMACENA ALEATORIAMENTE ASI QUE EL ORDEN NO SE MANTIENE
    sorted_desc_popular_unlock_stations = most_popular_stations(usos)

    """
    C8
    """
    most_popular_station_usage =  usage_from_most_popular_station(usos)