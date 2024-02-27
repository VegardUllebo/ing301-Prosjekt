
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


class Room:
    """
    Room er et rom i huset. Har areal og navn. Her kan en og registrere devices
    """
    def __init__(self, room_size, room_name) -> None:
        self.room_size = room_size
        self.room_name = room_name
        

        
    

class Floor:
    def __init__(self, level) -> None:
        self.level = level
        self.rooms = []        #opretter liste for room i hver etasje

    def add_room(self, room: Room):
        self.rooms.append(room)

class Device:
    
    def __init__(self, device_id, device, manifactor, modell_name, typeOfDevice, rememberNameDevice) -> None:
        self.device_id = device_id
        self.device = device
        self.manifactor = manifactor
        self.modell_name = modell_name
        self.typeOfDevice = typeOfDevice # String enten Aktuator/Sensor
        self.rememberNameDevice = rememberNameDevice

class SmartHouse:

    def __init__(self):
        # Assuming this structure for storing room details
        # Each item could be a dict with keys like 'floor', 'room_size', 'room_name'
        self.deviceList = []    #Liste over devices
        self.floors = []        #Oppretter liste for etasjer i hvert hus
        self.allRooms = []
        
        
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
        new_floor = Floor(self.level)
        self.floors.append(new_floor)
        print("Etasje Generert: ", new_floor) 
        
              
        return new_floor
        

    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        ikkje brukt - self.rooms.append({'floor': floor, 'room_size': room_size, 'room_name': room_name})
        """
        new_room = Room(room_size, room_name)         #Opretter Room
        self.floors[floor-1].add_room(new_room)       # legger til i floors liste
        #Floor.rooms.append(new_room)                 #legger til i rooms liste
        self.allRooms.append(new_room)                #lager liste over alle rom

        return new_room                               #Returnera objektet
       

    def get_floors(self):
        """
        # Extracting the floor levels from each room
        floor_levels = [room['floor'] for room in self.rooms]
        # Removing duplicates by converting the list to a set, then back to a list
        unique_floor_levels = list(set(floor_levels))
        # Returning the sorted list of unique floor levels
        return sorted(unique_floor_levels)

        
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        
        return self.floors
        


    def get_rooms(self, floor = None):
        """
        if floor is None:
            # Return all rooms if no floor is specified
            return self.rooms
        else:
            # Return only the rooms on the specified floor
            return [room for room in self.rooms if room['floor'] == floor]
        
        
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        
        """
           
                
        
        return self.allRooms


    def get_area(self):
        """
        total_area = sum(room['room_size'] for room in self.rooms)
        return total_area
        
        
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """
        totalAreal=0.0
        for areal in self.allRooms:
            totalAreal = areal.room_size + totalAreal
        
        return totalAreal


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        self.room = room
        self.device = device
        self.deviceList.append({'room': room , 'device': device})
        

    
    def get_devices(self, device_id = None):
        """
        This method retrieves a device object via its id.
        """
        if device_id is None:
            # Return all rooms if no floor is specified
            return self.deviceList
        else:
            # Return only the rooms on the specified floor
            return [device for device  in self.deviceList if device['device'] == device]





        
"""
class Bygning:
    def __init__(self, rooms) -> None:
        self.rooms = rooms
    
    def register_floor():        
        print("Floor register")
"""



"""    def is_actuator():      # Retunerer bool true visst device er aktuator    
        check = False

        if Device.typeOfDevice == "Aktuator":
            check=True
            return check
        return check
        

    def is_sensor():        # Returnerer bool true visst device er sensor        
        check = False

        if Device.typeOfDevice == "Sensor":
            check = True
            return check
        return check

    def get_device_type():  # Skal returnere string som svar med konkret ka type det er f.eks "heatPump", "smart Lock" osv
        svar = Device.device
        return svar"""
    
"""    def turn_on():          # ingen vet ka som skjer her vertfall, Roar som har konstruert detta lørdagskveld. -Vegard
        if is_actuator() == True:
            Aktuator.turn_on()"""
    
     
"""    def last_measurement():
         #
        
        Skal returnere ett objekt av type Measurment.
        Målenheten i målingen skal samsvare med måleenheten av sensoren (f.eks. måler en temperaturmåler in enheten celsius: "°C"). 
        For verdien kan du velge en helt tilfeldig numerisk verdi (du kan f.eks. bruke random modulen) 
        og timestamp skal være en tekstuell representasjon av et tidspunkt (du kan f.eks. bruke ISO-8601).
        
        pass


    def last_measurement():
        return measurement"""
    


class Aktuator(Device): #Skal arve fra device
    def __init__(self, deviceState, setPunkt ) -> None:
        self.deviceState = deviceState  #DeviceState er string on/off
        self.setPunkt = setPunkt        #setpunkt er int 0-100

    def turn_on():
        deviceState = "On"
        
    def turn_off():
        DeviceState = "Off"
