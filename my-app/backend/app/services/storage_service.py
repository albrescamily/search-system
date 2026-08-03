from core.clients import BUCKET, QDRANT_COLLECTION, model, qdrant_client, s3_client
from PIL import Image
import io

def upload_to_s3(file):
    key = file.filename

    s3_client.upload_fileobj(
        Fileobj=file.file,
        Bucket=BUCKET,
        Key=key,
    )

    return BUCKET,key

def download_from_s3(bucket: str, key: str):
    response = s3_client.get_object(
        Bucket=bucket,
        Key=key,
    )
    image_bytes = response["Body"].read()
    image = Image.open(io.BytesIO(image_bytes))
    return image