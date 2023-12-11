class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def debug(self):
        print(f"({self.x}, {self.y})")


class Person:
    def __init__(self, ID, name, location):
        self.ID = ID
        self.name = name
        self.location = location


class Employee(Person):
    def __init__(self, emp_id, job_title, per):
        super().__init__(per.ID, per.name, per.location)
        self.emp_id = emp_id
        self.job_title = job_title


vu = Person("12345", "Nguyen Chiem Minh Vu", Point(0, 0))
emp = Employee("1", "Programmer", vu)
print(f"{emp.emp_id}, {emp.job_title}, {emp.name}")