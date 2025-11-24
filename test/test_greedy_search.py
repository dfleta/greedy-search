import pytest
from src.greedy_search import find_best_station

def test_find_best_station():
    # Estados ya cubiertos
    covered_states = set(["wa", "id"])
        
    # Estaciones y estados que cubren
    stations = {
        "kone": set(["wa", "id", "mt"]),
        "ktwo": set(["or", "nv", "ca"]),
        "kthree": set(["nv", "ut"]),
    }
        
    best_station, best_gradient = find_best_station(stations, covered_states)
        
    assert best_station == "ktwo"   # ktwo cubre 3 nuevos estados
    assert best_gradient == 3       # Gradiente esperado es 3
