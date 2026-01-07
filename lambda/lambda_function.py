import json
import boto3

s3 = boto3.client("s3")

QUARANTINE_BUCKET = "quarentine-bucket6767"
QUARANTINE_PREFIX = "quarantine/"

def lambda_handler(event, context):
    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        print(f"Received file: {key} from bucket: {bucket}")

        try:
            # Simulated corruption rule
            if "fail" in key.lower():
                raise ValueError("Simulated file corruption")

            print(f"File {key} processed successfully")

        except Exception as e:
            print(f"ERROR processing {key}: {str(e)}")

            quarantine_key = f"{QUARANTINE_PREFIX}{key}"

            s3.copy_object(
                Bucket=QUARANTINE_BUCKET,
                CopySource={"Bucket": bucket, "Key": key},
                Key=quarantine_key,
            )

            print(f"Moved {key} to quarantine bucket")

    return {
        "statusCode": 200,
        "body": json.dumps("Processing complete"),
    }
