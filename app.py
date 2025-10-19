from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from models import db
from entities.user_entity import User  
from entities.type_pokemon_entity import TipoPokemon
##import controller
from controller.user_controller import user_bp
from controller.pokemons.pokemon_controller import pokemon_bp
from docs.swagger_config import init_swagger
app = Flask(__name__)
CORS(app)
init_swagger(app)


#Configuration DB
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

load_dotenv()

#Initialize DB and register controller
db.init_app(app)
app.register_blueprint(user_bp)
app.register_blueprint(pokemon_bp)



@app.route('/')
def ping():
    return jsonify({'message': 'pong'}), 200


def seed_types():
    types = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy']
    
    for type_name in types:
        if not db.session.query(TipoPokemon).filter_by(description=type_name).first():
            db.session.add(TipoPokemon(description=type_name))
    db.session.commit()



if __name__ == '__main__':
    with app.app_context():
      #  print("🧹 Limpando todas as tabelas antigas...")
       # db.drop_all()
        print("📦 Criando tabelas novas...")
        db.create_all() # <-- make the tables example User!
        seed_types()
        print("✅ Banco recriado com sucesso!")
    app.run(host='0.0.0.0', port=5000, debug=True)