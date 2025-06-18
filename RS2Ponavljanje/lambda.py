kvadriraj = lambda x : x **2
print(kvadriraj(5))  # Output: 25

zbroji = lambda x, y : (x + y) ** 2
print(zbroji(3, 4))  # Output: 49


niz = [1, 2, 3, 4, 5]
kvadriraj_niz = list(map(lambda x: x ** 2, niz))
print(kvadriraj_niz)  # Output: [1, 4,