podatak = str(input("Upišite lozinku: "))

def provjera_lozinke(podatak):
    if not 8 < len(podatak) < 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
    elif not any(char.isupper() for char in podatak) or not any(number.isdigit() for number in podatak):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    elif podatak == "password" or podatak == "lozinka":
        print("Lozinka ne smije sadržavati rijči 'password' ili 'lozinka'")
    else:
        print("Lozinka je jaka!")


provjera_lozinke(podatak)
