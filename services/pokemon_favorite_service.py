from entities.pokemon_usuario import Pokemon
from entities.type_pokemon_entity import TipoPokemon
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

            type_name = data.get("types")[0] if data.get("types") else None

            type_pokemon = db.session.query(TipoPokemon).filter(TipoPokemon.description == type_name).first()

            tipo_id = type_pokemon.id if type_pokemon else None

            pokemon = Pokemon(
                name=name,
                image=image,
                id_types_pokemon=tipo_id,
                user_id=user_id,
                code=data.get("code"),
                favorite=True
            )

            db.session.add(pokemon)
            db.session.commit()

            return {"success": True, "message": "Favorite pokemon added successfully"}, 201

        except Exception as e:
            db.session.rollback()
            return {"success": False, "error": str(e)}, 500
        

    def get_favorites(token):
        try:
            decoded = JwtUtil.verify_token(token)
            if not decoded.get("valid"):
                return {"success": False, "message": decoded.get("message", "Invalid token")}, 401

            user_id = decoded["data"].get("user_id")

            favorites = Pokemon.query.filter_by(user_id=user_id).all()
            favorites_list = [fav.to_dict() for fav in favorites]

            return {"success": True, "favorites": favorites_list}, 200

        except Exception as e:
            return {"success": False, "error": str(e)}, 500
        
    def delete_favorite(pokemon_id, token):
        try:

            verification = JwtUtil.verify_token(token) 
            
            user_id = verification["data"]["user_id"]

            pokemon_id_int = int(pokemon_id) 

            deleted_count = db.session.query(Pokemon).filter(
                Pokemon.id == pokemon_id_int, 
                Pokemon.user_id == user_id
            ).delete(synchronize_session='fetch')

            if deleted_count == 0:
                return {"message": "Fail in remove pokemon"}, 404
    

            db.session.commit()

            return {"success": True, "message": "Favorite pokemon deleted successfully"}, 200
        
        except Exception as e:
            db.session.rollback()
            return {"message": f"Erro interno ao deletar: {str(e)}", "success": False}, 500
        
    @staticmethod
    def update_battle_team(data, token):
        user_id = JwtUtil.verify_token(token)

        code_pokemon = data.get('code')
        action = data.get('action')

        if not code_pokemon or action not in ['add', 'remove']:
            return {"message": "Invalid data: 'code' and 'action' are required"}, 400
        
        try:
            user_pokemon = db.session.query(Pokemon).filter(
                Pokemon.user_id == user_id,
                Pokemon.code == code_pokemon
            ).first()

            if not user_pokemon:
                return {"message": "Pokemon not found in the user's team"}, 404
            
            if action == 'add':
                count = db.session.query(Pokemon).filter(
                    Pokemon.user_id == user_id,
                    Pokemon.battle_groupe == True
                ).count()

                if count >= 6:
                    return {"message": "You can only have up to 6 Pokemon in the battle team"}, 400
                
                user_pokemon.favorite = True
                user_pokemon.battle_groupe = True
                message = f"{user_pokemon.name} added to the battle team"

            elif action == 'remove':
                user_pokemon.battle_groupe = False
                message = f"{user_pokemon.name} removed from the battle team"

            db.session.commit()
            return {"message": message, "pokemon": user_pokemon.to_dict()}, 200

        except Exception as e:
            db.session.rollback()
            return {"message": f"Error to update the battle team: {str(e)}"}, 500
    
    @staticmethod
    def get_battle_team(token):
        user_id = JwtUtil.verify_token(token)

        team = db.session.query(Pokemon).filter(
            Pokemon.user_id == user_id,
            Pokemon.battle_groupe == True
        ).all()

        return [p.to_dict() for p in team], 200

        
