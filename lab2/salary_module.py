def calculate_month_salary(employee):
    """
    Розрахунок зарплати за формулою:
    Зарплата за місяць = (зарплата / 30) * відпрацьовані_дні
    """
    base_salary = employee["salary"]
    days = employee["days"]
    return (base_salary / 30) * days


def print_employees_recursive(employee_list, index=0):
    """Рекурсивне виведення імен співробітників"""
    if index < len(employee_list):
        print(employee_list[index])
        print_employees_recursive(employee_list, index + 1)
