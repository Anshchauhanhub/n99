import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from typing import Dict, Optional
from datetime import datetime
from pytz import timezone

load_dotenv()

class MongoDBHandler:
    """Handler class for MongoDB operations"""
    
    def __init__(self: str = None):
        """Initialize MongoDB connection"""
        # Get configuration from environment variables if not provided
        self.connection_string = os.getenv('MONGODB_URI')
        self.database_name = os.getenv('MONGODB_DATABASE')
        
        try:
            self.client = MongoClient(self.connection_string)
            # Test connection
            self.client.admin.command('ping')
            self.db = self.client[self.database_name]
        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise
    
    def write_one(self, collection:str, data) -> Optional[str]:
        """Insert a single document into a collection"""
        try:
            collection = self.db[collection]
            datetime_ist = datetime.now(timezone('Asia/Kolkata'))
            data['created_at'] = datetime_ist.strftime("%Y-%m-%d %H:%M:%S")
            result = collection.insert_one(data)
            return str(result.inserted_id)
        except OperationFailure as e:
            print(f"Failed to insert document: {e}")
            return None