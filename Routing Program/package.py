# package.py
# Defines the Package class for managing package delivery information, statuses, and updates.

import datetime

class Package:
    """Represents a delivery package with attributes for tracking its delivery status and times."""

    def __init__(self, id, address, city, state, zip_code, deadline, weight, status):
        """
        Initializes a new Package object.

        Parameters:
        - id: Unique package ID
        - address: Delivery address
        - city: City for delivery
        - state: State for delivery
        - zip_code: ZIP code for delivery
        - deadline: Delivery deadline time
        - weight: Package weight
        - status: Current delivery status
        """
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        self.truck_id = None

        # Handle delayed packages
        if self.id in [6, 25, 28, 32]:
            self.arrival_time = datetime.timedelta(hours=9, minutes=5)
        else:
            self.arrival_time = datetime.timedelta(hours=8)  # Default hub arrival ti

    def update_status(self, current_time):
        """
        Updates the package status based on the given current time.
        Special cases: Package 9 address correction and delayed packages.
        """
        # Special case: Fix Package 9's wrong address at or after 10:20 AM
        if self.id == 9 and current_time >= datetime.timedelta(hours=10, minutes=20):
            self.address = "410 S State St"
            self.city = "Salt Lake City"
            self.state = "UT"
            self.zip_code = "84111"

        # New logic explicitly handling delayed arrival
        if current_time < self.arrival_time:
            self.status = f"Delayed on flight—will arrive at depot at {self.arrival_time}"
        elif self.delivery_time and current_time >= self.delivery_time:
            self.status = f"Delivered at {self.delivery_time}"
        elif self.departure_time and current_time >= self.departure_time:
            self.status = f"En route (Left at {self.departure_time})"
        else:
            self.status = "At Hub"

    def __str__(self):
        """
        Returns a formatted string representation of the package and its status.
        """
        return (
            f"Package ID: {self.id} | "
            f"Address: {self.address}, {self.city}, {self.state} {self.zip_code} | "
            f"Deadline: {self.deadline} | "
            f"Weight: {self.weight} | "
            f"Status: {self.status}"
        )