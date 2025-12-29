from fastapi import APIRouter
from app.schemas.db_schema import TextRequest, TextResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.db_schema import TextRequest, TextResponse
from ml.predict import predict_category
from app.services.prediction_service import save_prediction

router = APIRouter()

@router.post("/categorize", response_model=TextResponse)
def categorize_api(
    request: TextRequest,
    db: Session = Depends(get_db)
):
    result = predict_category(request.text)

    save_prediction(
        db=db,
        text=request.text,
        category=result["category"],
        confidence=result["confidence"]
    )

    return TextResponse(
        category=result["category"],
        confidence=result["confidence"]
    )
