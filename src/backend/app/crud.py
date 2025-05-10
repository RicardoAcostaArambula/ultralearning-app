from app import models, schemas
from sqlalchemy.orm import Session


def create_project(db: Session, project: schemas.ProjectCreate):
    new_project = models.Project(**project.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project 

def get_all_projects(db: Session, user_id: int):
    return db.query(models.Project).filter(models.Project.user_id == user_id).all()

def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 
def get_all_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
#delete outline item

#add outline item

#get outline item notes

#write outline item notes

#update outline item notes
