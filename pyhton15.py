import os
os.system("cls")
juft = []
def func(lst: list):
    for i in lst:
        if i % 2 == 0:
            juft.append(i)

    return juft

lst = [1, -1000, 2, 19, 3, -5, 6, 7, -3, -8, 9, -10]

natija = func(lst)
print(natija)
