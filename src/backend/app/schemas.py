from pydantic import BaseModel
from datetime import date  
#model for creating a project
class ProjectCreate(BaseModel):
    title: str
    goal: str
    deadline: date
    user_id: int

class ProjectResponse(ProjectCreate):
    id: int
    class Config:
        from_attributes = True
#model for creating a user
class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(UserCreate):
    id: int
    class Config:
        from_attributes = True
#model for creating an outline item
class OutlineItemCreate(BaseModel):
    title: str
    type : str
    project_id: int
    notes : str
    is_complete : bool 
    due_date : date 
class OutlineItemResponse(OutlineItemCreate):
    id: int
    class Config:
        from_attributes = True

