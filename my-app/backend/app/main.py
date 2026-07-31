from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import boto3

BUCKET = "my-local-s3-bucket"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    "http://localhost:5173",
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the low-level S3 client
s3_client = boto3.client('s3',  
    endpoint_url="http://localhost.localstack.cloud:4566",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test")


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    s3_client.upload_fileobj(
        file.file,
        BUCKET,
        file.filename
    )

    return {"message": "Uploaded successfully!"}


@app.get("/images")
async def list_images():
    response = s3_client.list_objects_v2(Bucket=BUCKET)

    images = [
        {
            "key": obj["Key"],
            "url": s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": BUCKET, "Key": obj["Key"]},
                ExpiresIn=3600,
            ),
        }
        for obj in response.get("Contents", [])
    ]

    return {"images": images}

@app.delete("/delete-image")
async def delete_image(key:str):
    response = s3_client.delete_object(
        Bucket=BUCKET,
        Key=key

    )