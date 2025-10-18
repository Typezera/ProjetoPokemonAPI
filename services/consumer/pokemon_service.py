import requests
import os

class PokemonService:

    POKEMON_API_URL = os.getenv("POKEMON_API_URL", "https://pokeapi.co/api/v2/pokemon") ## load the POKEMON_API_URL from the .env file

    @staticmethod
    def get_all_pokemons(limit=50, offset=0):
        # search list of limited pokemons
        try:
            response = requests.get(f"{PokemonService.POKEMON_API_URL}?limit={limit}&offset={offset}")
            response.raise_for_status() ##throw an exception if the response status code is not 200
            data = response.json()

            pokemons = []

            for item in data.get("results", []):
                details_url = item.get("url")
                if not details_url:
                    continue

                details_response = requests.get(details_url)
                if details_response.status_code != 200:
                    print(f"Failed to get details for {item.get('name')}: {details_response.status_code}")
                    continue

                details = details_response.json()

                pokemons.append({
                    "id": details["id"],
                    "name": details["name"].capitalize(),
                    "image": details["sprites"]["front_default"],
                    "types": [t["type"]["name"] for t in details["types"]]
                })

            return {"success": True, "pokemons": pokemons}, 200
        
        except requests.exceptions.RequestException as e:
            print("Error consulting the Pokemon API:", e)
            return {"success": False, "error": "Failed to conect to the Pokemon API"}, 500
        

    @staticmethod
    def get_pokemon_by_name(name):
        ##Search one pokemon by name
        try:
            response = requests.get(f"{PokemonService.POKEMON_API_URL}/{name.lower()}")
            if response.status_code != 200:
                return {"success": False, "error": "Pokemon not found"}, 404
            
            data = response.json()
            pokemon = {
                "id": data["id"],
                "name": data["name"].capitalize(),
                "image": data["sprites"]["front_default"],
                "types": [t["type"]["name"] for t in data["types"]]
            }
            return {"success": True, "pokemon": pokemon}, 200
        
        except requests.exceptions.RequestException as e:
            print("Error consulting the Pokemon API:", e)
            return {"success": False, "error": "Failed to conect to the Pokemon API"}, 500
        


