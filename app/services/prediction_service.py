from sqlalchemy.orm import Session
from app.models.prediction import ExpensePrediction

def save_prediction(
    db: Session,
    text: str,
    category: str,
    confidence: float
):
    prediction = ExpensePrediction(
        text=text,
        predicted_category=category,
        confidence=confidence
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction
