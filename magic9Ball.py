
# Abhay Prasanna Rao
import math

print("Welcome to the Magic 9 Ball...")
print()

print("By: Abhay Prasanna Rao")
print()


while True:
    print("What would you like to do?")
    print()
    choice = input("[c]alculator, [p]rediction, [q]uit: ")
    print()
    if choice == 'c':
        print("You Choose C!")
        print()
        calc = input("Enter \"+\", \"-\", \"*\", \"/\", \"%\", or \"**\"" )
        x = float(input("Enter left hand side number: "))
        y = float(input("Enter right hand side number: "))
        print(calc)
        if calc == '+':
            sum = x+y
            print("The total is {0}".format(sum))
            exit()
        elif calc == '-':
            sub  = x-y
            print("The value is {0}".format(sub))
        elif calc == '*':
            mul = x*y
            print("The product is {0}".format(mul))
        elif  (calc == '/') and (y!=0):
            div = x/y
            print("The value is {0}".format(div))
        elif (calc == '%') and (y !=0):
            rem = x % y
            print("The reminder is {0}".format(rem))
        elif calc == '**':
            po = x ** y
            print("The answer is {0}".format(po))
        else:
            print("You must enter either \"+\", \"-\", \"*\", \"/\", \"%\", or \"**\"")
            print("Also, make sure that right side number is not zero! ")
            exit()
            

    elif choice == 'p':
        print("You Chosoe P!")
        st = input("What is your Question! ")
        p1 = "It is certain"
        p2 = "Outlook good"
        p3 = "You may relay on it"
        p4 = "Ask again later"
        p5 = "Concentrate and ask again"
        p6 = "Reply hazy, try again"
        p7 =  "My reply is no"
        p8 =  "My reply is no"
        p9 = "My sources say no",
        p10 = "Yeah, when the moon turns blue! "
        ch =len(st)%10
        if ch == 1:
            print(p1)
        elif ch ==2:
            print(p2)
        elif ch ==3:
            print(p3)
        elif ch ==4:
            print(p4)
        elif ch ==5:
            print(p5)
        elif ch ==6:
            print(p6)
        elif ch ==7:
            print(p7)
        elif ch ==8:
            print(p8)
        elif ch ==9:
            print(p9)
        elif ch == 10:
            print(p10)
        else:
            print('Error')
        exit()
        
    elif choice == 'q':
        print("You Choose to Quit!")
        print()
        print("Good Bye!")
        print()
        exit()

    else:
        print("Error!")
        print("Enter c or p or q only!")
        print()

