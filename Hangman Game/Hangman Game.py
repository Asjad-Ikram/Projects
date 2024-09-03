#Hangman Game

import json
import random
import string

def hangman():
    
    file=open("D:\Projects\Hangman Game\word-list.json")

    data=json.load(file)

    selected_word=random.choice(data)
         
    print("\n")
    print(selected_word["hint"])
    word=selected_word["word"].upper()
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()
    Lives=5

    while len(word_letters)>0:

        #Letters Used
        print("You have used these letters: "," ".join(used_letters))   

        #Current Word in display (W - R D)
        word_list=[letter if letter in used_letters else "-" for letter in word]    
        print("Current Word: "," ".join(word_list))
        
        user_letter=input("Guess a letter: \n").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else: 
                Lives=Lives-1
                print(f"You have {Lives} left")
                if Lives==0:
                    print(f"No more lives. The word was {word}")
                    break
        
        elif user_letter in used_letters:
            print("You hava already used this letter. Please select another letter\n")

        else:
            print("Invalid Entry")

    if Lives!=0:
        print(f"Congrats. The word is {word}")


     
    
    file.close()
     

hangman()