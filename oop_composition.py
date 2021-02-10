# composition lets you use methods and attributes from a parent class in a child class
# composition takes what you need where inheritance takes everything

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)  # create object which uses the Salary class and it's objects

    # create instance method and call the annual salary method from Salary class
    def total_salary(self):
        return self.obj_salary.annual_salary()


# create var with classes parameters that you wish to pass through certain salary class methods
emp = Employee('Blake', 21, 15000, 10000)
print(emp.total_salary())
