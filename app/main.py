from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def letsgoo():
    return {'message':'FAstapi for ml'}