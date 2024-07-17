import os
os.system("cls")
string = []
def func(lst: list):
    for i in lst:
        if isinstance(i, str):
            string.append(i)

    return string        


lst = ['100.0', '2.2', 1, 2, 'er', 12]
natija = func(lst)
print(natija)