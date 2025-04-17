def in_range(n: int, low: int, high: int) -> bool:
   
    return low <= n <= high

def main():
    
    
    num = int(input("Enter a number to check: "))
    
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))


    if high <= low:
        print("Error: Upper bound must be greater than lower bound.")
        return


    if in_range(num, low, high):
        
        print(f"{num} is between {low} and {high} (inclusive).")
        
    else:
        
        print(f"{num} is NOT between {low} and {high} (inclusive).")



if __name__ == "__main__":
    main()