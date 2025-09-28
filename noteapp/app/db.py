from motor.motor_asyncio import AsyncIOMotorClient
from config import MongoConfig

_client =AsyncIOMotorClient(MongoConfig.MONGO_URI)
db = _client[MongoConfig.MONGO_DB_NAME]
