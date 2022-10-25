import boto3
import json

def handler(event, context):
    sns_client = boto3.client("sns")
    sns_arn ="arn:aws:sns:ca-central-1:700366089459:fanout" 
    print(event)

    for record in event["Records"]:
        product = json.loads(record["body"])
        print(product)

    try:
        sns_client.publish(
            TopicArn=sns_arn,
            Subject=f"Your Order {product['id']} was placed",
            Message=record["body"]
            
            )

        print("successfully sent notification")
        print("This is testing")
    except Exception as exp:
        print(f"error occured, {exp}")