from dotenv import load_dotenv
import os

load_dotenv()

class MongoConfig:
    MONGO_URI =os.getenv("MONGOURI")
    MONGO_DB_NAME = os.getenv("MONGO_DBNAME")


