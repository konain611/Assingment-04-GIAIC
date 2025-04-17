def main():


    fahrenheit = input(" \033[1;3m Enter the temperature in Fahrenheit: \033[0m ")
    fahrenheit = float(fahrenheit)
    
    celsius = (fahrenheit - 32) * 5.0/9.0
    
    print(f"The temperature in Celsius is: {celsius:.2f}°C")

if __name__ == "__main__":
    main()