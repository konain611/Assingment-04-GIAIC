def main():
    
    dividend: int = int(input("Enter dividend: "))
    divisor: int = int(input("Enter divisor: "))
    
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor
    
    print("Quotient is " + str(quotient))
    print("Remainder is " + str(remainder))
    
    print("Hence the result of " + str(dividend) + " / " + str(divisor) + " is " + str(quotient) + " with a remainder of " + str(remainder))
    
if __name__ == "__main__":
    main()