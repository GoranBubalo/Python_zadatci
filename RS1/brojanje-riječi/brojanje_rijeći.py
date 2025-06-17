def brojanje_riječi(tekst):
    word = tekst.split()
    count = {}

    for i in word:
        count[i] = count.get(i, 0) + 1
    return count


# Meka a  foor loop AI!


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(brojanje_riječi(tekst))