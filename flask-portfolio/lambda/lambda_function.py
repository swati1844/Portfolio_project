import json
import boto3
import urllib.parse

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactMessages')

def lambda_handler(event, context):
    body = urllib.parse.parse_qs(event['body'])

    name = body.get('name', [''])[0]
    email = body.get('email', [''])[0]
    message = body.get('message', [''])[0]

    table.put_item(Item={
        'email': email,
        'name': name,
        'message': message
    })

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps('Message saved to DynamoDB!')
    }