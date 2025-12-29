from pydantic import BaseModel
from datetime import datetime

class TimeStamp(BaseModel):
    created_at: datetime.utcnow
    updated_at: datetime.utcnow

class TextRequest(TimeStamp):
    text: str

class TextResponse(TimeStamp):
    category: str
    confidence: float

class PredictionResponse(TimeStamp):
    text: str
    category: str
    confidence: float
    
    class Config:
        from_attributes = True