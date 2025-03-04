import matplotlib.pyplot as plt
import random

# estados de USA donde queremos ser escuchados
needed_states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
added_states = set(["nm", "tx", "ok", "ks", "co", "ne", "sd", "wy", "nd", "ia", "mn", "mo", "ar", "la"])

needed_states.update(added_states)

# estaciones de radio y estados que cubren
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

stations["ksix"] = set(["nm", "tx", "ok"])
stations["kseven"] = set(["ok", "ks", "co"])
stations["keight"] = set(["ks", "co", "ne"])
stations["knine"] = set(["ne", "sd", "wy"])
stations["kten"] = set(["nd", "ia"])
stations["keleven"] = set([ "mn", "mo", "ar"])
stations["ktwelve"] = set(["la"])
stations["kthirteen"] = set(["mo", "ar"])


def greedy_search_global(stations, needed_states):

    covered_states = set()
    stations_needed = []

    gradients = []
    num_states_covered = []

    while covered_states < needed_states:
        best_gradient = 0
        best_station = ""
        for station, station_states in stations.items():
            new_states = station_states - covered_states
            if len(new_states) > best_gradient:
                best_station = station
                best_gradient = len(new_states)
        if best_station:
            gradients.append(len(stations[best_station] - covered_states))
            covered_states = covered_states | (stations[best_station])
            num_states_covered.append(len(covered_states))
            stations_needed.append(best_station)
            stations.pop(best_station)

    print(f"covered: {covered_states}")
    print(f"stations: {stations_needed}")
    print(f"num states covered: {num_states_covered}")
    print(f"gradients: {gradients}")

    # Crear la visualización
    plt.figure(figsize=(10, 6))
    plt.bar(stations_needed, num_states_covered)
    plt.title('Mejora por estación en cada paso del algoritmo')
    plt.xlabel('Estaciones seleccionadas')
    plt.ylabel('Número de estados cubiertos')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def greedy_search_local(stations, needed_states):

    num_uncovered_states = []
    # stations_needed = []
    for _ in range(40):
        covered_states = set()
        stations_names = list(stations.keys())
        random_stations = random.sample(stations_names, k=10)
        for station in random_stations:
            covered_states = covered_states | (stations[station])
            # stations_needed.append(station)
        num_uncovered_states.append(len(needed_states - covered_states))

    # print(f"stations: {stations_needed}")
    print(f"num states uncovered: {num_uncovered_states}")

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(num_uncovered_states)), num_uncovered_states)
    plt.title('Mínimos locales')
    plt.xlabel('Iteracion')
    plt.ylabel('Número de estados sin cubrir')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    greedy_search_global(stations.copy(), needed_states)
    greedy_search_local(stations.copy(), needed_states)
