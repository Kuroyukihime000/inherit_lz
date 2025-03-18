from inherit import Employee
from inherit import Manager

def main():
    first = Employee('Иван Иванович', 'Менеджер', 50000, 24)
    second = Manager('Иван Иванович', 'Менеджер', 50000, 24,'Отдел продаж', 50)
    first.info1()
    first.calc_salary1()
    second.info2()
    second.calc_salary2

if __name__ == '__main__': #проверяем на прямой запуск
    main() #запускаем функцию