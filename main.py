from fastapi import FastAPI
myapp = FastAPI()

print("🔥 WELCOME MATTIS 🔥")

@myapp.get('/')
def index():
    return{'data': ' blog list'}

@myapp.get('/blog/unpublished')
def unpublished():
    return{'data': "all unpublished blogs"}

@myapp.get('/blog/{id}')
def show(id: int):
    return{'data': id}


@myapp.get('/blog/{id}/comments')
def comments(id):
    return {'data' : ['1','2']}