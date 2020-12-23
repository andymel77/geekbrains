# 1. Поработайте с переменными, создайте несколько, выведите на экран, 
# запросите у пользователя несколько чисел и строк и сохраните в переменные, 
# выведите на экран.

a = 1
b = 2
c = 4
print (a, b, c)

for i in range(0, 1):
    try:
        newA = int(input("Input int " + str(i+1) + ": "))
    except ValueError:
        print("Not an integer!")
    else:
        print('Your int:', newA)

    anyString = input("Input any string: ")
    print('Your string:', anyString)

# 2. Пользователь вводит время в секундах. Переведите время в часы, 
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
# from datetime import datetime

try:
    secs = int(input("Input date at secs: "))
    hours = secs // 3600
    minutes = (secs // 60) % 60
    seconds = secs % 60
    
    if hours < 10:
        strHours = "0" + str(hours)
    else:
        strHours = str(hours)

    if minutes < 10:
        strMinutes = "0" + str(minutes)
    else:
        strMinutes = str(minutes)

    if seconds < 10:
        strSeconds = "0" + str(seconds)
    else:
        strSeconds = str(seconds)
    
    strTime = strHours + ":" + strMinutes + ":" + strSeconds
except ValueError:
    print("Not a time in secs!")
else:
    print('Your formated time:', strTime)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

try:
    num = int(input("Input int: "))
    summa = num + int(str(num) + str(num)) + int(str(num) + str(num) + str(num))

except ValueError:
    print("Not an integer!")
else:
    print('Your int:', summa)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции

try:
    num = int(input("Input int: "))
    numString = str(num)

    lenNumString = len(numString)

    arrNum = [char for char in numString]

    maxNum = 0
    i = 0
    while i < lenNumString:
        if int(arrNum[i]) > maxNum:
            maxNum = int(arrNum[i])
        i = i + 1

except ValueError:
    print("Not an integer!")
else:
    print('Your max num:', maxNum)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, 
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, 
# или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если 
# фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли 
# к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы 
# в расчете на одного сотрудника.

try:
    proceeds = float(input("Input proceeds: "))
    costs = float(input("Input costs: "))

    if proceeds > costs:
        print('Profit')
        profit = proceeds - costs
        profitability = ((proceeds - costs)/proceeds)*100
        print('Profitability:', profitability)
        try:
            numEployees = float(input("Input number of employees: "))
            print('Profit per employee:', profit/numEployees)
        except ValueError:
            print("Not an integer!")
    
    elif proceeds < costs:
        print('Lesion')
    else:
        print('Breakeven point')
except ValueError:
    print("Not an float!")

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить 
# номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна 
# принимать значения параметров a и b и выводить одно натуральное число — номер дня.

day = 0

a = 2
b = 3
result = a

while True:
    if result >= b:
        print("на " + str(day+1) + "-й день спортсмен достиг результата — не менее 3 км.")
        break
    result = result * 1.1
    day = day + 1
    
