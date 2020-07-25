""" Modulo para la evaluacion de la beca WES-IT.
    Código escrito en python 3.8
"""


def es_multiplo():
    """ Muestra números del 1 al 100. Cuando el número es multiplo de 3, muestra "x3",
    si es multiplo de 5 muestra "x5" y si es multiplo de ambos muestra "x3 y x5.
    """
    for num in range(1, 101, 1):
        if num %3 == 0 and num %5 == 0:
            print("x3 y x5")
        elif num %5 == 0:
            print("x5")
        elif num %3 == 0:
            print("x3")
        else:
            print(num)


if __name__ == '__main__':
    es_multiplo()
