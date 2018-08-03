import cx_Oracle
con=cx_Oracle.connect("KUSH/KUSH")
cur=con.cursor()
class payment:
    def __init__(self,transac_id):
        self.pat_id=pat_id
    def pay_detail(self):
        details=[]
        schema=['Pat_Id: ','Amount: ','Transaction_Id: ','PayMode: ','Bill_Date: ']
        query=cur.execute('select * from payment where pat_id=:1',{'1':self.pat_id})
        for i in query.fetchone():
            details.append(i)
        for a,b in zip(schema,details):
            print(a,b)
            print('\n\n')
