import os
os.system("cls")

def func(dct):
     keys = set(dct.keys())
     values = set(dct.values())
     result = keys.union(values)
     return result


dct = {'a': 1, 'g': 3, 't': 2, 'd': 5}
natija = func(dct)
print(natija)