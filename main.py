from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

myapp = FastAPI()

print("🔥 WELCOME MATTIS 🔥")
#TUER UN PROCESSUS netstat -ano | findstr :8000 THEN taskkill /PID 12345 /F


@myapp.get('/blog')
def index(limit=10,published: bool= True, sort: Optional[str]= None ):
    #liste 10 published blogs plutôt que tous les blogs de la BDD

    if published:
        return{'data': f'{limit} published blogs from the database'}
    else:
        return{'data': f'{limit} blogs from the database'}

@myapp.get('/blog/unpublished')
def unpublished():
    return{'data': "all unpublished blogs"}

@myapp.get('/blog/{id}')
def show(id: int):
    return{'data': id}


@myapp.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data' : ['1','2']}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@myapp.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}


if __name__=='__main__':
    uvicorn.run(myapp,host='127.0.0.1',port=9000)