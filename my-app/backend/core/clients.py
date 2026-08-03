import boto3
from qdrant_client import QdrantClient
from qdrant_client.http import models as qdrant_models
from sentence_transformers import SentenceTransformer

BUCKET = "my-local-s3-bucket"
QDRANT_COLLECTION = "images"
EMBEDDING_SIZE = 512  # clip-ViT-B-32 output dimension

model = SentenceTransformer('clip-ViT-B-32')

s3_client = boto3.client('s3',
    endpoint_url="http://localhost.localstack.cloud:4566",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test")


qdrant_client = QdrantClient(url="http://localhost:6333")

if not qdrant_client.collection_exists(QDRANT_COLLECTION):
    qdrant_client.create_collection(
        collection_name=QDRANT_COLLECTION,
        vectors_config=qdrant_models.VectorParams(
            size=EMBEDDING_SIZE,
            distance=qdrant_models.Distance.COSINE,
        ),
    )