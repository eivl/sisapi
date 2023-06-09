from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.ext.mutable import MutableList

from database import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)
    org_id = Column(Integer, ForeignKey("orgs.id"), nullable=True)

    firstName = Column(String)
    lastName = Column(String)
    displayName = Column(String)
    foreignId = Column(String, unique=True, index=True)
    userPrincipalName = Column(String)
    username = Column(String)
    uniqueIdentifierNumber = Column(String)
    dateOfBirth = Column(DateTime)
    localUniqueIdentifierNumber = Column(String)
    mail = Column(MutableList.as_mutable(ARRAY(String)))

    org = relationship("Org", back_populates="person")


class Org(Base):
    __tablename__ = "orgs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String)
    foreignId = Column(String)
    legalOrgName = Column(MutableList.as_mutable(ARRAY(String)))
    orgNumber = Column(String)
    displayName = Column(String)

    person = relationship("Person", back_populates="org")