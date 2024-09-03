#Password Generator
from string import punctuation
import string
import random



def Password_Generator(Length,Amount):
    
    letters=string.ascii_letters
    Special_Char=string.punctuation

    Chars=letters + Special_Char

    for i in range(Amount):
        Password=""
        for j in range(Length):
            Password+=random.choice(Chars)
        print(Password)
    


Length=int(input("Enter the length of the Password: "))
Amount=int(input("Enter the Number of Passwords to generate: "))
Password_Generator(Length,Amount)
