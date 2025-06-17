broj_jedan = float(input("Unesi prvi broj: "))
broj_dva = float(input("Unesi drugi broj: "))

operatori = ["+", "-", "*", "/"]

operator = input("Unesi operaciju koju ćeš koristiti: ")
if operator not in operatori:
    print("Nepodržani operator!")

if operator == "+":
    print(f"Rezultat operacije {broj_jedan} + {broj_dva} je {broj_jedan + broj_dva}")
elif operator == "-":
    print(f"Rezultat operacije {broj_jedan} - {broj_dva} je {broj_jedan - broj_dva}")
elif operator == "*":
    print(f"Rezultat operacije {broj_jedan} * {broj_dva} je {broj_jedan * broj_dva}")
elif operator == "/":
    if broj_dva == 0:
        print("Dijeljenje s nulom nije dozvoljeno!")
    else:
        print(f"Rezultat operacije {broj_jedan} / {broj_dva} je {broj_jedan / broj_dva}")