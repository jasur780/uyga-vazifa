import os
os.system("cls")

dct = {'a' : 1, 'b' : 2, 'c' : 3}

func = {i: k for k, i in dct.items()}

print(func)