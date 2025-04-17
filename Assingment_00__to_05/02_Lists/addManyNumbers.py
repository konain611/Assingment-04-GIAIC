

def add_many_numbers(numbers)-> int:
  
    total: int = 0
    for number in numbers:
        total += number

    return total

def main():
    numbers: list[int] = [17, 41, 93, 45, 51] 
    sum_of_numbers: int = add_many_numbers(numbers)  
    print(sum_of_numbers) 
    

if __name__ == '__main__':
    main()