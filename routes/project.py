from fastapi import APIRouter
from models.project import Project
from database.project import create_project, get_project, get_projects, delete_project, update_project #, update_projmem


routes_project = APIRouter()


# CREATE USER
@routes_project.post("/create", response_model=Project)
def create(project: Project):
    return create_project(project.dict())


@routes_project.get("")
def get_by_id(id: str):
    return get_project(id)


# GET ALL USERS
@routes_project.get("/all")
def get_all():
    return get_projects()


# DELETE USER
@routes_project.delete("/delete")
def delete(project: Project):
    return delete_project(project.dict())


# UPDATE USER
@routes_project.patch("/update")
def update(project: Project):
    return update_project(project.dict())

# UPDATE PROJECT MENBER
@routes_project.patch("/update")
def update_projmem(project: Project):
    return update_project(project.dict())

