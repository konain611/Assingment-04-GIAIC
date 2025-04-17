
def get_first_element(First):
 
    print(First[0])



def get_First():
   
    First = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        First.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return First

def main():
    First = get_First()
    get_first_element(First)


if __name__ == '__main__':
    main()

