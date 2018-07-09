#!/usr/bin/python
#name:address_book.py
#function:the program can manage you address 
#author:Allen_fu
#time:2011.02.14
# today is valentine's day but I'm coding before the 

import cPickle as p 
import sys
a_book={}
class Book:
    global a_book
    flag=0 #if data changed the flag will be 1
    def __init__(self,name="<name>",address="<address>",phone="<phone_number>"):
        self.name=name
        self.address=address
        self.phone=phone
        
    def __del__(self): #when class exit the code will performance
        print 'Address Book exit' ####
        
    def add(self,name,address,phone): #add a user's address
        if name in a_book:
            print "The name \"%s\" is exist."%name
        else:
            a_book[name]=[address,phone]
            self.flag=1
            print "add %s's address success!"%name
    def delete(self,name): #delete a user's address 
        if name in a_book:
            del a_book[name]
            self.flag=1
            print 'del %s success!'%name
        else:
            print "no user named:%s"%name
    def find(self,name):
        if name in a_book:
            print '%-10s %-10s %-10s' %(self.name,self.address,self.phone)
            print '%-10s %-10s %-10s' %(name,a_book[name][0],a_book[name][1])
        else:
            print "can't find the name:%s"%name
    def ls(self): #list all user's address
        print '%-10s %-10s %-10s' %(self.name,self.address,self.phone)
        for name,address in a_book.items():
            print '%-10s %-10s %-10s'%(name,address[0],address[1])
    def exit_e(self): #system exit;if the data changed ask whether save or not 
        while True:
            if self.flag==1:
                i=raw_input("The data is changed do you wan't to save?(y/n)")
                if i=='y':
                    self.save()
                    break
                elif i=='n':
                    break
                else:
                    print "Please input right command!"
        sys.exit()
    def save(self):
        f=file(filename,'w')
        p.dump(a_book,f)
        print 'save the address book success.'
        f.close()
    
def printopt(): #print the commands that user can use
    print "You can type the options below:"
    print "To add a person:"
    print " add <name> <address> <phone_number>"
    print "To delete a person:"
    print " del <name>"
    print "To find a person's address book:"
    print " find <name>"
    print "To list all person in you address book:"
    print " list"
    print "To save data you changed:"
    print " save"
    print "To exit the program:"
    print " exit"
    print "To get help:"
    print " help"
    print '-------------------------------'

#The entry of the program
print 'The program is to manage your address book.'
filename=raw_input("what name of your address book? The default is Allens_ab.txt when you enter nothing.\n-->")
if len(filename)==0:
    print 'use default name \"Allens_ab.txt\"'
    filename="Allens_ab.txt"
    print '-------------------------------'
else:
    print 'use file name \"%s\"' %(filename)
    print '-------------------------------'
ab=Book() ####
try:
    f=file(filename)
    a_book=p.load(f)
    f.close()
except:
    pass
printopt() #print the usage to user 

while True: #handle the command that inputed by user
    cmd=raw_input("-->")
    cmd_s=cmd.split(' ')
    if cmd_s[0]=='add':
        if len(cmd_s)<4:
            print "wrong format."
            print "Usage: add <name> <address> <phone_number>"
        else:
            ab.add(cmd_s[1],cmd_s[2],cmd_s[3])
    elif cmd_s[0]=='del':
        ab.delete(cmd_s[1])
    elif cmd_s[0]=='find':
        ab.find(cmd_s[1])
    elif cmd_s[0]=='list':
        ab.ls()
    elif cmd_s[0]=='save':
        ab.save()
    elif cmd_s[0]=='exit':
        ab.exit_e()
    elif cmd_s[0]=='help':
        printopt()
    else:
        print 'command not found,please input the command above.'