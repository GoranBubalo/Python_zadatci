godina = input("Unesite godinu: ")

if godina.isdigit():
    godina = int(godina)
    if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
        print(f"{godina} je prijestupna godina.")
    else:
        print(f"{godina} nije prijestupna godina.")