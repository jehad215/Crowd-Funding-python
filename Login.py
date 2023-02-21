class Login:

    def findUser(self, email):
        file = open("usrsdb.txt", "r")
        flag = 0
        index = -1
        for line in file:
            index += 1
            if email in line:
                flag = 1
                break
        file = open("usrsdb.txt", "r")
        lines = file.readlines()
        userData = lines[index]
        file.close()
        userInfo = userData.split(":")
        if flag == 1:
            return userInfo
        else:
            return None

    def login(self):
        email = input("Please enter your email address: ")
        password = input("Please enter your password: ")
        user = self.findUser(email)
        if user != None :
            if password == user[4]:
                return user
            else:
                print("Incorrect password")
                self.login()
        else:
            print("No such user")
            self.login()

