def get_last_element(Last):
 
    print(Last[-1])
    
def get_Last():
    
    Last = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        Last.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return Last

def main():
    Last = get_Last()
    get_last_element(Last)
    
    
if __name__ == '__main__':
    main()