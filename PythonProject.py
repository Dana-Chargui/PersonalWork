import random
import math

#first we create a function called calculate, which takes in x, y (integers) and an operator in its parameter
def calculate(x, y, op):
    #instead of using if-elif, we use match case to check if the operator equals a specific string, then we return it as an expression
    match (op):
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y
        case 'sqrt':
            #here we use math.sqrt(x) to get the square root of x
            return math.sqrt(x)
        case _:
            #otherwise our default case to raise an error if the inserted operator is false
            raise ValueError("Unsupported operation")

#then we define a function that generates arithmetic questions
def gen_q():
    op = ['+', '-', '*', '/','^','sqrt'] #here we define our operators
    brackets1=['(',')']
    # then we create 2 variables that take a random integer from between 1-10, here we use import random
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    op = random.choice(op) #this allows us to assign a random operator for our variable based off of the list we created

    #to ensure we don't get an error if we divide by 0, we assign it another random integer if the op is /
    if (op=='/' and y==0):
        y = random.randint(1, 10)

    #this checks if our variable op is sqrt (square root)
    if op == 'sqrt':
        z = f"sqrt({x})" #with this we assign just the x value to it (z is our expression)
        res = calculate(x, None, op) #here we use import math to use the sqrt function on our x as a result, we don't need to insert a y value so we set it as NULL (none)
    else:
        z = f"{x} {op} {y}" #otherwise we just assign z the x value, operator and y value
        res = calculate(x, y, op)

    return z, res

#here we create a mainmenu function as well, we use this so we can keep calling it instead of rewriting the menu
def mainmenu():
    print("1.Start the quiz\n2.About BODMAS\n3.Quit\n\nwhich would you like to access first? : ")

print("\nWelcome to the Arithmetic Quiz!\nTest your BODMAS knowledge with this quiz\n")
mainmenu()
start = int(input())
exit = 0
count=0
while(True):
    match (start):
        case 1:
            while (exit != -1):
                try:
                    q, ans = gen_q()
                    print(f"Question : {q}")
                    user_answer = float(input(""))
                    if (user_answer == ans):
                        print(f"Well Done! you answered correctly with : {ans:.1f}")
                        count+=1
                        print(f"Total score : {count}")
                    else:
                        print(f"Nice try! you answered incorrectly, the correct answer was : {ans:.1f}")
                        print(f"Total score : {count}")
                    exit = int(input("you can always type -1 to exit or 0 to continue : "))
                except ValueError:
                    print("Please enter a valid integer.")
            mainmenu()
            start = int(input())
        case 2:
            print("\nBODMAS is an acronym for Brackets, Orders, Division and Multiplication, Addition and Subtraction.",
                  "\nIt dictates the order of operations in mathematical expressions: first, solve anything in brackets; then calculate powers or square roots (orders); ",
                  "\nfollowed by division and multiplication (left to right), and finally, perform addition and subtraction (left to right).",
                  "\nThis rule ensures that calculations are consistent and clear.\n")
            mainmenu()
            start = int(input())
        case 3:
            print("Thank you for using this program, have a good day!")
            break
        case _:
            print("please enter a number between 1 and 3")
            continue
