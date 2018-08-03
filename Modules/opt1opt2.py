import cx_Oracle
conn=cx_Oracle.connect('SYSTEM/SYSTEM')
cur=conn.cursor()


class insert:
    def __init__(self,pat_id,name,gender,address,tel,dr_code, age):
        self.pat_id = pat_id
        self.name = name
        self.gender = gender
        self.address = address
        self.tel = tel
        self.dr_code = dr_code
        self.age = age
    def enter(self):
        query=cur.execute("INSERT INTO patient VALUES (:1, :2, :3, :4, :5, :6, :7)",{'1': int(self.pat_id), '2': str(self.name), '3': str(self.gender) ,'4':str(self.address), '5': int(self.tel),'6': str(self.dr_code), '7': int(self.age)})
        conn.commit()
