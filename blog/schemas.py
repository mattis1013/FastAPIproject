from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title: str
    body: str
    class Config:
        from_attributes = True



class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]
    class Config:
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    owner: ShowUser
    class Config:
        from_attributes = True
