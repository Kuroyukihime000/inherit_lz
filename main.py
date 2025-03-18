from inherit import Employee
from inherit import Manager

def main():
    first = Employee('Иван Иванович', 'Менеджер', 2,  50000)
    second = Manager('Иван Иванович', 'Менеджер', 2 , 50000,'Отдел продаж', 50)
    first.info1()
    first.calc_salary1()
    second.info2()
    second.calc_salary2()

if __name__ == '__main__': #проверяем на прямой запуск
    main() #запускаем функцию