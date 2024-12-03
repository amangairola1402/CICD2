from flask import Blueprint, request, jsonify
from app.model import predict_roles

api_bp = Blueprint('api', _name_)

@api_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    sentence = data.get("sentence")
    
    if not sentence:
        return jsonify({"error": "No sentence provided"}), 400

    # Get role predictions
    roles = predict_roles(sentence)
    
    return jsonify({"sentence": sentence, "roles": roles})