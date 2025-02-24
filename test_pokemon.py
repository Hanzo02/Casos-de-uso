import pytest
import requests

# URL base de la API de Pokémon
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def test_get_pokemon_success():
    """
    Obtener información de un Pokémon válido
    Dado un nombre o ID de Pokémon válido, la API debe devolver su información correcta.
    """
    response = requests.get(f"{BASE_URL}pikachu")
    assert response.status_code == 200  # La respuesta debe ser exitosa
    data = response.json()
    assert data['name'] == 'pikachu'  # El nombre del Pokémon debe ser correcto

def test_get_pokemon_not_found():
    """
    Buscar un Pokémon inexistente
    Si se busca un Pokémon que no existe, la API debe devolver un error (404).
    """
    response = requests.get(f"{BASE_URL}xyz123")
    assert response.status_code == 404  # La respuesta debe ser un error 404

def test_get_pokemon_type():
    """
    Verificar el tipo de un Pokémon
    Comprobar que un Pokémon tiene el tipo correcto (por ejemplo, Pikachu debe ser "electric").
    """
    response = requests.get(f"{BASE_URL}pikachu")
    assert response.status_code == 200
    data = response.json()
    types = [t['type']['name'] for t in data['types']]
    assert 'electric' in types  # Pikachu debe ser de tipo eléctrico

def test_get_pokemon_stats():
    """
    Verificar estadísticas base de un Pokémon
    Asegurar que un Pokémon tenga sus estadísticas base correctamente cargadas.
    """
    response = requests.get(f"{BASE_URL}bulbasaur")
    assert response.status_code == 200
    data = response.json()
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    assert 'hp' in stats  # Debe tener la estadística de vida (HP)
    assert stats['hp'] > 0  # El valor de HP debe ser positivo

def test_response_time():
    """
    Probar la velocidad de respuesta de la API
    La API debe responder en un tiempo razonable (menos de 2 segundos).
    """
    import time
    start = time.time()
    response = requests.get(f"{BASE_URL}charizard")
    end = time.time()
    assert response.status_code == 200
    response_time = end - start
    assert response_time < 2.0  # La API debe responder rápido

def test_get_pokemon_moves():
    """
     Obtener la lista de movimientos de un Pokémon
    Verificar que la lista de movimientos de un Pokémon contenga al menos uno.
    """
    response = requests.get(f"{BASE_URL}charmander")
    assert response.status_code == 200
    data = response.json()
    moves = [move['move']['name'] for move in data['moves']]
    assert len(moves) > 0  # Debe tener al menos un movimiento

