from fastapi import FastAPI
import pickle
import re

# Initialize FastAPI app
app = FastAPI()

# Load model and vectorizer
model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

# Home route
@app.get("/")
def home():
    return {"message": "Smart Support AI API is running 🚀"}

# Prediction route
@app.get("/predict")
def predict(text: str):
    # Step 1: Clean input
    cleaned = clean_text(text)

    # Step 2: Convert to vector
    vec = vectorizer.transform([cleaned])

    # Step 3: Predict
    prediction = model.predict(vec)[0]

    # Step 4: Return result
    return {
        "input": text,
        "cleaned_input": cleaned,
        "prediction": prediction,
        "status": "success"
    }