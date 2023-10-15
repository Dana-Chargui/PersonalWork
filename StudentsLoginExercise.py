
import re
import random
import collections
import itertools
from getpass import getpass

def ex1():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print(L)
    # using the sum() function to calculate the sum of all items in the list
    Somme = sum(L)
    print("The sum of all items in the list is:", Somme)

def ex2():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print(L)
    produit = 1
    for item in L:
        produit *= item
    print("The product of all items in the list is:", produit)

def ex3():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print(L)
    smallest_num = min(L)
    largest_num = max(L)
    print("The smallest number in the list is:", smallest_num)
    print("The largest number in the list is:", largest_num)

def ex4():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = (input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print(L)

    def count_strings(L):
        count = 0
        for chaine in L:
            if len(chaine) >= 2 and chaine[0] == chaine[-1]:
                count += 1
        return count

    count = count_strings(L)
    print(count)

def ex5():
    def sort_tuples(tuples_list):
        return sorted(tuples_list, key=lambda x: x[-1])

    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    # Demander à l'utilisateur d'entrer une liste de tuples
    tuple_input = input("Enter a tuple list, separated by commas: ")
    # Convertir la chaîne d'entrée en une liste de tuples
    L = [tuple(item.split()) for item in tuple_input.split(',')]
    print(L)
    sorted_list = sort_tuples(L)
    print(sorted_list)

def ex6():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print(L)
    # Supprimer les doublons à l'aide de cette fonction
    L = list(set(L))
    print("The new list is : ", L)

def ex7():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    # Check if the list is empty
    if not L:
        print("The list is empty")
    else:
        print("The list is not empty")
    print("The list is: ", L)

def ex8():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    cloned_list = L[:]
    print("Original list:", L)
    print("Cloned list:", cloned_list)

def ex9():
    while True:
        try:
            y = int(input("Enter the number of strings you want to add: "))
            break
        except ValueError:
            print("Please enter an integer")
    LS = []
    for i in range(y):
        string = input("Enter string {}: ".format(i + 1))
        LS.append(string)
    print("List of strings:", LS)
    n = len(LS)
    # we creat a new list to find the words longer than n
    # we add the word only if it's longer than n (>n)
    long_words = [word for word in LS if len(word) > n]
    print("The words longer than", n, ":", long_words)


def ex10():
    while True:
        try:
            nbre = int(input("Give the number of items in the list 1 : "))
            break
        except ValueError:
            print("Please enter an integer")
    L1 = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L1.append(x)
    while True:
        try:
            nbre = int(input("Give the number of items in the list 2 : "))
            break
        except ValueError:
            print("Please enter an integer")
    L2 = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L2.append(x)

    def common_member(L1, L2):
        return bool(set(L1) & set(L2))

    print(L1)
    print(L2)
    print(common_member(L1, L2))

def ex11():
    def remove_elements(lst):
        # function that removes the 0th, 4th, and 5th elements from the specified list
        indices = [0, 4, 5]  # indices of elements to remove
        return [elem for i, elem in enumerate(lst) if i not in indices]

    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    modified_list = remove_elements(L)
    print(L)
    print(modified_list)

def ex12():
    def remove_even_numbers(lst):
        # FUNCTION to removes even numbers from the specified list.
        return [num for num in lst if num % 2 != 0]

    # returns a new list with the odd numbers.
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    odd_numbers = remove_even_numbers(L)
    print("The original list: ", L)
    print("The new list with the odd numbers: ", odd_numbers)

def ex13():
    def shuffle_list(lst):
        # FUNCTION that shuffles a specified list
        random.shuffle(lst)
        # returns the shuffled list.
        return lst

    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print("The original list: ", L)
    shuffled_list = shuffle_list(L)
    print("The shuffled list : ", shuffled_list)

def ex14():
    squares = [x ** 2 for x in range(1, 31)]
    # generate a list of squares of numbers between 1 and 30 (both included)
    print("First 5 elements:", squares[:5])
    # first 5 elements
    print("Last 5 elements:", squares[-5:])
    # last 5 elemnts

def ex15():
    squares = [x ** 2 for x in range(1, 21)]
    # generate a list of squares of numbers between 1 and 20 (both included)
    print("List except for the first 5 elements:", squares[5:])

def ex16():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print(L)
    permutations = list(itertools.permutations(L))
    # generate all permutations
    print("All permutations of the list:", permutations)

def ex17():
    while True:
        try:
            nbre = int(input("Give the number of items in the list 1 : "))
            break
        except ValueError:
            print("Please enter an integer")
    L1 = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L1.append(x)
    while True:
        try:
            nbre = int(input("Give the number of items in the list 2 : "))
            break
        except ValueError:
            print("Please enter an integer")
    L2 = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L2.append(x)

    difference = list(set(L1) - set(L2))
    # get the difference between L1 and L2
    print(L1)
    print(L2)
    print("The difference between the two lists L1 and L2:", difference)

def ex18():
    while True:
        try:
            y = int(input("Enter the number of strings you want to add: "))
            break
        except ValueError:
            print("Please enter an integer")
    LS = []
    for i in range(y):
        string = input("Enter string {}: ".format(i + 1))
        LS.append(string)
    print("List of strings:", LS)
    for index, item in enumerate(LS):
        print(f"The item at index {index} is {item}")

def ex19():
    while True:
        try:
            y = int(input("Enter the number of strings you want to add: "))
            break
        except ValueError:
            print("Please enter an integer")
    LS = []
    for i in range(y):
        string = input("Enter string {}: ".format(i + 1))
        LS.append(string)
    print("List of strings:", LS)
    item_to_find = input("Enter the item you wish to find in the list: ")
    if item_to_find in LS:
        index_of_item = LS.index(item_to_find)
        print(f"The index of '{item_to_find}' is {index_of_item}")
    else:
        print(f"'{item_to_find}' is not in the list {LS}.")

def ex20():
    while True:
        try:
            z = int(input("Enter the number of characters you want to add: "))
            break
        except ValueError:
            print("Please enter an integer")
    LC = []
    for i in range(z):
        char = input("Enter character {}: ".format(i + 1))
        LC.append(char)
    print("List of strings:", LC)
    LC = ''.join(LC)
    # we used the join() method to convert the list of characters into a single string
    print(LC)

def ex21():
    while True:
        try:
            nbre = int(input("Give the number of items in the list 1 : "))
            break
        except ValueError:
            print("Please enter an integer")
    L1 = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L1.append(x)
    while True:
        try:
            nbre = int(input("Give the number of items in the list 2 : "))
            break
        except ValueError:
            print("Please enter an integer")
    L2 = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L2.append(x)
    print("L1 is:", L1)
    print("L2 is:", L2)
    L2.extend(L1)
    print("L2 after appending L1:", L2)

def ex22():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print(L)
    random_item = random.choice(L)
    print("The random item from the list is....", random_item)

def ex23():
    def is_circularly_identical(list1, list2):
        # if both lists have the same length then return false
        if len(list1) != len(list2):
            return False
        # Concatenate one of the lists with itself
        concatenated_list = list1 + list1
        # Check if the second list is a sublist of the concatenated list
        if all(item in concatenated_list[i:i + len(list1)] for i, item in enumerate(list2)):
            return True
        else:
            return False

    while True:
        try:
            nbre = int(input("Give the number of items in the list 1 : "))
            break
        except ValueError:
            print("Please enter an integer")
    L1 = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L1.append(x)
    while True:
        try:
            nbre = int(input("Give the number of items in the list 2 : "))
            break
        except ValueError:
            print("Please enter an integer")
    L2 = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L2.append(x)
    print("L1 =", L1)
    print("L2 =", L2)
    print(is_circularly_identical(L1, L2))

def ex24():
    def second_smallest(numbers):
        sorted_numbers = sorted(numbers)
        return sorted_numbers[1]

    # we use the sorted() function in python to sort the list in ascending order
    # then we choose the second sorted number using its index position [1]
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print("The original list:", L)
    print("The second smallest number is:", second_smallest(L))

def ex25():
    while True:
        try:
            y = int(input("Enter the number of strings you want to add: "))
            break
        except ValueError:
            print("Please enter an integer")
    LS = []
    for i in range(y):
        string = input("Enter string {}: ".format(i + 1))
        LS.append(string)
    # we use the method : counter() from the collections module to count the frequency of each element
    count = collections.Counter(LS)
    print("List of strings:", LS)
    for item, frequency in count.items():
        print(f"{item} : {frequency}")

def ex26():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print(L)
    # we use the method : set() to get unique values
    unique_values = set(L)
    print("The unique values are :", unique_values)

def ex27():
    while True:
        try:
            y = int(input("Enter the number of strings you want to add: "))
            break
        except ValueError:
            print("Please enter an integer")
    LS1 = []
    for i in range(y):
        string = input("Enter string {}: ".format(i + 1))
        LS1.append(string)

    while True:
        try:
            y = int(input("Enter the number of strings you want to add: "))
            break
        except ValueError:
            print("Please enter an integer")
    LS2 = []
    for i in range(y):
        string = input("Enter string {}: ".format(i + 1))
        LS2.append(string)
    print("List 1 of strings:", LS1)
    print("List 2 of strings:", LS2)
    # we use a set intersection to find the common items
    common_items = set(LS1) & set(LS2)
    print(common_items)


def ex28():
    while True:
        try:
            nbre = int(input("Give the number of items in the list : "))
            break
        except ValueError:
            print("Please enter an integer")
    L = []
    for i in range(nbre):
        x = int(input("Give item " + str(i + 1) + ": "))
        L.append(x)
    print(L)
    # CONVERT the list to a STRING and THEN to an INTEGER(valeur)
    single_integer = int(''.join(map(str, L)))
    print(single_integer)


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
        return 1
    else:
        return 0

def password(pwd):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,12}$"
# compiling regex
    pat = re.compile(reg)
