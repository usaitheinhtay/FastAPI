import os
from dotenv import load_dotenv

load_dotenv()

class MysqlConfig:
    MongoDb_Uri = os.getenv("mysqluri")
    MongoDb_Name = os.getenv("DbName")