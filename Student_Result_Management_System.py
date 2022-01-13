import os
import random
from datetime import date

#function to add new Student in .Csv
def createStudent():
    flag = True
    studID = random.randint(0, 100)
    studName = str(input("Enter Student Name :"))
    while (flag == True):
        studemail = str(input("enter e-mail in proper format :"))
        if '@' not in studemail or '.' not in studemail:
            print('Enter Valid E-mail ID')
        else:
            break
    english_marks = int(input("enter marks of english :"))
    maths_marks = int(input("enter marks of maths :"))
    science_marks = int(input("enter marks of science :"))
    while (True):
        studDate_of_Birth = str(input('enter birthdate in (dd-mm-yyyy) format only :'))
        try:
            if '-' not in studDate_of_Birth and len(studDate_of_Birth) != 10 not in studDate_of_Birth:
                print('Enter Valid Student Brith date')
            else:
                break
        except:
            print('Enter Valid Student Brith date')

    total = english_marks + maths_marks + science_marks
    percentage = int((total / 300) * 100)
    print(studName, 'Your Total is :', total, '& Percentage is :', percentage)
    file = open('StudentResultDb.csv', 'a')
    file.writelines(f"\n{studID},{studName},{studemail},{english_marks},{maths_marks},{science_marks},{total},{percentage},{studDate_of_Birth}")
    file.close()
    print("\n\n New Record add Successfully \n\n")

# function to display All Records in file
def displayStudent():
    print("\n \n List of Present Records \n \n")
    print("StudentID-Student Name-Student Email-English marks-Maths Marks-Science Marks-Total-Percentage-Student-Date_of_Birth")
    file = open("StudentResultDb.csv", "r")
    while (True):
        content = file.readline()
        l = len(content)
        if (l == 0):
            break
        print(content.strip())
    file.close()

# Function to Search Student Details by Name
def findStudentByName():
    Search = str(input("Enter Student Name to search  "))
    file = open("StudentResultDb.csv", "r")
    flag = 0
    while (True):
        line = file.readline()
        length = len(line)
        if length == 0:
            break
        g = line.split(',')
        if (g[1] == Search):
            print("\n Record Found")
            print("Student ID = ", g[0])
            print("Student Name = ", g[1])
            print("Student E-mail = ", g[2])
            print("Student English Marks =", g[3])
            print("Student Math Marks =", g[4])
            print("Student Science Marks =", g[5])
            print("Total =", g[6])
            print("Percentage =", g[7])
            print("Date of Birth =", g[8])
            flag = 1
            break
    if (flag == 0):
        print('Record Not Found')
    file.close()

#function to delete Student by id
def removeStudentByID():
    id = int(input("enter student ID "))
    search = str(id)
    file = open("StudentResultDb.csv", "r")
    temp = open("temp.csv", "w")
    h = 0
    while (True):
        line = file.readline()
        l = len(line)
        if (l == 0):
            break
        g = line.split(',')
        if (g[0] != search):
            temp.write(line)
        if (g[0] == search):
            print('\n  Deleted recored is')
            print('\n',g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8])
            h = 1
    file.close()
    temp.close()
    if (h == 1):
        print("record deleted succsfully ")
        os.remove("StudentResultDb.csv")
        os.rename("temp.csv", "StudentResultDb.csv")
    elif (h == 0):
        print("record not found ")

# Function to separate bright Student
def brightStudent():
    flag = True
    file = open("StudentResultDb.csv", "r")
    while(True):
     list = []
     line = file.readline()
     g = line.split(',')
     for i in g:
         if int(g[7].strip()) >= 80:
            list.append(i)
            False
    file.close()
    print(list)

# Function to calculate age
def AgeCalculator():
    today = date.today()
    Search = str(input("Enter Student Name to search "))
    file = open("StudentResultDb.csv", "r")
    h = 0
    while (True):
        line = file.readline()
        g = line.split(',')
        if (g[1] == Search):
            print("Student is Present in Database")
            birthDateYear = int(g[8][-5:])
            age = (today.year - birthDateYear)
            print('Running year is ', today.year, '& birth year', birthDateYear)
            print("Age of ", Search, "is", age)
            h = 1
            break
    file.close()
    if h == 1:
        pass
    elif(h==0):
        print('Student Name not found in database')


# main function to control the program flow
def main():
    flag = True
    print("****************************************************************")
    print("\n Your options as follows :")
    print('\n 1.Add New Record')
    print('\n 2.Display All Record')
    print('\n 3.Search Student Record by Name')
    print('\n 4.Delete Student Record by Student ID')
    print('\n 5.Display list of Greater than 80% Students')
    print('\n 6.Calculate Age of the Student')
    print('\n 7.Exit')
    print("****************************************************************")
    while True:
        try:
            n = int(input("Enter your Choice :"))
            break
        except :
            print("Please input integer only...")
            continue

    while (flag == True):
            if (n == 7):
              print("Thank You....!")
              quit()
            elif n == 1:
              createStudent()
              main()
            elif n == 2:
              displayStudent()
              main()
            elif n == 3:
              findStudentByName()
              main()
            elif n == 4:
              removeStudentByID()
              main()
            elif n == 5:
              brightStudent()
              main()
            elif n == 6:
              AgeCalculator()
              main()
            else:
              print("Enter Choice between : 1-5 only")
              flag = False
              if flag == False:
                  main()





if __name__ == "__main__":
    main()


















