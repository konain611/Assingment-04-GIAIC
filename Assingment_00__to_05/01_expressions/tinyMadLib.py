SENTENCE_START: str = "\nCode in Place is fun. I learned to program and used Python to make my "

def main():
   
    adjective: str = input(" \033[1;3m Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter.\033[0m")

  
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")


if __name__ == '__main__':
    main()