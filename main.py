from fastapi import FastAPI, Depends, Query,Form

from sqlalchemy.orm import Session
from typing import Optional
from database import get_db
from crud import get_filtered_forms
from schemas import WheelSpecResponse,BogieForm
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import BogieForm
from crud import save_bogie_form
from database import get_db
from fastapi import FastAPI, Form, Depends
from sqlalchemy.orm import Session
import json
from models import BogieFormModel
from database import get_db, engine, Base

app=FastAPI()
@app.get("/api/forms/wheel-specifications", response_model=WheelSpecResponse)
def get_filtered_wheel_specifications(
    formnumber: Optional[str] = Query(None),
    submittedby: Optional[str] = Query(None),
    submitteddate: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    forms = get_filtered_forms(db, formnumber, submittedby, submitteddate)

    result = []
    for f in forms:
        result.append({
            "formnumber": f.formnumber,
            "submittedby": f.submittedby,
            "submitteddate": f.submitteddate,
            "fields": {
                "condemningdia": f.condemningdia,
                "lastshopissuesize": f.lastshopissuesize,
                "treaddiameternew": f.treaddiameternew,
                "wheelgauge": f.wheelgauge
            }
        })

    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": result
    }
@app.post("/api/forms/bogie-checksheet")
def submit_bogie_form(
    formNumber: str = Form(...),
    inspectionBy: str = Form(...),
    inspectionDate: str = Form(...),

    # BMBC
    adjustingTube: str = Form(...),
    cylinderBody: str = Form(...),
    pistonTrunnion: str = Form(...),
    plungerSpring: str = Form(...),

    # Bogie Checksheet
    axleGuide: str = Form(...),
    bogieFrameCondition: str = Form(...),
    bolster: str = Form(...),
    bolsterSuspensionBracket: str = Form(...),
    lowerSpringSeat: str = Form(...),

    # Bogie Details
    bogieNo: str = Form(...),
    dateOfIOH: str = Form(...),
    deficitComponents: str = Form(...),
    incomingDivAndDate: str = Form(...),
    makerYearBuilt: str = Form(...),

    db: Session = Depends(get_db)
):
    bmbc_data = json.dumps({
        "adjustingTube": adjustingTube,
        "cylinderBody": cylinderBody,
        "pistonTrunnion": pistonTrunnion,
        "plungerSpring": plungerSpring
    })
    bogie_checksheet = json.dumps({
        "axleGuide": axleGuide,
        "bogieFrameCondition": bogieFrameCondition,
        "bolster": bolster,
        "bolsterSuspensionBracket": bolsterSuspensionBracket,
        "lowerSpringSeat": lowerSpringSeat
    })
    bogie_details = json.dumps({
        "bogieNo": bogieNo,
        "dateOfIOH": dateOfIOH,
        "deficitComponents": deficitComponents,
        "incomingDivAndDate": incomingDivAndDate,
        "makerYearBuilt": makerYearBuilt
    })

    form_model = BogieFormModel(
        formNumber=formNumber,
        inspectionBy=inspectionBy,
        inspectionDate=inspectionDate,
        bmbcChecksheet=bmbc_data,
        bogieChecksheet=bogie_checksheet,
        bogieDetails=bogie_details
    )

    db.add(form_model)
    db.commit()
    db.refresh(form_model)

    return {"message": "Form submitted successfully."}


from models import BogieFormModel
from database import engine, Base

# Create all tables
Base.metadata.create_all(bind=engine)
