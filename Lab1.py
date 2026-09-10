import math

# Завдання 1

def task_1():
    x = float(input("Введіть невід'ємне значення х: "))
    while x < 0:
        print("Значення х повинно бути невід'ємним.")
        x = float(input("Введіть значення х: "))

    z = 2 + math.sqrt(x) 

    print("Результат обчислення z:", z)

# Завдання 2

def task_2():
    number = int(input("Введіть ціле число: "))

    max_digit = 0
    position = 1
    max_digit_position = 1
    while number != 0:
        digit = number % 10
        if digit > max_digit:
            max_digit = digit
            max_digit_position = position
        number //= 10
        position += 1
    position_from_left =  position - max_digit_position

    print("Найбільша цифра:", max_digit)
    print("Позиція найбільшої цифри зліва:", position_from_left)
       

# Завдання 3

def task_3():

#Частина 1
    n = int(input("Введіть значення n: "))

    numbers = [int(input(f"Введіть ціле число {i + 1}: ")) for i in range(n)]

    max_value = max(numbers)
    print("Максимальне значення серед введених чисел:", max_value)

#Частина 2
    odd_sum = 0
    odd_count = 0
    for i in range(n):
        if (numbers[i]) % 2 != 0:
            odd_sum += numbers[i]
            odd_count+= 1

    if odd_count == 0:
        print("Жодного непарного числа")
    else:
        average = odd_sum / odd_count
        print("Середнє арифметичне непарних чисел:", average)
    
#Частина 3
    negativ_list = []
    for i in range(n - 1):
        point = numbers[i]
        if point < 0:
            negativ_list.append(point)

    len_of_list = len(negativ_list)
    for j in range(len_of_list):
        print(negativ_list[j])

while True:
    print("\n ГОЛОВНЕ МЕНЮ ")
    print("1 Завдання")
    print("2 Завдання ")
    print("3 Завдання ")
    print("0. Вийти з програми")
    
    choice = input("Оберіть пункт меню: ")
    
    if choice == "1":
        task_1()
    elif choice == "2":
        task_2()
    elif choice == "3":
        task_3()
    elif choice == "0":
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір. Будь ласка, введіть 1, 2, 3 або 0.")
