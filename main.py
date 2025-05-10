from fastapi import FastAPI
from controller.controller import location_router, set_location_service
from controller.person_controller import router as person_router
from service.location_service import LocationService

app = FastAPI()


location_service = LocationService("data/divipola.csv")
set_location_service(location_service)


app.include_router(location_router)
app.include_router(person_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
