from sqlalchemy.orm import Session

import models.schemas as schemas
import models.models as models


def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()

def get_person_by_foreign_id(db: Session, foreign_id: str):
    return db.query(models.Person).filter(models.Person.foreignId == foreign_id).first()

def get_persons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()

def get_org(db: Session, org_id: int):
    return db.query(models.Org).filter(models.Org.id == org_id).first()

def get_org_by_foreign_id(db: Session, foreign_id: str):
    return db.query(models.Org).filter(models.Org.foreignId == foreign_id).first()

def get_orgs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Org).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def create_org(db: Session, org: schemas.OrgCreate):
    db_org = models.Org(**org.dict())
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
