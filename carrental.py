import time
import mysql.connector as myc
global mycon,mycursor
mycon=myc.connect(host="localhost",user="root",passwd="1234",database="temptravel")
mycursor=mycon.cursor()
def introduction():
    text='''
                                      WELCOME TO TEMPTRAVEL
                                                -best car rental service
    TempTravel was established in 1989, as a part of L&M Enterprises – a progressive and diversified Group.
    TempTravel license is owned by Mr.Deepak Shah and under his Chairmanship, 
    We have been serving its clientele in the UAE with regards to their short and long term car rental needs for more than 32 years.
    TempTravel Car Rental is one of the leading international car rental companies with headquarters in India, Established in 1958.
    With a fleet size in excess of 900,000 and staff strength of over 8000, operates in 80 countries and 500 locations world wide.
                    Call us directly for best rates and offers
                            ABU-DHABI : 0566474752
                            DUBAI     : 0567375367
                    Thanks for you support and co-operation
            We will serve you even during weekends and public holiday's
    '''
    for i in text:
        print(i,end='')
        time.sleep(0.010)
#customer menu and function
def cheapcar():
    print()
    print("1. for per day")
    print("2. for per month")
    cho=int(input("enter your choice:"))
    if cho==1:
        mycursor.execute("select * from carinfo where rentperday between 100 and 1000 and status='Available'")
        data=mycursor.fetchall()
        for i in data:
            print(i)
    elif cho==2:
        mycursor.execute("select * from carinfo where rentpermonth between 1000 and 3000 and status='Available'")
        data=mycursor.fetchall()
        for i in data:
            print(i)
def changedetails(uname,upass):
    print("Enter 1 to change address")
    print("Enter 2 to change phone number")
    ch=int(input("Enter your choice:"))
    if ch==1:
        p=input("enter new address:")
        qu="update customerinfo set address='{}' where username='{}' and password='{}'".format(p,uname,upass)
        mycursor.execute(qu)
        mycon.commit()
        print("successfully changed")
    elif ch==2:
        p=input("enter new phoneno:")
        qu="update customerinfo set phoneno={} where username='{}' and password='{}'".format(p,uname,upass)
        mycursor.execute(qu)
        mycon.commit()
        print("successfully changed")
def delacc(uname,upass):
    op=input("Are to sure to delete the account(yes/no):")
    if op=="yes" or op=="YES" or op=="Yes":
        qu="delete from customerinfo where username='{}' and password='{}'".format(uname,upass)
        mycursor.execute(qu)
        mycon.commit()
        print("successfully deleted")
    else:
        print()
def viewcustomercars():
    mycursor.execute("select * from carinfo where status='Available'")
    data=mycursor.fetchall()
    for i in data:
        print(i)
