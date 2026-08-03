import io
import uuid
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from qdrant_client.http import models as qdrant_models

from core.clients import BUCKET, QDRANT_COLLECTION, model, qdrant_client, s3_client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "Server is running smoothly!"}


@app.post("/embed/image")
async def embed_image(file: UploadFile = File(...)):
    img = Image.open(io.BytesIO(await file.read()))
    embedding = model.encode(img).tolist()
    print(embedding)




    return {"embedding": embedding}


@app.post("/embed/text")
async def embed_text(text: str):
    embedding = model.encode(text).tolist()
    return {"embedding": embedding}


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
async def delete_image(key: str):
    s3_client.delete_object(
        Bucket=BUCKET,
        Key=key
    )

    return {"message": "Deleted successfully!"}
