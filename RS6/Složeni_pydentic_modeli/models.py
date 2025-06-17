from pydantic import BaseModel
from typing import Optional, Literal, List, TypedDict
from datetime import datetime

class Izdavac(BaseModel):
    naziv:str
    adresa:str

class Knjiga(BaseModel):
    naslov:str
    ime_autora:str
    prezime_autora:str
    godine_izdavanja:Optional[int] = datetime.now().year
    broj_stranica:int
    izdavac:Izdavac

class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: List[Literal["dodavanje", "brisanje", "azuriranje", "citanje"]] = []

class StolInfo(TypedDict):
    broj: int
    lokacija: str

class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float

class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    jela: List[Jelo]
    ukupna_cijena: float

class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: List[float, float] = (0.0, 0.0)