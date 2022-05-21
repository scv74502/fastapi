from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime


def generate_userID():
    return str(uuid4())


def generate_date():
    return str(datetime.now())


class User(BaseModel):
    user_id: str =  Field(default_factory=generate_userID)
    position_score: set
    previous_project: set
    tech_stack: set


