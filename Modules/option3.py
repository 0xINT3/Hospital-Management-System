import cx_Oracle
conn = cx_Oracle.connect('SYSTEM/SYSTEM')
cur = conn.cursor()

class Reports:
    def __init__(self, pat_id):
        self.pat_id = pat_id

    def view_reports(self):
        schema = ['Diagnosis Number:', 'Problem:', 'Current Status:', 'Diagnosis Date:', 'Solution:', 'Patient ID:']
        diag = []
        query = cur.execute('Select * from patientdiagnosis where pat_id  = :1',{'1': self.pat_id})
        for i in query.fetchone():
            diag.append(i)
        print('\n')
        for a,b in zip(schema, diag):
            print(a,b)
        print('\n\n')
