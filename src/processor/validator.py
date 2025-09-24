from fastapi import HTTPException, status

class Validator:
    pass

    def is_validate_identifier_field(self,identifier: str | int, field: str = None) -> bool:
        #Verifica se o identinficador é um FLoat e retorna falso
        if isinstance(identifier, float):
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                                 detail="Identificador inválido, o mesmo não pode ser um número decimal.")
        
        # Verifica se o identificador é um número em formato string e converte para int
        if isinstance(identifier, str) and identifier.isdigit():
            identifier = int(identifier)
        #Verifica o campo field, se possui valor valido
        if field:
            '''
            Necessário verificar quais as opções validas desse campos
            '''
            pass
        return True
