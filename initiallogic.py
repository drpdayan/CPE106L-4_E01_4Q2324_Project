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


def get_lessee_list(mongo_uri="mongodb://localhost:27017/", database_name="ApartmentCollectionSystem", collection_name="Lessee_Information"):
    try:
        client = mc(mongo_uri)
        db = client[database_name]
        collection = db[collection_name]
        documents = list(collection.find())  
        return documents

    except mc.errors.PyMongoError as e:
        raise Exception(f"An error occurred while connecting to MongoDB: {e}")  



def find_lessee(unit):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    leese = db["Lessee_Information"]

    query = {"Unit": unit}
    projection = {"Lessee Name": 1, "Rental Purpose": 1, "TIN": 1}
    results = leese.find(query, projection)

    for x in results:
        lessee_info = {"Lessee Name": x["Lessee Name"], 
                       "Rental Purpose": x["Rental Purpose"], 
                       "TIN": x["TIN"]}
    return lessee_info



def check_unit(unit):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    unitstatus = db["Unit_Status"]

    query = {"Unit": unit}
    projection = {"Leasable Area": 1, "Occupancy Status": 1, "Lease Date": 1}
    results = unitstatus.find(query, projection)

    for x in results:
        unitstatus = {"Leasable Area": x["Leasable Area"], 
                       "Occupancy Status": x["Occupancy Status"], 
                       "Lease Date": x["Lease Date"]}
    return unitstatus



def update_unit(unit, status, date):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    unitstatus = db["Unit_Status"] 

    checkunit = unitstatus.find_one({"Unit": unit})
    while checkunit:
        if not checkunit:
            print(f"Unit Number '{unit}' not found.")
            return False
            
        # new_status = input("Enter New Occupancy Status (Occupied/Vacant):")
        new_status = status
        if new_status not in ("Occupied", "Vacant"):
            print("Invalid Input. Try Again")
            return False

        if new_status == "Occupied":
            # new_date = str(input("Enter New Lease Date (dd/mm/yyyy)"))
            new_date = str(date)
            unitstatus.update_one({"Unit":unit},{"$set":{"Occupancy Status": new_status, "Lease Date": new_date, "Lease Period": 1}})
            return True
        
        elif new_status == "Vacant":
            unitstatus.update_one({"Unit":unit},{"$set":{"Occupancy Status": new_status, "Lease Date": None, "Lease Period": 1}})
            return True



def update_lessee(unit, purpose, name, TIN):
    client = mc("mongodb://localhost:27017/")
    db = client["ApartmentCollectionSystem"]
    unitstatus = db["Lessee_Information"] 

    checkunit = unitstatus.find_one({"Unit": unit})
    while checkunit:
        if not checkunit:
            print(f"Unit Number '{unit}' not found.")
            return False
            
            
        # new_purpose= input("Enter Rental Purpose (Residential/Commercial/Vacant):")
        new_purpose = purpose

        
        if new_purpose not in ("Residential", "Commercial", "Vacant"):
            print("Invalid Input. Try Again")
            return False
        
        if new_purpose == "Vacant":
            unitstatus.update_one({"Unit":unit},{"$set":{"Lessee Name": None,"Rental Purpose": None ,"TIN": None}})
            return True

        elif new_purpose == "Residential" or "Commercial":
            # new_name = input("Enter New Lessee Name: ")
            new_name = name

            if new_purpose == "Residential":
                unitstatus.update_one({"Unit":unit},{"$set":{"Lessee Name": new_name,"Rental Purpose": new_purpose ,"TIN": None}})
                return True
            
            elif new_purpose == "Commercial":
                # new_TIN = int(input("Enter New TIN"))
                new_TIN = int(TIN)
                unitstatus.update_one({"Unit":unit},{"$set":{"Lessee Name": new_name,"Rental Purpose": new_purpose ,"TIN": new_TIN}})
                return True



    

def close_connection(client):
    client.close()

if __name__ == "__main__":
    x = input("Enter Unit Number: ")
    update_lessee(x)




  # # client = MongoClient(host="localhost", port=27017)
# client = mc("mongodb://localhost:27017/")

# # Get reference to 'chinook' database
# db = client["ApartmentCollectionSystem"]

# # Get a reference to the 'customers' collection
# lessee_info = db["Lessee_Information"]
# # print(lessee_info)

# client = mc("mongodb://localhost:27017/")
# db = client["ApartmentCollectionSystem"]
# lessee_info = db["Lessee_Information"]

# lessee_list= []

# for x in  lessee_info.find():
#     lessee_list.append(x)


# client.close()