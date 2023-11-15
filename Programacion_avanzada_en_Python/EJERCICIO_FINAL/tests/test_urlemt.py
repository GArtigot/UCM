from ..BiciMad.urlemt import UrlEmt
import pytest
import re
from datetime import datetime

@pytest.mark.parametrize(
    "a, expected", [
        (UrlEmt(), ['https://opendata.emtmadrid.es/', '/Datos-estaticos/Datos-generales-(1)'])
    ]
)
def test_emt(a,expected):
    """
    Test de la correcta inicialización de las constantes de la clase UrlEmt al construir un objeto de la misma
    :param a: objeto de la clase UrlEmt
    :param expected: array con las dos constantes que deberían crearse junto con la instancia de clase
    :return:
    """
    assert [a.EMT, a.GENERAL] == expected

@pytest.mark.parametrize(
    "a, expected", [
        (UrlEmt(), datetime(2021, 6, 1, 0, 0))
    ]
)
def test_emt2(a, expected):
    """
    Test para comprobar que al decargar los datos de la clase UrlEmt, el mes desde el cuál tenemos datos es Junio de 2021
    :param a: objeto de la clase urlemt
    :param expected: fecha 01/06/2021
    :return:
    """
    urls = list(UrlEmt.select_valid_urls())
    ex = r'_\d{2}_\d{2}_'
    pattern = re.compile(ex)
    dates = []
    for url in urls:
        year_month = re.search(pattern, url)[0]
        year_month_list = year_month.split('_')
        date_format = "-".join(year_month_list)
        date = datetime.strptime(date_format, '%y-%m')
        dates.append(date)

    earliest_date = min(dates)

    assert earliest_date == expected

@pytest.mark.parametrize(
    "a, b, expected", [
        (12, 21, '/getattachment/0417f179-9741-44ba-8f8c-0bc9fc2b06fe/trips_21_12_December-csv.aspx')
    ]
)
def test_emt3(a, b, expected):
    """
    Test para comprobar el correcto funcionamiento del método get_url de la clase UrlEmt
    :param a: mes de la fecha de los datos que queremos descargar
    :param b: año de la fecha de los datos que queremos descargar
    :param expected: url que nos permite descargar estos datos desde la web de la EMT
    :return:
    """
    url_emt_object = UrlEmt()
    assert url_emt_object.get_url(a, b) == expected

@pytest.mark.parametrize(
    "a, b, c , d", [
        (3, 1996, 3, 23)
    ]
)
def test_emt4(a, b, c, d):
    """
    Test para comprobar el control de excepciones del metodo get_url de la clase UrlEmt
    :param a: mes de la fecha de los datos que queremos descargar previa al dataset
    :param b: año de la fecha de los datos que queremos descargar previa al dataset
    :param c: mes de la fecha de los datos que queremos descargar que no se encuentra en el dataset
    :param d: año de la fecha de los datos que queremos descargar que no se encuentra en el dataset
    :return:
    """
    url_emt_object = UrlEmt()
    with pytest.raises(ValueError):
        url_emt_object.get_url(a, b)
        url_emt_object.get_url(c,d)