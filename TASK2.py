import random,os
userI =True
os.system("cls")
def randomOddNumber(a,b):
  a = a // 2
  b = b // 2 - 1
  number = random.randint(a,b)
  number = (number * 2) + 1
  return number
while userI==True:
    userInput = int(input("Please input a 4 digit number: "))
    compNumber = random.randint(1000, 9999)

    count = 0
    while userInput != compNumber:
         
        if (userInput % 2) == 0:

                compNumber= random.randrange(0, 10000, 2)
                count=count+1
        else:
              compNumber = randomOddNumber(0,9999)
              count =count+1
    print("Match was created on the", count, "attempt.")
    ex = False
    while ex == False:
        userAwnser = input("Would you like to play again?: ")
        if userAwnser == "no"or userAwnser=="No":
            userI = False
            ex = True
        elif userAwnser == "yes"or userAwnser=="Yes":
            userI = True
            ex = True
            os.system("cls")
        else:
            print("Error Not a valid awnser")
            ex = False
