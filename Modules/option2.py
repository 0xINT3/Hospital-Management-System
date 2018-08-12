import cx_Oracle
from datetime import datetime
con=cx_Oracle.connect("SYSTEM/SYSTEM")
cur=con.cursor()
class payment:
    def __init__(self,pat_id, amount, transaction, paymode, date):
        self.pat_id=pat_id
        self.amount = amount
        self.paymode = paymode
        self.transaction = transaction
        self.date = date
        
    def pay_detail(self):
        #date = datetime.now().strftime("%d-%m-%Y")
        query=cur.execute('insert into payment values(:1, :2, :3, :4, :5)',{'1': self.pat_id, '2': self.amount, '3': self.transaction, '4': self.paymode, '5': self.date})
        con.commit()
        con.close()
