from models import db


class Pokemon(db.Model):
    __tablename__ = 'pokemons_usuario'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    code = db.Column(db.String(100), nullable=False)

    name = db.Column(db.String(100), nullable=False)

    image = db.Column(db.String(255))

    id_types_pokemon = db.Column(db.Integer, db.ForeignKey('types_pokemons.id'), nullable=False)


    favorite = db.Column(db.Boolean, default=False, nullable=False)

    battle_groupe = db.Column(db.Boolean, default=False, nullable=False)
    #types = db.Column(db.String(255))

    tipo_pokemon_rel = db.relationship('TipoPokemon', 
        foreign_keys=[id_types_pokemon]
    )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'codigo': self.code,
            'name': self.name,
            'image': self.image,
            'types_pokemons': self.id_types_pokemon,
            'favorite': self.favorite,
            'battle_groupe': self.battle_groupe,
            'type_description': self.id_types_pokemon
        }
    
    def __repr__(self):
        return f"<PokemonUsuario {self.name} - User: {self.user_id}>"