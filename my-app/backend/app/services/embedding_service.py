from app.services.storage_service import download_from_s3
from core.clients import BUCKET, QDRANT_COLLECTION, model, qdrant_client, s3_client


def embed_image_from_s3(bucket: str, key: str):
    image = download_from_s3(
        bucket,
        key,
    )
    embeddings = model.encode(image).tolist()
    return embeddings


def embed_text_query(query: str):
    embeddings = model.encode(query).tolist()
    return embeddings