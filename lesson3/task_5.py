"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

summa = 0
exit_symbol = False

while True:
    number_str = input('Enter numbers separated by space (special symbol # to stop): ')
    number_arr = number_str.split()
    for el in number_arr:
        try:
            number = float(el)
            summa += number
        except ValueError as ex:
            print(ex)
            print('It\'s not a number')
            if el == '#': 
                exit_symbol = True
                break

    if exit_symbol:
        break

print('Summa:', summa)
        
