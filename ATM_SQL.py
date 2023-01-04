from cmath import pi
from distutils.util import copydir_run_2to3
import email
from http import server
from itertools import count
from math import lgamma
from operator import concat
from tkinter import INSERT
from tkinter.messagebox import NO
from tokenize import Name
import random
import ast
import itertools
import datetime
import smtplib
import string
import mysql.connector
from numpy import count_nonzero



# **********************SQL************************
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='bank'
)
mycursor=mydb.cursor()

def account_balence():
        # *********************Finding Account Balence********************
    
    sql=f"SELECT SUM(ammount) FROM {user_id} WHERE txn_type='Credit'"
    mycursor.execute(sql)
    totalCr=mycursor.fetchone()
    if totalCr[0]==None:
        totalCr=0
    else:
        totalCr=totalCr[0]

    sql=f"SELECT SUM(ammount) FROM {user_id} WHERE txn_type='Dedit'"
    mycursor.execute(sql)
    totalDr=mycursor.fetchone()
    if totalDr[0]==None:
        totalDr=0
    else:
        totalDr=totalDr[0]
    account_bal=totalCr-totalDr
    
    sql = "UPDATE accounnt_data SET account_bal = %s WHERE custm_id = %s"
    val = (account_bal, user_id)

    mycursor.execute(sql, val)
    mydb.commit()
    
    return account_bal
    
# *****************************Checking a data in database******************************
def check_data1(data,column1,tables):
    sql=f"SELECT {column1} FROM {tables}"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for x in myresult:
        if x[0]== data:
            return True
    return False
# ******************************table Empty or not**********************
def empty(tables):
    sql=f"SELECT COUNT(*) FROM {tables}"
    mycursor.execute(sql)
    myresult=mycursor.fetchone()
    if myresult[0]==0:
        return True
    else:
        return False
# ***********************************random Number(OTP)********************
def randm_num():
    list1=[0,1,2,3,4,5,6,7,8,9]
    
    rndm_num=""
    while len(rndm_num)!=6:
        rndm_num= rndm_num + str(random.choice(list1))+random.choice(string.ascii_letters)
    return rndm_num
        
# ********************************Gen. Custm_id*******************************
def custm_id1():
    list1=[0,1,2,3,4,5,6,7,8,9]
    
    custm_id=""
    while len(custm_id)!=8:
        custm_id= custm_id + str(random.choice(list1))+random.choice(string.ascii_letters)
    
    empt=empty("customer")
    if empt:
        return custm_id
    else:
        check_data=check_data1(custm_id,"custm_id", "customer")
    
        if check_data:
            custm_id1()
        else:
            return custm_id
    # ***************Gen. password******************
def gen_pass():   
    list3=['#','@','&','$']
    list2=[str(random.choice(list3)),random.choice(string.ascii_letters),random.randint(1,9)]
    list4=[random.choice(string.ascii_letters),random.randint(1,9),str(random.choice(list3))]
    password=""
    while len(password)!=8:
        password=password+str(random.choice(list2))+str(random.choice(list4))
    empt=empty("user_deta") 
    if empt:
        return password
    else:
        check_data=check_data1(password,"password","user_deta")
        if check_data:
            gen_pass()
        else:
            return password
    
   # *********************Gen account_no************************
def gen_ac():
    account_no="7412"
    while len(account_no)!=12:
        account_no=account_no+str(random.randint(1,9))
    empt=empty("accounnt_data")
    if empt:
        return account_no
    else:
        check_data=check_data1(account_no,"account_no","accounnt_data")
        if check_data:
            gen_ac()
        else:
            return account_no
        
# *****************************input email_id*******************************
def email_inpt():
    email_id=input("Enter Your Email Id>>> ")
    if empty("customer"):
        return email_id
    else:
        check_data=check_data1(email_id,"email_id","customer")
        if check_data:
            print("Email Already Exits \n Enter another Email>>>")
            email_inpt()
        else:
            return email_id
    
# *****************************input data*******************************
def data_inpt(data,column1,tables,data_type):
    inpt_data=data_type(input(f"Enter Your {data}>>> "))
    if empty("customer"):
        return inpt_data
    elif(str(inpt_data)=="" or str(inpt_data)==" "):
        print("Enter a Valid Data")
        data_inpt(data,column1,tables,data_type)
        
    else:
        check_data=check_data1(inpt_data,column1,tables)
        if check_data:
            print(f"{data} Already Exits \n Enter another {data}>>>")
            data_inpt(data,column1,tables,data_type)
        else:
            return inpt_data

count1=0
def display():
    print("***************************WELCOME TO SBI******************\n*******************PLEASE SELECT YOUR OPTIONS*************************")
    global count1
    def recur():
        global count1
        count1=count1+1
        if(count1==4):
            print("You tryed enough \n Have a Nice day")
            exit()
        print("*********************************\n 1.Open Account\n 2.Log In\n**********************************")
        opt=int(input("Enter your options>>>> "))
        if(opt==1):
            register()
        elif(opt==2):
            log_in()
        else:
            print("Opps You entered a wrong input \n Try Again")
            recur()
    recur()
        
