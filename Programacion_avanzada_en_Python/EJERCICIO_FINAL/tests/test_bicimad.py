from BiciMad.bicimad import BiciMad
import pytest


@pytest.mark.parametrize(
    "expected", [
        (['idBike', 'fleet', 'trip_minutes', 'geolocation_unlock', 'address_unlock', 'unlock_date', 'locktype',
          'unlocktype', 'geolocation_lock', 'address_lock', 'lock_date', 'station_unlock','unlock_station_name',
          'station_lock', 'lock_station_name'])
    ]
)
def test_bici_mad1(expected):
    """
    Test para comprobar que las columnas del DataFrame de datos del objeto BiciMad son las descritas en el enunciado
    :param expected: array con los nombres de las columnas dados en el enunciado
    :return:
    """
    bici_mad_object = BiciMad(2, 23)
    bici_mad_object.clean()
    data_df = bici_mad_object.data

    assert list(data_df.columns.values) == expected

@pytest.mark.parametrize(
    "expected", [
        ['fecha', 'unlock_date', 'lock_date']
    ]
)
def test_bici_mad2(expected):
    """
    Test para comprobar que todas las columnas del DataFrame de datos referidas a una fecha tienen el foramto correcto
    :param expected: columnas del DataFrame que contienen fechas
    :return:
    """
    bici_mad_object = BiciMad(2, 23)
    bici_mad_object.clean()
    data_df = bici_mad_object.data

    date_fields = data_df.select_dtypes(include=['datetime'])
    date_fields_list = []
    date_fields_list.append(date_fields.index.name)
    date_fields_list.extend(list(date_fields.columns))

    assert date_fields_list == expected

@pytest.mark.parametrize(
    "a, not_expected", [
        (BiciMad(2, 23), BiciMad(2, 23).data)
    ]
)
def test_bici_mad3(a, not_expected):
    """
    Test para comprobar el correcto funcionamiento de la función de limpieza de los datos de BiciMad
    :param not_expected: número de valores NaN antes de la limpieza, ha de ser menor que este
    :return:
    """
    a.clean()
    data_df = a.data

    assert data_df.isna().sum().sum() < not_expected.isna().sum().sum()


@pytest.mark.parametrize(
    "expected", [
        ([str, str, str, str])
    ]
)
def test_bici_mad4(expected):
    """
    Test para comprobar que la conversión del tipo de datos para las columnas 'fleet', 'idBike', 'station_lock'
    y 'station_unlock' es correcta.
    :param expected: lista con los tipos de datos que deberían tener los campos tras la conversión (str)
    :return:
    """
    bici_mad_object = BiciMad(2, 23)
    bici_mad_object.clean()
    data_df = bici_mad_object.data

    assert [type(data_df['fleet'][0]), type(data_df['idBike'][0]),
            type(data_df['station_lock'][0]), type(data_df['station_unlock'][0])] == expected

@pytest.mark.parametrize(
    "expected", [
        (['year', 'month', 'total_uses', 'total_time', 'most_popular_station', 'uses_from_most_popular'])
    ]
)
def test_bici_mad5(expected):
    """
    Test para comprobar que el nombre de las columnas devueltas en la función resumen de BiciMad se ajustan a las
    restricciones del enunciado.
    :param expected: lista con el título correcto que deberían tener los índices del objeto pd.Series devuelto
    :return:
    """
    bici_mad_object = BiciMad(2, 23)
    bici_mad_object.clean()
    resumen = bici_mad_object.resume()

    assert list(resumen.index.values) == expected

