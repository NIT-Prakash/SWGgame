'''
1 for snake
2 for water
0 for gun


'''
import random
while 1:
    computer = random.choice([-1, 0, 1])
    youstr = input('Choose "s" for Snake, "w" for Water, "g" for Gun\nEnter your choice: ')
    youDict = {"s" : 1, "w" : -1, "g" : 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
    if(youstr == 's' or youstr == 'g' or youstr == 'w'):
      pass
    else:
      print("You have choosed invalid option")
      break
    you = youDict[youstr]
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if(computer == you):
      print("Its a draw")

    else:
      if(computer == -1 and you == 1):
        print("You win!")

      elif(computer == -1 and you == 0):
        print("You lose!")

      elif(computer == 1 and you == -1):
        print("You lose!")

      elif(computer == 1 and you == 0):
        print("You win!")

      elif(computer == 0 and you == -1):
        print("You win!")

      elif(computer == 0 and you == 1):
        print("You lose")

      else:
        print("Something wrong!")