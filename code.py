
import boto3
import sys

def create_table(API,region,table_name):
    API.create_table(
        TableName=table_name,
        KeySchema=[
            {
                "AttributeName": "petname",
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "petname",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    #table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    
def upload_table(API,region,table_name):
    table = API.Table(table_name)
    table.put_item(
        Item={
            "breed": "Russian Blue",
            "petname": "Puddles"
        }
    )
    table.put_item(
        Item={
            "breed": "Scottish Fold",
            "petname": "Hosepipe"
        }
    )

def update_attr(API,table_name):
    table= API.Table(table_name)
    table= table.update_item(
        Key={
            "petname": "Hosepipe"
            },
            UpdateExpression='SET breed = :val1',
            ExpressionAttributeValues={
                ':val1': "British Shorthair"
            })
    
    
region=sys.argv[1]
table=sys.argv[2]

#Get ressource API
DDB_RESOURCE = boto3.resource("dynamodb", region_name=region)

#create_table(DDB_RESOURCE,region,table)
#upload_table(DDB_RESOURCE,region,table)
update_attr(DDB_RESOURCE,table)