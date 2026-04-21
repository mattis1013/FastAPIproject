from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(tags=['Blogs'])

@router.get('/blog',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def annihilate(id,db: Session = Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id :{id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done and deleted'


@router.put('/blog/{id}',status_code=200, response_model=schemas.ShowBlog)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id :{id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated'



@router.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id :{id}not found") #en une ligne
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"detail": f"Blog with id :{id}not found"}
    return blog


#.\blog-env\Scripts\Activate.ps1
#uvicorn main:app --reload
#uvicorn blog.main:app --reload --port 8000
#.\start_uvicorn.ps1