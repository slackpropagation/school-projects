import csv
import datetime
from hash_table import HashTable
from package import Package
from truck import Truck

# --- Load CSV Data ---
def load_package_data(filename, table):
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            pID = int(row[0])
            package = Package(
                id=pID,
                address=row[1],
                city=row[2],
                state=row[3],
                zip_code=row[4],
                deadline=row[5],
                weight=row[6],
                status="At Hub"
            )
            # Force the initially wrong address for package 9
            if pID == 9:
                package.address = "300 State St"
                package.city = "Salt Lake City"
                package.state = "UT"
                package.zip_code = "84103"
            table.insert(pID, package)

# --- Distance and Address Helpers ---
with open("data/Distance_Table.csv") as f:
    distances = list(csv.reader(f))
with open("data/Address_File.csv") as f:
    addresses = list(csv.reader(f))

def get_distance(i, j):
    val = distances[i][j]
    return float(val) if val else float(distances[j][i])

def get_address_index(addr):
    for row in addresses:
        if addr in row[2]:
            return int(row[0])
    raise ValueError(f"Address not found: {addr}")

# --- Trucks Setup ---
truck1 = Truck(truck_id=1, speed=18,
               packages=[1,13,14,16,20,29,30,17,10,19,12,31,34,15,26,40],
               depart_time=datetime.timedelta(hours=8))

truck2 = Truck(truck_id=2, speed=18,
               packages=[3,6,18,22,21,24,23,27,33,35,28,36,38,11,25,37],
               depart_time=datetime.timedelta(hours=9, minutes=5))

truck3 = Truck(truck_id=3, speed=18,
               packages=[2,4,5,7,8,9,32,39],
               depart_time=datetime.timedelta(hours=10, minutes=20))

# --- Hash Table ---
hash_map = HashTable()
load_package_data("data/WGUPS Package File.csv", hash_map)

# --- Nearest Neighbor Algorithm ---
def deliver(truck):
    """Deliver all of a truck’s packages, routing by nearest neighbor."""
    # Grab the Package objects for this truck
    not_delivered = [hash_map.lookup(pid) for pid in truck.packages]
    truck.packages.clear()

    while not_delivered:
        # local helper: choose the “effective” address of pkg 9
        def eff_addr(p):
            if p.id == 9 and truck.time >= truck.depart_time:
                return "410 S State St"
            return p.address

        # find the nearest next package
        nearest = min(
            not_delivered,
            key=lambda p: get_distance(
                get_address_index(truck.location),
                get_address_index(eff_addr(p))
            )
        )
        # compute distance/time
        dist = get_distance(
            get_address_index(truck.location),
            get_address_index(eff_addr(nearest))
        )
        truck.mileage += dist
        truck.time += datetime.timedelta(hours=dist / truck.speed)
        # move to that address
        truck.location = eff_addr(nearest)
        # record delivery/departure times & truck assignment
        nearest.delivery_time = truck.time
        nearest.departure_time = truck.depart_time
        nearest.truck_id = truck.id
        truck.packages.append(nearest.id)
        not_delivered.remove(nearest)

# --- Deliver All Packages ---
deliver(truck1)
deliver(truck2)
# ensure truck3 only leaves once the earliest of truck1/truck2 returns
truck3.depart_time = min(truck1.time, truck2.time)
truck3.time = truck3.depart_time
deliver(truck3)

# --- CLI Interface ---
print("WGUPS ROUTING PROGRAM")
print(f"Total mileage: {round(truck1.mileage + truck2.mileage + truck3.mileage, 2)} miles")
print(f"Truck 1 mileage: {round(truck1.mileage, 1)} miles")
print(f"Truck 2 mileage: {round(truck2.mileage, 1)} miles")
print(f"Truck 3 mileage: {round(truck3.mileage, 1)} miles")

while True:
    cmd = input("Type 'time' to check status, 'mileage' to see truck mileages, or 'exit' to quit: ").strip().lower()

    if cmd == "time":
        try:
            h, m, s = map(int, input("Enter time (HH:MM:SS): ").split(":"))
            check_time = datetime.timedelta(hours=h, minutes=m, seconds=s)
        except:
            print("Invalid time format.")
            continue

        choice = input("Type 'all' for all packages or 'solo' for one package: ").strip().lower()
        if choice == "all":
            for pid in range(1, 41):
                pkg = hash_map.lookup(pid)
                pkg.update_status(check_time)
                print(pkg, f"Truck #: {getattr(pkg, 'truck_id', 'N/A')}")
        elif choice == "solo":
            try:
                pid = int(input("Enter package ID: "))
                pkg = hash_map.lookup(pid)
                pkg.update_status(check_time)
                print(pkg, f"Truck #: {getattr(pkg, 'truck_id', 'N/A')}")
            except:
                print("Invalid package ID.")
        else:
            print("Cancelled.")
    elif cmd == "mileage":
        print(f"Truck 1 mileage: {round(truck1.mileage, 1)} miles")
        print(f"Truck 2 mileage: {round(truck2.mileage, 1)} miles")
        print(f"Truck 3 mileage: {round(truck3.mileage, 1)} miles")
    elif cmd == "exit":
        break
    else:
        print("Invalid command.")
