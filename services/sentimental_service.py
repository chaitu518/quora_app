from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(text: str) -> str:
    result = sentiment_model(text)[0]
    return result['label'].lower()
