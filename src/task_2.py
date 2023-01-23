class Vehicle:
    def __init__(self, reg_num, num_wheels, engine_power, model, make):
        self.reg_num= reg_num
        self.num_wheels= num_wheels
        self.engine_power= engine_power
        self.model= model
        self.make= make
        
    def print_details(self):
        return f"reg_num: {self.reg_num}\n num_wheels:{self.num_wheels}\n power: {self.engine_power}\n make:{self.make}\n model:{self.model}"

class Car(Vehicle):
    def __init__(self, reg_num, engine_power, make, model):
        
        super(Car, self).__init__(reg_num ,4 , engine_power, model, make)
        
    def print_details(self):
        print(super().print_details())

class Bike(Vehicle):
    def __init__(self, reg_num, engine_power, make, model):
        
        super(Bike, self).__init__(reg_num,2 , engine_power, model, make)
        

    def print_details(self):
        print(super().print_details())


