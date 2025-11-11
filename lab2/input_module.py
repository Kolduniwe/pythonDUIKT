def input_employees():
    employees = {}
    n = int(input("Скільки співробітників ви хочете додати? "))

    for i in range(n):
        name = input(f"\nВведіть ім'я співробітника №{i+1}: ")
        salary = float(input("Введіть місячну заробітну плату (грн): "))
        days = int(input("Введіть кількість відпрацьованих днів: "))

        employees[name] = {
            "salary": salary,
            "days": days
        }

    return employees