def register():
    fi_name= input("Enter Your First Name>>> ")
    la_name=input("Enter Your Last Name>>> ")
    dob=input("Enter Your Date Of Birth Format(date/month/year)>>>")
    email_id=data_inpt("Email Id","email_id","customer",str)
    
    # *******************Sending OTP On email***********************
    otp=randm_num()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('sbm.pvt.lmt@gmail.com','Hmt@2295')
    server.sendmail('sbm.pvt.lmt@gmail.com',email_id,f"Welocme To SBM Bank \n Your OTP is{otp}")
    print("Loding.........")
    inpt_otp=input("Enter Your OTP>>>>>")
    
    if otp==inpt_otp:
        
        contact=data_inpt("Contact No","contact_no","customer",int)
        
        pan=data_inpt("Pan No","pancard_no","customer",str)
        
        Adhhar_no=data_inpt("Aadhar No","aadhar_no","customer",int)
        pincode_no=int(input("Enter Your Pincode NO.>>>>"))
        address=input("Enter your address>>>>")
        city=input("Enter Your city>>>")
        state=input("Enter your State>>>")
        nationality=input("Enter Your Nationality>>>")
        marital_status=input("Enter Your Marital Statu>>")
        employment_tp=input("Enter your employment type>>")
        account_type=input("Enter acount type Saving / Cuurent>>>")
        

            
        custm_id=custm_id1()
        sql= "INSERT INTO customer(custm_id,f_name,l_name,dob,address,pincode,city,state,nationality,aadhar_no,pancard_no,marital_status,employment_type,email_id,contact_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=[(custm_id,fi_name,la_name,dob,address,
            pincode_no,city,state,nationality,Adhhar_no,
            pan,marital_status,employment_tp,email_id,contact)]
        mycursor.executemany(sql,val)
        # mydb.commit()
        password=gen_pass()
            
        
        sql="INSERT INTO user_deta(custm_id,password) VALUES (%s,%s)"
        val=(custm_id,password)
        mycursor.execute(sql,val)
        # mydb.commit()
        account_no=gen_ac()
            
            
        sql="INSERT INTO accounnt_data(custm_id,account_no,account_type) VALUES (%s,%s,%s)"
        val=(custm_id,int(account_no),account_type)
        mycursor.execute(sql,val)
        mydb.commit()
        
        
        # ***********************TXN Data*************************
        mycursor.execute(f"CREATE TABLE {custm_id} (sl_no INT AUTO_INCREMENT PRIMARY KEY,txn_date DATETIME,ammount BIGINT, txn_type VARCHAR(255))")
        
        
        
        # *********************Sending Mail********************
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('sbm.pvt.lmt@gmail.com','Hmt@2295')
        server.sendmail('sbm.pvt.lmt@gmail.com',email_id,
                        f'Welcome To SBM Bank \n Your Account is has been Successfully Opened\n Your Account Number is- {account_no}\n User Id- {custm_id}\n password- {password}')
        
        print("Loding.......")
        print(f"Your Account is Open Successfully\n your Account No. is :{account_no}\n  User Id and password has been sent on your Mail")
        
        
        print("Do You Want To log in Yes/No")
        opt=input("")
        if(opt.lower()=="yes"):
            log_in()
        else:
            print("*********THANK YOU*************\n HAVE A NICE DAY*****************")
            
            
    else:
        print("Invalid Otp Try Again")
    
def log_in():
    global user_id
    global count2
    count2=0
    
    def user_pswd():
        global user_id
        global count2
        user_id=input("Enter Your User_id : ")
        password=input("Enter Your Password: ")
        sql="SELECT custm_id,password FROM user_deta WHERE custm_id= %s"
        val=(user_id,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchone()
        
        if myresult==None:
            while count2<2:
                print("<<<<<Enter valid User id >>>")
                count2=count2+1
                user_pswd()
            print("*********You Have Tried Enough***********")
            
        elif(myresult[1]!=password):
            while count2<2:
                print("<<<<<<<<Enter valid Password >>>>>>>")
                count2=count2+1
                user_pswd()
            print("**************You have tried enough*********")  
                      
        elif(myresult[0]==user_id and myresult[1]==password):
            print("1.Check Your Balance \n 2.Withdrawal \n 3.Deposit \n 4.Mini Statement ")
            opt=int(input("Select your options>>>"))
            if(opt==1):
                Show_blance()
                
            elif(opt==2):
                debit()
            elif(opt==3):
                credit()
            elif(opt==4):
                mini_statement()
    user_pswd()
                
def debit():
    amnt=int(input("Enter Your Ammount : >>>"))
    account_bal=account_balence()
    
    
    if(amnt>account_bal):
        print("Insufficient Balance")
    else:
        sql=f"INSERT INTO {user_id} (txn_date,ammount,txn_type) VALUES(NOW(),{amnt},'Dedit')"
        mycursor.execute(sql)
        mydb.commit()
    
    account_bal=account_balence()
    
    print("Your Account Balence : ",account_bal)
    
    
        
        
# *************************Credit*******************************
def credit():
    amnt=int(input("Enter Your Ammount"))
    sql=f"INSERT INTO {user_id} (txn_date,ammount,txn_type) VALUES(NOW(),{amnt},'Credit')"
    mycursor.execute(sql)
    mydb.commit()
    account_bal=account_balence()
    print(account_bal)

# ****************************Check Balence*************************
def Show_blance():
    
    account_bal=account_balence()
    
    print("Your Account Balence : ",account_bal)
    opt=input("Do You want to Exit(y/n)")
    if opt=="y":
        exit()
    else:
        print("1.Withdrawal \n 2.Deposit \n 3.Mini Statement")
        opt=int(input("select your options >>>"))
        if opt==1:
            debit()
        elif opt==2:
            credit()
        elif opt==3:
            mini_statement()
def mini_statement():
    sql=f"SELECT * FROM {user_id} LIMIT 5"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
    
display()

        
        
        
    