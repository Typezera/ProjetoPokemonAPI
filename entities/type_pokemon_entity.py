from models import db

class TipoPokemon(db.Model):
    __tablename__ = 'types_pokemons'

    id = db.Column(db.Integer, primary_key=True)

    description = db.Column(db.String(50), unique=True, nullable=False)

   # pokemons = db.relationship('Pokemon', backref='', lazy='dynamic')

    #pokemons = db.relationship('Pokemon', backref='tipo_pokemon_rel', lazy='dynamic')


    def __repr__(self):
        return f"<TypePokemon {self.description}>"