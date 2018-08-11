import cx_Oracle
conn = cx_Oracle.connect('SYSTEM/SYSTEM@XE')
cur = conn.cursor()

class doctor:
    def __init__(self,dr_code):
        self.dr_code=dr_code
    def view_details(self):
       try:
        details=[]
        schema=['Dr code:','Name:','Gender:','Address:','Designation:']
        query=cur.execute('select * from doctor where dr_code=:1',{'1':self.dr_code})
        for i in query.fetchone():
            details.append(i)
        for a,b in zip(schema,details):
            print(a,b)
        print('\n\n')
    except:
        print("No such patient details.")

