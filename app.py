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
Input = input("Rock Paper or Scissors?: ")
if Input == 1 and response == "Paper":
    print("You lose")
    list.append("win")
elif Input == 3 and response == "Paper":
    print("You won")
    list.append("win")
elif Input == 1 and response == "Scissors":
    print("You won")
    list.append("win")
elif Input == 2 and response == "Scissors":
    print("You lost")
    list.append("lose")
elif Input == 2 and response == "Rock":
    print("You won")
    list.append("win")
elif Input == 3 and response == "Rock":
    print("You lost")
    list.append("lose")
elif Input == response:
    print("You draw")
    list.append("draw")
