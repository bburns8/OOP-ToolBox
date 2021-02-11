# composition lets you use methods and attributes from a parent class in a child class
# composition takes what you need where inheritance takes everything
# create your base or parent classes with attributes that your child will use
class AnnualSalary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

# instance method of our annual salary equation
    def annual_salary(self):
        return (self.pay * 12) + self.bonus


# base class hourly salary with attributes for hourly salary
class HourlySalary:
    def __init__(self, hours, hourly_pay):
        self.hours = hours
        self.hourly_pay = hourly_pay

# instance method of our hourly salary equation
    def hourly_salary(self):
        return self.hours * self.hourly_pay


# salary child class using pay and bonus derived from AnnualSalary
# added new attributes name and age for SalaryEmployee
class SalaryEmployee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = AnnualSalary(pay, bonus)  # create object which uses the AnnualSalary class and it's objects

    # create instance method and call the annual salary method from Salary class
    def total_salary(self):
        return self.obj_salary.annual_salary()


# hourly child class using hours and hourly_pay derived from HourlySalary
# added new attributes name and age for HourlyEmployee
class HourlyEmployee:
    def __init__(self, name, age, hours, hourly_pay):
        self.name = name
        self.age = age
        self.obj_hourly = HourlySalary(hours, hourly_pay)

    # instance method which calls the hourly_salary method from HourlySalary class
    def hourly_salary(self):
        return self.obj_hourly.hourly_salary()


# create var with classes parameters that you wish to pass through certain salary methods
emp = SalaryEmployee('Blake', 21, 15000, 10000)  # AnnualSalary employee
print(emp.total_salary())
emp = HourlyEmployee('Steve', 25, 40, 20)  # HourlySalary employee
print(emp.hourly_salary())
