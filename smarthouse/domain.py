
class Measurement:
    """
    This class represents a measurement taken from a sensor.
    Her skal vi legge inn våres klasser og utvide den eksisterende koden.
    Device_id - dato - klokkeslett - verdi - måleenhet
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit



# TODO: Add your own classes here!


class SmartHouse:

    def __init__(self):
        # Assuming this structure for storing room details
        self.rooms = []  # Each item could be a dict with keys like 'floor', 'room_size', 'room_name'
        self.deviceList = [] # list of devices.
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.        
        """
        self.level = level 
        print("Etasje Generert: ", level)       
        return level
    
    def register_all_device():
        """
        Here we will register all off the device information needed for the smarthouse in a dictonary
        """
        data = [
    {
        "Identifikator": "4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1",
        "Enhet": "Smart Lock",
        "Produsent": "MythicalTech",
        "Modellnavn": "Guardian Lock 7000"
    },
    {
        "Identifikator": "8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e",
        "Enhet": "CO2 sensor",
        "Produsent": "ElysianTech",
        "Modellnavn": "Smoke Warden 1000"
    },
    {
        "Identifikator": "a2f8690f-2b3a-43cd-90b8-9deea98b42a7",
        "Enhet": "Electricity Meter",
        "Produsent": "MysticEnergy Innovations",
        "Modellnavn": "Volt Watch Elite"
    },
    {
        "Identifikator": "5e13cabc-5c58-4bb3-82a2-3039e4480a6d",
        "Enhet": "Heat Pump",
        "Produsent": "ElysianTech",
        "Modellnavn": "Thermo Smart 6000"
    },
    {
        "Identifikator": "cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5",
        "Enhet": "Motion Sensor",
        "Produsent": "NebulaGuard Innovations",
        "Modellnavn": "MoveZ Detect 69"
    },
    {
        "Identifikator": "3d87e5c0-8716-4b0b-9c67-087eaaed7b45",
        "Enhet": "Humidity Sensor",
        "Produsent": "AetherCorp",
        "Modellnavn": "Aqua Alert 800"
    },
    
        ]
       
        

    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        self.rooms.append({'floor': floor, 'room_size': room_size, 'room_name': room_name})
        """self.floor = floor
        self.room_size = room_size
        self.room_name = room_name
        return floor, room_size, room_name
        print("Rom registrert: ", floor, room_size, room_name)
        """

    def get_floors(self):
        # Extracting the floor levels from each room
        floor_levels = [room['floor'] for room in self.rooms]
        # Removing duplicates by converting the list to a set, then back to a list
        unique_floor_levels = list(set(floor_levels))
        # Returning the sorted list of unique floor levels
        return sorted(unique_floor_levels)

        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        
        pass


    def get_rooms(self, floor = None):
        if floor is None:
            # Return all rooms if no floor is specified
            return self.rooms
        else:
            # Return only the rooms on the specified floor
            return [room for room in self.rooms if room['floor'] == floor]

        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        pass


    def get_area(self):
        total_area = sum(room['room_size'] for room in self.rooms)
        return total_area
        
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        self.room = room
        self.device = device
        

    
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        self.device_id = device_id
        pass

"""
class Bygning:
    def __init__(self, rooms) -> None:
        self.rooms = rooms
    
    def register_floor():        
        print("Floor register")
    
    

class Etasje:
    def __init__(self, number) -> None:
        self.number = number

    def register_room(floor, areal, name):        
        print("Room Registered")

class Device:
    
    def __init__(self, device_id, id, supplier, model_name , typeEnhet, huskeNavnEnhet, Sensor_Aktuator) -> None:
        self.device_id = device_id
        self.id = id
        self.supplier = supplier
        self.model_name  = model_name 
        self.typeEnhet = typeEnhet # String enten Aktuator/Sensor
        self.huskeNavnEnhet = huskeNavnEnhet
        self.Sensor_Aktuator = Sensor_Aktuator # Denne kan lett skifte navn seinare


    def is_actuator():      # Retunerer bool true visst device er aktuator    
        check = False

        if Device.Sensor_Aktuator == "Aktuator":
            check=True
            return check
        return check
        

    def is_sensor():        # Returnerer bool true visst device er sensor        
        check = False

        if Device.Sensor_Aktuator == "Sensor":
            check = True
            return check
        return check

    def get_device_type():  # Skal returnere string som svar med konkret ka type det er f.eks "heatPump", "smart Lock" osv
        svar = Device.typeEnhet
        return svar
    
    def turn_on():          # ingen vet ka som skjer her vertfall, Roar som har konstruert detta lørdagskveld. -Vegard
        if is_actuator() == True:
            Aktuator.turn_on()
    
     
    def last_measurement():
         #
        
        Skal returnere ett objekt av type Measurment.
        Målenheten i målingen skal samsvare med måleenheten av sensoren (f.eks. måler en temperaturmåler in enheten celsius: "°C"). 
        For verdien kan du velge en helt tilfeldig numerisk verdi (du kan f.eks. bruke random modulen) 
        og timestamp skal være en tekstuell representasjon av et tidspunkt (du kan f.eks. bruke ISO-8601).
        
        pass


    def last_measurement():
        return measurement
    


class Aktuator(Device): #Skal arve fra device
    def __init__(self, deviceState, setPunkt ) -> None:
        self.deviceState = deviceState  #DeviceState er string on/off
        self.setPunkt = setPunkt        #setpunkt er int 0-100

    def turn_on():
        deviceState = "On"
        
    def turn_off():
        DeviceState = "Off"
"""