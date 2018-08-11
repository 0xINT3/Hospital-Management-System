import cx_Oracle
conn = cx_Oracle.connect('SYSTEM/SYSTEM')
cur = conn.cursor()


class Staff_View:
    def __init__(self, staff_id):
        self.staff_id = staff_id

    def view_details(self):
        try:
	        details = []
	        schema = ['Staff ID:', 'Name:', 'Dept:', 'Gender:', 'Address:', 'Telephone:', 'Dr.Code:']
	        query = cur.execute('select * from staff_table where staff_id = :1',{'1':self.staff_id})
	        for i in query.fetchone():
	            details.append(i)
	        for a,b in zip(schema, details):
	            print(a,b)
	        print('\n\n')
	    except:
	    	print("\nNo such staff details.")
