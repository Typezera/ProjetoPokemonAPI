import yaml
from flasgger import Swagger

def init_swagger(app):
    swagger = Swagger(app)

    with open("docs/endpoints/user_docs.yaml", "r", encoding="utf-8") as f:
        user_spec = yaml.safe_load(f)

    with open("docs/endpoints/pokemon_docs.yaml", "r", encoding="utf-8") as f:
        pokemon_spec = yaml.safe_load(f)


    swagger.template = {
        "swagger": "2.0",
        "info": {
            "title": "Pokémon API",
            "description": "API developed to consume the PokéAPI (users and pokemons management)",
            "version": "1.0.0"
        },
        "basePath": "/",  
        "schemes": ["http"],
        "paths": {}
    }

    if "paths" in user_spec:
        swagger.template["paths"].update(user_spec["paths"])
    if "paths" in pokemon_spec:
        swagger.template["paths"].update(pokemon_spec["paths"])

    return swagger