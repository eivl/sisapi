import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from .models import Org, Person


app = FastAPI()


@app.post("/org")
def post_org(org: Org) -> JSONResponse:
    json_compatible_item_data = jsonable_encoder(org)
    return JSONResponse(content=json_compatible_item_data)


@app.post("/person")
def post_person(person: Person) -> JSONResponse:
    json_compatible_item_data = jsonable_encoder(person)
    return JSONResponse(content=json_compatible_item_data)


if __name__ == '__main__':
    uvicorn.run(app, port=7000, host='127.0.0.1')
