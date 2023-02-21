import re
class Project:

    @classmethod
    def sbydate(cls, date):
        file = open("projects.txt", "r")
        lines = file.readlines()
        projects = []
        for line in lines:
            if date in line:
                projects.append(line.split(":"))
        return projects

    @classmethod
    def delproject(cls, projectName, userID):
        file = open("projects.txt", "r")
        fileLines = file.readlines()
        index=-1
        filew = open("projects.txt", "w")
        for line in fileLines:
            index += 1
            if userID in line:
                if projectName in line:
                    continue
                else:
                    filew.write(line)
            else:
                filew.write(line)




    @classmethod
    def editproject(cls, projectName):
        file = open("projects.txt", "r")
        fileLines = file.readlines()
        index = -1
        for line in fileLines:
            index += 1
            if projectName in line:
                found = line.split(":")
                break
        
        pname = input("Please enter new project name: ")
        if pname != "":
            del found[1]
            found.insert(1,pname)
        pdiscribtion = input("Please enter new project discribtion: ")
        if pdiscribtion != "":
            del found[2]
            found.insert(2, pdiscribtion)
        ptotaltarget = input("Please enter new project total target: ")
        if ptotaltarget != "":
            del found[3]
            found.insert(3, ptotaltarget)
        pstartd = input("Please enter new project start date: ")
        if pstartd != "":
            del found[4]
            if re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', pstartd):
                found.insert(4, pstartd)
            else:
                print("Invalid format")
        pendd = input("Please enter new project start date: ")
        if pstartd != "":
            del found[4]
            if re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', pendd):
                found.insert(4, pendd)
            else:
                print("Wrong Format")
        updatedP = ':'.join(found)
        file = open("projects.txt", "r")
        fileLines = file.readlines()
        fileLines[index]=updatedP
        filew = open("projects.txt", "w")
        filew.writelines(fileLines)
        file.close()
        filew.close()


    def startdate(self, date):
        dateValid = re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', date)
        if dateValid:
            self.startDate = date
        else:
            anotherDate = input("Invalid format, Enter date in (dd/mm/yyyy) format: ")
            self.startdate(anotherDate)

    def enddate(self,date):
        dateValid = re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', date)
        if dateValid:
            self.endtDate = date
        else:
            anotherDate = input("Invalid format, Enter date in (dd/mm/yyyy) format: ")
            self.enddate(anotherDate)

    def create(self):
        self.title = input("Please enter the project title: ")
        self.Discribtion = input("EPlease enter the project discribtion: ")
        self.totalTarget = input("Please enter total target: ")
        startDate = (input("Please enter start date in (dd/mm/yyyy) format: "))
        self.startdate(startDate)
        endDate =  input("EPlease enter end date in (dd/mm/yyyy) format: ")
        self.enddate(endDate)
