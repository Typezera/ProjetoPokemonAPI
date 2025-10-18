from flask import Flask, jsonify
from flask_cors import CORS
import os
from models import db
##import controller
from controller.user_controller import user_bp
from entities.user_entity import User  
app = Flask(__name__)
CORS(app)


#Configuration DB
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize DB and register controller
db.init_app(app)
app.register_blueprint(user_bp)



@app.route('/')
def ping():
    return jsonify({'message': 'pong'}), 200


if __name__ == '__main__':
    with app.app_context():
      #  print("🧹 Limpando todas as tabelas antigas...")
       # db.drop_all()
        print("📦 Criando tabelas novas...")
        db.create_all() # <-- make the tables example User!
        print("✅ Banco recriado com sucesso!")
    app.run(debug=True)