#!/usr/bin/env python3

data = open(0).read().strip()
parts = data.split('\n\n')
seeds = list(map(int, parts[0].split(':')[1].split()))
if not seeds:
    print('no seeds')
    exit(1)

seed_to_soil_map = list(map(lambda x:list(map(int, x.split())), parts[1].splitlines()[1:]))
soil_to_fertilizer_map = list(map(lambda x:list(map(int, x.split())), parts[2].splitlines()[1:]))
fertilizer_to_water_map = list(map(lambda x:list(map(int, x.split())), parts[3].splitlines()[1:]))
water_to_light_map = list(map(lambda x:list(map(int, x.split())), parts[4].splitlines()[1:]))
light_to_temperature_map = list(map(lambda x:list(map(int, x.split())), parts[5].splitlines()[1:]))
temperature_to_humidity_map = list(map(lambda x:list(map(int, x.split())), parts[6].splitlines()[1:]))
humidity_to_location_map = list(map(lambda x:list(map(int, x.split())), parts[7].splitlines()[1:]))

maps = {
    'seed': ('soil', seed_to_soil_map),
    'soil': ('fertilizer', soil_to_fertilizer_map),
    'fertilizer': ('water', fertilizer_to_water_map),
    'water': ('light', water_to_light_map),
    'light': ('temperature', light_to_temperature_map),
    'temperature': ('humidity', temperature_to_humidity_map),
    'humidity': ('location', humidity_to_location_map),
}

def apply_mapping(value, mapping):
    for dest, source, run in mapping:
        if value in range(source, source + run):
            i = value - source
            return dest + i
    return value

def get_loc(type_, value, maps):
    while type_ != 'location':
        type_, mapping = maps[type_]
        value = apply_mapping(value, mapping)
    return value

min_loc = float('inf')
min_seed = seeds[0]
for seed in seeds:
    loc = get_loc('seed', seed, maps)
    if loc < min_loc:
        min_loc = loc
        min_seed = seed

print(min_loc)
