from pydantic import BaseModel, Field
from uuid import uuid4


def generate_projectID():
    return str(uuid4())


class ProjectPosition(BaseModel):
    position: str
    req_person: int


class Project(BaseModel):
    project_id: str = Field(default_factory=generate_projectID)
    manager_id: str
    member_id: set
    required_position: list[ProjectPosition]
    requrired_person: int
    tech_stack: set