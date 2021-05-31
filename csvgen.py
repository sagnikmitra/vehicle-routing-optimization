latup = 11.6204374
lonup = 104.9125845
latdown = 11.621318
londown = 104.923603
lat = latdown - latup
lon = londown - lonup
print(lat, lon)
for i in range(0, 5000):
    print(f"{latdown+lat},{londown+lon},1")
    latdown += lat
    londown += lon
