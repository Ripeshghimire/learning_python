import random 
rps = ["rock","paper","scissors"]
while True:
    userInput = input("Enter your choice: ").lower()
    random_generator = random.choice(rps).lower()
    #print(random_generator)
    if(random_generator == "rock" and userInput == "rock"):
        print("Same let's play again")
    elif(random_generator == "rock" and userInput == "scissors"):
        print("You lose")
    elif(random_generator == "rock" and userInput == "paper"):
        print("Paper wins.User wins")    
    elif(random_generator == "paper" and userInput == "scissors"):
        print("scissors wins")
    elif(random_generator == "paper" and userInput == "rock"):
        print(f'Paper wins {random_generator} to {userInput}')
    elif(random_generator == "paper" and userInput == "paper"):
        print(f'same choice!lets play again')
    elif(random_generator == "scissors" and userInput == "rock"):
        print(f'User wins {userInput} to {random_generator}')
    elif(random_generator == "scissors" and userInput == "paper"):
        print(f'User loses {random_generator} to {userInput}'  )
    elif(random_generator == "scissors" and userInput == "scissors"):
        print(f'Same choice both scissors ')
    elif(userInput == "exit"):
        break
    else:
        print('''Please use from the these choices 
              1.Rock 
              2.Paper
              3.Scissors
              4.Exit''')
        