from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

"""
Her skal dere bygge opp "demohuset" ved å bruke våres klasser
"""

#Register all of the information of the devices used in the house
test=DEMO_HOUSE.register_all_device()

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
# First floor devices
DEMO_HOUSE.register_device("Entrance",           "a2f8690f-2b3a-43cd-90b8-9deea98b42a7")
DEMO_HOUSE.register_device("Entrance",           "4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1")
DEMO_HOUSE.register_device("Guest Room 1",       "8d4e4c98-21a9-4d1e-bf18-523285ad90f6")
DEMO_HOUSE.register_device("Bathroom 1",         "3d87e5c0-8716-4b0b-9c67-087eaaed7b45")
DEMO_HOUSE.register_device("LivingRoom/Kitchen", "cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5")
DEMO_HOUSE.register_device("LivingRoom/Kitchen", "5e13cabc-5c58-4bb3-82a2-3039e4480a6d")
DEMO_HOUSE.register_device("LivingRoom/Kitchen", "8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e")
DEMO_HOUSE.register_device("Garage",             "4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1")

# Second floor devices
DEMO_HOUSE.register_device("Office",             "1a66c3d6-22b2-446e-bf5c-eb5b9d1a8c79")
DEMO_HOUSE.register_device("Bathroom 2",         "9e5b8274-4e77-4e4e-80d2-b40d648ea02a")
DEMO_HOUSE.register_device("Guest Room 2",       "6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28")
DEMO_HOUSE.register_device("Guest Room 3",       "7c6e35e1-2d8b-4d81-a586-5d01a03bb02c")
DEMO_HOUSE.register_device("Master Bedroom",     "4d8b1d62-7921-4917-9b70-bbd31f6e2e8e")
DEMO_HOUSE.register_device("Master Bedroom",     "c1e8fa9c-4b8d-487a-a1a5-2b148ee9d2d1")


listOffFloors = DEMO_HOUSE.get_floors()
totalArea = DEMO_HOUSE.get_area()
totalRooms = DEMO_HOUSE.get_rooms()

print(totalRooms)
print(totalArea)
print(listOffFloors)

"""print(DEMO_HOUSE.get_floors())
"""



# TODO: continue registering the remaining floor, rooms and devices

