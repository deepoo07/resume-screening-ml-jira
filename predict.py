import pickle
import re

model = pickle.load(open("resume_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z ]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

while True:
    text = input("\nEnter resume text (type 'exit' to stop): ")

    if text.lower() in ["exit", "quit", "stop"]:
        print("Exiting...")
        break

    if not text.strip():
        print("Please enter some text.")
        continue

    try:
        cleaned = clean_text(text)
        vector = tfidf.transform([cleaned])
        prediction = model.predict(vector)
        print("Predicted Category:", prediction[0])
    except Exception as e:
        print("Error:", e)