from vehicle import Vehicle

vehicles = {}

def add_vehicle(reg_num, car_type, owner):
    if reg_num in vehicles:
        print("This vehicle already exists.")
        return
    vehicles[reg_num] = Vehicle(reg_num, car_type, owner)

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Owner for vehicle registration {reg_num}, has been updated to {new_owner}")
    else:
        print("Vehicle not found.")


def display_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_info()