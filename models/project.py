from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime


def generate_projectID():
    return str(uuid4())


def generate_managerID():
    return str(uuid4())


class Project(BaseModel):
    project_id: str = Field(default_factory=generate_projectID)
    manager_id: str = Field(default_factory=generate_managerID)
    member_id: set
    required_position: dict
    requrired_person: int
    tech_stack: set


