broj = int(input("Unesi faktorijelu: "))
faktorijel = 1
for i in range (1,broj):
    broj *= faktorijel
    faktorijel +=1
    print(broj)