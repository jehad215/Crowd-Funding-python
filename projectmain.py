from Register import Register
from Login import Login
from project import Project
import re


def dateval(date):
    if re.match(r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', date):
        return date
    else:
        datee = input("Please enter date invalid format: ")
        dateval(datee)

def menu2(user):
   
    option = input("Please select a choice from:\n              C --> Create project \n              V --> View All projects \n              E --> Edit project \n              D --> Delete project \n              S --> Search for a project \n              Q --> Back to mane menu\n:")
                
    if option == "C" or option == "c":
        print("  Create Project")
        print(" ----------------\n")
        project = Project()
        project.create()
        profeatures = [user[0], project.title, project.Discribtion, project.totalTarget, project.startDate, project.endtDate]
        l = " "
        for item in profeatures:
            l += item
            l += ":"
        file = open("projects.txt", "a")
        file.write(l)
        file.write("\n")
        file.close()
        menu2(user)
        
    elif option == "v" or option == "V":
        print("  View all projects")
        print(" -------------------\n")
        file = open("projects.txt", "r")
        lines = file.readlines()
        for line in lines:
            profeatures=line.split(":")
            print("Project Title: ", profeatures[1])
            print("Project Details: ", profeatures[2])
            print("Project Total Target: ", profeatures[3])
            print("Project Start Date: ", profeatures[4])
            print("Project End Date: ", profeatures[5])
            print("\n")
        menu2(user)
        
    elif option == "E" or option == "e":
        print(" Edit Project")
        print(" ---------------\n")
        print("Please enter project title you want to edit: ")
        userID = user[0]
        file = open("projects.txt", "r")
        lines = file.readlines()
        userProjects = []
        i=0
        for line in lines:
            projectList = line.split(":")
            if projectList[0] == userID:
                userProjects.projectList[1]
            i+=1
        j=1
        for project in userProjects:
            print(j, "_", project)
            j += 1
        optionoice = input()
        Project.editproject(optionoice)
        menu2(user)

    elif option == "D" or option == "d":
        print("   Delete Project")
        print("  ----------------\n")
        print("Enter the project title you want to delete: ")
        userID = user[0]
        file = open("projects.txt", "r")
        lines = file.readlines()
        userProjects = []
        i = 0
        for line in lines:
            projectList = line.split(":")
            if projectList[0] == userID:
                userProjects.append(projectList[1])
            i += 1
        j = 1
        for project in userProjects:
            print(j, "_", project)
            j += 1
        optionoice = input()
        Project.delproject(optionoice, user[0])
        menu2(user)

    elif option == "S" or option == "s":
        print(" Search for project using start date")
        print(" --------------------------------------\n")
        date = input("Enter Project Start Date to Search: ")
        optioneckdate = dateval(date)
        if optioneckdate:
            projects = Project.sbydate(optioneckdate)
        for project in projects:
            print("Project Title: ", project[1])
            print("Project Details: ", project[2])
            print("Project Total Target: ", project[3])
            print("Project Start Date: ", project[4])
            print("Project End Date: ", project[5])
            print("\n")
            menu2(user)

    elif option == "Q" or option == "q":
            pass

def menu1 ():
    print(" \n       Welcome in my donation consol app         ")
    option = input("Please select a choice from:\n              R --> Registeration \n              L --> Login \n              Exit \n:")
    
    if option == "R" or option == "r":
        print("   Registeration")
        print("  ----------------")
        user = Register()
        user.register()
        strID= str(user.id)
        list = [strID, user.fname, user.lname, user.email, user.password, user.phonenum]
        l = " "
        for item in list:
            l += item
            l += ":"
        file = open("usrsdb.txt","a")
        file.write(l)
        file.write("\n")
        file.close()
        menu1()
    
    elif option == "L" or option == "l":
        print("   Login")
        print("  -------")
        user = Login()
        userInfo = user.login()
        menu2(userInfo)
        menu1()
    
    elif option == "exit":
        pass

menu1()