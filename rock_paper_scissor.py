import random
user_count=0
comp_count=0
print("----------------------ROCK-PAPER-SCISSORS-------------------------")

choice=input("do you want to play....")
if(choice=="yes".lower()):
    while(True):
        user_choice=input("enter your choice")
        list=["rock","paper","scissor"]
        comp_choice=random.choice(list)
        print("computer choice is",comp_choice)
        if (user_choice=="rock" and comp_choice=="scissor") or (user_choice=="paper" and comp_choice=="rock") or (user_choice=="scissor" and comp_choice=="paper"):
            print("you won the match")
            user_count=user_count+1
        elif (comp_choice=="rock" and user_choice=="scissor") or (comp_choice=="paper" and user_choice=="rock") or (comp_choice=="scissor" and user_choice=="paper"):
            print("computer wins the match")
            comp_count=comp_count+1
        elif (user_choice==comp_choice):
            print("both tie")
        choice=input("do you want to play....")
        if(choice=="yes".lower()):
            continue
        else:
            break
            
    
    print("RESULT=YOUR SCORE=",user_count,"computer score=",comp_count)
if(user_count>comp_count):
    print("CONGRATULATIONS.....you won thw tournament")
else:
    print("you loose....BETTER LUCK NEXT TIME")
