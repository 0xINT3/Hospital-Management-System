import cx_Oracle
conn=cx_Oracle.connect('KUSH/KUSH')
cur=conn.cursor()

class appointment:
    def __init__(self,pat_id,specialization):
        self.pat_id=pat_id
        self.specialization=specialization
    def schedule(self):
        if('select * from doctor where self.specialization'):
            print("Appointment done for patient with patient id",self.pat_id)
        else:
            print("Unavailability of this type of specialised doctor in this hospital")

            
