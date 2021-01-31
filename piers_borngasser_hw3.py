

while True:

        userinput = raw_input("Please enter a positive year to check: ")

        if userinput.isdigit():
            check = int(userinput)
            if check % 4 == 0 and (check % 100 != 0 or check % 400 == 0):
                print( "The year " + str(check) + " is a leap year")
            else:
                print( "The year " + str(check) + " is not a leap year")
            break


        else:
            print("That is not a positive integer year")
            continue


    
