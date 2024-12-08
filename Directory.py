#Program Name: Vehicle Inventory Program
#Program Author: Jon Langan      Date: 2024
#Program Objective: Running an "Automobile" class to be used by a car dealership
#as a vehicle inventory program. Class must include proper attributes. Program
#must also include a constructor, add/remove abilities, and capabilites to
#update vehicle information in inventory.
#------------------------------------------------------------------------
#Psuedocode:
#    1. Begin program with displaying what program is intended for
#    2. Intialize Automobile class and variables "init". This is considered
#        a constructor
#    3. Define "add vehicle" function and collect user input for car info
#    4. Define built-in "str" method that will turn the returning variables
#        from "add vehicle" function as a readable string
#    5. Intialize "CarList" list outside of class
#    6. Define "edit" function and ask what inventory entry needs edited
#        before taking new car info
#    7. Define main menu and user options
#    8. Include simple if/else branching path for each user option: add, delete,
#        show inventory, update inventory, export inventory, and quit program
#    9. The "if __name__" clause executes all top level code if imported but
#        not functions
#    10. Run program and allow user menu to intialize...
#------------------------------------------------------------------------

                 #Simple inventory program for car dealership lot
print("Automobile inventory for lot")
class Automobile:

    def __init__(self):  #Constructor used to hold and initialize variables
        self.__make = " "
        self.__model = " "
        self.__color = " "
        self.__year = 0
        self.__mileage = 0

    def add_vehicle(self):
        self.__make = input("Enter make: ")  #Defined function to add car
        self.__model = input("Enter model: ")  #information from user input
        self.__color = input("Enter color: ")
        self.__year = int(input("Enter year: "))
        self.__mileage = int(input("Enter mileage: "))

    def __str__(self):   #Built-in method that returns a readable string
        return("%d %s %s Color: %s Mileage: %d" %    #representation of an object
               (self.__year, self.__make, self.__model, self.__color, self.__mileage))

CarList = [] #Intialized outside of class and NOT in its scope

def edit(CarList):
        print(CarList)
        pos = int(input("Enter numerical spot of car being edited:  "))
        new_car = car.add_vehicle()    #Defined function to update inventory
        new_car = car.__str__()         #entry with new car information
        CarList[pos-1] = new_car
        print("Car updated!")

        
def main():
    menu = {}
    menu["1"]="Add Car."     #Defining each user option capable of being
    menu["2"]="Delete Car."     #selected and utilized
    menu["3"]="Update Inventory."
    menu["4"]="Show Inventory."
    menu["5"]="Export Complete Car Inventory."
    menu["6"]="Quit."
        
user=True 
while user:    #Creating user menu to be displayed on-screen
    print ("""     
    1. Add A Car
    2. Delete A Car
    3. Update Inventory
    4. Show Inventory
    5. Export Inventory
    6. Quit
    """)                #Simple branching if-else path for user options
    ans=input("What would you like to do? ")
    if ans=="1":   #Add Inv entry
        car = Automobile()   
        car.add_vehicle()
        CarList.append(car.__str__())
    elif ans=="2":  #Delete Inv entry
        if len(CarList) < 1:
            print("Currently no vehicles in inventory...")
            continue
        print(CarList)
        item = int(input("Enter numerical spot of car being deleted: "))
        if item - 1 > len(CarList):
            print("Invalid entry...")
        else:
            CarList.remove(CarList[item-1])
            print()
            print("This car has been deleted.")
    elif ans=="3":    #Update Inv entry
        edit(CarList)
    elif ans=="4":  #Show Inv
        print(CarList)
    elif ans=="5":   #Export
        f = open("vip.txt", "w")
        f.write(str(CarList))
        print("Success! Vehicle Inventory Program (VIP) file available on desktop!")
        f.close()
    elif ans=="6":  #End
        print("\n Ending program...")
        break
    elif ans !="":  #Invalid
        print("\n Please pick an option from the list.")

if __name__ == "__main__":
    main()
