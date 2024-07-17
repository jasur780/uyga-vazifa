import os
os.system("cls")

def func(dct: dict):
    if not dct:
        return None
    maxkey = max(dct, key=dct.get)
    return maxkey


dct = {'a': 10, 'b': 20, 'c': 30, 'd': 300}
natija = func(dct)
print(natija)