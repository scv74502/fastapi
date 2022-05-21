from boto3 import resource
from os import getenv

dynamodb = resource("dynamodb",
                    aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
                    aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
                    region_name=getenv("REGION_NAME"))


# tables = [
    # {
        # "TableName": "users",
        # "KeySchema": [
            # {
                # 'AttributeName': 'UserID',
                # 'KeyType': 'HASH'
            # },
        # ],
        # "EXProject": [
            # {
                # 'AttributeName': '',
                # 'AttributeType': 'SS'
            # },
            # {
                # 'AttributeName': 'created_at',
                # 'AttributeType': 'S'
            # }
        # ],
    # },
# ]

# create user_info tables
user_info = [
    {
        "TableName": "user_info",
        "KeySchema": [
            {
                'AttributeName': 'user_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'created_at',
                'KeyType': 'RANGE'

            }
            # {
                # 'AttributeName': 'position_score',
                # 'KeyType': 'RANGE'
            # },
            # {
                # 'AttributeName': 'previous_project',
                # 'KeyType': 'RANGE'
            # },
            # {
                # 'AttributeName': 'tech_stack',
                # 'KeyType': 'RANGE'
            # },
        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'user_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'created_at',
                'AttributeType': 'S'
            }

            # {
                # 'AttributeName': 'position_score',
                # 'AttributeType': 'S'
            # },
        ],
    },
]


project_info = [
    {
        "TableName": "project_info",
        "KeySchema": [
            {
                'AttributeName': 'project_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'manager_id',
                'KeyType': 'RANGE'
            },
            # {
                # 'AttributeName': 'member_id',
                # 'KeyType': 'RANGE'
            # },
            # {
                # 'AttributeName': 'required_position',
                # 'KeyType': 'RANGE'
            # },
            # {
                # 'AttributeName': 'required_person',
                # 'KeyType': 'RANGE'
            # },
#
            # {
                # 'AttributeName': 'tech_stack',
                # 'KeyType': 'RANGE'
            # },

        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'project_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'manager_id',
                'AttributeType': 'S'
            },
            # {
                # 'AttributeName': 'member_id',
                # 'AttributeType': 'S'
            # },
            # {
                # 'AttributeName': 'required_position',
                # 'AttributeType': 'S'
            # },
            # {
                # 'AttributeName': 'required_person',
                # 'AttributeType': 'N'
            # },
            # {
                # 'AttributeName': 'tech_stack',
                # 'AttributeType': 'S'
            # }

        ],
    },
]


def create_user_table():
    try:
        for table in user_info:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:
        print(e)


def create_project_table():
    try:
        for table in project_info:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:
        print(e)
