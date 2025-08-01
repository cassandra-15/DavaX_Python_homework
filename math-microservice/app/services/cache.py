# Placeholder content for cache.py
import redis
import os
import json
from typing import Optional

# Redis connection setup
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

# --------------------
# Cache Helpers
# --------------------


def generate_cache_key(operation: str, value: str) -> str:
    return f"{operation}:{value}"


def get_cached_result(operation: str, value: str) -> Optional[float]:
    key = generate_cache_key(operation, value)
    result = redis_client.get(key)
    return float(result) if result is not None else None


def set_cached_result(operation: str, value: str, result: float, ttl_seconds: int = 3600):
    key = generate_cache_key(operation, value)
    redis_client.setex(key, ttl_seconds, json.dumps(result))
