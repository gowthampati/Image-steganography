from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    app.secret_key = 'your_secret_key'

    from app.routes import main
    app.register_blueprint(main)

   
