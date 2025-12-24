import pickle, os

# Setting Absolute Path to current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Now, we are loading the model and vectoriz once
with open(os.path.join(BASE_DIR, 'category_model.pkl'), 'rb') as cat:
    model = pickle.load(cat)

with open(os.path.join(BASE_DIR, 'vectorizer.pkl'), 'rb') as vect:
    vectorizer = pickle.load(vect)

def predict_category(text: str) -> dict:
    """
    Predict Expense Category and Confidence 
    """
    # Text to Vector
    text_vector = vectorizer.transform([text])

    # Category Predictor
    prediction = model.predict(text_vector)[0]

    # Confidence of Prediction
    probability = model.predict_proba(text_vector)[0]
    confidence = float(max(probability))

    return {
        "Category": prediction,
        "Confidence": confidence
    }


if __name__ == "__main__":
    test_text = input('Enter the Text :: ')
    result = predict_category(test_text)
    print("Input:", test_text)
    print("Output:", result)