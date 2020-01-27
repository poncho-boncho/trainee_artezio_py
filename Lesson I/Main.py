import MyModuls
def main():
    MyModuls.information()

    choice = int(input("What to check? \n"))
    if choice == 1:
         print(MyModuls.capital_letter())
    elif choice == 2:
        print(MyModuls.char_count())

    elif choice == 3:
         print(MyModuls.slice_str())

    elif choice == 4:
        print(MyModuls.rows_count())

    elif choice == 5:
        print(MyModuls.sets())

    elif choice == 6:
        print(MyModuls.generate_dictionary())

    elif choice == 7:
        print(MyModuls.union_dictionaries())

    elif choice == 8:
        print(MyModuls.highest_values())

    elif choice == 9:
        test_list = [1,2,3,3,4,2,1,4,5,6,7,4]
        print("old list =" , test_list)
        print("new list =" , MyModuls.remove_dup(test_list))

    elif choice == 10:
        list_one =[1,2,3,4,5]
        list_two = [3,4,5,6,7,8]

        print("list_one =", list_one, "\n list_two = ",list_two)
        print("difference = ",MyModuls.difference_lists(list_one , list_two))

    else:
        print("das")
        print(choice)
main()
