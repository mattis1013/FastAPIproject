#activer l'env virtuelle : .\blog-env\Scripts\Activate.ps1
#lancer le main sur le terminal , uvicorn blog.main:app --reload --port 8000



from fastapi import FastAPI,
from .database import engine, get_db
from . import models
from .routers import blog, user
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)



@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blog'])
def annihilate(id,db: Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id :{id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done and deleted'


@app.put('/blog/{id}',status_code=200, response_model=schemas.ShowBlog,tags=['blog'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id :{id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated'



@app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['blog'])
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id :{id}not found") #en une ligne
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"detail": f"Blog with id :{id}not found"}
    return blog


@app.post('/user', response_model=schemas.ShowUser,tags=['users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id :{id} is not available")
    return user
