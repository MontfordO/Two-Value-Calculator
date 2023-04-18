print("This software will make a calculation based on two given numbers. The calculation will then be stored inside the .txt file you have specified.")
print("------------------------------------------------------------")
print("Would you like to create a new .txt file for the software to output answers to?")
print("Or would you prefer to use an existing .txt file inside this directory?")
print("------------------------------------------------------------")
fileSelection = input("NEW or EXISTING : ").lower().strip(" ")
fileSelectionCheck = False

while fileSelectionCheck is False :

    if fileSelection == "new" :
        
        newFileCheck = False
        # This loop will exit if no file with the the same name is found in the directory and a new .txt file will be made
        # If a file with the same name is found, the user will be asked if they'd like to either overwrite the existing file, or use the existing file
        while newFileCheck is False :
            
            fileName = input("Enter name of new input file: ")
            fileName = fileName + ".txt"

            try :
                f = open(fileName,mode="r",encoding="utf-8")
                f.close()

            except FileNotFoundError :
                newFileCheck = True
                fileSelectionCheck = True

                f = open(fileName,mode="w",encoding="utf-8")
                f.close()

                print("File created: " + fileName)

            else:
                print("An existing file with this name was found in the directory.")
                reselectionOption = input("Would you like to use the existing file instead? (Y/N) : ").lower().strip(" ")
                reselectionCheck = True
                while reselectionCheck is True:

                    if reselectionOption == "y" :
                        reselectionCheck = False
                        fileSelection = "useExisting"
                        newFileCheck = True
                    
                    elif reselectionOption == "n" :
                        reselectionCheck = False
                        renameOption = input("Would you like to rename the new file? If no, the existing file will be overwritten. (Y/N) : ").lower().strip(" ")

                        if renameOption == "y" :
                            break

                        elif renameOption == "n" :
                            fileSelection = "overwrite"
                            break

                        else :
                            print("That option was invalid. Make sure you are selecting either Y/N")

                    else :
                        print("That option was invalid. Make sure you are selecting either Y/N")
                        reselectionOption = input("Would you like to use the existing file instead? (Y/N) : ").lower().strip(" ")            

    elif fileSelection == "existing" :
        fileName = input("Input name of existing file: ").replace(".txt","").strip(" ")
        existingFileCheck = False
        # This loop will not exit until an existing file has been found in the directory
        # If an existing file is not found, the user will be asked if they'd like to create a new file with the entered name, in which the loop will be redirected to the "new" section
        while existingFileCheck is False :
            try :
                f = open(fileName + ".txt",mode="r",encoding="utf-8")
                f.close()

            except FileNotFoundError :
                print("The file could not be found in the directory.")
                print("Be aware of these factors - ")
                print("-- The file is a .txt file")
                print("-- The file is in the directory (folder) alongside this .py file")
                print("-- The capitalisation is correct")
                print("-- You do not need to include \".txt\" in the input")
                print("------------------------------------------------------------")
                reselectionOption = input("Would you like to make a new file instead? (Y/N) : ").lower().strip(" ")
                reselectionCheck = False

                while reselectionCheck is False:
                    if reselectionOption == "y" :
                        fileSelection = "new"
                        reselectionCheck = True
                        existingFileCheck = True

                    elif reselectionOption == "n" :
                        reselectionCheck = True
                        existingFileCheck = True
                    
                    else :
                        print("That option was invalid. Make sure you are selecting either Y/N")
                        reselectionOption = input("Would you like to make a new file instead? (Y/N) : ").lower().strip(" ")
                        print("------------------------------------------------------------")

            else :
                fileSelectionCheck = True
                existingFileCheck = True
                fileName = fileName + ".txt"

    elif fileSelection == "useExisting" :
        break

    elif fileSelection == "overwrite" :
        f = open(fileName,mode="w",encoding="utf-8")
        f.close()
        print("File overwritten: " + fileName)
        break

    else :
        print("Your file selection input was not valid. Please confirm either NEW or EXISTING")
        print("------------------------------------------------------------")
        fileSelection = input("NEW or EXISTING : ").lower().strip(" ")

print("Using file: " + fileName)

if fileSelection == "useExisting" or fileSelection == "existing" :
    print("------------------------------------------------------------")
    overwriteSelect = input("Would you like to overwrite the contents of the file, or add to the current contents? (OVERWRITE/ADD) : ").lower().strip(" ")
    overwriteCheck = False    
    while overwriteCheck is False :
        if overwriteSelect == "overwrite" :
            f = open(fileName,mode="w",encoding="utf-8")
            print(f"Contents of {fileName} cleared.")
            break
        elif overwriteSelect == "add" :
            break
        else :
            print("Your input was not valid. Please confirm either OVERWRITE or ADD ")
            print("------------------------------------------------------------")
            overwriteSelect = input("Would you like to overwrite the contents of the file, or add to the current contents? (OVERWRITE/ADD) : ").lower().strip(" ")

