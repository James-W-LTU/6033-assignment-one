# loads in the spam detection model
model = joblib.load('models/spam_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')