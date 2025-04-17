import random

DONE_LIKELIHOOD = 0.3  # 30% chance to stop at each number

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return
        print(curr_num, end=' ')

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done")

if __name__ == "__main__":
    main()