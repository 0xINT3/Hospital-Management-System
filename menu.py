import cx_Oracle
conn = cx_Oracle.connect('SYSTEM/SYSTEM')
cur = conn.cursor()
#import class_doctor
        
def print_menu():       ## Your menu design here
    
    print ('''-----------------------------Menu-----------------------------
    	1. Patient registration
    	2. Patient Payment
    	3. Medical reports
    	4. Bill Receipts
    	5. Doctor Details
    	6. Patient Details
    	7. Staff Details
    	8. Exit''')


print("Welcome to Hospital Management System!") 
loop=True      
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = int(input("Enter your choice [1-8]: "))
     
    if choice==1:     
        print ("----------------------Menu 1 has been selected---------------------")
        
        choice_2 = int(input('''Enter choice:
        	1. Schedule Appointment
        	2. New Entry'''))

        if choice_2 == 1:
            pass
        
        elif choice_2==2:
            import opt1opt2

            k=int(input("enter the patientid: "))
            l=input("name: ")
            m=input("gender: ")
            n=input("address: ")
            o=int(input("telephone number: "))
            p=input("doctor code: ")
            q = int(input("Enter age"))
            obj1=opt1opt2.insert(k,l,m,n,o,p,q)

            obj1.enter()
        ## Hospital sub-menu
    elif choice==2:
        print ("----------------------Menu 2 has been selected---------------------")
        import option2
        k=int(input("Enter the patient id of patient to check payment details: "))
        obj2=option2.payment(k)
        obj2.pay_detail()
        ## You can add your code or functions here
    elif choice==3:
        print ("----------------------Menu 3 has been selected---------------------")
        import option3
        pat_id = int(input("Enter patient ID:"))
        obj3 = option3.Reports(pat_id)
        obj3.view_reports()
        
        ## Medical report sub-menu
    elif choice==4:
        print ("----------------------Menu 4 has been selected---------------------")
        import option4
        l=int(input("Enter the patient id to generate bill receipt"))
        obj4=option4.receipt(l)
        obj4.display()

        ## You can add your code or functions here
    elif choice==5:
        print ("----------------------Menu 5 has been selected---------------------")
        choice = int(input('''Select an option:
        1. View Details
        2. Add Doctor
        '''))
        if choice == 1:
            import option5
            dr_code=int(input("Enter the doctor code"))
            ob5=option5.doctor(dr_code)
            ob5.view_details()

        if choice == 2:
            import opt5choice2
            k = int(input("Doctor Code: "))
            l = input("Name: ")
            m = input("Gender: ")
            n = input("Address: ")
            p = input("Designation: ")

            obj = opt5choice2.insert(k,l,m,n,p)
            obj.enter()
    elif choice==6:
        print ("----------------------Menu 6 has been selected---------------------")

        import option6
        pat_id = int(input("Please Enter Patient ID: "))
        obj6 = option6.Pat_View(pat_id)
        obj6.view_details()

        
    elif choice==7:
        print ("----------------------Menu 7 has been selected---------------------")
        choice = int(input("""Select an option:
        1. View details
        2. Add staff member
        """))
        if choice == 1:
            import option7
            staff_id = int(input("Enter staff ID: "))
            obj7 = option7.Staff_View(staff_id)
            obj7.view_details()
            
        elif choice ==2:
            import opt7choice2
            k=int(input("enter the Staff ID: "))
            l=input("Name: ")
            m=input("Dept: ")
            n=input("Gender: ")
            o=input("Address: ")
            p=int(input("Cell Number: "))
            q = int(input("Doctor Code"))
            obj1=opt7choice2.Staff(k,l,m,n,o,p,q)
            obj1.enter()
                     
        else:
                     print("Invalid Option")
    else:
        loop=False # This will make the while loop to end as not value of loop is set to False
