from pydantic import BaseModel

class Knjiga(BaseModel):
    id:int
    naslov:set
    autor:str
    
class KnjigaRequest(BaseModel):
    naslov:str
    autor:str

class KnjigaResponse(KnjigaRequest):
    id:int