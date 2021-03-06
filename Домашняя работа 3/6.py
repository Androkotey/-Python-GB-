# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


# Вариант 1
def int_func_1(word):
    assert word.isascii() and word[0].islower()
    return word.title()


print(int_func_1('winter'))


# Вариант 2
def int_func_2(word):
    assert word.isascii() and word[0].islower()
    return chr(ord(word[0]) - 32) + word[1:]


print(int_func_2('winter'))

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def capitalizer(string):
    """Принимает строку из слов, разделённых пробелом.
    Выводит в консоль строку, в которой каждое слово начинается с заглавной буквы"""

    string = string.split()

    for i in range(len(string)):
        string[i] = int_func_2(string[i])

    print(' '.join(string))


capitalizer('aaa bbb ccc ddd qqq www')
