import json
import boto3

from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    lastname = event['queryStringParameters']['LastName']
    table = dynamodb.Table('voters8')
    response = table.query(
        IndexName="LastName-index",
        KeyConditionExpression=Key('LastName').eq(lastname)
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response['Items']),
         'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
        }
    }

