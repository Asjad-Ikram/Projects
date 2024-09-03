import random

def RPS_Game():
    Bot_choice=random.choice(["Rock","Paper","Scissor"])
    User_Choice=input("Choose Rock, Paper or Scissor\n")

    if Bot_choice==User_Choice:          #Incase of a tie
        print("It's a tie")
    
    if is_win(User_Choice,Bot_choice):
        print("Congrats you Won!")
    
    else:
        print("You Lost")

def is_win(User,Opponent):
    #r>s ,p>r ,s>p
    if (User=="Paper" and Opponent=="Rock") or (User=="Rock" and Opponent=="Scissor") or (User=="Scissor" and Opponent=="Paper"):
        return True   

        
RPS_Game()
