import requests
class PokemonConfig:
    def __init__(self):
        self.url = 'https://pokeapi.co/api/v2/pokemon/'

class PokemonAPI:
    def __init__(self, config: PokemonConfig):
        self.config = config
    
    def __call__(self, *args, **kwds):
        return self.get_id_name(*args, **kwds)
    
    def get_id_name(self, name: str = None) -> dict:
        '''
        Esse método faz a requisição para a API do Pokemon e retorna o JSON com as informações do Pokemon.
        Segue o link da API: https://pokeapi.co/docs/v2#pokemon

        Args:
            name (str, optional): Nome do Pokemon. Defaults to None.
        Returns:
            dict: Retorna um dicionário com as informações do Pokemon.
        '''
        try:
            if not name:
                return None
            res = requests.get(self.config.url + name)
            return res.json()
        
        except Exception as e:
            print(f'Error in request API Pokemon:{self.config.url + name}. Erro:{e}')
            return None