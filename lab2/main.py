
from input_module import input_employees
from salary_module import calculate_month_salary, print_employees_recursive

def main():
    # 1. Введення даних
    employees = input_employees()

    # 2. Розрахунок зарплат
    print("\n=== Зарплата співробітників ===")
    for name, data in employees.items():
        total = calculate_month_salary(data)
        print(f"{name}: {total:.2f} грн")

    # 3. Рекурсивне виведення імен
    print("\n=== Список співробітників (рекурсивно) ===")
    print_employees_recursive(list(employees.keys()))

if __name__ == "__main__":
    main()
