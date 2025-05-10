from fastapi import FastAPI,Depends,Path
from sqlalchemy.orm import Session
import models 
from models import Posts, CategoryEnum
from database import engine,SessionLocal 
from typing import Annotated
from fastapi.exceptions import HTTPException
from starlette import status
from pydantic import BaseModel,Field
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:  # Use finally to ensure DB is closed properly without hiding errors
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

class PostRequest(BaseModel):
    title : str = Field(min_length=4,max_length=200,default="placeholder title")
    category : CategoryEnum 
    content : str = Field(min_length=6)
    is_published : bool = False

@app.get("/",status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return db.query(Posts).all()

@app.get("/hello")
async def sayHello():
    return {
        'hello' : 'hello'
    }
@app.get("/world")
async def sayWorld():
    return {
        'world' : 'world'
    }
@app.get("/new")
async def sayWorld():
    return {
        'new' : 'new'
    }
@app.get("/posts/{post_id}",status_code=status.HTTP_200_OK)  # Changed to GET
async def read_post(db: db_dependency,post_id: int = Path(gt = 0)):
    post_record = db.query(Posts).filter(Posts.id == post_id).first()
    if post_record is not None:
        return post_record 

    raise HTTPException(status_code=404, detail="Post not found.")

@app.post("/posts",status_code=status.HTTP_201_CREATED)
async def create_post(db:db_dependency,post_request:PostRequest):
    post_model = Posts(**post_request.dict())

    db.add(post_model)
    db.commit()

    return {
        'title' : post_request.title
    }