from fastapi import APIRouter, HTTPException
from typing import List
from model.person import Person
from service.treen_service import tree_n

router = APIRouter(prefix="/persons", tags=["Persons"])

@router.post("/", response_model=Person)
def create_person(person: Person):
    try:
        node = tree_n.create_person(person)
        return node.person
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[Person])
def get_all_persons():
    return tree_n.get_persons()

@router.get("/{person_id}", response_model=Person)
def get_person_by_id(person_id: int):
    node = tree_n.find_node_by_id(person_id)
    if not node:
        raise HTTPException(status_code=404, detail="Person not found")
    return node.person

@router.put("/{person_id}", response_model=Person)
def update_person(person_id: int, updated: Person):
    success = tree_n.update_person(person_id, updated)
    if not success:
        raise HTTPException(status_code=404, detail="Person not found")
    return updated

@router.delete("/{person_id}")
def delete_person(person_id: int):
    success = tree_n.delete_person(person_id)
    if not success:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"message": "Person deleted successfully"}

@router.get("/with-adult-daughter", response_model=List[Person])
def persons_with_adult_daughter():
    return tree_n.get_persons_with_adult_daughter()

@router.get("/filter", response_model=List[Person])
def filter_by_location_type_gender(loc: str, td: str, gr: str):
    return tree_n.filter_by_location_typedoc_gender(loc, td, gr)

@router.get("/by-location/{location_code}", response_model=List[Person])
def get_by_location(location_code: str):
    return tree_n.get_persons_by_location(location_code)
