from fastapi import FastAPI
from fastapi.responses import FileResponse
from openai import OpenAI
import os
from schema import TTSRequest


app = FastAPI()

API_KEY = os.getenv("API_KEY")

@app.post("/to-speech")
def openai_tts(request : TTSRequest):
    client = OpenAI(api_key=API_KEY)

    response = client.audio.speech.create(

        model= "tts-1",
        voice= request.voice,
        input= request.input,

    )

    audio_path = "output.mp3"
    response.stream_to_file(audio_path) 

    return FileResponse(
        path=audio_path,
        media_type="audio/mpeg",
        filename="output.mp3",
    )
