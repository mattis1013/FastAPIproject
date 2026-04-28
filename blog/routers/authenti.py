from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, schemas, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(tags=['Authentification'])


@router.post('/login')
def login(request: schemas.Login, db : Session= Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = 'Invalid Credentials')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid password')
    # generate a JWT TOKEN and return it
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token" : access_token, "token_type": "bearer"}
