from pydantic import BaseModel


class TTSRequest(BaseModel):
    
    input: str
    voice: str
