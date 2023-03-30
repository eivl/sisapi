import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
import models.schemas as schemas
import models.models as models
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/org")
def post_org(org: schemas.OrgCreate) -> JSONResponse:
    json_compatible_item_data = jsonable_encoder(org)
    return JSONResponse(content=json_compatible_item_data)


@app.post("/person", response_model=schemas.Person)
def post_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_foreign_id(db, foreign_id=person.foreignId)
    if db_person:
        raise HTTPException(status_code=400, detail="Person already registered")
    return crud.create_person(db=db, person=person)

if __name__ == '__main__':
    uvicorn.run(app, port=7000, host='127.0.0.1')
