from flask import Flask

def create_app():
    app = Flask(_name_)
    
    # Load model
    from app.model import load_model
    load_model()  # Ensure model is loaded at startup

    # Register API routes
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app