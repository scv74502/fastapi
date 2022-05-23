from .db import dynamodb
from typing import Optional
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
        response["Items"][0]['previous_project'].add("test")
        print(response["Items"][0]['previous_project'])
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
        UpdateExpression = "SET "
        ExpressionAttributeValues = {}

        if user["position_score"] is not None:
            UpdateExpression += "position_score = :position_score,"
            ExpressionAttributeValues[":position_score"] = user["position_score"]

        if user["previous_project"] is not None:
            UpdateExpression += "previous_project = :previous_project,"
            ExpressionAttributeValues[":previous_project"] = user["previous_project"]

        if user["tech_stack"] is not None:
            UpdateExpression += "tech_stack = :tech_stack,"
            ExpressionAttributeValues[":tech_stack"] = user["tech_stack"]

        UpdateExpression = UpdateExpression.rstrip(",")

        response = table.update_item(
            Key={
                "user_id": user["user_id"]
            },
            UpdateExpression = UpdateExpression,
            # UpdateExpression="SET position_score = :position_score, previous_project = :previous_project, tech_stack = :tech_stack",
            # ExpressionAttributeValues={
                # ":position_score": user["position_score"],
                # ":previous_project": user["previous_project"],
                # ":tech_stack": user["tech_stack"]
            # }
            ExpressionAttributeValues = ExpressionAttributeValues
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)
