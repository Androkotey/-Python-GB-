# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться
# после них.

rating = [7, 5, 3, 3, 2]

while True:
    new_rating = int(input('Введите элемент рейтинга (для выхода введите число < 0): '))
    if new_rating < 0:
        exit()
    rating.append(new_rating)
    rating.sort(reverse=True)
    print(f'Текущий рейтинг: {rating}')
