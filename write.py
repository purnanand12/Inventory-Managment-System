#Importing datetime module to print present date and time while generating an invoice:
import datetime

def Generate_Rent_Invoice(customer_name, phone_number, address, customer_rented_details):
    """
    This function takes customer name, phone number, address and details of transaction as a parameters.
    It generate the invoice in the file.           
    """

    purchase_details = customer_rented_details

    grand_total = 0 #Calculating the grand total amount of all the equipments that the customer rent:
    for row in range(len(purchase_details)):
        grand_total += int(purchase_details[row][3])
    
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hours = str(datetime.datetime.now().hour)
    minutes = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    
    rented_year = year+"-"+month+"-"+day
    rented_hours = hours+"-"+minutes+"-"+second
    file_name = "Rent "+customer_name+" "+rented_hours+".txt"

    serial_number = 1
    
    file = open(file_name,"w")
    file.write("---------------------------------------------------------------------------------------------------------"+"\n")
    file.write("\t\t\t\tParty Equipments Rental Store\t\t\tPhone: 086-102040"+"\n")
    file.write("\t\t\t\t\tKathmandu \t\t\t\tEmail: panj45@gmail.com"+"\n\n")
    file.write("Customer Name: "+customer_name+"\t\t\tRENT INVOICE\t\t\t\t"+"Date: "+rented_year+"\n\n")
    file.write("Phone Number : "+phone_number)
    file.write("\t\t\t\t\t\t\t\tTime: "+rented_hours+"\n\n")
    file.write("Address      : "+address+"\n\n")
    file.write("---------------------------------------------------------------------------------------------------------"+"\n")
    file.write("S.N   ""Equipment Name\t\t\tBrand Name\t\tQuantity\t\tTotal Amount"+"\n")
    file.write("---------------------------------------------------------------------------------------------------------"+"\n")
    for row in range(len(customer_rented_details)):
        file.write(str(serial_number)+"     "+str(customer_rented_details[row][0])+"\t\t\t"+str(customer_rented_details[row][1])+"\t\t\t"+str(customer_rented_details[row][2])+"\t\t\t"+"$"+str(customer_rented_details[row][3])+"\n\n")
        serial_number += 1
    file.write("---------------------------------------------------------------------------------------------------------"+"\n\n")
    file.write("\t\t\t\t\t\t\t\tTotal Rented Amount:\t$"+str(grand_total))
    file.close()    
    


def Update_Stock_Rent(new_items):
    """
    This function takes 2-D lists of equipments in which number of quantities of equipments are updated after renting
    and re-write the file again.
    """
    
    available_items = new_items
    file = open("Equipments.txt","w")
    for row in range(len(available_items)):
        for col in range(len(available_items[row])):
            file.write(str(available_items[row][col]))
            if col < len(available_items[row]) - 1:
                file.write(",")
        file.write("\n")
    file.close()


def Update_Stock_Return(new_items):
    """
    This function takes 2-D lists of equipments in which number of quantities of equipments are updated after returning
    and re-write the file again.
    """
    
    available_items = new_items
    file = open("Equipments.txt","w")
    for row in range(len(available_items)):
        for col in range(len(available_items[row])):
            file.write(str(available_items[row][col]))
            if col < len(available_items[row]) - 1:
                file.write(",")
        file.write("\n")
    file.close()

def Generate_Return_Invoice(customer_name, phone_number, address, customer_returned_details):
    """
    This function takes customer name, phone number, address and details of transaction as a parameters.
    It generate the invoice in the file.           
    """

    purchase_details = customer_returned_details

    grand_total_rented_amount = 0 #Calculating the grand total amount of all the equipments that the customer rent:  
    grand_total_fined_amount = 0 #Calculating the grand total fined amount of all the equipments:
    for row in range(len(purchase_details)):
        grand_total_rented_amount += int(purchase_details[row][3])
        grand_total_fined_amount += int(purchase_details[row][4])
        
    
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hours = str(datetime.datetime.now().hour)
    minutes = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    
    returned_year = year+"-"+month+"-"+day
    returned_hours = hours+"-"+minutes+"-"+second
    file_name = "Return "+customer_name+" "+returned_hours+".txt"

    serial_number = 1
    
    file = open(file_name,"w")
    file.write("-----------------------------------------------------------------------------------------------------------------------------"+"\n")
    file.write("\t\t\t\t\tParty Equipments Rental Store\t\t\t\t\tPhone: 086-102040"+"\n")
    file.write("\t\t\t\t\t\tKathmandu \t\t\t\t\t\tEmail: panj45@gmail.com"+"\n\n")
    file.write("Customer Name: "+customer_name+"\t\t\tRETURN INVOICE\t\t\t\t\t\t"+"Date: "+returned_year+"\n\n")
    file.write("Phone Number : "+phone_number)
    file.write("\t\t\t\t\t\t\t\t\t\tTime: "+returned_hours+"\n\n")
    file.write("Address      : "+address+"\n\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------------"+"\n")
    file.write("S.N   ""Equipment Name\t\t\tBrand Name\t\tQuantity\t\tTotal Amount\t\tFined Amount"+"\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------------"+"\n")
    for row in range(len(customer_returned_details)):
        file.write(str(serial_number)+"     "+str(customer_returned_details[row][0])+"\t\t\t"+str(customer_returned_details[row][1])+"\t\t\t"+str(customer_returned_details[row][2])+"\t\t\t"+"$"+str(customer_returned_details[row][3])+"\t\t\t"+"$"+str(customer_returned_details[row][4])+"\n\n")
        serial_number += 1
    file.write("-----------------------------------------------------------------------------------------------------------------------------"+"\n\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\tTotal Rented Amount:\t$"+str(grand_total_rented_amount)+"\n\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\tTotal Fined Amount:\t$"+str(grand_total_fined_amount)+"\n\n")            
    file.close() 
