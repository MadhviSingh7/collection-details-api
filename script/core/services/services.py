from script.core.utilities.db import client
from script.core.utilities.logger import logger
from bson import ObjectId

# Convert ObjectId to string
def serialize(doc):

    doc["_id"] = str(doc["_id"])
    return doc


def get_databases():

    logger.info("TEST LOG - get_databases called")

    try:
        dbs = client.list_database_names()

        logger.info("Fetched Databases")

        return dbs

    except Exception as e:

        logger.error("Error fetching databases: " + str(e))

        raise Exception(str(e))


# Get Collections
def get_collections(db_name):

    try:
        db = client[db_name]

        cols = db.list_collection_names()

        logger.info(f"Fetched Collections from {db_name}")

        return cols

    except Exception as e:

        logger.error("Collection Error: " + str(e))

        raise Exception(str(e))


# Get Documents
def get_documents(db_name, collection):
    try:
        db = client[db_name]
        col = db[collection]

        # Only fetch documents that are not soft deleted
        docs = [serialize(x) for x in col.find({"is_deleted": False})]

        logger.info(f"Fetched Documents from {db_name}.{collection}")
        return docs

    except Exception as e:
        logger.error("Fetch Document Error: " + str(e))
        raise Exception(str(e))


def generate_employee_id(db_name, collection):
    """
    Generate next employee_id like emp_101, emp_102...
    """
    db = client[db_name]
    col = db[collection]

    # Find the last employee_id in the collection
    last_doc = col.find_one(sort=[("employee_id", -1)])  # descending order
    if last_doc and "employee_id" in last_doc:
        last_id_num = int(last_doc["employee_id"].split("_")[1])
        next_id = f"emp_{last_id_num + 1}"
    else:
        next_id = "emp_101"  # start if no documents

    return next_id

#create document
def create_document(db_name, collection, data):
    try:
        db = client[db_name]
        col = db[collection]

        # Generate employee_id automatically
        if "employee_id" not in data:
            data["employee_id"] = generate_employee_id(db_name, collection)

        # Soft delete default
        data["is_deleted"] = False

        result = col.insert_one(data)
        logger.info(f"Inserted Document in {db_name}.{collection}")
        return str(result.inserted_id)

    except Exception as e:
        logger.error("Insert Error: " + str(e))
        raise Exception(str(e))


# Update Document
def update_document(db_name, collection, id, data):

    try:
        db = client[db_name]
        col = db[collection]

        object_id = ObjectId(id)

        result = col.update_one(
            {"_id": object_id},
            {"$set": data}
        )

        logger.info(f"Updated Document {id} in {db_name}.{collection}")

        return result.modified_count

    except Exception as e:

        logger.error("Update Error: " + str(e))

        return 0


# Delete Document
def delete_document(db_name, collection, id):
    try:
        db = client[db_name]
        col = db[collection]

        # Soft delete: mark is_deleted True
        result = col.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"is_deleted": True}}
        )

        logger.info(f"Soft Deleted Document {id} in {db_name}.{collection}")

        return result.modified_count  # 1 if document updated, 0 if not found

    except Exception as e:
        logger.error("Delete Error: " + str(e))
        return 0