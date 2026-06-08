from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def letsgoo():
    return {'message':'FAstapi for ml'}


@app.get("/data")
def show():
    with open('data.json','r') as f:
        data = json.load(f)
    
    return data