print("------------------------------------------------------------")
operationSelect = input("Would you like to make a calculation, or view the current log of results stored in the .txt file? (CALC/LOG) : ").lower().strip(" ")
operationCheck = True
while operationCheck is True:
    
    if operationSelect == "calc" :
        # This segment will check the number input against an exception
        # If the ValueError comes back as true, the number check variable will stay false
        # I chose to specify ValueError as this is the common exception in this case
        # Only when a valid int input is given will the while loop break
        number_check = False
        while number_check is False :
            try :
                number1 = float(input("Enter the first number : "))

            except ValueError :
                print("The input is not a number")

            else :
                number_check = True

        number_check = False

        while number_check is False :
            try :
                number2 = float(input("Enter the second number : "))

            except ValueError :
                print("The input is not a number")

            else :
                number_check = True

        # The while loop in this segment will confirm if a valid operation (+,-,x,/) has been input

        operation = input("Input the operation type (+,-,x,/) : ")

        while (operation != "+") and (operation != "-") and (operation != "x") and (operation != "/") :
            operation = str(input("The operation selection was not valid - input one of the following operation types (+,-,x,/) : "))

        print("------------------------------------------------------------")

        # If a valid input has been received, the if/elif segment will perform the required calculation
        # Making the last statement else or elif (remaining operation) is interchangeable in this scenario, as only 4 possible inputs can filter through from the while loop
        if operation == "+" :
            result = number1+number2
            print(f"Your calculation is : {number1} + {number2}")
            print(f"The result of your calculation is : {result}")
            
            f = open(fileName,mode="a",encoding="utf-8")
            f.write("\n")
            f.write(f"{number1} + {number2} = {result}")
            print("This result has been recorded in the text file")

        elif operation == "-" :
            result = number1-number2
            print(f"Your calculation is : {number1} - {number2}")
            print(f"The result of your calculation is : {result}")
            
            f = open(fileName,mode="a",encoding="utf-8")
            f.write("\n")
            f.write(f"{number1} - {number2} = {result}")
            print("This result has been recorded in the text file")

        elif operation == "x" :
            result = number1*number2
            print(f"Your calculation is : {number1} x {number2}")
            print(f"The result of your calculation is : {result}")

            f = open(fileName,mode="a",encoding="utf-8")
            f.write("\n")
            f.write(f"{number1} x {number2} = {result}")   
            print("This result has been recorded in the text file")

        elif operation == "/" :
            result = number1/number2
            print(f"Your calculation is : {number1} / {number2}")
            print(f"The result of your calculation is : {result}")

            f = open(fileName,mode="a",encoding="utf-8")
            f.write("\n")
            f.write(f"{number1} / {number2} = {result}")
            print("This result has been recorded in the text file")
        
        print("------------------------------------------------------------")
        newOperation = input("Would you like to perform another operation? (Y/N) : ").lower().strip(" ")

        newOperationCheck = True
        while newOperationCheck is True :
            # This segment will check whether the input given is valid
            if newOperation == "y" :
                operationSelect = ""
                operationSelect = input("Would you like to make a calculation, or view the current log of results stored in the .txt file? (CALC/LOG) : ").lower().strip(" ")

                newOperationOptionCheck = False

                while newOperationOptionCheck is False :

                    if operationSelect == "calc" :
                        newOperationCheck = False
                        break

                    elif operationSelect == "log" :
                        newOperationCheck = False
                        break

                    else :
                        print("Your input was not valid. Please confirm either CALC or LOG")
                        print("------------------------------------------------------------")
                        operationSelect = input("Would you like to make a calculation, or view the current log of results stored in the .txt file? (CALC/LOG) : ").lower().strip(" ")

            elif newOperation == "n" :
                operationCheck = False
                break
                
            else :
                print("Your input was not valid. Please confirm either Y or N")
                print("------------------------------------------------------------")
                newOperation = input("Would you like to perform another operation? (Y/N) : ").lower().strip(" ")

    elif operationSelect == "log" :
        print("------------------------------------------------------------")
        print("Current calculation list: ")
        f = open(fileName,mode="r",encoding="utf-8")
        print(f.read())
        print("------------------------------------------------------------")
        newOperationCheck = True
        newOperation = input("Would you like to perform another operation? (Y/N) : ").lower().strip(" ")
        while newOperationCheck is True :
        # This segment will check whether the input given is valid
            if newOperation == "y" :
                print("------------------------------------------------------------")
                operationSelect = ""
                operationSelect = input("Would you like to make a calculation, or view the current log of results stored in the .txt file? (CALC/LOG) : ").lower().strip(" ")
                newOperationOptionCheck = False
                # This segment will check whether the input given is valid
                while newOperationOptionCheck is False :

                    if operationSelect == "calc" :
                        newOperationCheck = False
                        break

                    elif operationSelect == "log" :
                        newOperationCheck = False
                        break

                    else :
                        print("Your input was not valid. Please confirm either CALC or LOG")
                        newOperationOptionCheck = True

            elif newOperation == "n" :
                operationCheck = False
                break
                
            else :
                print("Your input was not valid. Please confirm either Y or N ")
                print("------------------------------------------------------------")
                newOperation = input("Would you like to perform another operation? (Y/N) : ").lower().strip(" ")
    
    else :
        print("Your input was not valid. Please confirm either CALC or LOG")
        print("------------------------------------------------------------")
        operationSelect = input("Would you like to make a calculation, or view the current log of results stored in the .txt file? (CALC/LOG) : ").lower().strip(" ")

print("------------------------------------------------------------")
input("Operation(s) complete")

## As an afternote - there may be some parts not annotated for explanation regarding the use of bool variables labelled "-Check"
## I used this technique consistently throughout this script, as it felt like the most logical way to defend queries against invalid inputs
## The theory is that once the necessary checks have been made against the input given by the user, the code can continue without outlying variables
## I understand this may not be the most memory-efficient technique, however it has seemed to cover most potential invalid inputs without using try exceptions too often