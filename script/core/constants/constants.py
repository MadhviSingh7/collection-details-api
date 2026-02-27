# RESPONSE STATUS

SUCCESS = "Success"
ERROR = "Error"

# SUCCESS MESSAGES

FETCH_DATABASES_SUCCESS = "Able to fetch DB details successfully"

FETCH_COLLECTIONS_SUCCESS = "Able to fetch collections from {db_name}"

FETCH_DOCUMENTS_SUCCESS = "Able to fetch documents from {db_name}.{collection}"

CREATE_DOCUMENT_SUCCESS = "Document created successfully"

UPDATE_DOCUMENT_SUCCESS = "Document updated successfully"

DELETE_DOCUMENT_SUCCESS = "Document deleted successfully"

# ERROR MESSAGES


DATABASE_FETCH_ERROR = "Unable to fetch database details"

COLLECTION_FETCH_ERROR = "Unable to fetch collections"

DOCUMENT_FETCH_ERROR = "Unable to fetch documents"

DOCUMENT_NOT_FOUND = "Document not found"

INSERT_ERROR = "Unable to insert document"

UPDATE_ERROR = "Unable to update document"

DELETE_ERROR = "Unable to delete document"


# ROUTES


DATABASES_ROUTE = "/databases"

COLLECTIONS_ROUTE = "/collections/{db_name}"

DATA_ROUTE = "/data/{db_name}/{collection}"

CREATE_ROUTE = "/data/{db_name}/{collection}"

UPDATE_ROUTE = "/data/{db_name}/{collection}/{id}"

DELETE_ROUTE = "/data/{db_name}/{collection}/{id}"