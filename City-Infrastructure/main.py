"""
1. City Infrastructure Management System
Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python 
to build a simulated City Infrastructure Management System. This system will incorporate classes, objects,
 methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

- Code Example: Provide a basic structure for the Vehicle class without methods.

    class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
- Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration script 
showing the creation of Vehicle objects and updating their owners.

"""
# The following methods (items that are more recording info driven) get pulled into the functions (things that are action oriented) to assist in making changes.
from vehicle import Vehicle
from menu_funcs import add_vehicle, update_vehicle_owner, display_vehicles


while True:

    choice = input("Please type your selection ('add', 'update', 'display' or 'exit') vehicle registration.\n").lower()
    if choice == "exit":
        print("Shutting down......")
        break
    try:
        if choice == 'add':
            reg_num = input("Please type the registration number:\n")
            car_type = input("What type of vehicle is it?\n")
            owner = input("What is the current owner's name?\n")
            add_vehicle(reg_num, car_type, owner)
            print(f"Vehicle with registration number {reg_num} added.")

        elif choice == "update":
            reg_num = input("Please enter the registration number of the vehicle you wish to update.\n")
            new_owner = input("Please provide the new owner's name:\n")
            update_vehicle_owner(reg_num, new_owner)

        elif choice == "display":
            print("\nHere are all registered vehicles:\n")
            display_vehicles()

        else:
            print("Incorrect selection, please try again.")
        

    except Exception as e:
        print(f"Error occurred: {e}")
       
