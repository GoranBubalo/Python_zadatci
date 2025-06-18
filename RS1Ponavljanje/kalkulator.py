broj1 = input("Unesite prvi broj: ")
broj2 = input("Unesite drugi broj: ")

operator = input("Unesite operator (+, -, *, /): ")

if operator == "+":
    rezultat = float(broj1) + float(broj2)
    print("Zbroj je:", rezultat)
elif operator == "-":
    rezultat = float(broj1) - float(broj2)
    print("Zbroj je:", rezultat)
elif operator == "*":
    rezultat = float(broj1) * float(broj2)
    print("Zbroj je:", rezultat)
elif operator == "/":
    if float(broj2) != 0:
        rezultat = float(broj1) / float(broj2)
        print("Zbroj je:", rezultat)
else:
    rezultat = "Dijeljenje s nulom nije dozvoljeno."