from fastapi import APIRouter
from models.project import Project
from database.project import create_project, get_project, get_projects, delete_project, update_project


routes_project = APIRouter()


# CREATE USER
@routes_project.post("/create", response_model=Project)
def create(project: Project):
    return create_project(project.dict())


# GET USER BY ID
@routes_project.get("/get/{id}")
def get_by_id(id: str):
    return get_project(id)


# GET ALL USERS
@routes_project.get("/all")
def get_all():
    return get_projects()


# DELETE USER
@routes_project.post("/delete")
def create(project: Project):
    return delete_project(project.dict())


# UPDATE USER
@routes_project.post("/update")
def create(project: Project):
    return update_project(project.dict())