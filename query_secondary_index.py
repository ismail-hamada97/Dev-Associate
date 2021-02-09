import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('lostcats')

resp = table.query(
    # Add the name of the index you want to use in your query.
    IndexName="breed_index",
    KeyConditionExpression=Key('breed').eq('Bengal'),
)

print("The query returned the following items:")
for item in resp['Items']:
    print(item)