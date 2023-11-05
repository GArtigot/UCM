import numpy as np


def read_data(fname: str, tipo: type) -> np.ndarray:
    # Escribe aquí tu código
    # No olvides documentar la función

def set_of_areas(zonas: np.ndarray)-> set[int]:
    """

    Examples:
    --------
    >>> set_of_areas(np.arange(10).reshape(5, 2))
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    >>> set_of_areas(np.zeros(10, dtype=np.int_).reshape(5, 2))
    {0}
    >>> set_of_areas(np.array([2, 3, 4, 2, 3, 4], dtype=np.int_).reshape(3, 2))
    {2, 3, 4}
    >>> set_of_areas(np.zeros(3, dtype=np.float_))
    Traceback (most recent call last):
        ...
    TypeError: The elements type must be int, not float64
    """
    # Escribe aquí tu código
    # No olvides documentar la función



# def mean_areas ...

    # Escribe aquí el código de la función mean_areas
    # No olvides documentar la función y escribir las anotaciones de tipos
    # Añade más ejemplos para doctest



# ------------ test  --------#
import doctest

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
    test_doc()   # executing tests
