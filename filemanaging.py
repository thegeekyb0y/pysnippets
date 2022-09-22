# Question: Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.

import pickle

def  Writerecord(sroll,sname):
    with open ('StudentRecord1.dat','ab') as Myfile:
        srecord={"SROLL":sroll,"SNAME":sname}        
        pickle.dump(srecord,Myfile)

def Readrecord():
    with open ('StudentRecord1.dat','rb') as Myfile:
        print("\n-------DISPALY STUDENTS DETAILS--------")
        print("\nRoll No.",' ','Name','\t',end='')
        print()
        while True:
           try:
               rec=pickle.load(Myfile)
               print(' ',rec['SROLL'],'\t  ' ,rec['SNAME'])
           except EOFError:
               break
def Input():
    n=int(input("How many records you want to create :"))
    for _ in range(n):
        sroll=int(input("Enter Roll No: "))
        sname=input("Enter Name: ")
        Writerecord(sroll,sname)

def SearchRecord(roll):
    with open ('StudentRecord1.dat','rb') as Myfile:
       while True:
          try:
               rec=pickle.load(Myfile)
               if rec['SROLL']==roll:
                   print("Roll NO:",rec['SROLL'])
                   print("Name:",rec['SNAME'])

          except EOFError:
              print("Record not find..............")
              print("Try Again..............")
              break

def main():

    while True:
        print('\nYour Choices are: ')
        print('1.Insert Records')
        print('2.Dispaly Records') 
        print('3.Search Records (By Roll No)')
        print('0.Exit (Enter 0 to exit)')
        ch=int(input('Enter Your Choice: '))
        if ch==1:
            Input()
        elif ch==2:
            Readrecord()
        elif ch==3:
            r=int(input("Enter a Rollno to be Search: "))
            SearchRecord(r)
        else:
            break
main()
