import redis

def get_redis_connection():
    return redis.Redis(
    host='redis-17375.c308.sa-east-1-1.ec2.redns.redis-cloud.com',
    port=17375,
    decode_responses=True,
    username="solano",
    password="@Abc12345678",
)
