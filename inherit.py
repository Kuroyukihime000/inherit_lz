import datetime

def worked_days(year, month):
    first_day = datetime.date(year, month, 1)
    if month == 12:
        last_day = datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        last_day = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

    worked_days_count = 0

    for day in range((last_day - first_day).days + 1):
        current_day = first_day + datetime.timedelta(days=day)
        if current_day.weekday() < 5:
            worked_days_count += 1

    return worked_days_count

current_date = datetime.datetime.now()

month = current_date.month
year = current_date.year

class Employee:
    emp_count = 0
    def __init__(self, name, position, procent_position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        self.worked_days = worked_days(year, month)  # Вызываем функцию с текущими значениями
        self.procent_position = procent_position

    def info1(self):
        print(f"Имя: {self.name}, Должность: {self.position}, Оклад: {self.salary}")

    def calc_salary1(self):
        self.salary_all = self.procent_position * self.salary * self.worked_days
        print(f"Зарплата = {self.salary_all}")

class Manager(Employee):
    def __init__(self, name, position, procent_position, salary, department, num_employees):
        super().__init__(name, position, procent_position, salary)
        self.department = department 
        self.num_employees = num_employees

    def info2(self):
        print(f"Имя: {self.name}, Должность: {self.position}, Оклад: {self.salary}, Отдел: {self.department}, Кол-во работников: {self.num_employees}")

    def calc_salary2(self):
        self.calc_salary0 = (self.procent_position * self.salary * self.worked_days + 
                              self.procent_position * self.salary * self.worked_days * (1 / self.num_employees))
        print(f"Зарплата: {self.calc_salary0}")