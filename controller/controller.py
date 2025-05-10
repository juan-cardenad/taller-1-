from fastapi import APIRouter, HTTPException, Depends
from typing import List
from model.location import Location
from service.location_service import LocationService

location_router = APIRouter(prefix="/locations", tags=["Locations"])

# Singleton instance for dependency injection
location_service_instance: LocationService = None

def set_location_service(service: LocationService):
    global location_service_instance
    location_service_instance = service

def get_location_service():
    return location_service_instance

@location_router.get("/departments", response_model=List[Location])
def get_departments(service: LocationService = Depends(get_location_service)):
    return service.get_departments()

@location_router.get("/by-department/{department_code}", response_model=List[Location])
def get_municipalities_by_department_code(department_code: int, service: LocationService = Depends(get_location_service)):
    return service.get_municipalities_by_department_code(department_code)

@location_router.get("/by-code/{code}", response_model=Location)
def get_municipality_by_code(code: int, service: LocationService = Depends(get_location_service)):
    location = service.get_municipality_by_code(code)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@location_router.get("/capitals", response_model=List[Location])
def get_capital_municipalities(service: LocationService = Depends(get_location_service)):
    return service.get_capital_municipalities()
