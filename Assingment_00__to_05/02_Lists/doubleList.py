

def main():
    numbers: list[int] = [24, 92, 566, 246]  
    for i in range(len(numbers)): 
        elem_at_index = numbers[i] 
        numbers[i] = elem_at_index * 2  
        
        
    print(numbers) 
    
if __name__ == '__main__':
    main()