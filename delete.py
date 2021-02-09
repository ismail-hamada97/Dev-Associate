import boto3

dynamodb= boto3.resource('dynamodb', 'us-east-1')
table=dynamodb.Table('lostcats')
table.delete_item(
    Key={
        'petname': 'Puddles'
    })