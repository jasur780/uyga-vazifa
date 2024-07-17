import os
os.system("cls")

def func(dct: dict):
    key = max(dct.keys())

    print(f"{key} Eng katda key")

dct = {'d': 4,'a': 10, 'b': 2, 'c': 3}

func(dct)