"""rock scissor game using python """
import os
import time
import sys
import random

x='''hello dear!,
   welcome to the game,\n
Enter \'rock\' for rock',
Enter \'paper\' for paper',
Enter \'scissor\' for scissor.'''
for i in x:
    print(i,end="")
    time.sleep(.1)
   


input("\npress any key from keyboard if you are ready to play the game:")

while True:
    print("Here we go , Guess the item in :")
    time.sleep(1.9)
    os.system('clear')
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
        os.system('clear')
    
    print("rock,paper,scissor")
    # computer guess the random element
    Computer_Guess=random.choice([1,2,3])
    # print(Computer_Guess)
    
    if Computer_Guess==1:
            Computer_Guess='rock'


    elif Computer_Guess==2:
            Computer_Guess='paper'
    else:
            Computer_Guess='scissor'
    PlayerMove=input("enter your move:")
    # tie condition
    if ((PlayerMove==Computer_Guess=='rock') or (PlayerMove==Computer_Guess=='paper') or (PlayerMove==Computer_Guess=='scissor')):
        print(f"{PlayerMove} versus {Computer_Guess}")
        print("it's a tie.")
        # Player win condition
    elif ((PlayerMove=='paper' and Computer_Guess=='rock') or (PlayerMove =='scissor' and Computer_Guess=='paper') or (PlayerMove=='rock' and Computer_Guess=='scissor')) :
        print(f"{PlayerMove} versus {Computer_Guess}")
        print("you won.")
        # computer win condition

    elif ((Computer_Guess=='paper' and PlayerMove=='rock') or (Computer_Guess =='scissor' and PlayerMove=='paper') or (Computer_Guess=='rock' and PlayerMove=='scissor')):
        print(f"{PlayerMove} versus {Computer_Guess}")
        print("computer wins.")   
    print("do you want to play again? ") 

    n=input("press y to continue or q to exit.")
    if  n=='q':
        print("thank you for playing the game.")
        sys.exit()
    else:
        os.system('clear')
        continue
