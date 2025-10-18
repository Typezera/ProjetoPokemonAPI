from flask import Blueprint, jsonify, request
from middleware.auth_middleware import jwt_required
from services.consumer.pokemon_service import PokemonService

pokemon_bp = Blueprint('pokemon_bp', __name__)

@pokemon_bp.route('/pokemons', methods=['GET'])
@jwt_required
def get_pokemons():
    limit = request.args.get("limit", default=50, type=int)
    offset = request.args.get("offset", default=0, type=int)
    response, status = PokemonService.get_all_pokemons(limit, offset)
    return jsonify(response), status

@pokemon_bp.route('/pokemons/<name>', methods=['GET'])
@jwt_required
def get_pokemon_by_name(name):
    response, status = PokemonService.get_pokemon_by_name(name)
    return jsonify(response), status