class Vehicle:

    def __init__(self, reg_num, car_type, owner):
        self.reg_num = reg_num
        self.car_type = car_type
        self.owner = owner


    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_info(self):
        print(f"Registration Number: {self.reg_num}, Make of Vehicle: {self.car_type}, Current Owner: {self.owner}")