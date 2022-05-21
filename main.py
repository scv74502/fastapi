from fastapi import FastAPI
from database.db import create_user_table, create_project_table
from routes.user import routes_user
from routes.project import routes_project



app = FastAPI()


app.include_router(routes_user, prefix="/user")
app.include_router(routes_project, prefix="/project")



create_user_table()
create_project_table()