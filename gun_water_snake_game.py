# Gun water Snake game
from random import choice
from time import sleep
print("Loading...",end=" ")
sleep(3)
print("\rDone!     ")
n=input("Enter your choice:")
computer_value= choice([-1,1,0])
mapping = dict(zip(["water", "snake", "gun"], [0, -1, 1]))
value=mapping[n]
reverse_mapping = {v: k for k, v in mapping.items()}
print("Computer chose:", reverse_mapping[computer_value])
if value== computer_value:
    print('It\'s a draw')
elif value==0 and computer_value==1:
    print("You win")  
elif value==1 and computer_value==0:
    print('You lose')
    print("Game over")
elif value==-1 and computer_value==0:
    print('You win')
elif value==0 and computer_value==-1:
    print('You lose')
    print("Game over")
elif value==1 and computer_value==-1:
    print('You win')
elif value==-1 and computer_value==1:
    print('You lose')
    print("Game over")

