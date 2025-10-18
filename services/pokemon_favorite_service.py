from entities.pokemon_entity import Pokemon
from models import db
from security.jwt_util import JwtUtil

class PokemonFavoriteService:
    @staticmethod
    def add_favorite(data, token):
        try:
            decoded = JwtUtil.verify_token(token)
            if not decoded.get("valid"):
                return {"success": False, "message": decoded.get("message", "Invalid token")}, 401
            
            user_id = decoded["data"].get("user_id")

            name = data.get("name")
            image = data.get("image")
            types = ", ".join(data.get("types", []))

            pokemon = Pokemon(name=name, image=image, types=types, user_id=user_id)
            db.session.add(pokemon)
            db.session.commit()

            return {"success": True, "message": "Favorite pokemon added successfully"}, 201
        except Exception as e:
            return {"success": False, "error": str(e)}, 500
        
