import doctest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def summary(input_array: np.ndarray) -> tuple[float, float, float, float]:
    """
    function that returns the minimum, maximum, mean and standard deviation of an array
    :param a: ndarray
    :return: tuple of float
       a tuple of four float values: min, max, mean, std
    Examples
    --------
    >>> summary(np.array([[1,2,3], [4,5,6]]))   # array sin nan
    (1, 6, 3.5, 1.707825127659933)
    >>> summary(np.array([[1,np.nan,3], [4,5,6]]))   # array con un nan
    (nan, nan, nan, nan)
    >>> summary(np.array([]))   # array vacío
    Traceback (most recent call last):
    ...
    ValueError: zero-size array to reduction operation minimum which has no identity
    """

    input_df = pd.DataFrame(input_array)

    return (input_df.values.min(), input_df.values.max(), input_df.values.mean(), input_df.values.std())

def check_nulls(array_input: np.ndarray) -> bool:
    """
    function that checks the validity od sensor data
    :param a: np.ndarray
    :return: bool
       indicates if data contains nan
    Examples
    --------
    >>> check_nulls(np.array([[1,2,3], [4,5,6]]))   # array sin nan
    True
    >>> check_nulls(np.array([[1,np.nan,3], [4,5,6]]))   # array con un nan
    False
    >>> check_nulls(np.array([]))   # array vacío
    True
    """

    input_df = pd.DataFrame(array_input)
    nan_in_column = input_df.isna().any()
    nan_in_df = nan_in_column.any()

    return not bool(nan_in_df)

def ith(temperature: np.ndarray, humidity: np.ndarray) -> np.ndarray:
    """
    Calculates the temperature-humidity index (THI) of each of the grid cells.
    The ith-value of each cell must be rounded to the nearest integer
    :param temperature:  np.ndarray
        temperatures collected by the sensor in a grid
    :param humidity:  np.ndarray
        humidity data collected by the sensor on a grid
    :return:  np.ndarray
        temperature-humidity index (THI) (round to the nearest integer)
    :raise ValueError: if shape of input arrays is not the same
    >>> ith(np.array([[1,2,3], [4,5,6]]), np.array([[1,2,3], [4,5,6]]))
    array([[47., 48., 48.],
           [49., 50., 51.]])
    >>> ith(np.array([[1,np.nan,3], [4,5,6]]), np.array([[1,2,3], [4,5,6]]))
    array([[47., nan, 48.],
           [49., 50., 51.]])
    >>> ith(np.array([[1], [4]]), np.array([[1], [4]]))
    array([[47.],
           [49.]])
    >>> ith(np.array([[2,3], [4,5]]), np.array([[1,2,3], [4,5,6]]))  # dimensiones distintas
    Traceback (most recent call last):
        ...
    ValueError: Shape of data sensors must be the same. Temperature: (2, 2) != humidity: (2, 3)
    """

    if temperature.shape != humidity.shape:
        raise ValueError('Shape of data sensors must be the same. Temperature: ' + str(temperature.shape)
                         + ' != ' + 'humidity: ' + str(humidity.shape))

    ith = 0.8 * temperature + (humidity/100) * (temperature - 14.3) + 46.4

    return np.around(ith, 0)

def isStress(ith: np.ndarray) -> np.ndarray:
    """
    Determines the grid points where serious stress occurs.
    :param ith: np.ndarray
       temperature-humidity index (THI)
    :return: np.ndarray
       True values indicate serious stress
    >>> isStress(np.array([[47.], [49.]]))
    array([[False],
           [False]])
    >>> isStress(np.array([[47., 79., 48.], [49.,50. ,81.]]))
    array([[False,  True, False],
           [False, False,  True]])
    >>> isStress(np.array([[80, np.nan, 48.], [49., 50., 88.]]))
    array([[ True, False, False],
           [False, False,  True]])
    """

    return np.where(ith > 78, True, False)

def test_doc() -> None:
    """
    The following instructions are to execute the tests of same functions
    If any test is fail, we will receive the notice when executing
    :return: None
    """
    doctest.run_docstring_examples(check_nulls, globals(), verbose=True)  # vemos los resultados de los test
    doctest.run_docstring_examples(ith, globals(), verbose=True)  # vemos los resultados de los test
    doctest.run_docstring_examples(isStress, globals(), verbose=False)  # solo los resultados de los test que fallan
    doctest.run_docstring_examples(summary, globals(), verbose=False)  # solo los resultados de los test que fallan


if __name__ == "__main__":
    test_doc()  # executing tests

    temperatures = np.loadtxt(r'C:\Users\germa\Desktop\Documentos Importantes\Máster UCM\UCM\Programacion_avanzada_en_Python\ej_3\datos\temperaturas.txt')
    humidity = np.loadtxt(r'C:\Users\germa\Desktop\Documentos Importantes\Máster UCM\UCM\Programacion_avanzada_en_Python\ej_3\datos\humedad.txt')

    ITH = ith(temperatures, humidity)

    plt.imshow(ITH, cmap='autumn', interpolation='nearest')

    #for i in range(temperatures.shape[0]):
    #    for j in range(temperatures.shape[1]):
    #        plt.annotate(str(ITH[i][j]), xy=(j + 0.5, i + 0.5),
    #                     ha='center', va='center', color='black')

    plt.show()

