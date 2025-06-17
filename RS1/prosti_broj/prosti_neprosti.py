def isPrime(number):
    if number % 2 == 0:
        return False
    else:
        return True

def prime_is_range(start, end):
    lista = []
    for i in range(start,end):
        lista.append(i)
    return lista
    
print(isPrime(7))
print(isPrime(10))

print(prime_is_range(5,55))