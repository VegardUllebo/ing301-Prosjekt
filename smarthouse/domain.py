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
        pass
        

    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """

        pass


    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        pass


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        pass


    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        pass

    
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        pass

class Bygning:
    pass

class Etasje:
    pass

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
        check = false

        if Sensor_Aktuator == "Aktuator":
            check=true
            return check
        return check
        

    def is_sensor():        # Returnerer bool true visst device er sensor        
        check = false

        if Sensor_Aktuator == "Sensor":
            check = true
            return check
        return check

    def get_device_type():  # Skal returnere string som svar med konkret ka type det er f.eks "heatPump", "smart Lock" osv
        svar = typeEnhet
        return svar

    def last_measurement():
         #
        """
        Skal returnere ett objekt av type Measurment.
        Målenheten i målingen skal samsvare med måleenheten av sensoren (f.eks. måler en temperaturmåler in enheten celsius: "°C"). 
        For verdien kan du velge en helt tilfeldig numerisk verdi (du kan f.eks. bruke random modulen) 
        og timestamp skal være en tekstuell representasjon av et tidspunkt (du kan f.eks. bruke ISO-8601).
        """ 
        pass






    def last_measurement():
        return measurement
    

    