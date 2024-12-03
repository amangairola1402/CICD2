import torch
from transformers import RobertaTokenizer, RobertaForTokenClassification
import nltk

# Ensure NLTK data is available
nltk.download('punkt')

# Load tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
model = RobertaForTokenClassification.from_pretrained("roberta-base")

def load_model():
    """ Load model into memory. This can include loading any other resources. """
    global model, tokenizer
    print("Model and tokenizer loaded successfully.")

def predict_roles(sentence):
    """ Perform prediction on a sentence and format output. """
    inputs = tokenizer(sentence, return_tensors="pt")
    outputs = model(**inputs).logits
    predictions = torch.argmax(outputs, dim=2).tolist()[0]
    
    # Map predictions to role labels
    labels = ["Agent", "Theme", "Instrument", "Experiencer", "Location", "Source", "Goal", "Recipient", "Manner"]
    predicted_roles = [labels[pred] for pred in predictions if pred != -100]
    
    return predicted_roles