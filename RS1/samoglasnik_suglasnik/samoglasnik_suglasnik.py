def count_vowels_consonants(tekst):
    vowel = 0
    consonant = 0
    for char in tekst:
        if char in vowels:
            vowel += 1
        elif char in consonants:
            consonant += 1
    return {"vowels" : vowel, "cosonants" : consonant}

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))