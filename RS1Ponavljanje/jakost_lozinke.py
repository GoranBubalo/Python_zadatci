
lozinka = input("Unesite lozinku: ")

def provjera_lozinke(lozinka):
    if len(lozinka) < 8  or len(lozinka) > 15:
        print("Lozinka mora biti između 8 i 15 znakova.")
    elif lozinka.lower() == "lozinka" or  lozinka.lower() == "password":
        print("Lozinka ne smije biti 'lozinka' ili 'password'.")
    elif not any(char.isdigit() for char in lozinka) :
        print("Lozinka mora sadržavati barem jedan broj.")
    elif not any(char.isupper() for char in lozinka):
        print("Lozinka mora sadržavati barem jedno veliko slovo.")
    elif lozinka == "lozinka" or  lozinka == "password":
        print("Lozinka ne smije biti 'lozinka' ili 'password'.")
    else:
        print("Lozinka je jaka.")

provjera_lozinke(lozinka)