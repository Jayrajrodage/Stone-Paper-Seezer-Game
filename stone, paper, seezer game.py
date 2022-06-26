import random
chance = 6
no_of_chnace=0
human_point=0
computer_point=0
list = ["stone", "paper", "seezer"]
print("\t\t\t\t\tWelcome to game")
while no_of_chnace<chance:
     a = str(input("enter stone,paper or seezer "))
     b = random.choice(list)
     if a==b:
         print("match tied both have 0 point")
     elif a =="stone" and b=="paper":
         computer_point=computer_point+1
         print(f"your guess is {a} and computer guess is {b}")
         print("computer guess win")
         print(f"computer point are{computer_point} and human points are {human_point}")

     elif a=="stone" and b=="seezer":
         human_point=human_point+1
         print(f"Your guess is {a} and computer guess is {b}")
         print("human guess win")
         print(f"computer points are{computer_point} and human pionts are {human_point}")

     elif a=="seezer" and b=="stone":
         computer_point=computer_point+1
         print(f"Your guess is {a} and computer guess is {b}")
         print("computer guess win")
         print(f"computer points are{computer_point} and human pionts are {human_point}")

     elif a=="seezer" and b=="paper":
         human_point=human_point+1
         print(f"Your guess is {a} and computer guess is {b}")
         print("human guess win")
         print(f"computer points are{computer_point} and human pionts are {human_point}")

     elif a=="paper" and b=="seezer":
         computer_point=computer_point+1
         print(f"Your guess is {a} and computer guess is {b}")
         print("human guess win")
         print(f"computer points are{computer_point} and human pionts are {human_point}")

     elif a=="paper" and b=="stone":
         human_point=human_point+1
         print(f"Your guess is {a} and computer guess is {b}")
         print("human guess win")
         print(f"computer points are{computer_point} and human pionts are {human_point}")
     else:
         print("enter valid input")
     no_of_chnace=no_of_chnace+1

if human_point>computer_point:
    print(f"\nhuman points are {human_point} and human is winner ")
elif human_point==computer_point:
    print("match ties booth have same point")
else:
    print(f"\ncomputer points are{computer_point} computer is winner")
