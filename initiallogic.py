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

def close_connection(client):
    client.close()

# if __name__ == "__main__":
#   lessee_list = get_lessee_list()
#   print(lessee_list)




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