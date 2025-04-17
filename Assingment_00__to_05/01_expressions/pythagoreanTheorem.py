import math

def main():
    
    ab: float = float(input("Enter length of side ab: "))
    ac: float = float(input("Enter length of side ac: "))
    
    bc: float = math.sqrt(ab**2 + ac**2)
    
    print("Length of side bc(hypotneous) is " + str(bc))
    
if __name__ == "__main__":
    main()