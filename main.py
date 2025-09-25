from fastapi import FastAPI, HTTPException, status
from src.service.pokemon_service import PokemonService

# Create FastAPI instance
app = FastAPI(
    title="Pokemon API - Api do Jean",
    description="API para consultar informações de Pokemons.",
    version="1.0.0"
)

# Instancia do serviço de Pokemon
pokemon_service = PokemonService()

@app.get("/pokemon/")
async def query_pokemon(identifier: str, field: str = None) -> str:
    """
    Endpoint para buscar informações de Pokemon
    
    Args:
        identifier: ID ou nome do Pokemon
        field: Campo de busca (id, name, weight, height)
    Returns:
        Informações do Pokemon ou mensagem de erro
        Retorna HTTP 400 se o identificador for inválido
        Retorna HTTP 404 se o Pokemon não for encontrado
        Retorna HTTP 500 para erros internos
        Retorna HTTP 200 para sucesso, sendo um Json stringficado, conforme solicitado
    """
    try:
        request = pokemon_service.get_query_pokemon(identifier, field)
        if request:
            return request
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                             detail=str(e))