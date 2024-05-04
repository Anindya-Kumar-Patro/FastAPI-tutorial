from fastapi import FastAPI
from typing import Optional 

## import this for sending Request Body 
from pydantic import BaseModel
app = FastAPI()

## NORMAL get routes to static endpoint
@app.get('/')
def index():
    return 'Index page'
    
@app.get('/about')
def about():
    return {'data': {'details': 'This is about page'}}

## Dynamic endpoints with id as int
# we can pass id: int which will define id as only int type OR
# we can pass id directly without specifying datatype
@app.get('/blog/{id}')
def show(id: int):
    return {'data': {'blog_id': id}}

## This wont get loaded as fastAPI reads line by line so it will give
## error stating interger is expected
# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data': {'blog_id': 'unpublished data'}}

@app.get('/blog/{id}/comments')
def show(id: int):
    return {'data': {'comments': 'This is a comment'}} 
    
## Query code
## http://localhost:8000/blog?limit=10&published=true
## Optional is to specify is it is optional or not and [str] is type(sort)
@app.get('/blog')
def query(limit=10, published:bool=True, sort: Optional[str] = None):
    if published:
        return {'data': {f'{limit} blogs from db and published blogs'}}   
    return {'data': {f'{limit} blogs from db'}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data':f'This is blog created with title: {blog.title}'}
 