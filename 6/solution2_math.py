#!/usr/bin/env python3

# Time:        55     99     97     93
# Distance:   401   1485   2274   1405

time=55999793
current_record_distance=401148522741405

# f = distance raced
f = lambda charging_time: charging_time * (time - charging_time)

# condition
# f(charging_time) > current_record_distance

# charging_time * (time - charging_time) - current_record_distance > 0
# charging_time * time - charging_time * charging_time - current_record_distance = 0
# - charging_time * charging_time + charging_time * time - current_record_distance = 0
# charging_time * charging_time - charging_time * time + current_record_distance = 0

import math
charging_time_1 = time/2 - ((time/2)**2 - current_record_distance)**.5
charging_time_2 = time/2 + ((time/2)**2 - current_record_distance)**.5

print(charging_time_1)
print(charging_time_2)
print(math.floor(charging_time_2) - math.ceil(charging_time_1) + 1)
