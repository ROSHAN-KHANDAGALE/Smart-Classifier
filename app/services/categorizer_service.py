from ml.predict import predict_category

def category_predictor(text: str) -> dict:
    """
    Calls ML model and returns prediction
    """
    return predict_category(text)