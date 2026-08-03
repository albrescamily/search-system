import uuid
from core.clients import QDRANT_COLLECTION, qdrant_client
from qdrant_client.http import models as qdrant_models


def index_image(bucket: str, key: str, embedding: list):
    point_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{bucket}/{key}"))

    qdrant_client.upsert(
        collection_name=QDRANT_COLLECTION,
        points=[
            qdrant_models.PointStruct(
                id=point_id,
                vector=embedding,
                payload={"bucket": bucket, "key": key},
            )
        ],
    )

    return point_id
