import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from src.service.pokemon_service import PokemonService
from fastapi import HTTPException

pokemon_service = PokemonService()

def test_avulso():
    """Test case: query_pokemon(132, field="id")"""
    identifier = "ditto"

    request = pokemon_service.get_query_pokemon(identifier)
    assert request is not None

test_avulso()