def book(uname,upass):
    viewcustomercars()
    print("enter 1 to book for a month")
    print("enter 2 to book for a day")
    print("enter 3 to exit")
    ch=int(input("Enter your choice:"))
    carno=int(input("Enter car number to book:"))
    if ch==1:
        qu="select * from carinfo where carno={}".format(carno)
        mycursor.execute(qu)
        data=mycursor.fetchone()
        print(data)
        op=input("Are to sure to book this car (yes/no):")
        if op=="yes" or op=="YES" or op=="Yes":
            qu="select rentpermonth+advanceamount as totalcost from carinfo where carno={}".format(carno)
            mycursor.execute(qu)
            data=mycursor.fetchone()
            (a,)=data
            print("Your total cost is",a,"Dhs")
            print()
            print("    PAYMENT")
            print("Select your convinient payment mode")
            print()
            print("enter 1 for card")
            print("enter 2 for cash on delivery")
            ch=int(input("Enter choice:"))
            if ch==2:
                p="Not Available"
                qu="update carinfo set status='{}' where carno={}".format(p,carno)
                mycursor.execute(qu)
                mycon.commit()
                qui="update customerinfo set carbooked={} where username='{}' and password='{}'".format(carno,uname,upass)
                mycursor.execute(qui)
                mycon.commit()
                print("Your Total bill amount is:",a,"Dhs")
                print("Car will be delivered within 12 hours of booking.Our agent will contact you at the time of delivery")
                print("for further enquiry contact our customer service")
                print()
                print("Thank you for accessing our service!!")
            elif ch==1:
                print("Your Total bill amount is:",a,"Dhs")
                a=int(input("Enter card number:"))
                b=input("Enter card holder's name(same as in card):")
                c=int(input("Enter cvv number:"))
                d=input("Enter date of expiry:")
                otp=int(input("Enter OTP number:"))
                if otp==1234:
                    p="Not Available"
                    qu="update carinfo set status='{}' where carno={}".format(p,carno)
                    mycursor.execute(qu)
                    mycon.commit()
                    qui="update customerinfo set carbooked={} where username='{}' and password='{}'".format(carno,uname,upass)
                    mycursor.execute(qui)
                    mycon.commit()
                    print("Your payment has been successful")
                    print("Car will be delivered within 12 hours of booking")
                    print("for further enquiry contact our customer service")
                    print()
                    print("Thank you for accessing our service!!")
                else:
                    print("Entered wrong OTP")
                    book()
    elif ch==2:
        qu="select * from carinfo where carno={}".format(carno)
        mycursor.execute(qu)
        data=mycursor.fetchone()
        print(data)
        op=input("Are to sure to book this car (yes/no):")
        if op=="yes" or op=="YES" or op=="Yes":
            qu="select rentperday+advanceamount as totalcost from carinfo where carno={}".format(carno)
            mycursor.execute(qu)
            data=mycursor.fetchone()
            (a,)=data
            print("Your total cost is",a,"Dhs")
            print()
            print("    PAYMENT")
            print("Select your convinient payment mode")
            print()
            print("enter 1 for card")
            print("enter 2 for cash on delivery")
            ch=int(input("Enter choice:"))
            if ch==2:
                p="Not Available"
                qu="update carinfo set status='{}' where carno={}".format(p,carno)
                mycursor.execute(qu)
                mycon.commit()
                qui="update customerinfo set carbooked={} where username='{}' and password='{}'".format(carno,uname,upass)
                mycursor.execute(qui)
                mycon.commit()
                print("Your Total bill amount is:",a,"Dhs")
                print("Car will be delivered within 12 hours of booking.Our agent will contact you at the time of delivery")
                print("for further enquiry contact our customer service")
                print()
                print("Thank you for accessing our service!!")
            elif ch==1:
                print("Your Total bill amount is:",a,"Dhs")
                print()
                a=int(input("Enter card number:"))
                b=input("Enter card holder's name(same as in card):")
                c=int(input("Enter cvv number:"))
                d=input("Enter date of expiry:")
                otp=int(input("Enter OTP number:"))
                if otp==1234:
                    p="Not Available"
                    qu="update carinfo set status='{}' where carno={}".format(p,carno)
                    mycursor.execute(qu)
                    mycon.commit()
                    qui="update customerinfo set carbooked={} where username='{}' and password='{}'".format(carno,uname,upass)
                    mycursor.execute(qui)
                    mycon.commit()
                    print("Your payment has been successful")
                    print("Car will be delivered within 12 hours of booking")
                    print("for further enquiry contact our customer service")
                    print()
                    print("Thank you for accessing our service!!")
                else:
                    print("Entered wrong OTP")
                    book()
def returncar(uname,upass):
    carno=int(input("Enter car number to be returned"))
    qu="select * from customerinfo where carbooked={} and username='{}' and password='{}'".format(carno,uname,upass)
    mycursor.execute(qu)
    data=mycursor.fetchall()
    if len(data)==1:
        a=0
        qui="update customerinfo set carbooked={} where username='{}' and password='{}'".format(a,uname,upass)
        mycursor.execute(qui)
        mycon.commit()
        p="Available"
        qu="update carinfo set status='{}' where carno={}".format(p,carno)
        mycursor.execute(qu)
        mycon.commit()
def signin():#Customer basic menu
    print()
    print()
    print("    SIGN IN")
    print("if forgot username and password contact our customer service")
    print()
    uname = input('Enter your username :')
    upass = input('Enter your Password :')
    q='select * from customerinfo where username="{}" and password ="{}"'.format(uname,upass)
    mycursor.execute(q)
    data= mycursor.fetchall()
    if len(data)==1: #Check if entered username and password is correct
        print()
        print()
        print('successfully signed in')
        while True:
            print()
            print()
            print("1. search all cars")
            print("2. to search the cheapest cars")
            print("3. to book a car")
            print("4. to return a car")
            print("5. change personal details")
            print("6. to delete account")
            print("7. to exit")
            ch=int(input("Enter your choice:"))
            if ch==1:
                viewcustomercars()
            elif ch==2:
                cheapcar()
            elif ch==3:
                book(uname,upass)
            elif ch==4:
                returncar(uname,upass)
            elif ch==5:
                changedetails(uname,upass)
            elif ch==6:
                delacc(uname,upass)
                break
            elif ch==7:
                print("Thank you for visiting!!")
                print("--------------------------------------------------------------------------")
                break
    else:
        print("Entered wrong username or password")
        signin() #When wrong entries is entered
