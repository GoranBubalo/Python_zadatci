from pydantic import BaseModel

class CreateProizvod (BaseModel):
    naziv: str
    boja: str
    cijena: float

class Film(BaseModel):
    id:int
    naziv:str
    genre:str
    godina:int

class FilmResponse(BaseModel):
    id: int
    naziv:str
    genre: str
    godina:int
    
class CreateMovie(BaseModel):
    naziv:str
    genre:str
    godina:int
    
class Korisnik(BaseModel):
    id: int
    ime: str
    prezime: str
    email: str
    dob: int
    racun_aktivan: bool = True
    
class Proizvod(BaseModel):
    id: int
    naziv: str
    cijena: float
    kategorija: str
    boja: str
    
class StavkaNarudzbe(BaseModel):
    id: int
    proizvod: Proizvod
    narucena_kolicina: int
    ukupna_cijena: float

class Narudzba(BaseModel):
    id: int
    ime_kupca: str
    prezime_kupca: str
    stavke: list[StavkaNarudzbe]
    ukupna_cijena: float

class Loto(BaseModel):
    id: int
    rezultati: dict[int, int]
    
class BaseProizvod(BaseModel):
    naziv: str
    cijena: float
    kategorija: str
    boja: str
class RequestProizvod(BaseProizvod): # nasljeđujemo atribute iz BaseProizvod modela
    pass # ne dodajemo niti jedan novi atribut
class ResponseProizvod(BaseProizvod): # nasljeđujemo atribute iz BaseProizvod modela
    id: int
    cijena_pdv: float