from motor.motor_asyncio import AsyncIOMotorClient
from config import MysqlConfig
import mysql.connector

client = AsyncIOMotorClient(mysql.connector.connect.MysqlConfig)

db = client[MysqlConfig.Db_Name]