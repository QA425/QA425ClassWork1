def get_total_with_tax(value, tax_percentage):
    total = value + value * tax_percentage / 100
    return total


print(f'Сумма с налогом: {get_total_with_tax(10000, 13)}')

salary = 60000
income_tax = 13
print(f'Сумма с налогом: {get_total_with_tax(salary, income_tax)}')
print(f'Сумма с налогом: {get_total_with_tax(value=salary, tax_percentage=income_tax)}')

