from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key


table = dynamodb.Table("user_info")


def create_user(user: dict):
    try:
        table.put_item(Item=user)
        return user
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_user(id: int):
    try:
        response = table.query(
            KeyConditionExpression=Key("user_id").eq(id)
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_users():
    try:
        response = table.scan(
            Limit=5,
            AttributesToGet=["position_score", "previous_project", "tech_stack"]
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def delete_user(user:dict):
    print(user)
    try:
        response = table.delete_item(
            Key={
                'user_id': user['user_id']
            }
        )
        return response
    except ClientError as e:
        print(e)
        return JSONResponse(content=e.response["Error"], status_code=500)


def update_user(user: dict):
    try:
        response = table.update_item(
            Key={
                "user_id": user["user_id"],
            },
            UpdateExpression="SET position_score = :position_score, previous_project = :previous_project, tech_stack = tech_stack",
            ExperssionAttributeValues={
                ":position_score": user["position_score"],
                ":previous_project": user["previous_project"],
                ":tech_stack": user["tech_stack"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)