# searching regex
    mat = re.search(pat, pwd)
# validating conditions
    if mat:
        return 1
    else:
        return 0

def mainmenu():
    EXE = True
    while EXE:
        print("1: Sign up")
        print("2: Log in")
        print("3: Quit")
        choice=input("Enter your choice: ")
        match choice:
            case '1':
                signup()
                mainmenu()
                break
            case '2':
                login()
                break
            case '3':
                quiting = input("Do you wish to exit? press Y/N : ")
                if (quiting == 'Y' or quiting == 'y'):
                    print("Thank you for using our program! till next time!")
                    EXE = False
                    break
                else:
                    mainmenu()
                break
            case _:
                print("please enter a number between 1 to 3")

L_pwd = []
L_email = []

def signup():
    print("Sign up")
    for i in range(3):
        while True:
            email = input("email address : ")
            if isValid(email) == 1:
                L_email.append(email)
                break
            else:
                print("Invalid email, please enter your email address correctly..")
        while True:
            try:
                pwd = getpass("password : ")
                if password(pwd) == 1:
                    L_pwd.append(pwd)
                    print("You have successfully signed up!")
                    break
                else:
                    print("Invalid password, it must be 8 to 12 long and contains : (a number, a capital letter, a lowercase letter, and a special character)")
            except ValueError:
                print("error")

    for i in range(3):
        print(f"{L_email[i]} password is {L_pwd[i]}")

