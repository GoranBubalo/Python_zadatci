broj = int(input("Unesi faktorijelu: "))
faktorijela = 1
iteracija = 1

while iteracija <= broj:
    faktorijela*= iteracija
    iteracija+=1

print(f"Faktorijel broja {broj} je {faktorijela}")
