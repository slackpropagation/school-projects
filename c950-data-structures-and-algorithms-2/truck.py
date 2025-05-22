# Truck class for managing delivery truck properties and operations
# Part of the WGUPS Routing Program
import datetime

class Truck:
    """
    Represents a delivery truck that transports packages in the system.
    Tracks speed, packages, capacity, location, departure time, and mileage.
    """

    def __init__(self, speed, packages, start_address="4001 South 700 East", depart_time=None, truck_id=None):
        """
        Initializes a Truck object with speed, assigned packages, starting location,
        departure time, and truck ID. Defaults to starting at the hub at 8:00 AM if no time provided.

        Args:
        - speed (int): Truck speed in miles per hour
        - packages (list): List of package IDs
        - start_address (str): Truck starting location
        - depart_time (datetime.timedelta): Truck departure time
        - truck_id (int): Unique truck identifier
        """
        self.id = truck_id  # Truck ID (1, 2, or 3)
        self.speed = speed  # miles per hour
        self.packages = packages  # list of package IDs
        self.capacity = 16  # fixed per scenario
        self.location = start_address
        self.depart_time = depart_time
        self.time = depart_time if depart_time else datetime.timedelta(hours=8)
        self.mileage = 0.0

    def __str__(self):
        """
        Returns a string summarizing the truck's current status including packages,
        mileage, location, and departure time.
        """
        return (
            f"Truck ID: {self.id} | Packages: {self.packages} | Mileage: {self.mileage:.2f} miles | "
            f"Location: {self.location} | Departed: {self.depart_time}"
        )
