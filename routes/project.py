from fastapi import APIRouter
from models.project import Project
from database.project import create_project, get_project, get_projects, delete_project, update_project


routes_project = APIRouter()

# CREATE USER


@routes_project.put("/create", response_model=Project)
def create(project: Project):
    return create_project(project.dict())



@routes_project.get("/get/id")
def get_by_id(project_id: str):
    return get_project(project_id)

# GET ALL USERS


@routes_project.get("/all")
def get_all():
    return get_projects()

# DELETE USER


@routes_project.delete("/delete")
def create(project: Project):
    return delete_project(project.dict())

# UPDATE USER


@routes_project.patch("/update")
def create(project: Project):
    return update_project(project.dict())
