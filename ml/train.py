import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Load dataset
df = pd.read_csv("data/expenses.csv")

# 2. Separate input and output
X = df["text"]
y = df["category"]

# 3. Convert text to numerical form;./
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X_vectorized = vectorizer.fit_transform(X)

# 4. Train the model
# Logistic Regression -> because we are classifying the data.
model = LogisticRegression(max_iter=200)
model.fit(X_vectorized, y)

# 5. Save model and vectorizer
with open("ml/category_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("ml/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("\nModel Training\nModel training completed successfully\n")
