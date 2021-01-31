

userinput = input("What year are we looking at: ")
#print(userinput)
if userinput % 4 == 0 and (userinput % 100 != 0 or userinput % 400 == 0):

    print( "The year " + str(userinput) + " is a leap year")
else:
    print( "The year " + str(userinput) + " is not a leap year")