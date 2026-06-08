<<<<<<< HEAD
from fastapi import FastAPI, HTTPException, Path, Query
=======
from fastapi import FastAPI
>>>>>>> 49dac57
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

<<<<<<< HEAD
#path parameter
@app.get('/path/{id}')
def path_pram(id: str = Path(..., description='id no for client accoding to stored in dataset', examples='1')):
=======

@app.get('/path/{id}')
def path_pram(id: str):
>>>>>>> 49dac57
    with open('data.json','r') as f:
        data = json.load(f)

        if id in data:
            return data[id]
<<<<<<< HEAD
        
        raise HTTPException(status_code=404, detail='not found')



#Query parameter
from fastapi import FastAPI, Query, HTTPException

@app.get('/sort')
def sort(
    sort_by: str = Query(..., description='Sort by height, weight, or bmi'),
    order: str = Query(..., description='asc or des')
):

    valid = ['height', 'weight', 'bmi']

    if sort_by not in valid:
        raise HTTPException(
            status_code=400,
            detail=f'Invalid field. Choose from {valid}'
        )

    if order not in ['asc', 'des']:
        raise HTTPException(
            status_code=400,
            detail='Order must be asc or des'
        )

    data = show()

    reverse = True if order == 'des' else False

    sorted_data = sorted(
        data,
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse
    )

    return sorted_data
=======
        return {'error':'data not found'}




   

      



>>>>>>> 49dac57
