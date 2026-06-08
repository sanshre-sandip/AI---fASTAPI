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


@app.get('/path/{id}')
def path_pram(id: str):
    with open('data.json','r') as f:
        data = json.load(f)

        if id in data:
            return data[id]
        return {'error':'data not found'}




   

      



