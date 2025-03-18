#Created by Kuroyukihime000

class Employee:
    emp_count = 0
    def __init__(self, name, position, salary, worked_days):
        self.name = name
        self.position = position
        self.salary = salary
        self.worked_days = worked_days

    def info1(self):
        print (f"Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}")

    def calc_salary1(self):
        self.salary_all = self.position*self.salary*self.worked_days
        print(f" salary = {self.salary_all}")

    
class Manager(Employee):
    def __init__(self, name, position, salary, worked_days, department, num_employees):
        super().__init__(name, position, salary, worked_days)
        self.department = department 
        self.num_employees = num_employees

    def info2(self):
        super().info1()
        print(f"Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}, department : {self.department}, Кол-во работников : {self.num_employees}")
    
    def calc_salary2(self):
        super().calc_salary()
        self.calc_salary0 = self.position*self.salary*self.worked_days + self.position*self.salary*self.worked_days*
        print(f"Зарплата : {self.calc_salary0}")
        




