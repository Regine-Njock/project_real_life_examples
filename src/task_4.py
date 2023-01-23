class Employee:
    def __init__ (self, name, emp_id):
        self.name= name
        self.emp_id= emp_id
        self.salary= 0

    def get_salary(self):
        return self.salary

    def print_details(self):
        return f"name: { self.name}\tId: {self.emp_id}\tsalary: {self.salary}"

class Manager(Employee):
    def __init__ (self, name, emp_id, base_salary, team_size, bonus):
        self.base_salary= base_salary
        self.team_size= team_size
        self.bonus= bonus
        super().__init__(name, emp_id)
        
    def calc_salary(self):
        self.salary = (self.team_size * self.bonus) + self.base_salary


    def print_details(self):
        #print(super().print_details())
        print(f"{super().print_details()} base: {self.base_salary}\tteam_s: {self.team_size}\tbonus: {self.bonus}")
class Clerk(Employee):
    def __init__ (self, name, emp_id, hourly_wage, num_hours):
        self.hourly_wage= hourly_wage
        self.num_hours= num_hours
        super().__init__(name, emp_id)
        

    def calc_salary(self):
        self.salary = self.hourly_wage * self.num_hours

    def print_details(self):
        print(super().print_details())
        print(f"wage: {self.hourly_wage}\thours: {self.num_hours}")
