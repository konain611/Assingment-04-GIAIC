def main():
    list0 = [] 

    val = input("Enter a value: ") 
    
    
    while val:  
        list0.append(val) 
        val = input("Enter a value or press enter to stop: ") 

    print("Here's the list:", list0)



if __name__ == '__main__':
    main()