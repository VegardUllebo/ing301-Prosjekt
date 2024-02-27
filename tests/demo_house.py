from smarthouse.domain import SmartHouse
from smarthouse.domain import Device

DEMO_HOUSE = SmartHouse()

"""
Her skal dere bygge opp "demohuset" ved å bruke våres klasser
"""

#Register all of the information of the devices used in the house
"""test=DEMO_HOUSE.register_all_device()"""

# Building house structure
ground_floor   = DEMO_HOUSE.register_floor(1)
second_floor   = DEMO_HOUSE.register_floor(2)
entrance       = DEMO_HOUSE.register_room (1, 13.5, "Entrance")
guest_Room1    = DEMO_HOUSE.register_room (1, 8,    "Guest Room 1")
bathroom1      = DEMO_HOUSE.register_room (1, 6.3,  "Bathroom 1")
livingKitchen  = DEMO_HOUSE.register_room (1, 39.75,"LivingRoom/Kitchen")
Garage         = DEMO_HOUSE.register_room (1, 19,   "Garage")
hallway        = DEMO_HOUSE.register_room (2, 10,   "Hallway")
office         = DEMO_HOUSE.register_room (2, 11.75,"Office")
bathroom2      = DEMO_HOUSE.register_room (2, 9.25, "Bathroom 2")
guestroom2     = DEMO_HOUSE.register_room (2, 8,    "Guest Room 2")
guestroom3     = DEMO_HOUSE.register_room (2, 10,   "Guest Room 3")
dressingroom   = DEMO_HOUSE.register_room (2, 4,    "Dressing Room")
Master_bedroom = DEMO_HOUSE.register_room (2, 17,   "Master Bedroom")


# Register Devices
device_list = []
device_list.append(Device("4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1", "Smart Lock", "MythicalTech", "Guardian Lock 7000", "Sensor", "GodLåsen"))
device_list.append(Device("8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e", "CO2 sensor", "ElysianTech", "Smoke Warden 1000", "Sensor", "FiseSensor"))
device_list.append(Device("a2f8690f-2b3a-43cd-90b8-9deea98b42a7", "Electricity Meter", "MysticEnergy Innovations", "Volt Watch Elite", "Actuator", "w2242"))
device_list.append(Device("5e13cabc-5c58-4bb3-82a2-3039e4480a6d", "Heat Pump", "ElysianTech", "Thermo Smart 6000", "Actuator", "w2242"))
device_list.append(Device("cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5", "Motion Sensor", "NebulaGuard Innovations", "MoveZ Detect 69", "Actuator", "w2242"))
device_list.append(Device("3d87e5c0-8716-4b0b-9c67-087eaaed7b45", "Humidity Sensor", "AetherCorp", "Aqua Alert 800", "Actuator", "w2242"))
device_list.append(Device("8d4e4c98-21a9-4d1e-bf18-523285ad90f6", "Smart Oven", "AetherCorp", "Pheonix HEAT 333", "Actuator", "w2242"))
device_list.append(Device("9a54c1ec-0cb5-45a7-b20d-2a7349f1b132", "Automatic Garage Door", "MythicalTech", "Guardian Lock 9000", "Actuator", "w2242"))
device_list.append(Device("c1e8fa9c-4b8d-487a-a1a5-2b148ee9d2d1", "Smart Oven", "IgnisTech Solutions", "Ember Heat 3000", "Actuator", "w2242"))
device_list.append(Device("4d8b1d62-7921-4917-9b70-bbd31f6e2e8e", "Temperature Sensor", "AetherCorp", "	SmartTemp 42", "Actuator", "w2242"))
device_list.append(Device("7c6e35e1-2d8b-4d81-a586-5d01a03bb02c", "Air Quality Sensor", "CelestialSense Technologies", "AeroGuard Pro", "Actuator", "w2242"))
device_list.append(Device("1a66c3d6-22b2-446e-bf5c-eb5b9d1a8c79", "Smart Plug", "MysticEnergy Innovations", "FlowState X", "Actuator", "w2242"))
device_list.append(Device("9e5b8274-4e77-4e4e-80d2-b40d648ea02a", "Dehumidifier", "ArcaneTech Solutions", "	Hydra Dry 8000", "Actuator", "w2242"))
device_list.append(Device("6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28", "Light Bulp", "Elysian Tech", "Lumina Glow 4000", "Actuator", "w2242"))





# Building sensor structure
# First floor devices
DEMO_HOUSE.register_device("Entrance",           device_list[0].device_id)
DEMO_HOUSE.register_device("Entrance",           device_list[1].device_id)
DEMO_HOUSE.register_device("Guest Room 1",       device_list[2].device_id)
DEMO_HOUSE.register_device("Bathroom 1",         device_list[3].device_id)
DEMO_HOUSE.register_device("LivingRoom/Kitchen", device_list[4].device_id)
DEMO_HOUSE.register_device("LivingRoom/Kitchen", device_list[5].device_id)
DEMO_HOUSE.register_device("LivingRoom/Kitchen", device_list[6].device_id)
DEMO_HOUSE.register_device("Garage",             device_list[7].device_id)

# Second floor devices
DEMO_HOUSE.register_device("Office",             device_list[8].device_id)
DEMO_HOUSE.register_device("Bathroom 2",         device_list[9].device_id)
DEMO_HOUSE.register_device("Guest Room 2",       device_list[10].device_id)
DEMO_HOUSE.register_device("Guest Room 3",       device_list[11].device_id)
DEMO_HOUSE.register_device("Master Bedroom",     device_list[12].device_id)
DEMO_HOUSE.register_device("Master Bedroom",     device_list[13].device_id)



#listOffFloors = DEMO_HOUSE.get_floors()
totalArea = DEMO_HOUSE.get_area()
totalRooms = DEMO_HOUSE.get_rooms()

print(totalArea)

#print(listOffFloors[1].level)

# TODO: continue registering the remaining floor, rooms and devices

