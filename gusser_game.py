import random
print("Welcome to random number gusser game")
print("I will guss number from 1 to 100 ")
Difficulty = str(input("What is your difficulty Easy or hard:- ")).lower()
def difficiulty(Difficulty):
    random_number = random.randint(1,100)
    if Difficulty == "easy":
        print("you will get 10 chances")
        chances = 10
        while True:
            number_choosen = int(input("Guss the number now:- "))
            if number_choosen != random_number:
                chances -= 1
                if chances == 0:
                    return "You Lost"
                    break
                else:
                    print("Not correct number")
            else:
                return "you won"
    elif Difficulty == "hard":
        chances = 5
        print("You will get 5 chances")
        while True:
            number_choosen = int(input("Guss the number now:- "))
            if number_choosen != random_number:
                chances -= 1
                if chances == 0:
                    return "You Lost"
            else:
                return "You Won"
print(difficiulty(Difficulty))
