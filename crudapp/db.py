from motor.motor_asyncio import AsyncIOMotorClient
from config import MongoConfig

client = AsyncIOMotorClient(MongoConfig.MongoUri)
db = client[MongoConfig.MongoDb]