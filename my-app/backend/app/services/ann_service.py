from core.clients import QDRANT_COLLECTION, qdrant_client

def ann_search(embedding: list, limit: int = 20):
    results = qdrant_client.query_points(
        collection_name=QDRANT_COLLECTION,
        query=embedding,
        limit=limit,
    ).points

    return [point.payload for point in results]