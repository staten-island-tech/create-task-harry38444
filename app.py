import random
response = 0
list = []
randomnumber = int(random.randrange(1,3))
if int(randomnumber) == 1:
    response = "Rock"
elif int(randomnumber) == 2:
    response = "Paper"
elif int(randomnumber) == 3:
    response = "Scissors"
def rockpaperscissorsgame():
    Input = input("Rock, Paper or Scissors?: ")
    if Input == "Rock" and response == "Paper":
        print("Opponent chose:", response)
        print("You lost")
        list.append("loss")
    elif Input == "Scissors" and response == "Paper":
        print("Opponent chose:", response)
        print("You won")
        list.append("win")
    elif Input == "Rock" and response == "Scissors":
        print("Opponent chose:", response)
        print("You won")
        list.append("win")
    elif Input == "Paper" and response == "Scissors":
        print("You lost")
        list.append("loss")
    elif Input == "Paper" and response == "Rock":
        print("Opponent chose:", response)
        print("You won")
        list.append("win")
    elif Input == "Scissors" and response == "Rock":
        print("Opponent chose:", response)
        print("You lost")
        list.append("loss")
    elif Input == response:
        print("Opponent chose:", response)
        print("You drawed")
        list.append("draw")
    else: 
        print("Error, check spelling and write the first letter in capital")
continue_game = "Yes"
while continue_game.upper() == "Yes":
    rockpaperscissorsgame()
    continue_game = input("Would you like to continue the game? Yes/No:")
print("Statistics:", list) 