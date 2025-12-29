from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.models.base import Base

class ExpensePrediction(Base):
    __tablename__ = "expense_predictions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    predicted_category = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
