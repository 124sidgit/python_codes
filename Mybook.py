#Mini project of management
from datetime import datetime
import time


NAME = []
DOB = []
GENDER = []
AGE = []
MOBLIE = []

class Details_User:
    
#Function to create New Users
    
    def New_users(self):
        
        while True:
            try:
                Name = input("Enter your Full Name:").upper()
                if(Name == ""):
                    print("Invalid input. Your Name cannot be blank.")
                    continue
                if Name.isdigit():
                    print("No Numeric values Allowed Here!!")  
                    continue  
                break
            except ValueError:
                print("Only Alphabet")

        while True:
            try:
                Dob = input("Enter Date Of Birth(dd-mm-yyyy):")
                dob2=datetime.strptime(Dob,"%d-%m-%Y")
                break
            except ValueError:
                print("Only in given format")

        while True:
            try:
                Gender = input("Enter Gender:").upper()
                if(Gender == ""):
                    print("Invalid input. Your Gender cannot be blank")
                    continue
                if not Gender.isalpha():
                    print("No Numeric values Allowed Here!!")  
                    continue
                break
            except ValueError:
                print("Only Alphabet")

        while True:
            try:
                Age = input("Enter Age:")
                Age = int(Age)
                break
            except ValueError:
                print("Not Valid integer ...")  

        while True:
            try:
                Mobile = (input("Enter Phone Number:"))
                Mobile = int(Mobile)
                break
            except ValueError:
                print("Not Valid integer ...")

        NAME.append(Name)
        DOB.append(Dob)
        GENDER.append(Gender)
        AGE.append(Age)
        MOBLIE.append(Mobile)


#Function to delete User Account
    
    def Delete_users(self):
        if(len(NAME)==0 and len(DOB)==0 and len(GENDER)==0 and len(AGE)==0 and len(MOBLIE)==0):
            print()
            print("___Oops! Nothing to Delete___")
            print("  __No Data is Available!!__")
            print()
        else:
            try:
                mobile=int(input("Enter Phone Number:"))
                src = MOBLIE.index(mobile)  
                
                NAME.remove(NAME[src])
                DOB.remove(DOB[src])
                GENDER.remove(GENDER[src])
                AGE.remove(AGE[src])
                MOBLIE.remove(MOBLIE[src]) 
                    
                print("___User Account Deleted Successfully___")
                
            except ValueError:
                print("No such Mobile Number Exist")    

            
#Function to Update User Details
    
    def Update_user_data(self):
        if(len(NAME)==0 and len(DOB)==0 and len(GENDER)==0 and len(AGE)==0 and len(MOBLIE)==0):
            print()
            print("___Oops! Nothing to Update___")
            print("  __No Data is Available!!__")
            print()

        else:
            
            while True:
                try:
                    attritute = (input("You can Update(Name,Dob,Gender,Age,Mobile) here:"))
                    attritute = str(attritute)
                    break 
                except ValueError:
                    print("Not Valid...")

            if(attritute == 'Name' or 'name'):
                try:
                    Old_name = input("Enter your Old Name:").upper()
                    Local_name = NAME.index(Old_name)

                    New_name = input("Enter your New Name:").upper()
                    NAME[Local_name] = New_name
                    print("___Name Updated Successfully___")
                    print("")
                except ValueError:
                    print("No such Name available")    

            if(attritute == 'Dob' or 'dob'):
                try:
                    Old_dob = input("Enter your Old DOB:").upper()
                    Local_dob = DOB.index(Old_dob)

                    New_dob = input("Enter your New DOB:").upper()
                    DOB[Local_dob] = New_dob
                    print("___DOB Updated Successfully___")
                    print("")
                except ValueError:
                    print("No such Dob available")    

            if(attritute == 'Gender' or 'gender'):
                try:
                    Old_gender = input("Enter your Old Gender:").upper()
                    Local_gender = GENDER.index(Old_gender)

                    New_gender = input("Enter your New Gender:").upper()
                    GENDER[Local_gender] = New_gender
                    print("___Gender Updated Successfully___")
                    print("")
                except ValueError:
                    print("No such Gender available")    

            if(attritute == 'Age' or 'age'):
                try:
                    Old_age = int(input("Enter your Old Age:"))
                    Local_age = AGE.index(Old_age)

                    New_age = input("Enter your New Age:")
                    AGE[Local_age] = New_age
                    print("___Age Updated Successfully___")
                    print("")
                except ValueError:
                    print("No such Age available")    

            if(attritute == 'Mobile' or 'mobile'):
                try:
                    Old_no = int(input("Enter your Old Number:"))
                    Local_no = MOBLIE.index(Old_no)

                    New_no = input("Enter your New Number:")
                    MOBLIE[Local_no] = New_no
                    print("___Mobile Number Updated Successfully___")
                    print("")  
                except ValueError:
                    print("No such Mobile Number available")      
            

                

#Function to Display User Details
    
    def Display_users(self):
        if(len(NAME)==0 and len(DOB)==0 and len(GENDER)==0 and len(AGE)==0 and len(MOBLIE)==0):
            print()
            print("___Oops! Nothing to Display___")
            print("  __No Data is Available!!__")
            print()
        else:
            print("User's Name:",end="\n")
            for a in NAME:
                print(a,end="\n\n")  

            print("User's Date of Birth:",end="\n")    
            for b in DOB:
                print(b,end="\n\n")    

            print("User's Gender",end="\n")    
            for c in GENDER:
                print(c,end="\n\n")       

            print("User's Age:",end="\n")
            for d in AGE:
                print(d,end="\n\n")    

            print("User's Phone Numbers")    
            for e in MOBLIE:
                print(e,end="\n\n")    


                         
sim = Details_User()

while True:
    print("--------------------------------------")
    print("           Welcome To Mybook          ")
    print("               From'\U0001F970'       ")
    print("--------------------------------------")

    time.sleep(1)
    print("1)CREATE NEW ACCOUNT\n2)DELETE USER ACCOUNT\n3)UPDATE USER ACCOUNT\n4)DISPALY PROFILE\n5)EXIT\n")
    while True:
        try:
            option = (input("Select Appropriate Option from [1-5]:"))
            option = int(option)
            break
        except ValueError:
            print("Not valid integer ...")

    if option == 1:
        sim.New_users()
    elif option == 2:
        sim.Delete_users()
    elif option == 3:
        sim.Update_user_data()
    elif option == 4:
        sim.Display_users()

    elif(option == 5):
        print()
        print("      '\U0001F970'Thank You'\U0001F970'  ")
        print("  _____For Using Mybook_____     ")
        print("     '\U0001F970'Visit Again'\U0001F970'")
        print()
        time.sleep(1)
        print("Please Submit Your Valuable Feedback:")
        feed = int(input("1.Happy 2.Not Happy 3.Good\n"))
        if(feed == 1):
            print("Thank You!! So Much Your Feedback must be appreciated'\U0001F603")
        elif(feed == 2):
            print("ThankYou!! We will improve and give our Best'\U0001F614")
        elif(feed == 3):
            print("Thank You!! We will do our Best'\U0001F642")    
        time.sleep(1)     
        exit()

    
    else:
        print("Selct option from [1-5]")
          
    input("\nPress Enter to continue:")    