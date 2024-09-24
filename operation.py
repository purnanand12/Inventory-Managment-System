#Import the read module
#Import the write module
#Import the datetime module
import read
import write
import datetime

#Call the function of read module that return all the available equipments as 2-D Array which are stored in a variable:
available_items = read.Available_Products()

def Display_Available_Items():
    """
    This function prints the availble equipments with their serial number, equipment name, brand name, price and number of quantity
    in a tabular form.
    """
    
    print("S.N\tName\t\t\tBrand\t\tPrice\t\tQuantity")
    print("------------------------------------------------------------------------------")
    print()
    serial_number = 1
    for row in range(len(available_items)):
        for col in range(len(available_items[row])):
            if col == 0 :
                print(serial_number,"     ",available_items[row][col],end="\t\t")
            else:
                print(available_items[row][col],end="\t\t")
        print("\n")
        serial_number += 1
    print("------------------------------------------------------------------------------")

def Rent_Equipments():
    """
    This function displays all the available equipments at the store. Then it asks to the customer equipment ID, number of quantity,
    number of days, name of the customer, phone number, and address to rent. It updates the number of quantity and generates an invoice
    on the screen and also in the file.
    """

    customer_rented_details = []
    
    continue_display = False
    while continue_display == False:        

        #Display all the available equipments at the store:
        print("All the available equipments at our store are listed below:")
        print()
        print("------------------------------------------------------------------------------")
        print("S.N\tName\t\t\tBrand\t\tPrice\t\tQuantity")
        print("------------------------------------------------------------------------------")
        print()
        symbol_number = 1
        for row in range(len(available_items)):
            for col in range(len(available_items[row])):
                if col == 0 :
                    print(symbol_number,"     ",available_items[row][col],end="\t\t")
                else:
                    print(available_items[row][col],end="\t\t")
            print("\n")
            symbol_number += 1
        print("------------------------------------------------------------------------------")

        #Select the equipment ID and check the valid equipment ID:
        equipment_ID = 0
        
        continue_loop = False
        while continue_loop == False:        
            try:
                equipment_ID = int(input("Enter a valid equipment ID to rent: "))
                print()
                if equipment_ID <= 0 or equipment_ID > (len(available_items)):
                    print("Invalid equipment Id")
                    print()
                else:
                    continue_loop = True
            except ValueError:
                print()
                print("Invalid equipment Id")
                print()

        #Display the details of the equipment according to the user's equipment ID:
        print("All the details of the selected equipments are given below:")
        print()
        print("------------------------------------------------------------------------------")
        print("S.N\tName\t\t\tBrand\t\tPrice\t\tQuantity")
        print("------------------------------------------------------------------------------")
        print()
        equipment_number = equipment_ID
        for row in range(equipment_ID-1,len(available_items)):
            for col in range(len(available_items[row])):
                if col == 0 :
                    print(equipment_number,"     ",available_items[row][col],end="\t\t")
                else:
                    print(available_items[row][col],end="\t\t")
            break
        print()
        print("------------------------------------------------------------------------------")
        print()

        
        #Input total number of the quantity of equipment to rent:
        number_Of_Quantity = 0

        total_quantity = int(available_items[equipment_ID-1][3])
    
        if total_quantity == 0:
            print("Dear sir/madam, the items you have selected is no more at our store. Please select another equipments.")
            print()
            continue
        else:            
            loop = False
            while loop == False:
                try:
                    number_Of_Quantity = int(input("Enter the total number of quantity to rent: "))
                    print()
                    if number_Of_Quantity > total_quantity:
                        print("Dear Sir/Madam, the number of quantities you provide are out of stock.")
                        print()                
                    elif number_Of_Quantity <= 0:
                        print("Invalid number of quantity")
                        print()
                    else:
                        loop = True
                except ValueError:
                    print()
                    print("Invalid number of quantity")
                    print()

        #Update the number of quantity after renting:
        new_quantity = total_quantity - number_Of_Quantity
        available_items[equipment_ID-1][3] = new_quantity
        write.Update_Stock_Rent(available_items)    
        
        #Input total number of days to rent:
        rented_days = 0

        finish = False
        while finish == False:        
            try:
                rented_days = int(input("Enter number of days to rent: "))
                print()
                if rented_days <= 0:
                    print("Invalid numbe of days")
                    print()
                else:
                    finish = True
            except ValueError:
                print()
                print("Invalid numbe of days")
                print()

        #Calculate the total amount of selected equipment:
        total_amount = 0
        
        price = available_items[equipment_ID-1][2]
        price_of_selected_equipment = price.replace("$","")
        if rented_days <=5:
            total_amount = int(number_Of_Quantity) * int(price_of_selected_equipment)
        else:
            total_amount = int(number_Of_Quantity) * int(price_of_selected_equipment) * int((rented_days+4)//5)
            

        #Store the details of transaction in 2-D Array:
        duplicate_equipment_name = False
        for item in customer_rented_details:
            if item[0] == str(available_items[equipment_ID-1][0]):
                item[2] += int(number_Of_Quantity)
                item[3] += int(total_amount)
                duplicate_equipment_name = True
                break
            
        if not duplicate_equipment_name:
            new_rent = [available_items[equipment_ID-1][0],available_items[equipment_ID-1][1], number_Of_Quantity, total_amount]
            customer_rented_details.append(new_rent)

        #Ask if customer wants to rent more:
        continue_rent = input("Would you like to rent more from our store?\n\nYes/No\n\n")
        print()
        display = False
        while display == False:
            if continue_rent.lower() == "yes":
                display = True
            elif continue_rent.lower() == "no":
                display = True
            else:
                print()
                continue_rent = input("Would you like to rent more from our store?\n\nYes/No\n\n")
                print()
        if continue_rent.lower() == "no":
            continue_display = True
        else:
            continue_display = False

    #Ask for customer's personal details to generate an invoice:
    print("----------------------------------------------------------------------------------")
    print()
    print("Please provide your following personal information to generate an invoice of transaction.")
    print()
    customer_name = input("Enter your full name: ")
    print()
    phone_number = 0

    #Check the valid phone number:
    right_number = False
    while right_number == False:
        try:            
            phone_number = input("Enter you phone number: ")
            if int(phone_number) <= 0:
                print()
                print("Invalid phone number")
                print()
                continue
            else:
                right_number = True
        except ValueError:
            print()
            print("Invalid phone number")
            print()
    
    print()
    address = input("Enter your address: ")
    print()
    print("----------------------------------------------------------------------------------")

    #Generate and display the invoice on the screen:
    grand_total = 0
    for row in range(len(customer_rented_details)):
        grand_total += int(customer_rented_details[row][3])
    
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hours = str(datetime.datetime.now().hour)
    minutes = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    
    rented_year = year+"-"+month+"-"+day
    rented_hours = hours+"-"+minutes+"-"+second

    serial_number = 1
    
    print("---------------------------------------------------------------------------------------------------------")
    print()
    print("\t\t\t\tParty Equipments Rental Store\t\t\tPhone: 086-102040")
    print()
    print("\t\t\t\t\tKathmandu \t\t\t\tEmail: panj45@gmail.com")
    print()
    print("Customer Name: "+customer_name,end="\t\t\t"+"RENT INVOICE\t\t\t\t"+"Date: "+rented_year)
    print("\n")
    print("Phone Number : "+phone_number,end="\t\t\t\t\t\t\t\tTime: "+rented_hours)
    print("\n")
    print("Address      : "+address)
    print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    print()
    print("S.N   ""Equipment Name\t\t\tBrand Name\t\tQuantity\t\tTotal Amount")
    print()
    print("---------------------------------------------------------------------------------------------------------")
    print()
    for row in range(len(customer_rented_details)):
        print(str(serial_number)+"     "+str(customer_rented_details[row][0])+"\t\t\t"+str(customer_rented_details[row][1])+"\t\t\t"+str(customer_rented_details[row][2])+"\t\t\t"+"$"+str(customer_rented_details[row][3]))
        serial_number += 1
        print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    print()
    print("\t\t\t\t\t\t\t\tTotal Rented Amount:\t$"+str(grand_total))

    #Generate the same invoice in a text file:
    write.Generate_Rent_Invoice(customer_name, phone_number, address, customer_rented_details)
    
def Return_Equipments():
    """
    This function displays all the available equipments at the store. Then it asks to the customer equipment ID, number of quantity,
    number of days while renting, number of days while returning,  name of the customer, phone number, and address to return.
    It updates the number of quantity and generates an invoice on the screen and also in the file.
    """

    customer_returned_details = []

    continue_display = False
    while continue_display == False:        

        #Display all the available equipments at the store:
        print("All the available equipments at our store are listed below:")
        print()
        print("------------------------------------------------------------------------------")
        print("S.N\tName\t\t\tBrand\t\tPrice\t\tQuantity")
        print("------------------------------------------------------------------------------")
        print()
        symbol_number = 1
        for row in range(len(available_items)):
            for col in range(len(available_items[row])):
                if col == 0 :
                    print(symbol_number,"     ",available_items[row][col],end="\t\t")
                else:
                    print(available_items[row][col],end="\t\t")
            print("\n")
            symbol_number += 1
        print("------------------------------------------------------------------------------")

        #Select the equipment ID and check the valid equipment ID:
        equipment_ID = 0
        
        continue_loop = False
        while continue_loop == False:        
            try:
                equipment_ID = int(input("Enter a valid equipment ID of whose equipments that you want return: "))
                print()
                if equipment_ID <= 0 or equipment_ID > (len(available_items)):
                    print("Invalid equipment Id")
                    print()
                else:
                    continue_loop = True
            except ValueError:
                print()
                print("Invalid equipment Id")
                print()
    
        
        #Input total number of the quantity of equipment to rent:
        number_Of_Quantity = 0

        total_quantity = int(available_items[equipment_ID-1][3])
        
        loop = False
        while loop == False:
            try:
                number_Of_Quantity = int(input("Enter the total number of quantity that you want to return: "))
                print()               
                if number_Of_Quantity <= 0:
                    print("Invalid number of quantity")
                    print()
                else:
                    loop = True
                    
            except ValueError:
                    print()
                    print("Invalid number of quantity")
                    print()
        
        #Update the number of quantity after returning:
        new_quantity = total_quantity + number_Of_Quantity
        available_items[equipment_ID-1][3] = new_quantity
        write.Update_Stock_Return(available_items)

        #Input total number of days while renting and returning:
        rented_days = 0
        returned_days = 0

        finish = False
        while finish == False:        
            try:
                rented_days = int(input("Enter number of days while renting: "))
                print()
                if rented_days <= 0:
                    print("Invalid number of rented days")
                    print()
                    continue
                returned_days = int(input("Enter number of days while returning: "))
                print()
                if returned_days <= 0:
                    print("Invalid number of returned days")
                    print()
                    continue
                else:
                    finish = True
                print()
            except ValueError:
                print()
                print("Invalid number of days")
                print()

        #Calculate the total amount of selected equipment:
        price = available_items[equipment_ID-1][2]
        price_of_selected_equipment = price.replace("$","")

        total_rented_amount = 0
        
        if rented_days <=5:
            total_rented_amount = int(number_Of_Quantity) * int(price_of_selected_equipment)
        else:
            total_rented_amount = int(number_Of_Quantity) * int(price_of_selected_equipment) * int((rented_days+4)//5)

        #Calculate the total fined amount of selected equipment:
        total_fined_amount = 0

        if returned_days <= rented_days:
            total_fined_amount = 0
        else:

            #If the quotient of rented days and returned days are equal:
            if ((rented_days+4)//5) == ((returned_days+4)//5):
                total_fined_amount = 0
            else:
                fine_per_day = int(price_of_selected_equipment)/5

                #If rented days is multiple of 5 then calculating fined amount directly by multiplying the difference:
                if rented_days%5 == 0:
                    difference_in_days = returned_days - rented_days
                    total_fined_amount = int(number_Of_Quantity) * int(fine_per_day) * int(difference_in_days)
                else:
                    rented_days_quotient = rented_days//5

                    #Find the number of remaining days to make rented days a multiple of 5:
                    remaining_days = (rented_days_quotient + 1)*5 - rented_days

                    #Find the difference in days after making the rented days multiple of 5 and then calculating fined amount:
                    final_days = returned_days - (rented_days + remaining_days)
                    
                    total_fined_amount = int(number_Of_Quantity) * int(fine_per_day) * int(final_days)                                                                    
                
            
        #Store the details of transaction in 2-D Array:
        duplicate_equipment_name = False
        for item in customer_returned_details:
            if item[0] == str(available_items[equipment_ID-1][0]):
                item[2] += int(number_Of_Quantity)
                item[3] += int(total_rented_amount)
                item[4] += int(total_fined_amount)
                duplicate_equipment_name = True
                break
            
        if not duplicate_equipment_name:
            new_return = [available_items[equipment_ID-1][0],available_items[equipment_ID-1][1], number_Of_Quantity, total_rented_amount, total_fined_amount]
            customer_returned_details.append(new_return)

        #Ask if customer wants to return more:
        continue_return = input("Would you like to returnn more?\n\nYes/No\n\n")
        print()
        display = False
        while display == False:
            if continue_return.lower() == "yes":
                display = True
            elif continue_return.lower() == "no":
                display = True
            else:
                print()
                continue_return = input("Would you like to return more?\n\nYes/No\n\n")
                print()
                
        if continue_return.lower() == "no":
            continue_display = True
        else:
            continue_display = False
    
    #Ask for customer's personal details to generate an invoice:
    print("----------------------------------------------------------------------------------")
    print()
    print("Please provide your following personal information to generate an invoice of transaction.")
    print()
    customer_name = input("Enter your full name: ")
    print()
    phone_number = 0
    
    #Check the valid phone number:
    right_number = False
    while right_number == False:
        try:            
            phone_number = input("Enter your phone number: ")
            if int(phone_number) <= 0:
                print()
                print("Please enter a valid number")
                print()
                continue
            else:
                right_number = True
        except ValueError:
            print()
            print("Invalid Phone Number")
            print()
    print()
    address = input("Enter your address: ")
    print()
    print("----------------------------------------------------------------------------------")

    #Generate and display the invoice on the screen:
    grand_total_rented_amount = 0
    grand_total_fined_amount = 0
    
    for row in range(len(customer_returned_details)):
        grand_total_rented_amount += int(customer_returned_details[row][3])
        grand_total_fined_amount += int(customer_returned_details[row][4])
    
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hours = str(datetime.datetime.now().hour)
    minutes = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    
    returned_year = year+"-"+month+"-"+day
    returned_hours = hours+"-"+minutes+"-"+second
   
    serial_number = 1
    
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print()
    print("\t\t\t\t\tParty Equipments Rental Store\t\t\t\t\tPhone: 086-102040")
    print()
    print("\t\t\t\t\t\tKathmandu \t\t\t\t\t\tEmail: panj45@gmail.com")
    print()
    print("Customer Name: "+customer_name,end="\t\t\t"+"RETURN INVOICE\t\t\t\t\t\t"+"Date: "+returned_year)
    print("\n")
    print("Phone Number : "+phone_number,end="\t\t\t\t\t\t\t\t\t\tTime: "+returned_hours)
    print("\n")
    print("Address      : "+address)
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print()
    print("S.N   ""Equipment Name\t\t\tBrand Name\t\tQuantity\t\tTotal Amount\t\tFined Amount")
    print()
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print()
    for row in range(len(customer_returned_details)):
        print(str(serial_number)+"     "+str(customer_returned_details[row][0])+"\t\t\t"+str(customer_returned_details[row][1])+"\t\t\t"+str(customer_returned_details[row][2])+"\t\t\t"+"$"+str(customer_returned_details[row][3])+"\t\t\t"+"$"+str(customer_returned_details[row][4]))
        serial_number += 1
        print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print()
    print("\t\t\t\t\t\t\t\t\t\t\tTotal Rented Amount:\t$"+str(grand_total_rented_amount))
    print()
    print("\t\t\t\t\t\t\t\t\t\t\tTotal Fined Amount:\t$"+str(grand_total_fined_amount))   

    #Generate the same invoice in a text file:
    write.Generate_Return_Invoice(customer_name, phone_number, address, customer_returned_details)


