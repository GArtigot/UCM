import numpy as np
import doctest

def read_data(fname: str, tipo: type) -> np.ndarray:
    """
    Función para la lectura de datos desde un fichero especificado y su almacenamiento en un nparray.

    :param fname: Nombre del fichero que contiene los datos
    :param tipo: Tipo de dato que conformará el nparray resultante
    :return: nparray con los datos contenidos en el fichero.
    """

    return np.loadtxt(fname, tipo)

def set_of_areas(zonas: np.ndarray)-> set[int]:
    """
    Función que devuelve las distintas zonas en un array de entrada
#    Examples:
#    --------
#    >>> set_of_areas(np.arange(10).reshape(5, 2))
#    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#    >>> set_of_areas(np.zeros(10, dtype=np.int_).reshape(5, 2))
#    {0}
#    >>> set_of_areas(np.array([2, 3, 4, 2, 3, 4], dtype=np.int_).reshape(3, 2))
#    {2, 3, 4}
#    >>> set_of_areas(np.zeros(3, dtype=np.float_))
#    Traceback (most recent call last):
#        ...
#    TypeError: The elements type must be int, not float64
    """

    if zonas.flatten().dtype != 'int32':
        raise TypeError('The elements type must be int, not ' + zonas.flatten().dtype)
    else:
        zonas_distc = np.unique(zonas.flatten())
        return zonas_distc

def mean_areas(zonas: np.ndarray, valores: np.ndarray) -> np.ndarray:
    """
    Función para calcular la media de valores en cada zona geográfica.
    :param zonas: ndarray con las distintas zonas geográficas
    :param valores: ndarray con los valores
    :return av_zonas: ndarray con la media de valores por zona
    """

    zonas_unicas = set_of_areas(zonas)
    av_zonas = zonas

    for zona in zonas_unicas:
        mask = valores == zona
        valores_area = valores[mask]
        media_area = np.average(valores_area)

    return av_zonas

    # Escribe aquí el código de la función mean_areas
    # No olvides documentar la función y escribir las anotaciones de tipos
    # Añade más ejemplos para doctest

def test_doc()-> None:
    """
    The following instructions are to execute the tests of same functions
    If any test is fail, we will receive the notice when executing
    :return: None
    """
    doctest.run_docstring_examples(read_data, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(set_of_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(mean_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan


if __name__ == "__main__":
    #test_doc()   # executing tests
    zonas = read_data(r'C:\Users\germa\Desktop\Documentos Importantes\Máster UCM\UCM\Programacion_avanzada_en_Python\ej_2\datos\zonas.txt', int)
    valores = read_data(r'C:\Users\germa\Desktop\Documentos Importantes\Máster UCM\UCM\Programacion_avanzada_en_Python\ej_2\datos\valores.txt', int)

    prueba = mean_areas(zonas, valores)
