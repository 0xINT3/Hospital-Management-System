import cx_Oracle
con=cx_Oracle.connect('KUSH/KUSH')
cur=con.cursor()
class receipt:
    def __init__(self,pat_id):
        self.pat_id=pat_id
    def display(self):
        details=[]
        schema=['Amount: ','Transaction Id: ','Paymode: ','Bill_date: ']
        query=cur.execute('select AMOUNT,TRANSCATION_ID,PAYMODE,BILL_DATE from payment where pat_id=:1',{'1':self.pat_id})
        for i in query.fetchone():
            details.append(i)
        for a,b in zip(schema,details):
            print(a,b)
            print('\n\n')
            
        
