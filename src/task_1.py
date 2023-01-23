class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def print_details(self):
        return f"name: {self.name} \n age: {self.age}"



class Student(Person):
    def __init__(self,name, age, s_id, gpa):
        self.s_id= s_id
        self.gpa= gpa
        
        super(Student, self).__init__(name, age)

    def print_details(self):
        print("\n Student record: \n")
        print(super().print_details())
        print(f"ID:{self.s_id} \n gpa:{self.gpa}")
   


class Teacher(Person):
    def __init__(self, name, age, t_id, specialization):
        self.t_id= t_id
        self.specialization= specialization
        super(Teacher, self).__init__(name, age)

    def print_details(self):
        print("Teacher record: \n")
        print(super().print_details())
        print(f"ID:{self.t_id} \n spacialization:{self.specialization}")

