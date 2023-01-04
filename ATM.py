import email
from itertools import count
from math import lgamma
from tokenize import Name
import random
import ast
import itertools
import datetime


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
    Name= input("Enter Your Name>>> ")
    dob=input("Enter Your Date Of Birth Format(date/month/year)>>>")
    email_id=input("Enter Your Email Id>>> ")
    pan=input("Enter your Pan Number>>> ")
    Adhhar_no=input("Enter Your Aadhar Number>>> ")
    pin_c=input("Create Your ATM pin>>> ")
    list1=[0,1,2,3,4,5,6,7,8,9]
    gen_card=""
    while len(gen_card)!=16:
        gen_card= gen_card + str(random.choice(list1))
    dict_data1={
        "Name":Name,"DOB":dob,"PAN":pan,"AAdhar_NO":Adhhar_no,"ATM_PIN":pin_c,"Card_no":gen_card,"Email_id":email_id,"Ac_Bal":0.00,"txt":{},'txt_count':0
    }
    with open(f"{email_id}.txt",'w') as f:
        f.write(f"{dict_data1}")   
    print(f"Your Account is Open Successfully \n Your card no. is {gen_card} \n User Id : {email_id}")
    print("Do You Want To log in Yes/No")
    opt=input("")
    if(opt.lower()=="yes"):
        log_in()
    else:
        print("*********THANK YOU*************\n HAVE A NICE DAY*****************")

def log_in():
    global dict_data
    user_id=input("Enter Your User_id : ")
    with open(f"{user_id}.txt",'r') as f:
        dict_data=f.read()
    dict_data = ast.literal_eval(dict_data)
    count2=0
    lg_pin=input("Enter Your ATM Pin : ")
    while dict_data["ATM_PIN"]!=lg_pin:
        count2=count2+1
        print("You Entered Wrong PIN")
        lg_pin=input("Enter Again Your ATM Pin : ")
        if count2==3:
            break
    if(user_id==dict_data["Email_id"] and dict_data["ATM_PIN"]==lg_pin):
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
    elif(dict_data["ATM_PIN"]!=lg_pin):
        print("***********Worng PIN*************Thank You ")
def debit():
    global dict_data
    dict_data["txt_count"] = dict_data["txt_count"]+1
    txt_count = dict_data["txt_count"]
    txt_name = "txt00"+str(txt_count)
    file_name=dict_data["Email_id"]
    amnt=int(input("Enter Your Ammount : "))
    if(amnt>dict_data["Ac_Bal"]):
        print("Insufficient Balance")
    else:
        dict_data["Ac_Bal"]=dict_data["Ac_Bal"]-amnt
        dict_data["txt"][txt_name]=str(amnt)+"Dr"
        print(f"Now your Balance is ",dict_data["Ac_Bal"])
    with open(f"{file_name}.txt",'w') as f:
        f.write(f"{dict_data}")
def credit():
    file_name=dict_data["Email_id"]
    dict_data["txt_count"]=dict_data["txt_count"]+1
    txt_count=dict_data["txt_count"]
    txt_name="txt00"+str(txt_count)
    amnt=int(input("Enter Your Ammount"))
    dict_data["Ac_Bal"]=dict_data["Ac_Bal"]+amnt
    dict_data["txt"][txt_name]=str(amnt)+"Cr"
    print("Now Your current Balance is : ",dict_data["Ac_Bal"] ,"\n ******************THANK YOU*************************")
    with open(f"{file_name}.txt",'w') as f:
        f.write(f"{dict_data}")
def Show_blance():
    print(dict_data["Ac_Bal"])
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
    len1=len(dict_data["txt"])
    if len(dict_data["txt"])>5:
        slicedDict = dict(itertools.islice(dict_data["txt"].items(), len1-4 ,len1-1))
    else:
        slicedDict = dict(itertools.islice(dict_data["txt"].items(), 0,4))
    print(slicedDict)
    
display()

        
        
        
    