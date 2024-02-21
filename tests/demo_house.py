from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

"""
Her skal dere bygge opp "demohuset" ved å bruke våres klasser
"""

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)
second_floor = DEMO_HOUSE.register_floor(2)
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
hall1     = DEMO_HOUSE.register_room(second_floor,22,"hall")
entrance1 = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
hall2     = DEMO_HOUSE.register_room(second_floor,22,"hall")
entrance2 = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
hall3     = DEMO_HOUSE.register_room(second_floor,22,"hall")
entrance3 = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
hall4     = DEMO_HOUSE.register_room(second_floor,22,"hall")
entrance4 = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
hall5     = DEMO_HOUSE.register_room(second_floor,22,"hall")
entrance5 = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
hall6     = DEMO_HOUSE.register_room(second_floor,22,"hall")

listOffFloors = DEMO_HOUSE.get_floors()

print(listOffFloors)

"""print(DEMO_HOUSE.get_floors())
"""



# TODO: continue registering the remaining floor, rooms and devices

