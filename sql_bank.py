from dataclasses import dataclass
from itertools import count
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='bank'
)
mycursor=mydb.cursor()
custm_id='4b2s2S5O'
count2=0
def user_pswd():
    global count2
    user_id=input("Enter Your User_id : ")
    password=input("Enter Your Password: ")
    sql="SELECT custm_id,password FROM user_deta WHERE custm_id= %s"
    val=(user_id,)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchone()
        
    if(myresult==None):
        while count2<2:
            print("Enter valid User id / Password>>>")
            count2=count2+1
            print(count2)
            user_pswd()
        print("**************You have tried enough\n Have a Nice Day*********")
    # elif(myresult[0]==user_id and myresult[1]==password):
    #     print("1.Check Your Balance \n 2.Withdrawal \n 3.Deposit \n 4.Mini Statement ")
    #     opt=int(input("Select your options>>>"))
        # if(opt==1):
        #     Show_blance()
        # elif(opt==2):
        #     debit()
        # elif(opt==3):
        #     credit()
        # elif(opt==4):
        #     mini_statement()
        # # elif(myresult[0]!=user_id or myresult[1]!=password):
        #     count2=0
        #     while count2<3:
        #         print("Enter valid User id / Password>>>")
        #         user_pswd()
        #         count2=count2+1
        #     if count2==3:
        #         print("**************You have tried enough\n Have a Nice Day*********")
user_pswd()