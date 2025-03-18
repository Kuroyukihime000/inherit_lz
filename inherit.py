#Created by Kuroyukihime000

class Employee:
    emp_count = 0
    def __init__(self, name, position, procent_position, salary, worked_days):
        self.name = name
        self.position = position
        self.salary = salary
        self.worked_days = worked_days
        self.procent_position = procent_position

    def info1(self):
        print (f"Имя: {self.name}, Должность: {self.position}, Оклад: {self.salary}")

    def calc_salary1(self):
        self.salary_all = self.procent_position*self.salary*self.worked_days
        print(f" Зарплата = {self.salary_all}")

    
class Manager(Employee):
    def __init__(self, name, position, procent_position, salary, worked_days, department, num_employees):
        super().__init__(name, position, procent_position, salary, worked_days)
        self.department = department 
        self.num_employees = num_employees

    def info2(self):
        print(f"Имя: {self.name}, Должность: {self.position}, Оклад: {self.salary}, department : {self.department}, Кол-во работников : {self.num_employees}")
    
    def calc_salary2(self):
        self.calc_salary0 = self.procent_position*self.salary*self.worked_days + self.procent_position*self.salary*self.worked_days*(1/self.num_employees)
        print(f"Зарплата : {self.calc_salary0}")
        




