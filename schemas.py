from pydantic import BaseModel
from typing import List

class BMBCChecksheet(BaseModel):
    adjustingTube: str
    cylinderBody: str
    pistonTrunnion: str
    plungerSpring: str

class BogieChecksheet(BaseModel):
    axleGuide: str
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str

class BogieDetails(BaseModel):
    bogieNo: str
    dateOfIOH: str
    deficitComponents: str
    incomingDivAndDate: str
    makerYearBuilt: str

class BogieForm(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: str
    bmbcChecksheet: BMBCChecksheet
    bogieChecksheet: BogieChecksheet
    bogieDetails: BogieDetails
class WheelFields(BaseModel):
    condemningdia: str
    lastshopissuesize: str
    treaddiameternew: str
    wheelgauge: str

class WheelSpecification(BaseModel):
    formnumber: str
    submittedby: str
    submitteddate: str
    fields: WheelFields

class WheelSpecResponse(BaseModel):
    success: bool
    message: str
    data: List[WheelSpecification]


