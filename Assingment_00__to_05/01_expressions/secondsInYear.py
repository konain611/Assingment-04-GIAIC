
DAYS_IN_A_YEAR = 365
HOURS_IN_A_DAY = 24
MINUTES_IN_AN_HOUR = 60
SECONDS_IN_A_MINUTE = 60

def main():
    
    seconds_in_a_year: int = DAYS_IN_A_YEAR * HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR * SECONDS_IN_A_MINUTE
    
    print("There are " + str(seconds_in_a_year) + " Seconds in a year")
    
if __name__ == "__main__":
    main()