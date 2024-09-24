def Available_Products():
    
    """This function reads the text file and return all the available items as 2-D Array form"""
    file = open("Equipments.txt","r")
    equipments = file.read()
    file.close()
    
    items = equipments.split("\n")
    itemList = []
    for row in items:
                
        if row.strip(): #Checking if the row is empty or contains white space:
            values = row.split(",")
            itemList.append(values)
    return itemList

