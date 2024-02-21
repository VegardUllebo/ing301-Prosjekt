from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

"""
Her skal dere bygge opp "demohuset" ved å bruke våres klasser
"""

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)
second_floor = DEMO_HOUSE.register_floor(2)
entrance = DEMO_HOUSE.register_room(ground_floor, 145.55, "Entrance")
hall1     = DEMO_HOUSE.register_room(second_floor,1,"hall")
entrance1 = DEMO_HOUSE.register_room(ground_floor, 1, "Entrance")
hall2     = DEMO_HOUSE.register_room(second_floor,1,"hall")
entrance2 = DEMO_HOUSE.register_room(ground_floor, 1, "Entrance")
hall3     = DEMO_HOUSE.register_room(second_floor,1,"hall")
entrance3 = DEMO_HOUSE.register_room(ground_floor, 1, "Entrance")
hall4     = DEMO_HOUSE.register_room(second_floor,1,"hall")
entrance4 = DEMO_HOUSE.register_room(ground_floor, 1, "Entrance")
hall5     = DEMO_HOUSE.register_room(second_floor,1,"hall")
entrance5 = DEMO_HOUSE.register_room(ground_floor, 1, "Entrance")
hall6     = DEMO_HOUSE.register_room(second_floor,1,"hall")

listOffFloors = DEMO_HOUSE.get_floors()
totalArea = DEMO_HOUSE.get_area()
totalRooms = DEMO_HOUSE.get_rooms()

print(totalRooms)
print(totalArea)
print(listOffFloors)

"""print(DEMO_HOUSE.get_floors())
"""



# TODO: continue registering the remaining floor, rooms and devices

