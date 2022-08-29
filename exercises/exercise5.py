"""For, Sum, Reduce."""


def sumatoria_basico(n: int) -> int:
    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar un bucle FOR.
    """


# NO MODIFICAR - INICIO
def sumatoria_basico(n: int) -> int:
    num = 0
    for i in range(n):
        num = num + i
        return num

assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def sumatoria_sum(n: int) -> int:
    """Re-Escribir utilizando la función sum.

    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """


# NO MODIFICAR - INICIO
def sumatoria_sum(n: int) -> int:
    suma = sum(range(n), n)
    return suma

assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


from typing import Iterable  # noqa: E402


def multiplicar_basico(numeros: Iterable[float]) -> float:
    """Toma un lista de números y devuelve el producto todos los númereos. Si
    la lista está vacia debe devolver 0.

    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
    """


# NO MODIFICAR - INICIO
def multiplicar_basico(numeros: Iterable[float]) -> float:
    for i in range(len(numeros)):
        
        if i == 0:
            mult = numeros[i] * numeros[i+1]
        
        mult * i+1
        return mult    
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
# NO MODIFICAR - FIN
