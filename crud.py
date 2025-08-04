import json
from models import BogieFormModel
from schemas import BogieForm
from sqlalchemy.orm import Session
from models import WheelSpecificationForm

def get_filtered_forms(db: Session, formnumber=None, submittedby=None, submitteddate=None):
    query = db.query(WheelSpecificationForm)

    if formnumber:
        query = query.filter(WheelSpecificationForm.formnumber == formnumber)
    if submittedby:
        query = query.filter(WheelSpecificationForm.submittedby == submittedby)
    if submitteddate:
        query = query.filter(WheelSpecificationForm.submitteddate == submitteddate)

    return query.all()



from sqlalchemy.orm import Session
from models import BogieFormModel
from schemas import BogieForm
import json

def save_bogie_form(db: Session, form_data: BogieForm):
    db_form = BogieFormModel(
        formNumber=form_data.formNumber,
        inspectionBy=form_data.inspectionBy,
        inspectionDate=form_data.inspectionDate,
        bmbcChecksheet=json.dumps(form_data.bmbcChecksheet.dict()),
        bogieChecksheet=json.dumps(form_data.bogieChecksheet.dict()),
        bogieDetails=json.dumps(form_data.bogieDetails.dict())
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form
