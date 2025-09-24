from fastapi import FastAPI
from src.service.pokemon_service import PokemonService

# Create FastAPI instance
app = FastAPI(
    title="Pokemon API - Api do Jean",
    description="API para consultar informações de Pokemons.",
)


@app.get("/")
#Rota para solicitar informações de Pokemons
def get_name_id():
    return {"Hello": "World"}
