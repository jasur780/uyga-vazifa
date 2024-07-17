import os
os.system("cls")

def add(lst: list) -> list:
    l = []
    for i in lst:
        if isinstance(i, int):
            if i > 0:
                l.append(i + 5)
            else:
                l.append(i - 5)
        else:
            l.append(i)
    return l

# Example usage
lst = [10, -3, 'hello', 4.5, 0, -1, 8]
result = add(lst)
print(result)  
