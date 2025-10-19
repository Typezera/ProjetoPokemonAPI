from services.pokemon_favorite_service import PokemonFavoriteService
from flask import Blueprint, jsonify, request
from middleware.auth_middleware import jwt_required
from services.consumer.pokemon_service import PokemonService

pokemon_bp = Blueprint('pokemon_bp', __name__, url_prefix="/api/pokemons" )

#### Rote for get all pokemons for limit you want


### Rote for get pokemon by name
@pokemon_bp.route('/name/<name>', methods=['GET'])
@jwt_required
def get_pokemon_by_name(name, user_data):
    response, status = PokemonService.get_pokemon_by_name(name)
    return jsonify(response), status

### Rote for add pokemon favorite
@pokemon_bp.route('/favorite', methods=['POST'])
@jwt_required
def add_favorite(user_data):
    data = request.get_json()
    token = request.headers.get('Authorization').split(" ")[1]
    response, status = PokemonFavoriteService.add_favorite(data, token)
    return jsonify(response), status

### Rote for get pokemon favorites
@pokemon_bp.route('/favorites', methods=['GET'])
@jwt_required
def get_favorites(user_data):
    token = request.headers.get('Authorization').split(" ")[1]
    response, status = PokemonFavoriteService.get_favorites(token)
    return jsonify(response), status


### Rote for add and remove pokemon to battle team
@pokemon_bp.route('/favorite/<pokemon_id>', methods=['DELETE'])
@jwt_required
def delete_favorite(pokemon_id, user_data):
    token = request.headers.get('Authorization').split(" ")[1]
    response, status = PokemonFavoriteService.delete_favorite(pokemon_id, token)
    return jsonify(response), status


## Rote for add pokemon to battle team and remove
@pokemon_bp.route('/battle_team', methods=['POST'])
@jwt_required
def handle_battle_team(user_data):
    data = request.get_json()
    token = request.headers.get('Authorization').split(" ")[1]

    response, status = PokemonFavoriteService.update_battle_team(data, token)
    return jsonify(response), status

# rote list pokemon in battle team
@pokemon_bp.route('/battle_team', methods=['GET'])
@jwt_required
def get_battle_team(user_data):
    token = request.headers.get('Authorization').split(" ")[1]
    response, status = PokemonFavoriteService.get_battle_team(token)
    return jsonify(response), status



@pokemon_bp.route('/', methods=['GET'])
@jwt_required
def get_pokemons(user_data):
    limit = request.args.get("limit", default=50, type=int)
    offset = request.args.get("offset", default=0, type=int)
    response, status = PokemonService.get_all_pokemons(limit, offset)
    return jsonify(response), status