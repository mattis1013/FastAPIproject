#activer l'env virtuelle : .\blog-env\Scripts\Activate.ps1
#lancer le main sur le terminal et definir son port, uvicorn blog.main:app --reload --port 8000

from fastapi import FastAPI
from .database import engine, get_db
from . import models
from .routers import blog, user, authenti
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authenti.router)
app.include_router(blog.router)
app.include_router(user.router)


