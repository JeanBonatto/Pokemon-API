import requests
from loguru import logger
from typing import Union

class PokemonConfig:
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/pokemon/'

class PokemonAPI:
    def __init__(self, config: PokemonConfig = None):
        self.config = config or PokemonConfig()
        self.STATUS_OK = [200, 201, 202]
    
    def get_id_name(self, identifier: Union[str, int] = None) -> dict:
        '''
        Esse método faz a requisição para a API do Pokemon e retorna o JSON com as informações do Pokemon.
        Segue o link da API: https://pokeapi.co/docs/v2#pokemon

        Args:
            name (str, optional): Nome do Pokemon. Defaults to None.
        Returns:
            dict: Retorna um dicionário com as informações do Pokemon.
        '''
        try:
            logger.info(f"Requisição para API do Pokemon com identificador: {identifier}")
            if not identifier:
                raise ValueError("Nome do Pokemon não pode ser vazio")
            url_full = self.config.url + str(identifier).lower().strip()
            res = requests.get(url_full)
            if res.status_code not in self.STATUS_OK:
                logger.error(f'Error in request API Pokemon:{url_full}. Status Code:{res.status_code}')
                return res
            return res.json()
        
        except Exception as e:
            logger.error(f"Erro ao fazer a requisição para API do Pokemon: {str(e)}")
            return None