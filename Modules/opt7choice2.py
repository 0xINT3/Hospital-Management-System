import cx_Oracle
conn=cx_Oracle.connect('SYSTEM/SYSTEM')
cur=conn.cursor()


class Staff:
    def __init__(self,staff_id,name, dept, gender, address, cell ,dr_code):
        self.staff_id = staff_id
        self.name = name
        self.dept = dept
        self.gender = gender
        self.address = address
        self.cell = cell
        self.dr_code = dr_code
    def enter(self):
        query=cur.execute("INSERT INTO staff_table VALUES (:1, :2, :3, :4, :5, :6, :7)",{'1': int(self.staff_id), '2': str(self.name), '3': str(self.dept) ,'4':str(self.gender), '5': str(self.address),'6': int(self.cell), '7': int(self.dr_code)})
        conn.commit()
