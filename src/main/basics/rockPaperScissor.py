import random

"""
Algorithum 

1. Display the options 
2. Collect the input to usr
3. Validate the input in range of 0 to 3 
4. if usr != 0 : continue
5. Genrate random number between 1 to 3 = com
6. Match the number
    1. If com = usr, draw 
    2. If usr = 1 and com = 3, usr win
    3. If usr = 2 and com = 1, usr win
    4. If usr = 3 and com = 2, usr win
    5. else loose

"""
 
"""
Stretegy :
1.Rock wins the scissor  
2.paper wins the rock
3.Scissors win paper
"""

from random import randint

def fun_display():
    print("Please enter the number based on below option: \n 0.Exit\n 1.Rock\n 2.Paper\n 3.Scissors")

def fun_input():
    try:
        return int(input('Enter the choice : '))
    except (Exception) as e:
        print("invalid input try again... ",e,"\n\n")

        fun_main()

def fun_main():
    usr = 13
    
    while usr  :
        fun_display()
        usr = fun_input()
        com = randint(1,3)
        print('Computer choose ',com)

        if usr not in (0,1,2,3) : 
            print("In valid input, try again") 
        elif usr == 0 :
            print("See you next time")
        elif usr == com : 
            print("Draw")
        elif usr == 1 and com == 3 :
            print("You win")
        elif usr == 2 and com == 1:
            print("You win")
        elif usr == 3 and com == 2:
            print("You win")
        else :
            print("You Loose")
        print("\n\n")

fun_main()

    


        



