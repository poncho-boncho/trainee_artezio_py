def information():
    print("""
    1. Написать функцию, которая печатает квадраты всех нечетных чисел в произвольном интервале [0, Х]. А так же количество таких чисел.
2. Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’
3. Написать функцию вычисления факториала числа
4. Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3, только возвращает список). 
5. Написать программу, которая принимает от пользователя имя и пароль. Сравнивает пароль с заданным в коде.
	В случае совпадения печатает в консоль "Password for user: <Имя пользователя> is correct"
	Если пароль не совпадает, то печатает в консоль 
	"Password for user: <Имя пользователя> is incorrect"
	"Please try again..."
	И снова запрашивает пароль (не завершается).
    """)

def input_num(str):
    print(str)
    n = int(input())
    return n

def print_square_number(number):
    i =1
    n =0
    while i <=number:
        print(i*i)
        i+=2
        n+=1
    print("total numbers =", n)

def division_check(a,b,c):
    n=0
    if a >b:
        max=a
        min=b
    else:
        max=b
        min=a

    for i in range(min+1,max):
        if i%c ==0:
            print('{',i,'}',end=' ')
            n+=1
    print("\nTotal",end=' ')

    return n

def factorial(number):
    a =1
    for i in range(1,number+1):
        a *=i
    print("factorial of a number",number,'=',end=' ')
    return a

def my_range(start , stop=None, step=1):
    list_range =list()
    if stop is None:
        stop = start
        start = 0
    if start>stop:

       while start>stop:
           list_range.append(start)
           start += step
    else:
        while start < stop:
            list_range.append(start)
            start+=step

    return list_range

def authorization():
    login = input("Enter your login: ")
    password = "qwerty"
    input_pass = input("Enter your password: ")
    while input_pass !=password:
            print("Password for user:",login,"is incorrect \n"
                    "Please tre again...")
            input_pass = input("Enter your password: ")
    print("Password for user:",login,"is correct")