def signup():
    print()
    print()
    print("    SIGN UP")
    firstname=input("Enter your firstname:")
    lastname=input("Enter your lastname:")
    address=input("Enter your address:")
    phoneno=int(input("Enter phone number:"))
    nationality=input("Enter nationality:")
    licenseno=int(input("Enter licenseno:"))
    username=input("Enter username:")
    a=input("Re-enter your username:")
    if username==a:
        password=input("Enter your password:")
        b=input("Re-enter your password:")
        if password==b:
            ins="insert into customerinfo(firstname,lastname,address,phoneno,nationality,licenseno,username,password) values('{}','{}','{}',{},'{}',{},'{}','{}')".format(firstname,lastname,address,phoneno,nationality,licenseno,username,password)
            mycursor.execute(ins)
            mycon.commit()
            print()
            print("Sucessfully added")
            signin()
        else:
            print()
            print("wrong entries entered")
            signup()
    else:
        print()
        print("wrong entries entered")
        signup()
def customer():
    print("1. To sign in")
    print("2. To sign up")
    chr=int(input("Enter your choice:"))
    if chr==1:
        signin()
    if chr==2:
        signup()
    
#staff menu and functions
def staff():#Staff basic menu
    password=input("Enter staff password:")
    while True:
        if password=="staff@temp":
            print()
            print()
            print("1. To view all car details")
            print("2. To add new car")
            print("3. to delete a car")
            print("4. to change the details of a car")
            print("5. To view details of customer who booked a particular car")
            print("6. To view details of all customers")
            print("7. Enter 7 to exit")
            print()
            chr=int(input("Enter your choice:"))
            if chr==1:
                viewcars()
            elif chr==2:
                addcar()
            elif chr==3:
                delcar()
            elif chr==4:
                changede()
            elif chr==5:
                carbooked()
            elif chr==6:
                viewcustomers()
            elif chr==7:
                print("--------------------------------------------------------------------------")
                break
        else:
            print("Wrong password!!!")
            break
def carbooked():
    carno=int(input("Enter carno:"))
    qu="select * from customerinfo where carbooked={}".format(carno)
    print()
    mycursor.execute(qu)
    data=mycursor.fetchone()
    print(data)
def viewcustomers():
    mycursor.execute("select * from customerinfo")
    data=mycursor.fetchall()
    for i in data:
        print(i)
def changede():
    print()
    print('''enter 1 to change rent per day
enter 2 to change rent per month
enter 3 to change advance amount
enter 4 to change status''')
    ch=int(input("Enter your choice:"))
    if ch==1:
        carno=int(input("enter car no whose rent per day is to be changed:"))
        p=float(input("enter new rent (per day):"))
        qu="update carinfo set rentperday={} where carno={}".format(p,carno)
        mycursor.execute(qu)
        mycon.commit()
        print("successfully changed")
    elif ch==2:
        carno=int(input("enter car no whose rent per month is to be changed:"))
        p=float(input("enter new rent (per month):"))
        qu="update carinfo set rentpermonth={} where carno={}".format(p,carno)
        mycursor.execute(qu)
        mycon.commit()
        print("successfully changed")
    elif ch==3:
        carno=int(input("enter car no whose advance amount is to be changed:"))
        p=float(input("enter new advance:"))
        qu="update carinfo set advanceamount={} where carno={}".format(p,carno)
        mycursor.execute(qu)
        mycon.commit()
        print("successfully changed")
    elif ch==4:
        carno=int(input("enter car no whose status is to be changed:"))
        p=input("enter new status:")
        qu="update carinfo set status='{}' where carno={}".format(p,carno)
        mycursor.execute(qu)
        mycon.commit()
        print("successfully changed")
def viewcars():
    mycursor.execute("select * from carinfo")
    data=mycursor.fetchall()
    for i in data:
        print(i)
def addcar():
    carno=int(input("Enter car number:"))
    companyname=input("Enter company name:")
    carmodelname=input("Enter model name:")
    yearofmanu=input("Enter year of manufacture:")
    rentperday=float(input("Enter rent per day:"))
    rentpermonth=float(input("Enter rent per month:"))
    advanceamount=float(input("Enter advance amount:"))
    print()
    status= "Available"
    ins="insert into carinfo values({},'{}','{}','{}',{},{},{},'{}')".format(carno,companyname,carmodelname,yearofmanu,rentperday,rentpermonth,advanceamount,status)
    mycursor.execute(ins)
    mycon.commit()
    print("Sucessfully added")
def delcar():
    carno=int(input("enter car no of car to be deleted:"))
    qu="delete from carinfo where carno={}".format(carno)
    mycursor.execute(qu)
    mycon.commit()
    print("successfully deleted")
#introduction paragraph
introduction()
print()
print()
print()
print()
print("Enter 'C' to enter as customer")
print("Enter 'S' to enter as staff")
enteras=input("Enter your choice:")
if enteras=="c" or enteras=="C":
    customer()
elif enteras=="s" or enteras=="S":
    staff()
