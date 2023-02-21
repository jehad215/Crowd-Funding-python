import re
class Register:
    
    def fname(self, fname):
        fnameValid = re.fullmatch(r'[a-zA-Z]+$',fname)
        if fnameValid:
            self.fname=fname
        else:
            anotherFname = input("Only letters valid, please enter valid name again: ")
            self.fname(anotherFname)

    def lname(self, lname):
        lnameValid = re.fullmatch(r'[a-zA-Z]+$', lname)
        if lnameValid:
            self.lname = lname
        else:
            anotherLname = input("Only letters valid, please enter valid name again: ")
            self.lname(anotherLname)

    def email(self, email):
        emailValid = re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email)
        if emailValid:
            self.email = email
        else:
            anotherEmail = input("Invalid email, please enter your email in right format: ")
            self.email(anotherEmail)

    def passw(self):
        password = input("Enter your password: ")
        confirmpwd= input("Enter your password again: ")
        if password != confirmpwd:
            print("Confirm password match")
            self.passw()
        else:
            self.password = password

    def phone(self, number):
        numberValid = re.match(r'^01[0125][0-9]{8}$', number)
        if numberValid:
            self.phonenum = number
        else:
            anothernum = input("Inter valid phone number: ")
            self.phone(anothernum)

    def register(self):
        self.id = id(self)
        fname= input("Please enter your first name: ")
        self.fname(fname)
        lname = input("Please enter your second name: ")
        self.lname(lname)
        email = input("Please enter your email: ")
        self.email(email)
        self.passw()
        number = input("Please enter you phone number: ")
        self.phone(number)

    