import os
from dotenv import load_dotenv

load_dotenv()

class MongoConfig:
    MongoUri = os.getenv("MongoUri")
    MongoDb = os.getenv("MongoDb")
