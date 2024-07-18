from pymongo import MongoClient as mc
import pprint
import re

client =mc("mongodb://127.0.0.1:27017/")
leese = None
db = None

def open_connection():
    try:
        # Get reference to 'chinook' database
        db = client["ApartmentCollectionSystem"]
        # # Get a reference to the 'customers' collection
        # customers_collection = db["customers"]
        # doc1 = customers_collection.find_one()
        return True
    except:
        return False


def check_unit(unit):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    unitexpense = db["Unit_Expenses"] 

    checkunit = unitexpense.find_one({"Unit": unit})
    if checkunit:
        print("Goodjob")
    else:
        print("GG")
        
#parameters (unit, check_out, outstanding, month, rent, electricity, water)
def add_expense(unit, month, check_out, outstanding,  rent, electricity, water):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    unitexpense = db["Unit_Expenses"] 

    checkunit = unitexpense.find_one({"Unit": unit})
    while checkunit:
        if not checkunit:
            print(f"Unit Number '{unit}' not found.")
            break
        
        
        # new_month = input("Enter Month: ")
        new_month = month
        if new_month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
            print("Invalid Month. Try Again")
            return False
        
        # check_outstanding= input("Outstanding Balance? y/n: ")
        check_outstanding = check_out
        if check_outstanding == True:
            # new_outstanding = float(input ("Enter Outstanding Balance Amount: "))
            new_outstanding = float(outstanding)
            if not isinstance(new_outstanding, float):
                print("Invalid Input Outstanding. Try Again.")
                return False
        else:
            new_outstanding = float(0.00)

        # new_rent =  float(input("Enter Rent: "))
        new_rent =  float(rent)
        if not isinstance(new_rent, float):
            print("Invalid Input Rent. Try Again.")
            return False

        # new_electricity = float(input("Enter Electricity Bill: "))
        new_electricity = float(electricity)
        if not isinstance(new_electricity, float):
            print("Invalid Input Elec. Try Again.")
            return False
        
        # new_water =  float(input("Enter Water Bill: "))
        new_water =  float(water)
        if not isinstance(new_water, float):
            print("Invalid Input Water. Try Again.")
            return False

        new_expense = {"Unit": unit, "Month": new_month, "Rent": new_rent, "Electricity": new_electricity, "Water": new_water, "Outstanding Balance": new_outstanding,}
        unitexpense.insert_many([new_expense])
        
        break
        


if __name__ == "__main__":
    add_expense("1G", "May", True, 1, 1.0, 1.0, 1.0)