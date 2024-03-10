print("Welcome to the  RR bank")
class account:
    def __init__(self):
        self.name = input("Enter the name:")
        self.address = input("Enter the address:")
        self.cus()

    def cus(self):
        self.i=input("1.Resume existing journey, 2.Open Your Account Now")
        if self.i =="1":
            n=int(input("Enter the Mobile Number:"))
            a=int(input("Enter the Account Number:"))
        elif self.i == "2":
            t=input("Select: 1.personal Account, 2.Family Account")
            
        self.name =input("Enter the name:")
        self.gurdian_name = input("Enter the guardian name:")
        self.age = int(input("Enter the age:"))
        self.gender = input("Enter the gender: 1.select")
        if self.gender=="1":
            print("select the options :2.male, 3.female, 4.others")
            if self.gender=="2":
                print("Male")
            elif self.gender=="3":
                print("Female")
            elif self.gender=="4":
                print("Others")
        else:
            print("select any option")
        self.ph_No = int(input("Enter the phone number:"))
        self.occupation = input("Enter the occupation:")
        self.address = input("address:")
        self.Email = input("Enter the Email:")
        self.Pan_no = int(input("Enter Pan No:"))

class family(account):
    def members(self):
        marital =input("1.Married, 2.Unmarried:")
        if marital =="1":
            print("Married")
            n =int(input("Enter the no of family members:"))
        else:
            print("Unmarried")

    def child(self):
        chl =int(input("Enter the number of children:"))     
        ty=input("Enter the Type of Account: 1.Saving Account, 2.Current Account")
        if ty=="1":
            print("Saving Account")
        else:
            print("Current Account")
        final=input("Select the statement of Account through: 1.by post, 2.by hand, 3.Email, 4.Not required")
        if final=="1":
            print("By post")
        elif final=="2":
            print("By Hand")
        elif final=="3":
            print("Email")
        elif final=="4":
            print("Not required")
        sign=input("Signature:")
        print("Your Account Will Be created")    

class ins(account):
    def policy(self):
        age=int(input("Enter the children age:"))
        if age<=18:
            print("Not eligible for insurance policy")
        else:
            print("Eligible for insurance")

a =account()
a.cus()

b =family()
b.members()
b.child()

c =ins()
c.policy()

print("Account opening individuals// joint")

date = int(input("Enter the date:"))
branch = input("Enter the branch name:")
