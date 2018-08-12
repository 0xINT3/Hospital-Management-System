import cx_Oracle
conn = cx_Oracle.connect('KUSH/KUSH')
cur = conn.cursor()

class Pat_View:
    def __init__(self, pat_id):
        self.pat_id = pat_id
        
    def view_details(self):
        try:
            details = []
            schema = ['Pat ID:', 'Name:','Gender:', 'Address:', 'Telephone:', 'Dr.Code:', 'Age:','bed_no: ']
            query = cur.execute('select * from patient where pat_id = :1',{'1':self.pat_id})        
            for i in query.fetchone():
                details.append(i)
            query=cur.execute('select * from bed_allot where pat_id =:1',{'1':self.pat_id})  #detials for bed number also added
            for i in query.fetchone():
                details.append(i)
            for a,b in zip(schema, details):
                print(a,b)
            print('\n\n')
        except:
            print("No such patient details.")
