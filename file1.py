from fastapi import FastAPI
from enum import Enum
app = FastAPI()

# These request can be seen in localhost:8000/docs -- Flask Apis self build postman
# GET request
@app.get('/new_get')
async def home():
    return {"filename" : __name__}

@app.post('/')
async def home():
    return {"post" : __name__}

@app.put('/')
async def home():
    return {"put" : __name__}        

# Route
@app.get('/list-items')
def list_items(): 
    return {"message": "list items route"}
    
#### IF THERE ARE ANY STATIC LINKS WITH SAME ROUTE AND DYNAMIC LINKS AS WELL
#### THEN ADD STATIC FIRST AND THEN DYNAMIC    
# # By default items id is string    
# @app.get('/list-items')
# async def get_items(item_id):
#     return {"message": item_id}    

@app.get('/list-items/{item_id}')
async def get_items(item_id: int):
    return {"message": item_id}        

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegie"
    meat = "meat"    

@app.get('/food/{food_name}')
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.fruits:
        return {"food": food_name}
    elif food_name == FoodEnum.vegetables:
        return {"food" : food_name}
    return {"food": "Wrong"}            