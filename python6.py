import os
os.system("cls")

def func(dct: dict):
    value = max(dct.values())

    print(f"{value} Eng katda values")

dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

func(dct)