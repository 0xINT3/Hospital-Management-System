import cx_Oracle
conn = cx_Oracle.connect('SYSTEM/SYSTEM')
cur = conn.cursor()

class Pat_View:
    def __init__(self, pat_id):
        self.pat_id = pat_id
        
    def view_details(self):
        details = []
        schema = ['Pat ID:', 'Name:','Gender:', 'Address:', 'Telephone:', 'Dr.Code:', 'Age:']
        query = cur.execute('select * from patient where pat_id = :1',{'1':self.pat_id})
        for i in query.fetchone():
            details.append(i)
        for a,b in zip(schema, details):
            print(a,b)
        print('\n\n')
