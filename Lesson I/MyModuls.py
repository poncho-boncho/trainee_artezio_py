def information():
    print("""
    1. You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
    For example, alison heck should be capitalized correctly as Alison Heck. 
    Given a full name, your task is to capitalize the name appropriately. 
    Input Format:A single line of input containing the full name, S.
    Constraints:* 0 < len(S) < 1000* 
    The string consists of alphanumeric characters and spaces.
    Note: in a word only the first character is capitalized. 
    Example 12abc when capitalized remains 12abc.
    Output Format:Print the capitalized string, S.

    2. Write a Python program to count the number of characters (character frequency) in a string.
    Sample String : google.com
    Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

    3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
    Sample String : 'w3resource'
    Expected Result : 'w3ce'
    Sample String : 'w3'
    Expected Result : 'w3w3'
    Sample String : ' w'
    Expected Result : Empty String

    4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2

    5. You are given with 3 sets, find if third set is a subset of the first and the second sets
    Input: set([1,2]), set([2,3), set([2])
    Expected result: True
    Input: set([1,2]), set([3,4), set([5])
    Expected result: False

    6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
    Sample Dictionary ( n = 5) :
    Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

    7. Write a Python script to merge two Python dictionaries

    8. Write a Python program to find the highest 3 values in a dictionary

    9. Write a Python program to remove duplicates from a list.

    10. Write a Python program to get the difference between the two lists
    """)

def capital_letter():                                                     ############
    str=""                                                                ## task 1 ##
    while str.__len__() <= 0 or str.__len__() > 1000:                     ############
        str = input("enter str")
        list = str.split()

    for item in list:
        print(item.upper()[0][0]+item[1:item.__len__()], end=' ')
    return " "

def char_count():                                                        ############
    str = input("enter str")                                             ## task 2 ##
    chars = []                                                           ############
    i = 0;
    for char in str:
        if char not in chars:
            chars.append(char)

    for i in range(len(chars)):
        print('\'',chars[i],'\'' ':' , str.count(chars[i]))
    return " "

def slice_str():                                                        ############
    str = input("enter str")                                            ## task 3 ##
    if (str.__len__()==1):                                              ############
        print("Empty String")

    else:
        print ("word = ",str)
        print("first 2 letters =", str[0:2])
        print("last  2 letters =", str[str.__len__()-2:str.__len__()])
        print("cropped string  =",str[0:2] + str[str.__len__()-2:str.__len__()])

    return " "

def rows_count():                                                       ############
                                                                        ## task 4 ##
                                                                        ############
    print("""                                                           
             ############################################
             ###        enter at least 2 lines        ###
             ###                then                  ###
             ###        press   enter  2 times        ###
             ############################################
    """)
    list_str = list()
    str = ""
    count = 0
    while True:
        word = input()
        if word:
            str += word + " "
            if len(word) >= 2:
                list_str.append(word)
                if word[0:1] == word[word.__len__()-1:word.__len__()]:
                    count+=1

        elif len(list_str)>2:
            print("you entered",list_str)
            print("count : " , count)
            break

    return list_str

def sets():                                                             ############
    i=1                                                                 ## task 5 ##
    list_sets = list()                                                  ############
    while len(list_sets) < 3:
        print("enter the" , i , "set")
        str = input().split(' ')
        i+=1
        list_sets.append(str)

    set0 = set(list_sets[0])
    set1 = set(list_sets[1])
    sub_set = set(list_sets[2])
    union_set = set0.union(set1)

    print(" set 1 =" ,set0)
    print(" set 2 =", set1)
    print(" set 3 =", sub_set)
    print("subset is",sub_set.issubset(union_set))


    return ' '

def generate_dictionary():                                              ############
    n = int(input(" n = "))                                             ## task 6 ##
    print( {a:a**2 for a in range(1, n+1)})                             ############

    return " "

def union_dictionaries():                                               ############
    dictionary_one = {1:"Pilot",2:"Lawnmower Dog", 3:"Anatomy Park"}    ## task 7 ##
                                                                        ############
    dictionary_two = {4: "M.Night Shaym-Aliens", 5:"Meeseeks and Destroy", 6:"Rick Potion"}

    print("dictionariesOne =", dictionary_one)
    print("dictionariesTwo = ", dictionary_two)
    dictionary_one.update(dictionary_two)

    print("union dictionaries",dictionary_one)
    return " "

def highest_values():                                                   ############
    dictionary = dict()                                                 ## task 8 ##
    n = int(input("Enter the amount of dictionaries"))                  ############
    i = 0
    j =0
    high_numb = list()

    while len(dictionary)<n:
        print("enter value dictionary",len(dictionary)+1)
        number = int(input())
        dictionary[i] =number
        i+=1

    for i in sorted(dictionary.values(), reverse =True):
        high_numb.append(i)

    if len(high_numb)==2:
        print(high_numb[0])
        print(high_numb[1])
    elif len(high_numb)==1:
        print(high_numb[0])
    else:
        while j <3:
            print(high_numb[j])
            j+=1

    return " "

def remove_dup(t_list):                                                 ############
    my_list = list()                                                    ## task 9 ##
    for i in t_list:                                                    ############
        if i not in my_list:
            my_list.append(i)

    return my_list

def difference_lists(list_one,list_two):                                ############
    set_one = set(list_one)                                             ## task 10##
    set_two = set(list_two)                                             ############

    diff_set_one = set_one.difference(set_two)
    diff_set_two = set_two.difference(set_one)

    diff_set_one = list(diff_set_one)
    diff_set_two = list(diff_set_two)

    return diff_set_one + diff_set_two









