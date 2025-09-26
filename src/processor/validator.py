from loguru import logger
from fastapi import HTTPException, status
class ValidatorConfig:
    def __init__(self):
        self.fields_identificador = ["id", "name"]
        self.fields_opcional = ["weight", "height"]
        self.fields = self.fields_identificador + self.fields_opcional

class Validator:
    def __init__(self, config: ValidatorConfig = None):
        self.config = config or ValidatorConfig()

    def is_validate_identifier_field(self,identifier: str | int, field: str = None) -> str:
        '''
        Método para validar o identificador e o campo field
        Args:
            identifier (str | int): Identificador do Pokemon (ID ou nome)
            field (str, optional): Campo de busca ["id", "name", "weight", "height"]. Defaults to None.
        '''
        
        try:
            logger.info(f"Validando identificador: {identifier}, Campo: {field}")
            #Verifica se o identinficador é um FLoat e retorna falso
            if isinstance(identifier, float):
                msg = "Identificador inválido, o mesmo não pode ser um número decimal."
                logger.error(msg)
                return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                    detail=msg)
            
            # Verifica se o identificador é um número em formato string e converte para int
            if isinstance(identifier, str) and identifier.isdigit():
                identifier = int(identifier)
            #Verifica o campo field, se possui valor valido
            if field:
                field = field.strip()
                if field not in self.config.fields:
                    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                        detail=f"Campo inválido, os campos válidos são: {', '.join(self.config.fields)}")
            logger.info(f"Identificador e campo validados com sucesso: {identifier}, Campo: {field}")
            return identifier, field
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Erro em realizar a validação dos campos: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro na validação: {str(e)}"
            )
