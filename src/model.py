import torch
from transformers import pipeline

class SentimentClassifier:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.classifier = pipeline("sentiment-analysis", model=model_name)
        
    def predict(self, texts):
        return self.classifier(texts)

if __name__ == "__main__":
    clf = SentimentClassifier()
    texts = ["I love this product, it works great!", "This is terrible and broken."]
    results = clf.predict(texts)
    for text, result in zip(texts, results):
        print(f"Text: {text}\nSentiment: {result['label']} (Score: {result['score']:.4f})\n")
