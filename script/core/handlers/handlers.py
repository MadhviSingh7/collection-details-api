from fastapi import APIRouter, HTTPException, Body
from script.core.services.services import *
from script.core.constants.constants import *

router = APIRouter()

# Common Success Response
def success_response(message: str, data):
    return {
        "status": SUCCESS,
        "message": message,
        "data": data
    }


# ==========================
# GET APIs (existing)
# ==========================
@router.get(DATABASES_ROUTE)
def databases():
    try:
        dbs = get_databases()
        return success_response(FETCH_DATABASES_SUCCESS, dbs)
    except Exception as e:
        raise HTTPException(500, DATABASE_FETCH_ERROR)


@router.get(COLLECTIONS_ROUTE)
def collections(db_name: str):
    try:
        cols = get_collections(db_name)
        return success_response(FETCH_COLLECTIONS_SUCCESS.format(db_name=db_name), cols)
    except Exception as e:
        raise HTTPException(500, COLLECTION_FETCH_ERROR)


@router.get(DATA_ROUTE)
def get_data(db_name: str, collection: str):
    try:
        docs = get_documents(db_name, collection)
        return success_response(FETCH_DOCUMENTS_SUCCESS.format(db_name=db_name, collection=collection), docs)
    except Exception as e:
        raise HTTPException(500, DOCUMENT_FETCH_ERROR)


# ==========================
# POST API - Create Document
# ==========================
@router.post(DATA_ROUTE)
def create_data(db_name: str, collection: str, data: dict = Body(...)):
    try:
        inserted_id = create_document(db_name, collection, data)
        return success_response(f"Document created in {db_name}.{collection}", {"inserted_id": inserted_id})
    except Exception as e:
        raise HTTPException(500, f"Error creating document: {str(e)}")


# ==========================
# PUT API - Update Document
# ==========================
@router.put(DATA_ROUTE + "/{id}")
def update_data(db_name: str, collection: str, id: str, data: dict = Body(...)):
    try:
        updated_count = update_document(db_name, collection, id, data)
        if updated_count == 0:
            raise HTTPException(404, "Document not found or no changes applied")
        return success_response(f"Document {id} updated in {db_name}.{collection}", {"modified_count": updated_count})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Error updating document: {str(e)}")


# ==========================
# DELETE API - Soft Delete Document
# ==========================
@router.delete(DATA_ROUTE + "/{id}")
def delete_data(db_name: str, collection: str, id: str):
    try:
        deleted_count = delete_document(db_name, collection, id)
        if deleted_count == 0:
            raise HTTPException(404, "Document not found")
        return success_response(f"Document {id} deleted from {db_name}.{collection}", {"deleted_count": deleted_count})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Error deleting document: {str(e)}")