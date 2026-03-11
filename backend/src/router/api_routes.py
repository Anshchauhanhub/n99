from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

from src.db.mongo import MongoDBHandler
from src.model.spider import get_movie_listings

from bson.objectid import ObjectId
from datetime import datetime

from loguru import logger

router = APIRouter()

mongo = MongoDBHandler()

@router.get("/api/qFetch")
async def get_survey_questions():
    """Get survey questions from the database (MongoDB)"""
    try:
        question = mongo.read_one(collection="questions", field="questions")

        return question
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))