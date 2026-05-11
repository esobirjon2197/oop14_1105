class Employee:
    company_name = "Google"
    work_time = "09:00 - 18:00"

    def __init__(self, fullname, salary, position, age):
        self.fullname = fullname
        self.salary = salary
        self.position = position
        self.age = age

    def show_employee(self):
        print(self.fullname, self.salary, self.position)

    def increase_salary(self, amount):
        self.salary += amount

    def change_position(self, new_position):
        self.position = new_position


e = Employee("Ali", 1000, "Junior", 25)
e.show_employee()

print("-----")

e.increase_salary(500)
e.change_position("Senior")

e.show_employee()
