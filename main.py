import time
from Tkinter import *
from tkMessageBox import *

#List of Student Grades
GRADES = ['K',1,2,3,4,5, 'Middle', 'High', 'College']

#Adds studdent info and Check In time to checkins.csv
def addToFile():
    out = open('checkins.csv', 'a')
    out.write(student.get() + ',' + grade.get() + ',' + teacher.get() + ',' + subject.get() + ',' + time.strftime('%c') +'\n')
    out.close()
    showinfo(title="Check-In",message=student.get()+" checked in Successfully!")

def main():
    #File with Student names, Subjects, and Teacher Names
    f = open('data.csv')
    l = f.read().split('\n')
    f.close()
    for line in xrange(len(l)):
        l[line] = l[line].split(',')

    #Populate Menus
    students = []
    teachers = []
    subjects = []
    for line in l[1:]:
        if line[0] != '':
            students += [line[0]]
        if line[1] != '':
            subjects += [line[1]]
        if line[2] != '':
            teachers += [line[2]]

    runGui(students,subjects,teachers)

def initLabels():
    studentLabel = Label(root, text="Student:")
    gradeLabel = Label(root, text="Grade:")
    teacherLabel = Label(root, text="Teacher:")
    subjectLabel = Label(root, text="Subject:")

    studentLabel.grid(row=0,column=0,sticky=N+S+E+W)
    gradeLabel.grid(row=1,column=0,sticky=N+S+E+W)
    teacherLabel.grid(row=2,column=0,sticky=N+S+E+W)
    subjectLabel.grid(row=3,column=0,sticky=N+S+E+W)


def initMenus(students,subjects,teachers):
    global student
    global grade
    global teacher
    global  subject
    student = StringVar(root)
    student.set(students[0])
    grade = StringVar(root)
    grade.set(GRADES[0])
    teacher = StringVar(root)
    teacher.set(teachers[0])
    subject = StringVar(root)
    subject.set(subjects[0])

    #assign values to menus
    studentBox = apply(OptionMenu, (root,student) + tuple(students))
    studentBox.grid(row=0,column=1,sticky=N+S+E+W)
    gradeBox = apply(OptionMenu, (root,grade) + tuple(GRADES))
    gradeBox.grid(row=1,column=1,sticky=N+S+E+W)
    teacherBox = apply(OptionMenu, (root,teacher) + tuple(teachers))
    teacherBox.grid(row=2,column=1,sticky=N+S+E+W)
    subjectBox = apply(OptionMenu, (root,subject) + tuple(subjects))
    subjectBox.grid(row=3,column=1,sticky=N+S+E+W)

#Gui Code
def runGui(students,subjects,teachers):
    global root
    root = Tk()
    Grid.columnconfigure(root,1,weight=1)
    initLabels()
    initMenus(students,subjects,teachers)
    Button(root,text="Check-In",command = addToFile).grid(row=4,columnspan=2)
    root.title('Check-In')
    root.iconbitmap('bg.ico')
    root.geometry('255x155')
    root.resizable(width=False, height=False)
    root.mainloop()
if __name__ == "__main__":
    main()