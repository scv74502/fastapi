from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("project_info")


def create_project(project: dict):
    try:
        table.put_item(Item=project)
        return project
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_project(project_id: str):
    try:
        response = table.query(
            KeyConditionExpression=Key("project_id").eq(project_id)
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_projects(limit=5):
    try:
        response = table.scan(
            Limit=limit,
            AttributesToGet=["project_id", "manager_id", "member_id", "required_position", "requrired_person", "tech_stack"]
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def delete_project(project: dict):
    try:
        response = table.delete_item(
            Key={
                "project_id": project["project_id"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def update_project(project: dict):
    try:
        UpdateExpression = "SET "
        ExpressionAttributeValues = {}

        if project["manager_id"] is not None:
            UpdateExpression += "manager_id = :manager_id,"
            ExpressionAttributeValues[":manager_id"] = project["manager_id"]

        if project["member_id"] is not None:
            UpdateExpression += "member_id = :member_id,"
            ExpressionAttributeValues[":member_id"] = project["member_id"]

        if project["tech_stack"] is not None:
            UpdateExpression += "tech_stack = :tech_stack,"
            ExpressionAttributeValues[":tech_stack"] = project["tech_stack"]

        if project["required_position"] is not None:
            UpdateExpression += "required_position = :required_position,"
            ExpressionAttributeValues[":required_position"] = project["required_position"]

        if project["tech_stack"] is not None:
            UpdateExpression += "tech_stack = :tech_stack,"
            ExpressionAttributeValues[":tech_stack"] = project["tech_stack"]

        UpdateExpression = UpdateExpression.rstrip(",")

        response = table.update_item(
            Key={
                "project_id": project["project_id"]
            },
            UpdateExpression = UpdateExpression,
            ExpressionAttributeValues = ExpressionAttributeValues
        )
        return response

    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)
