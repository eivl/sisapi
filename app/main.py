from typing import Union, Optional, Literal

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field, validator


class Address(BaseModel):
    address_line_1: str = Field(title='Address line 1', description='Address line 1', example='Postboks 340')
    address_line_2: Optional[str] = Field(default=None, title='Address line 2', description='Address line 2')
    address_line_3: Optional[str] = Field(default=None, title='Address line 3', description='Address line 3')
    city: str = Field(title='City', description='City', example='Oslo')
    zipcode: str = Field(title='Zipcode', description='Zipcode', example='0100')
    country: Optional[str] = Field(default='Norway', title='Country', description='Country', example='Norway')


class Feide(BaseModel):
    norEduOrgUniqueIdentifier: Optional[str] = Field(default=None, title='NorEduOrgUniqueIdentifier', description='The number assigned the higher educational institution by Universities and Colleges Admission Service ("Samordna opptak", SO).', example='00000185')
    norEduOrgUnitUniqueIdentifier: Optional[str] = Field(default=None, title='NorEduOrgUnitUniqueIdentifier', description='The identifier describing an organizational unit.', example='332244')
    norEduPersonLegalName: Optional[str] = Field(default=None, title='NorEduPersonLegalName', description='The legal name of the person.', example='Ola Jens Normann')
    eduPersonPrincipalName: Optional[str] = Field(default=None, title='EduPersonPrincipalName', description='Full Feide-name.', example='olanor123@universitetet.no')
    eduPersonPrimaryAffiliation: Optional[str] = Field(default=None, title='EduPersonPrimaryAffiliation', description='Primary role at the organization: student or employee', example='student')
    eduPersonAffiliation: Optional[list[str]] = Field(default=None, title='EduPersonAffiliation', description='Roles at organization in Feide', example=["member", "student", "staff", "employee"])
    eduPersonEntitlement: Optional[list[str]] = Field(default=None, title='EduPersonEntitlement', description='Information about rights, roles and groups that this person has', example=["urn:mace:feide.no:sigma:confusa:admin", "urn:mace:feide.no:stillingskode:stat:1011", "http://example.org/contracts/HEd123"])


class Person(BaseModel):
    firstName: str = Field(title='First name', description='First name as string', example='Ola')
    lastName: str = Field(title='Last name', description='Last name as string', example='Normann')
    displayName: str = Field(title='Display name', description='The name of the user as it should be displayed', example='Ola Normann')
    foreignId: Optional[str] = Field(default=None, title='Foreign ID', description='ID from external system as string', example='abc123')
    userPrincipalName: Optional[EmailStr] = Field(default=None, title='User principal name', description='Full Feide-name', example='olanor123@universitetet.no')
    username: Optional[str] = Field(default=None, title='Username', description='The person\'s local username at the school owner', example='olanor123')
    uniqueIdentifierNumber: Optional[str] = Field(default=None, title='Unique identifier number', description='Shall be a unique identification number issued by Folkeregisteret or Utlendingsdirektoratet (UDI) or Samordna Opptak: - National identity number - D-number - DUF-number - S-number/So-number (student-number issued by Samordna Opptak) or empty string', example='28088933134')
    dateOfBirth: Optional[str] = Field(default=None, title='Date of birth', description='Date of birth as string', example='1989-08-28')
    localUniqueIdentifierNumber: Optional[str] = Field(default=None, title='Local unique identifier number', description='Shall be a unique identification number issued by the school owner', example='123456')
    mail: Optional[list[EmailStr]] = Field(default=None, title='Email', description='The person\'s email. Shall be a personal address', example=["ola.nordmann@universitetet.no", "olanor123@stud.universitetet.no"])
    privateMail: Optional[list[EmailStr]] = Field(default=None, title='Private email', description='The person\'s private email. Shall be a personal address', example=["olanor@privateprovider.no"])
    mobile: Optional[list[str]] = Field(default=None, title='Mobile', description='Mobile number connected to this person', example=['+47 12345678'])
    privateMobile: Optional[list[str]] = Field(default=None, title='Private mobile', description='Private mobile number connected to this person', example=['+47 12345678'])
    telephoneNumber: Optional[list[str]] = Field(default=None, title='Telephone number', description='Telephone number connected to this person', example=['+47 12345678'])
    postalAddress: Optional[list[Address]] = Field(default=None, title='Postal address', description='Postal address connected to this person', example=[{"address_line_1": "Universitetsgata 1", "zipcode": "1234", "city": "Oslo"}])
    orgRef: Optional[list[str]] = Field(default=None, title='Organization reference', description='The organization the user belongs to')
    orgUnitPrimaryRef: Optional[str] = Field(default=None, title='Primary organization unit reference', description='The primary organization unit the user belongs to')
    orgUnitRef: Optional[list[str]] = Field(default=None, title='Organization unit reference', description='The organization units the user belongs to')
    roles: Optional[list[str]] = Field(default=None, title='Roles', description='The roles the user has. Feide calls this eduPersonAffiliation', exsample=['member', 'student', 'staff', 'employee'])
    preferredLanguage: Optional[str] = Field(default=None, title='Preferred language', description='The person\'s preferred language, defined by ISO 639-3 og BCP 47', example='nb')
    eduPersonOrcid: Optional[list[str]] = Field(default=None, title='ORCID iD', description='The person\'s ORCID iD. The iD is a 16-digit number, separated into four groups of four digits, with a hyphen between each group', example=['0000-0002-1825-0097'])
    eduPersonPrincipalNamePrior: Optional[list[str]] = Field(default=None, title='eduPersonPrincipalNamePrior', description='Each value of this multivalued attribute represents an ePPN (eduPersonPrincipalName) value that was previously associated with the entry. The values MUST NOT include the currently valid ePPN', example=["foo@hsww.wiz"])
    feide: Optional[Feide] = Field(default=None, title='Feide', description='Feide attributes')
    extra: Optional[dict] = Field(default=None, title='Extra', description='Extra attributes')


class Org(BaseModel):
    type: Literal['ORG', 'UNIT'] = Field(title='Type', description='ORG or UNIT as string. ORG is a legal entity, UNIT is a department or similar', example='ORG')
    foreignId: Optional[str] = Field(default=None, title='Foreign ID', description='ID from external system as string', example='abc123')
    legalOrgName: Optional[list[str]] = Field(default=None, title='Legal organization name', description='The official name of the organization', example=['Universitetet i Norge'])
    orgNumber: Optional[str] = Field(default=None, title='Organization number', description='Organization\'s number from Brønnøysundregistrene as string', example='NO179530458')
    displayName: Optional[str] = Field(default=None, title='Display name', description='The name of the organization as it should be displayed', example='UiN')
    telephoneNumber: Optional[list[str]] = Field(default=None, title='Telephone number', description='Telephone number as string', example=['+47 12345678'])
    mail: Optional[list[EmailStr]] = Field(default=None, title='Email', description='Email address as string', example=['kontakt@universitetet.no'])
    postalAddress: Optional[list[Address]] = None
    feide: Optional[Feide] = Field(default=None, title='Feide', description='Feide attributes, can be used to link to Feide in the future.')


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
