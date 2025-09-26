import json
import requests
from loguru import logger
from fastapi import HTTPException,status
from src.core.external.api_pokemon import PokemonAPI
from src.processor.validator import Validator
from src.processor.data_processor import DataProcessorString

class PokemonService:
    def __init__(self, pokemon_api: PokemonAPI = None, validator: Validator = None):
        self.pokemon_api = pokemon_api or PokemonAPI()
        self.validator = validator or Validator()
        self.data_processor = DataProcessorString()
        pass

    def get_query_pokemon(self, identifier: str | int, field: str = None) -> dict | HTTPException:
        '''
        Realiza a requisição para API, realizna a validação dos campos e retorna o resultado
        '''
        
        try:
            logger.info(f"Consultando Pokemon: {identifier}, Campo: {field}")
            # Verifica se os Campos são validos
            identifier,field = self.validator.is_validate_identifier_field(identifier, field)
            
            #Faz o tratamento das strings
            identifier = self.data_processor.process_string(identifier)
            if field:
                field = self.data_processor.process_string(field)
            # Busca Pokemon
            logger.info(f"Buscando Pokemon: {identifier}, Campo: {field}")
            pokemon_data = self.pokemon_api.get_id_name(identifier)
            
            if not pokemon_data:
                raise HTTPException(
                    status_code=pokemon_data.status_code,
                    detail=pokemon_data.text
                )
            
            # Filtra por característica se necessário
            if field in self.validator.config.fields_opcional:
                filtered_data = {
                    "name": pokemon_data["name"],
                    "id": pokemon_data["id"],
                    field: pokemon_data[field]
                }
                return json.dumps(filtered_data)

            return json.dumps(pokemon_data)
        
        except HTTPException as http_exc:
            logger.error(f"HTTPException ao consultar Pokemon: {http_exc.detail}")
            raise http_exc
        except Exception as e:
            logger.error(f"Erro ao consultar Pokemon: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
