import random

NUM_SIDES = 6

def main():
    
    dice1: int = random.randint(1, NUM_SIDES)
    dice2: int = random.randint(1, NUM_SIDES)
    
    total: int = dice1 + dice2
    
    print("Dice have", NUM_SIDES, "sides each")
    print("First die: " + str(dice1))
    print("Second die: " + str(dice2))
    print("Total of two dice: " + str(total))
    
if __name__ == "__main__":
    main()