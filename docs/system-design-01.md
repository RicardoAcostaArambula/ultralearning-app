# 1. Overview
- The system will help ultralearners speed up the start time for any ultralearning project,  
as well as help them review, discover weak points and archieve ultralearning goals faster.

- In a fast moving world, learning and learning fast is an essential skill. The ultralearning  
project helps you waste no time and focus on learning. 

# 2. Core Features (MVP)
List of essential features needed for first launch.
- Create new project
- Autogenerate outline to archieve learning goals based on user input either by providing the  
source (book pdf or table of contents), or just learning goals
- Edit outline
- Track progress (first 100 days, hours worked)
- Exercises for drilling topics
- Exams 
- targeting weak points suggestions. 
- note taking inside each item in outline

# 3. Stretch Features (Optional / Future)
- suggested timeline based on user input for how long the project will be 
- schedule time in calendar linked existing calendar apps (ex. google calendar) 
- remainders 
- some kind of place where all sources for learning are placed (books as pdfs, links to youtube videos, or any other source)
- Review suggestions (Anki sytle)

# 4. Tech Stack
Frontend: Streamlit
Backend: FastAPI - Python
Database: SQLite
Authentication: simple token auth (FastAPI)
Deployment: TBD
Optional: Google Calendar

# 5. System Architecture Diagram (Optional for now)


# 6. Key API Endpoints
createAccount(String username, String email String password) -> success/failure
login(String email, String password) -> String username, String password
createProject(String data) -> Project
generateOutline(int projectId) -> Outline
deleteItem(int id) -> success/failure
updateProgress(int day) -> success/failure
completeTask(int taskId) -> success/failure

# 7. Data Models
User
- userId: int PK
- username: String
- password: String
- projects: List[Project] FK

Project
- projectId (PK): int
- goal: String
- deadline: Date
- outline: Outline (FK)

Outline
- outlineId (PK): int
- projectId (FK): int
- Items: List[Strings
