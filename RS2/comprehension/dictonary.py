from math import sqrt
korijeni = {value :  round(sqrt(value),2) for value in range(50,501,50)}
print(korijeni) # {50: 7.07, 100: 10.0, 150: 12.25, 200: 14.14, 250: 15.81, 300: 17.32,
# 350: 18.71, 400: 20.0, 450: 21.21, 500: 22.36}