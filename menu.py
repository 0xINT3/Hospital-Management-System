import cx_Oracle
import quotes
from time import ctime
conn = cx_Oracle.connect('KUSH/KUSH')       # Connecting to the database
cur = conn.cursor()                             # Setting cursor at the starting of connection
        
def print_menu():       # Menu at the opening of the system 

    print("-----------------------------Menu-----------------------------".center(150))
    print ('''
    	1. Patient registration
    	2. Patient Payment
    	3. Medical reports
    	4. Bill Receipts
    	5. Doctor Details
    	6. Patient Details
    	7. Staff Details
    	8. Exit''')
def main():          
        loop = True
        while loop: # Will run until loop = True
            print_menu()    # Calling the menu function
            while True:
                    try:
                        choice = int(input("Enter your choice [1-8]: "))
                    except:
                        print("Please enter the integer value")
                        continue
                    else:
                        break
            if choice==1:     
                print ("----------------------Menu 1 has been selected---------------------".center(150))
                while True:
                    try:
                        choice_2 = int(input('''Enter choice:
                        1. Schedule Appointment
                        2. New Entry
                        3. Exit
                        Choice: '''))
                    except:
                        print("Please enter an integer value")
                        continue
                    else:
                        break


                if choice_2 == 1:
                    import opt1choice1
                    k=input("Enter the pat_id: ")
                    choice=int(input('''Availability:
                                      1.Heart Specialist
                                      2.Eye Specialist
                                      3.Skin Specilaist
                                      4.Basic Checkup
                                      Choice: '''))
                    if choice == 1:
                        l = "Heart Specialist"
                    elif choice == 2:
                        l = "Eye Specialist"
                    elif choice == 3:
                        l = "Skin Specialist"
                    else:
                        l = "Basic Checkup"
                    
                    obj1_1=opt1choice1.appointment(k,l)
                    obj1_1.schedule()
                
                
                elif choice_2 == 2:
                    import opt1opt2

                    k = int(input("Enter the Patient ID: "))
                    l = input("Name: ")
                    m = input("Gender: ")
                    n = input("Address: ")
                    o = int(input("Telephone Number: "))
                    p = input("Doctor code: ")
                    q = int(input("Age"))
                    obj1 = opt1opt2.insert(k,l,m,n,o,p,q)
                    obj1.enter()
                else:
                    pass # for exiting the sub-menu
                    
                
            elif choice == 2:
                
                print ("----------------------Menu 2 has been selected---------------------".center(150))
                import option2
                k = int(input("Enter the Patient ID of patient to check payment details: "))
                obj2=option2.payment(k)
                obj2.pay_detail()
                
            elif choice == 3:
                print ("----------------------Menu 3 has been selected---------------------".center(150))
                import option3
                pat_id = int(input("Enter patient ID:"))
                obj3 = option3.Reports(pat_id)
                obj3.view_reports()
                
            elif choice == 4:
                print ("----------------------Menu 4 has been selected---------------------".center(150))
                import option4
                l=int(input("Enter the patient id to generate bill receipt"))
                obj4=option4.receipt(l)
                obj4.display()

            elif choice==5:
                print ("----------------------Menu 5 has been selected---------------------".center(150))
               
                while True:
                    try:
                        choice = int(input('''Select an option:
                1.View Details
                2. Add Doctor
                3. Exit
                Choice: '''))
                    except:
                        print("Please enter the integer value")
                        continue
                    else:
                        break
                if choice == 1:
                    import option5
                    dr_code=int(input("Enter the doctor code"))
                    ob5=option5.doctor(dr_code)
                    ob5.view_details()

                elif choice == 2:
                    import opt5choice2
                    k = int(input("Doctor Code: "))
                    l = input("Name: ")
                    m = input("Gender: ")
                    n = input("Address: ")
                    p = input("Designation: ")

                    obj = opt5choice2.insert(k,l,m,n,p)
                    obj.enter()
                else:
                    pass      #for exiting the submenu

            elif choice==6:
                print ("----------------------Menu 6 has been selected---------------------".center(150))

                import option6
                pat_id = int(input("Please Enter Patient ID: "))
                obj6 = option6.Pat_View(pat_id)
                obj6.view_details()

                
            elif choice==7:
                print ("----------------------Menu 7 has been selected---------------------".center(150))

                while True:
                    try:
                        choice = int(input('''Select an option:
                1. View details
                2. Add staff member
                3. Exit
                Choice: '''))
                    except:
                        print("Please enter the integer value")
                        continue
                    else:
                        break
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
                    pass # for exiting the sub-menu
                             
            elif choice == 8:
                    return
                    print("Have a nice day!")
            else:
                print("Invalid input.....Enter the integer between[1-8]".center(150))

def login():
    for i in range(0,3):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if  username == 'admin' or username == 'Admin' and password == 'admin' or password == 'Admin':
            main()
            break
        else:
            if i == 2:
                print("Exiting...")
                exit()
            else:
                print("\nInvalid Login Details....Please try again.\n")

    
print("Welcome to Hospital Management System!".center(150))
print(ctime().center(150))
print('\n')
print(quotes.display().center(150))
print('\n')
print("Please enter login details!".center(150))
login()
