from datetime import date 
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey 
from app.database import Base

class Project(Base):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    title : Mapped[str] 
    goal  : Mapped[str] 
    deadline : Mapped[date] 
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id")) 

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)  
    username: Mapped[str]  
    password : Mapped[str] 

class OutlineItem(Base):
    __tablename__ = "outline_items"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id")) 
    title: Mapped[str] 
    type: Mapped[str] 
    notes: Mapped[str] 
    is_complete: Mapped[bool] 
    due_date: Mapped[date] 


