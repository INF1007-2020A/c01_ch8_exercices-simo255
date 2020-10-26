#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def comparer(fichierr1 : str, fichierr2 : str):
    with open(fichier1, 'r') as f, open(fichier2,"r") as k:
        same = True
        while same:
            a= fichier1.read
            b=fichier2.read
            same =  a==b
    return -1 if same else f1.tell

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    comparer(fichier1, fichier2)

    pass
