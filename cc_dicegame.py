import random

high_score = 0

def roll_dice():
        global high_score
        roll_a = random.randint(1, 6)
        roll_a2 = random.randint(1, 6)
        total = roll_a + roll_a2

        print("You roll a...", str(roll_a))
        print("You roll a...", str(roll_a2))
        print()

        print("You have rolled a total of: ",str(total))
        print()

        if total > high_score:
            print("New high score!")
            print()
            high_score = total
            



def dice_game():
        while True:
            print("Current High Score: ",str(high_score))

            choice = input("1) Roll Dice\n2) Leave Game\nEnter Your choice: ")
            print() 

            if choice == "1":
                roll_dice()
            elif choice == "2":
                  print("Goodbye!")
                  break
            else:
                  continue
                
dice_game()
