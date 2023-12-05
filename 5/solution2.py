#!/usr/bin/env python3

data = open(0).read().strip()
parts = data.split('\n\n')
seed_data = list(map(int, parts[0].split(':')[1].split()))
seed_ranges = []
for seed_start, run in list(zip(seed_data, seed_data[1:]))[::2]:
    seed_ranges.append((seed_start, run))
if not seed_ranges:
    print('no seeds')
    exit(1)

seed_to_soil_map = list(map(lambda x:list(map(int, x.split())), parts[1].splitlines()[1:]))
soil_to_fertilizer_map = list(map(lambda x:list(map(int, x.split())), parts[2].splitlines()[1:]))
fertilizer_to_water_map = list(map(lambda x:list(map(int, x.split())), parts[3].splitlines()[1:]))
water_to_light_map = list(map(lambda x:list(map(int, x.split())), parts[4].splitlines()[1:]))
light_to_temperature_map = list(map(lambda x:list(map(int, x.split())), parts[5].splitlines()[1:]))
temperature_to_humidity_map = list(map(lambda x:list(map(int, x.split())), parts[6].splitlines()[1:]))
humidity_to_location_map = list(map(lambda x:list(map(int, x.split())), parts[7].splitlines()[1:]))

reverse_map = {
    'soil': ('seed', seed_to_soil_map),
    'fertilizer': ('soil', soil_to_fertilizer_map),
    'water': ('fertilizer', fertilizer_to_water_map),
    'light': ('water', water_to_light_map),
    'temperature': ('light', light_to_temperature_map),
    'humidity': ('temperature', temperature_to_humidity_map),
    'location': ('humidity', humidity_to_location_map),
}

# literally brute force from lowest location upwards
# 30 mintes for 1.3e9, 2hours for 2<<31 (4.2e9)
# removed all function invocations and made range checks explicit for speed
# `type_ != 'seed'` check unnecessary, checking first two letters is enough (for speed)
# reuse loc variable to reduce variable declarations and garbage collections
for location in range(2 << 31):
    orig_location = location
    type_ = 'location'
    while type_[0] != 's' or type_[1] != 'e':
        type_, mapping = reverse_map[type_]
        for source, dest, run in mapping:
            if source <= location < source + run:
                i = location - source
                location = dest + i
                break
    seed = location
    for seed_start, run in seed_ranges:
        if seed_start <= seed < seed_start + run:
            print(orig_location)
            exit(0)
