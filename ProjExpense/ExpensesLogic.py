from pymongo import MongoClient as mc
import pprint
import re

client =mc("mongodb://127.0.0.1:27017/")
leese = None
db = None

def open_connection():
    try:
        db = client["ApartmentCollectionSystem"]
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
        
def get_unit_expense_all(unit):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    unitexpense = db["Unit_Expenses"] 

    checkunit = unitexpense.find_one({"Unit": unit})
    while checkunit:
        if not checkunit:
            print(f"Unit Number '{unit}' not found.")
            break

        UnitExpenseAll = []
        getunit = unitexpense.find({"Unit": unit})
        for x in getunit:
            x.pop("_id", None)
            UnitExpenseAll.append(x)
        break

    return UnitExpenseAll

def get_unit_expense_month(unit, month):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    unitexpense = db["Unit_Expenses"] 


    checkunit = unitexpense.find_one({"Unit": unit})
    while checkunit:
        if not checkunit:
            print(f"Unit Number '{unit}' not found.")
            return False

        UnitExpenseMonth = []
        new_month = month
        if new_month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
            print("Invalid Month. Try Again")
            return False
        
        # projection = {"Unit": 1, "Month": 1}
        getunit = unitexpense.find({"Unit": unit, "Month": month})

        
        for x in getunit:
            x.pop("_id", None)
            UnitExpenseMonth.append(x)
        break

    return UnitExpenseMonth

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
        
def delete_expense(unit, month):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    unitexpense = db["Unit_Expenses"] 


    checkunit = unitexpense.find_one({"Unit": unit})
    while checkunit:
        if not checkunit:
            print(f"Unit Number '{unit}' not found.")
            return False

        UnitExpenseMonth = []
        new_month = month
        if new_month not in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
            print("Invalid Month. Try Again")
            return False
        
        # projection = {"Unit": 1, "Month": 1}
        getunit = unitexpense.find({"Unit": unit, "Month": month})
        delete_doc = unitexpense.delete_one({"Unit": unit, "Month":month})
        
        getunit
        delete_doc

        if delete_doc.deleted_count >= 1:
            print("Document Deleted!")
            break
        else:
            print("No Document Found")
            break


def get_values(unit, month):
    UnitMonthlyExpense = get_unit_expense_month(unit, month)
    get_val = UnitMonthlyExpense[0]
    u_val = get_val['Unit']
    m_val = get_val['Month']
    r_val = get_val['Rent']
    e_val = get_val['Electricity']
    w_val = get_val['Water']
    o_val = get_val['Outstanding Balance']
    return u_val, m_val, r_val, e_val, w_val, o_val

def get_unit_expense_all_line(unit):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    unitexpense = db["Unit_Expenses"] 

    checkunit = unitexpense.find_one({"Unit": unit})
    while checkunit:
        if not checkunit:
            print(f"Unit Number '{unit}' not found.")
            break

        UnitExpenseAll = []
        getunit = unitexpense.find({"Unit": unit})
        for x in getunit:
            x.pop("_id", None)
            UnitExpenseAll.append(x)
        
        month_mapping = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11  ,"December": 12}
        for x in UnitExpenseAll:
            x["Month_Num"] = month_mapping.get(x["Month"], None)
            

        break

    return UnitExpenseAll

# if __name__ == "__main__":
#     unit = input("Enter Unit: ")
#     month = input("Enter Month: ")
#     get_unit_expense_month(unit, month)
#     print(get_unit_expense_month(unit, month))

# if __name__ == "__main__":
#     unit = input("Enter Unit: ")
#     get_unit_expense_all(unit)
#     print(get_unit_expense_all(unit))


# if __name__ == "__main__":
#     unit = input("Enter Unit: ")
#     month = input("Enter Month: ")
#     get_values(unit, month)
#     getit = get_values(unit, month)
#     u_val, m_val, r_val, e_val, w_val, o_val = getit
#     print(u_val, m_val, r_val, e_val, w_val, o_val)


# if __name__ == "__main__":
#     unit = input("Enter Unit: ")
#     month = input("Enter Month: ")
#     delete_expense(unit, month)

if __name__ == "__main__":
    unit = input("Enter Unit: ")
    get_unit_expense_all_line(unit)
    print(get_unit_expense_all(unit))
