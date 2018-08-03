import cx_Oracle
conn=cx_Oracle.connect('KUSH/KUSH')
cur=conn.cursor()
class entry:
    def __init__(self,pat_id,name,gender,address,tel,dr_code):
        self.pat_id=pat_id
        self.name=name
        self.gender=gender
        self.address=address
        self.dr_code=dr_code
    def enter(self):
      query=cur.execute("INSERT INTO patient VALUES (:1, :2, :3, :4, :5, :6)",{'1': self.pat_id,'2': "\'"+ str(self.name)+ "\'", '3': "\'"+ str(self.gender)+ "\'" ,'4': "\'"+str(self.address)+ "\'" , '5': self.tel,'6': "\'"+str(self.dr_code)})
    
