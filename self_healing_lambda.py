import boto3
import os

ecs = boto3.client("ecs", region_name=os.environ.get("AWS_REGION", "ap-south-1"))

CLUSTER = os.environ["ECS_CLUSTER"]
SERVICE = os.environ["ECS_SERVICE"]


def lambda_handler(event, context):
    print("Received ECS task failure event:")
    print(event)

    response = ecs.update_service(
        cluster=CLUSTER,
        service=SERVICE,
        desiredCount=1,
        forceNewDeployment=True
    )

    print("Self-healing deployment triggered.")

    return {
        "statusCode": 200,
        "message": "CloudSentinel self-healing deployment triggered",
        "service": response["service"]["serviceName"],
        "desiredCount": response["service"]["desiredCount"]
    }
