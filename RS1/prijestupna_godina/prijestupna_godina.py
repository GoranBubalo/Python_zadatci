godina = int(input("Unesite godinu po izboru: "))

if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
    print(f"Godina {godina}. je prijestupna.")
else:
    print(f"Godina {godina}. nije prijestupna.")