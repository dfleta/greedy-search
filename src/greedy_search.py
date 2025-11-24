import random

# estados USA donde queremos ser escuchados
needed_states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
added_states = set(
    ["nm", "tx", "ok", "ks", "co", "ne", "sd", "wy", "nd", "ia", "mn", "mo", "ar", "la"]
)

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
stations["keleven"] = set(["mn", "mo", "ar"])
stations["ktwelve"] = set(["la"])
stations["kthirteen"] = set(["mo", "ar"])


def find_best_station(stations, covered_states):
    best_station = ""
    best_gradient = 0
    for station, station_states in stations.items():
        new_states = station_states - covered_states
        if len(new_states) > best_gradient:
            best_station = station
            best_gradient = len(new_states)
    return best_station, best_gradient


def greedy_search_global(stations, needed_states):
    stations_remaining = stations.copy()
    covered_states = set()
    stations_needed = []

    gradients = []
    num_states_covered = []

    while covered_states < needed_states:
        best_station, best_gradient = find_best_station(
            stations_remaining, covered_states
        )

        if best_station:
            gradients.append(best_gradient)
            covered_states |= stations_remaining[best_station]
            num_states_covered.append(len(covered_states))
            stations_needed.append(best_station)
            del stations_remaining[best_station]

    return (stations_needed, num_states_covered, gradients, covered_states)


def greedy_search_local(stations, needed_states):
    NUM_SEARCHES = 40
    MAX_NUM_STATIONS = 10
    num_uncovered_states = []
    # stations_needed = []
    for _ in range(NUM_SEARCHES):
        covered_states = set()
        stations_names = list(stations.keys())
        random_stations = random.sample(stations_names, k=MAX_NUM_STATIONS)
        for station in random_stations:
            covered_states = covered_states | (stations[station])
            # stations_needed.append(station)
        num_uncovered_states.append(len(needed_states - covered_states))
    return num_uncovered_states
