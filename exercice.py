#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(1, r"W:\Alexandre\Ecoles\Polytechnique_2020-2021\INF1007\c04-ch6-exercices")
from exo22 import frequence


# TODO: Définissez vos fonction ici
def exo1(a = 10,b = 4,c = 6,mass_volum = 67):
    V = 4/3*(math.pi*a*b*c)
    M = mass_volum * V

    return V, M



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(exo1())

    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence). __getitem__ )[-1]("ceci est un mot")))

    pass
