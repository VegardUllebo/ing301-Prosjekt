from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

"""
Her skal dere bygge opp "demohuset" ved å bruke våres klasser
"""

#Register all of the information of the devices used in the house
DEMO_HOUSE.register_all_device()

# Building house structure
ground_floor   = DEMO_HOUSE.register_floor(1)
second_floor   = DEMO_HOUSE.register_floor(2)
entrance       = DEMO_HOUSE.register_room (ground_floor, 13.5, "Entrance")
guest_Room1    = DEMO_HOUSE.register_room (ground_floor, 8,    "Guest Room 1")
bathroom1      = DEMO_HOUSE.register_room (ground_floor, 6.3,  "Bathroom 1")
livingKitchen  = DEMO_HOUSE.register_room (ground_floor, 39.75,"LivingRoom/Kitchen")
Garage         = DEMO_HOUSE.register_room (ground_floor, 19,   "Garage")
hallway        = DEMO_HOUSE.register_room (second_floor, 10,   "Hallway")
office         = DEMO_HOUSE.register_room (second_floor, 11.75,"Office")
bathroom2      = DEMO_HOUSE.register_room (second_floor, 9.25, "Bathroom 2")
guestroom2     = DEMO_HOUSE.register_room (second_floor, 8,    "Guest Room 2")
guestroom3     = DEMO_HOUSE.register_room (second_floor, 10,   "Guest Room 3")
dressingroom   = DEMO_HOUSE.register_room (second_floor, 4,    "Dressing Room")
Master_bedroom = DEMO_HOUSE.register_room (second_floor, 17,   "Master Bedroom")

# Building sensor structure

DEMO_HOUSE.register_device(livingKitchen, )

listOffFloors = DEMO_HOUSE.get_floors()
totalArea = DEMO_HOUSE.get_area()
totalRooms = DEMO_HOUSE.get_rooms()

print(totalRooms)
print(totalArea)
print(listOffFloors)

"""print(DEMO_HOUSE.get_floors())
"""



# TODO: continue registering the remaining floor, rooms and devices

