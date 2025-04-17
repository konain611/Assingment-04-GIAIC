
C : int = 299792458

def main():
    
    massInKG: float = float(input("Enter mass in kilograms(kg): "))
    energyInJoules: float = massInKG * (C**2)
    
    print("e = mc^2...")
    print("m = " + str(massInKG) + " kg")
    print("c = " + str(C) + " m/s")
    
    print(str(energyInJoules) + " Joules of energy")
    
if __name__ == "__main__":
    main()