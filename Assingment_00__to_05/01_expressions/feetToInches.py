

INCHES_PER_FOOT = 12

def main():
    
    feet: float = float(input("Enter feet: "))
    
    inches: float = feet * INCHES_PER_FOOT
    
    print(str(feet) + " feet is " + str(inches) + " inches")
    
if __name__ == "__main__":
    main()