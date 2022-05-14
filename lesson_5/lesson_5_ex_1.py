from collections import namedtuple

qty_company = int(input('Введите количество предприятий: '))
Company = namedtuple('Company', 'name profit_avg')
companies = []
total_profit = 0
for _ in range(qty_company):
    name = input(f'Введите название компании: ')
    profit = 0
    for j in range(4):
        profit += int(input(f'Введите прибыль в {j + 1} квартал: '))
    total_profit += profit
    companies.append(Company(name=name, profit_avg=(profit / 4)))

total_profit_avg = total_profit / (4 * qty_company)
print(f'Средняя прибыль по всем предприятиям: {total_profit_avg}', f'Прибыльные компании:', sep='\n')
for company in companies:
    if company.profit_avg > total_profit_avg:
        print(f'{company.name} со средней прибылью: {company.profit_avg}')

print(f'Убыточные компании:')
for company in companies:
    if company.profit_avg <= total_profit_avg:
        print(f'{company.name} со средней прибылью: {company.profit_avg}')



