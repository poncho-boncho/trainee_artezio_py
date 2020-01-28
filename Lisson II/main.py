import Moduls_task2

def main():
    Moduls_task2.information()
    choice = int(input("What to check? \n"))
    if choice == 1:
        str = "[0,X] - enter the number that will replace X"
        Moduls_task2.print_square_number(Moduls_task2.input_num(str))

    if choice == 2:
        print (Moduls_task2.division_check (
            Moduls_task2.input_num("enter a"),
            Moduls_task2.input_num("enter b"),
            Moduls_task2.input_num("enter c")
        ))
    if choice == 3:
        print(Moduls_task2.factorial(Moduls_task2.input_num("factorial of what number?")))
    if choice == 4:
        print("my_range(5) =",Moduls_task2.my_range(5))
        print("my_range(10, 100, 10) =",Moduls_task2.my_range(10,100,10))
        print("my_range(100, 10, -15) =",Moduls_task2.my_range(100,10,-15))
    if choice ==5:
        Moduls_task2.authorization()
main()