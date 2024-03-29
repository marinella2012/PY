'''
Рита по поручению Тимофея наводит порядок в правильных скобочных
последовательностях (ПСП), состоящих только из круглых скобок (). Для этого ей
надо сгенерировать все ПСП длины 2n в алфавитном порядке —– алфавит состоит из
( и ) и открывающая скобка идёт раньше закрывающей.

Помогите Рите —– напишите программу, которая по заданному n выведет все ПСП в
нужном порядке.

Рассмотрим второй пример. Надо вывести ПСП из четырёх символов. Таких всего
две:

(())
()()
(()) идёт раньше ()(), так как первый символ у них одинаковый, а на второй
позиции у первой ПСП стоит (, который идёт раньше ).
Формат ввода
На вход функция принимает n — целое число от 0 до 10.

Формат вывода
Функция должна напечатать все возможные скобочные последовательности заданной
длины в алфавитном (лексикографическом) порядке.
'''


def get_brackets(n, prefix):
    if n == 0:
        print(prefix)
    else:
        if n > len(prefix):
            get_brackets(n - 1, prefix + '(')
        if len(prefix) == 0:
            return
        if prefix.count(')') == 0 and n > len(prefix):
            get_brackets(n - 1, prefix + ')')
        if prefix.count('(') < n:
            get_brackets(n - 1, prefix + '(')
        if prefix.count('(') == prefix.count(')'):
            get_brackets(n - 1, prefix + '(')
        if prefix.count('(') > prefix.count(')'):
            get_brackets(n - 1, prefix + ')')


if __name__ == '__main__':
    n = int(input())
    get_brackets(n * 2, '')


'''
Ввод:
3

Вывод:
((()))
(()())
(())()
()(())
()()()
'''
