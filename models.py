from sqlalchemy import Column, String
from database import Base


class WheelSpecificationForm(Base):
    __tablename__ = "wheel_specifications"  # actual table name

    formnumber = Column(String, primary_key=True, nullable=False)
    submittedby = Column(String)
    submitteddate = Column(String)
    condemningdia = Column(String)
    lastshopissuesize = Column(String)
    treaddiameternew = Column(String)
    wheelgauge = Column(String)

class BogieFormModel(Base):
    __tablename__ = "bogie_forms"

    formNumber = Column(String, primary_key=True, nullable=False)
    inspectionBy = Column(String)
    inspectionDate = Column(String)

    bmbcChecksheet = Column(String)  # stored as JSON string
    bogieChecksheet = Column(String)
    bogieDetails = Column(String)
