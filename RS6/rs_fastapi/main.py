from fastapi import FastAPI
from models import Proizvod, CreateProizvod, Film,CreateMovie, FilmResponse,  BaseProizvod, RequestProizvod, ResponseProizvod
import random

proizvodi = [
 {"id": 1, "naziv": "majica", "boja": "plava", "cijena": 50},
 {"id": 2, "naziv": "hlače", "boja": "crna", "cijena": 100},
 {"id": 3, "naziv": "tenisice", "boja": "bijela", "cijena": 150},
 {"id": 4, "naziv": "kapa", "boja": "smeđa", "cijena": 20}
]

filmovi = [
 {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
 {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
 {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
 {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

app = FastAPI()

# Dohvaćanje svih proizvoda 
"""@app.get('/proizvodi')
def get_proizvodi():
    return proizvodi"""

# query parametar funcija - filtriranje , sortiranje po boji
@app.get("/proizvodi") # Naglašavamo da je povratna vriednost tipa Proizvod 
def get_proizvod_by_query(boja:str = None , max_cijena:int = 100):
    pronadeni_proizvod = [proizvod for proizvod in proizvodi if proizvod["boja"] == boja and proizvod["cijena"] == max_cijena]
    return pronadeni_proizvod



# Stvaranje novog proizvoda 
@app.get("proizvodi/{naziv}")
def get_product_by_name(naziv:str):
    pronadeni_proizvod = next((proizvod for proizvod in proizvodi if proizvod["naziv"] == naziv),None)
    return pronadeni_proizvod

""""
# Dodavanje novih proizvoda u postojeću listu 
@app.post('/proizvodi',response_model=Proizvod)
def add_proizvod(proizvod:CreateProizvod):
    new_id = len(proizvodi) + 1
    #proizvod_s_id = Proizvod(id = new_id, naziv=proizvod.naziv, boja=proizvod.boja, cijena=proizvod.cijena)
    proizvdo_s_id = Proizvod(id=new_id, **proizvod.model_dump())
    return proizvdo_s_id"""

# Testno kombiniranje svih 3 načina odreživanje rute
@app.post('/proizvodi/{id_proizvod}')
def update_skladiste(proizvod:dict,id_proizvod:int,kategorija:str = "građevisnki materijal"):
    pass

# Dohvaćanje svih filmova iz baze podataka, validacija outputa modelom
# Novo -> dodaj query parametre, omogućava filtriranje  
"""@app.get('/filmovi' )
def get_movies(genre:str = None, min_godina:int = 2000):
    validacija_filmova_all_data = [
        Film(id=film["id"], naziv=film["naziv"], genre=film["genre"], godina=film["godina"])
        for film in filmovi
        if (genre is None or film["genre"] == genre) and film["godina"] >= min_godina
    ]
    #validacija_filmova = [Film(**film) for film in filmovi]
    return validacija_filmova_all_data"""

# Pretraživanje filma po id-u i validacija
@app.get('/filmovi/{id}')
def get_movie_by_id(id:int):
    find_movie = next((Film(**film) for film in filmovi if film["id"] == id))
    return find_movie   

# Dodavanje novih filmova u listu filmovi, automatsko generiranje novog id-a,  validacija
@app.post('/filmovi', response_model=Film)
def add_movie(film:CreateMovie):
    new_id = len(filmovi) + 1
    adding_new_movie = Film(id = new_id, **film.model_dump())
    return adding_new_movie

# Novi naćin dohvaćanja svih filmova iz baze podataka
@app.get('/filmovi', response_model=list[FilmResponse])
def dohvati_filmove():
    return filmovi


@app.post("/proizvodi", response_model=ResponseProizvod) # validacija i serijalizacija HTTP odgovora prema ResponseProizvod modelu
def dodaj_proizvod(proizvod: RequestProizvod): # RequestProizvod model koristimo za validaciju podataka koje klijent šalje
    PDV_MULTIPLIER = 1.25
    some_id = random.randrange(1, 100) # simuliramo dodjelu ID-a
    cijena_pdv = proizvod.cijena * PDV_MULTIPLIER # računamo cijenu s PDV-om
    proizvod_spreman_za_pohranu : ResponseProizvod = {**proizvod.model_dump(), "id":some_id, "cijena_pdv":cijena_pdv} # ne instanciramo novi ResponseProizvod, već koristimo typehinting
    proizvodi.append(proizvod_spreman_za_pohranu)
    return proizvod_spreman_za_pohranu