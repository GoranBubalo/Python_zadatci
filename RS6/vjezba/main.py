from fastapi import FastAPI
from models import KorisnikBase, KorisnikCreate, KorisnikResponse
from datetime import datetime

app = FastAPI()


@add.post("/korsnici", response_model = KorisnikResponse)
def registracija_korinika(korisnik: KorisnikCreate):
    datum_registracije = datetime.now()
    korisnik_spreman_za_pohranu : KorisnikResponse = {**korisnik.model_dump(), "lozinka_hash" : lozinka_hash,"datum_registracije": datum_registracije}
    print(f"Korisnik spreman za pohranu: {korisnik_spreman_za_pohranu}")