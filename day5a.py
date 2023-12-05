with open("input5.txt", 'r') as fp:
    data = fp.read()
    
lines = data.split("\n")
seeds = list(map(int, lines[0].strip("seeds :").split()))

print(seeds)

def get_map(map_data):
    out_map = {}
    lines = map_data.split("\n")
    name = lines[0]
    ranges = lines[1:]
    for r in ranges:
        destination_start, source_start, count = r.split()
        destination_start, source_start, count = int(destination_start), int(source_start), int(count)
        for i, j in zip(range(source_start, source_start+count), (range(destination_start, destination_start+count))):
            out_map[i] = j
        #print(destination_start, source_start, count)
    return out_map

all_maps = data.split("\n\n")

seed_to_soil = get_map(all_maps[1])
soil_to_fertilizer = get_map(all_maps[2])
fertilizer_to_water = get_map(all_maps[3])
water_to_light = get_map(all_maps[4])
light_to_temperature = get_map(all_maps[5])
temperature_to_humidity = get_map(all_maps[6])
humidity_to_location = get_map(all_maps[7])
print(humidity_to_location)

locations = []
for s in seeds:
    #location = humidity_to_location[temperature_to_humidity[light_to_temperature[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[s]]]]]]]
    #locations.append(location)
    a = seed_to_soil.get(s, s)
    b = soil_to_fertilizer.get(a, a)
    c = fertilizer_to_water.get(b, b)
    d = water_to_light.get(c, c)
    e = light_to_temperature.get(d, d)
    f = temperature_to_humidity.get(e, e)
    g = humidity_to_location.get(f, f)

    locations.append(g)

print(min(locations))