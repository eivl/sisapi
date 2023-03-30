from sqlalchemy.orm import Session

import models.schemas as schemas
import models.models as models


def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()

def get_person_by_foreign_id(db: Session, foreign_id: str):
    return db.query(models.Person).filter(models.Person.foreignId == foreign_id).first()