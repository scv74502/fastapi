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


def get_user(user_id: str):
    try:
        response = table.query(
            KeyConditionExpression=Key("user_id").eq(user_id)
        )
        print(response)
        print(response["Items"])
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_users(limit=5):
    try:
        response = table.scan(
            Limit=limit,
            AttributesToGet=["user_id", "position_score", "previous_project", "tech_stack"]
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def delete_user(user: dict):
    try:
        print(user)
        response = table.delete_item(
            Key={
                "user_id": user['user_id']
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def update_user(user: dict):
    try:
        response = table.update_item(
            Key={
                "user_id": user["user_id"]
            },
            UpdateExpression="SET position_score = :position_score, previous_project = :previous_project, tech_stack = :tech_stack",
            ExpressionAttributeValues={
                ":position_score": user["position_score"],
                ":previous_project": user["previous_project"],
                ":tech_stack": user["tech_stack"]
            }
        )
        return response
    except ClientError as e:
        print(e)
        return JSONResponse(content=e.response["Error"], status_code=500)
