from fastapi import FastAPI
from uvicorn import run
from fastapi.responses import JSONResponse
import RPi.GPIO as GPIO
from schemas import auth

app = FastAPI()

@app.post('/on')
async def main_func(auth : auth) -> JSONResponse:
    if auth.api_key == 'auth':
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        GPIO.output(7, True)
        return JSONResponse({'Light Turned on':'Sucess'})

@app.post('/off')
async def main_func(auth : auth) -> JSONResponse:
    if auth.api_key == 'auth':
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)
        GPIO.output(7, False)
        return JSONResponse({'Light Turned off':'Sucess'})

if __name__ == '__main__':
    run('server:app')