def email_splitter(email):
    username = email.split('@')[0]
    print('welcome', username)

def login():
    print("Authentication")
    print("Log in")
    if (len(L_email)==0):
        print("you need to sign up first")
        mainmenu()
    else:
        while True:
            try:
                emaillog = input("email address : ")
                if isValid(emaillog) == 1:
                    if emaillog in L_email:
                        break
                    else:
                        print("Incorrect email, please enter your email correctly")
                        continue
                else:
                    print("Invalid email, please enter your email correctly")
            except ValueError :
                print("error")
        while True:
            try:
                pwdlog = getpass("password : ")
                if password(pwdlog) == 1:
                    if pwdlog in L_pwd:
                        print("You have successfully logged in!")
                        email_splitter(emaillog)
                        index=L_email.index(emaillog)
                        if (index==0):
                            serie1()
                        elif (index==1):
                            serie2()
                        else:
                            serie3()
                    else:
                        print("Incorrect password, please enter your password correctly")
                        continue
                else:
                    print("Invalid password, please enter your password correctly")
                    continue
            except ValueError :
                print("error")

def serie1():
    print("To access the Series, select the corresponding numbers.. ")
    EXET=True
    while EXET:
        for i in range(10):
            print(f"{i+1}. serie {i+1}")
        print("11. Exit and log out")
        serie = int(input("Which exercise do you wish to access: "))
        match serie:
            case 1:
                ex1()
                menu=input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 2:
                ex2()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 3:
                ex3()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 4:
                ex4()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 5:
                ex5()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 6:
                ex6()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 7:
                ex7()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 8:
                ex8()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 9:
                ex9()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 10:
                ex10()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 11:
                quit=input("Do you wish to go back to the menu? press Y/N : ")
                if(quit=='Y' or quit=='y'):
                    print("Thank you for stopping bye! till next time!")
                    EXET=False
                    mainmenu()
                else:
                    continue
            case _:
                print("serie not recognized")

def serie2():
    print("To access the Series, select the corresponding numbers.. ")
    EXET=True
    while EXET:
        for i in range(10,20):
            print(f"{i+1}. serie {i+1}")
        print("21. Exit and log out")
        serie = int(input("Which exercise do you wish to access: "))
        match serie:
            case 11:
                ex11()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 12:
                ex12()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 13:
                ex13()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 14:
                ex14()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 15:
                ex15()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 16:
                ex16()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 17:
                ex17()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 18:
                ex18()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 19:
                ex19()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 20:
                ex20()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 21:
                quit=input("Do you wish to go back to the menu? press Y/N : ")
                if(quit=='Y' or quit=='y'):
                    print("Thank you for stopping bye! till next time!")
                    EXET=False
                    mainmenu()
                else:
                    continue
            case _:
                print("serie not recognized")

def serie3():
    print("To access the Series, select the corresponding numbers.. ")
    EXET=True
    while EXET:
        for i in range(20,28):
            print(f"{i+1}. serie {i+1}")
        print("28. Exit and log out")
        serie = int(input("Which exercise do you wish to access: "))
        match serie:
            case 21:
                ex21()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 22:
                ex22()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 23:
                ex23()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 24:
                ex24()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 25:
                ex25()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 26:
                ex26()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 27:
                ex27()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 28:
                ex28()
                menu = input("tap y to go back to the main menu Y/N ")
                if (menu == 'Y' or menu == 'y'):
                    print("redirecting you to the main menu..")
                    mainmenu()
                    break
                else:
                    continue
            case 29:
                quit=input("Do you wish to go back to the menu? press Y/N : ")
                if(quit=='Y' or quit=='y'):
                    print("Thank you for stopping bye! till next time!")
                    EXET=False
                    mainmenu()
                else:
                    continue
            case _:
                print("serie not recognized")

mainmenu()
