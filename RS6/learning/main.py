from fastapi import FastAPI, HTTPException
from models import Knjiga, KnjigaRequest, KnjigaResponse

app = FastAPI()

knjige = [
 {"id": 1, "naslov": "Ana Karenjina", "autor": "Lav Nikolajevič Tolstoj"},
 {"id": 2, "naslov": "Kiklop", "autor": "Ranko Marinković"},
 {"id": 3, "naslov": "Proces", "autor": "Franz Kafka"}
]

@app.get("/knjige/{naslov}", response_model=Knjiga)
def dohvati_knjigu(naslov: str):
    for knjiga in knjige:
        if knjiga["naslov"] == naslov:
            return knjiga # vraćamo knjigu ako je pronađena
    raise HTTPException(status_code=404, detail="Knjiga nije pronađena") # podižemo iznimku ako knjiga nije pronađena s odgovarajućom porukom i statusnim kodom


@app.post('/knjige', response_model=KnjigaResponse)
def dodaj_knjigu():
    passs