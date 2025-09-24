import requests
from fastapi import HTTPException
from src.core.external.api_pokemon import PokemonAPI
from src.processor.validator import Validator

class PokemonService:
    def __init__(self, pokemon_api: PokemonAPI = None, validator: Validator = None):
        self.pokemon_api = pokemon_api or PokemonAPI()
        self.validator = validator or Validator()
        pass

    def get_query_pokemon(self, identifier: str | int, field: str = "name") -> dict | HTTPException:
        '''
        Realiza a requisição para API, realizna a validação dos campos e retorna o resultado
        '''
        
        try:
            # Verifica se os Campos são validos
            is_valido = self.validator.is_validate_identifier_field(identifier, field)
            if is_valido is not True:
                return is_valido
                
            response = self.pokemon_api.get_id_name()
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException:
            raise HTTPException(status_code=404, detail="Pokemon não encontrado")
