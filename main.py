#Import the operation module
#Import the read module
#Import the write module
import operation
import read
import write

#Printing company's name, address, phone and email:
print()
print("\t\t\t\t\tParty Equipments Rental Store",end="\t\t\tPhone: 086-102040")
print("\t\t\t\t\t\t\t\t\t\tKathmandu",end="\t\t\t\tEmail: panj45@gmail.com")
print()
print("-----------------------------------------------------------------------------------------------------------------------------------")
print()
print("\t\t\t\t\tWelcome to our store!!")
print()
print("Dear Sir/Madam, we have the top branded rental equipments with very low costs. You are allowed to choose any of the options below.")
print("Please choose appropriate option.")
print()
print("-----------------------------------------------------------------------------------------------------------------------------------")
print()


def Main():
    """
    This function displays the option of display all the equipments, rent, return and exit option.
    """
    
    continue_Choice = False
    while continue_Choice == False:
        print()
        print("1. Display all the available equipments")
        print()
        print("2. To rent an equipments")
        print()
        print("3. To return an equipments")
        print()
        print("4. To exit")
        print()
        option = 0

        #Check the valid option:
        try:
            print("-----------------------------------------------------------------------------------------------------------------------------------")
            option = int(input("Enter your choice: "))
            print()
        except ValueError:
            print()
            print("Invalid Input")
        
            
        #Apply condition according to user's option:
        if option == 1:
            print("All the available equipments are listed below:")
            print()
            print("------------------------------------------------------------------------------")
            operation.Display_Available_Items()
            print()
                    
        elif option == 2:
            print()
            operation.Rent_Equipments()
            print()
                    
        elif option == 3:
            print()
            operation.Return_Equipments()
            print()
                    
        elif option == 4:
            print("Thanks for visiting us!! Please give us another chance in future")
            continue_Choice = True
                
        else:
            print()
            print("Please enter an appropriate option")

Main()
