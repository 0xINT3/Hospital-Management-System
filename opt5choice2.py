import cx_Oracle
conn=cx_Oracle.connect('SYSTEM/SYSTEM')
cur=conn.cursor()


class insert:
    def __init__(self,dr_code,name,gender,address,designation):
        self.dr_code = dr_code
        self.name = name
        self.gender = gender
        self.address = address
        self.designation = designation
    def enter(self):
        query=cur.execute("INSERT INTO doctor VALUES (:1, :2, :3, :4, :5)",{'1': int(self.dr_code), '2': str(self.name), '3': str(self.gender) ,'4':str(self.address), '5': str(self.designation)})
        conn.commit()
