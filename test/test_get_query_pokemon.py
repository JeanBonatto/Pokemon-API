import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from src.service.pokemon_service import PokemonService
from fastapi import HTTPException

pokemon_service = PokemonService()

def test_get_pokemon_by_numeric_id():
    """Test case: query_pokemon(132, field="id")"""
    request = pokemon_service.get_query_pokemon(132, "id")
    assert request is not None
    assert '"name": "ditto"' in request

def test_get_pokemon_by_string_id():
    """Test case: query_pokemon("132", field="id")"""
    request = pokemon_service.get_query_pokemon("132", "id")
    assert request is not None
    assert '"name": "ditto"' in request

def test_get_pokemon_by_id_no_field():
    """Test case: query_pokemon(133)"""
    request = pokemon_service.get_query_pokemon(133)
    assert request is not None
    assert '"name": "eevee"' in request

def test_get_pokemon_by_name():
    """Test case: query_pokemon("squirtle")"""
    request = pokemon_service.get_query_pokemon("squirtle")
    assert request is not None
    assert '"name": "squirtle"' in request

def test_get_pokemon_invalid_name():
    """Test case: query_pokemon("dito")"""
    with pytest.raises(HTTPException) as exc_info:
        pokemon_service.get_query_pokemon("dito")
    assert exc_info.value.status_code == 404

def test_get_pokemon_by_weight():
    """Test case: query_pokemon(40, field=" weight")"""
    request = pokemon_service.get_query_pokemon(40, " weight")
    assert request is not None
    assert '"weight":' in request

def test_get_pokemon_by_weight_string():
    """Test case: query_pokemon("40", field=" weight")"""
    request = pokemon_service.get_query_pokemon("40", " weight")
    assert request is not None
    assert '"weight":' in request

if __name__ == "__main__":
    pytest.main(["-v", __file__])