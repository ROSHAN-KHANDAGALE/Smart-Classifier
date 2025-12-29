from fastapi import APIRouter
from app.schemas.db_schema import TextRequest, TextResponse
from app.services.categorizer_service import category_predictor

router = APIRouter()

@router.post("/categorize", response_model=TextResponse)
def categorize_expense_api(request: TextRequest):
    result = category_predictor(request.text)
    return result
