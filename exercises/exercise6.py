"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
    """


# NO MODIFICAR - INICIO
def numeros_al_final_basico(lista: List[Union[float, str]]):
    numeros = []
    for i in lista:
        if type(i) != str:
            numeros.append(i)
            lista.remove(i)
    lista.extend(numeros)
    return lista

assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    """Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
    """


# NO MODIFICAR - INICIO
def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    listaletras = [i for i in lista if type(i) == str]
    listanumeros = [i for i in lista if type(i) == int]
    listaletras.extend(listanumeros)
    return listaletras

assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
