from fastapi import FastAPI, Depends, HTTPException
from datetime import date 
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, SessionLocal
from typing import List
from sqlalchemy.exc import SQLAlchemyError

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#post initial message
@app.get("/")
def read_root():
    return {"message": "Welcome to the Ultralearning App backend!"}


#creates project
@app.post("/projects", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    try: 
        return crud.create_project(db, project)
    except SQLAlchemyError as e:
        db.rollback()
        print("SQLAlchemyError:", e)
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        print("General Exception:", e)
        raise HTTPException(status_code=500, detail=str(e))

#fectching one project
@app.get("/projects/{project_id}", response_model=schemas.ProjectResponse)
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id)
    if not project: 
        raise HTTPException(status_code=404, detail="Project not found")
    return project
#fetching all projects from user
@app.get("/projects", response_model=List[schemas.ProjectResponse])
def read_projects(user_id: int, db: Session = Depends(get_db)):
    projects = crud.get_all_projects(db, user_id)
    if not projects:
        raise HTTPException(status_code=404, detail="Projects not found")
    return projects

#posting a new user
@app.post("/users", response_model=schemas.UserResponse)
def post_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

#getting all users
@app.get("/users", response_model=List[schemas.UserResponse])
def read_all_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users

@app.get("/users/{username}", response_model=schemas.UserResponse)
def get_user(username: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
