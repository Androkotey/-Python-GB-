# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))

profit = (revenue - costs) / revenue
if profit < 0:
    print('Фирма убыточна!')
else:
    print('Фирма прибыльна!')
    print(f'Рентабельность выручки: {profit:.2f}')

num_employees = int(input('Введите количество сотрудиков: '))
print(f'На одного сотрудника приходится {revenue / num_employees:.2f} от прибыли фирмы')
