from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

"""
Her skal dere bygge opp "demohuset" ved å bruke våres klasser
"""

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
# TODO: continue registering the remaining floor, rooms and devices

