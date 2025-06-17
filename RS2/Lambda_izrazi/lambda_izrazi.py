def kvadriraj(x):
    return x ** 2

# lambda

kvadriraj = lambda x: x ** 2
print(kvadriraj(5))

# ili 

# lambda 

print((lambda x : x **2)(3))

def zbroji_pa_kvadriraj(a, b):
    return (a + b) ** 2

zbroji_pa_kvadriraj_lambda = lambda x,y : (x+y) ** 2
print(zbroji_pa_kvadriraj_lambda(2,2))

def kvadriraj_duljinu(niz):
    return len(niz) ** 2    

kvadriraj_duljinu_lambda = lambda niz: len(niz) ** 2

niz = "python je zakon"
print(kvadriraj_duljinu_lambda(niz))

def pomnozi_i_potenciraj(x, y):
    return (y * 5) ** x

pom_potenciraj = lambda x, y : (y * 5) ** x
print(pom_potenciraj(2,2))

def paran_broj(x):
    if x % 2 == 0:
        return True
    else:
        return None

paran_br = lambda x : True if x % 2 == 0 else None
print(paran_br(5))
