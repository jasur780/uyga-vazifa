import os
os.system("cls")
def func(lst: list) -> int:
    return sorted(lst)[-2]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
natija = func(lst)

print(natija)