import random

Actual_Number=random.randint(1,10)
Guess=0

while Guess!=Actual_Number:
    Guess=int(input("Guess: "))
    print("Sorry wrong number")

print(f"Yes you are correct. The number is {Guess}")
