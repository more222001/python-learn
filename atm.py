
import time

print("please insert your card")
time.sleep(5)

password=1234
pin=int(input("enter your atm pin:"))
balance=5000
if pin==password:
    while True:

     print("""
    1==balance
    2==withdraw balance
    3==depoist balance
    4==exit
   """ 
   )
     try:
       option=int(input("please enter your choice  "))
     except:
        print("enter valid option")

     if option==1:
        print(f"your current balnce is {balance}")
        print("========================================")

     if option==2:
        withdraw_amount=int(input("please enter withdraw_amount "))
        balance=balance-withdraw_amount
        print(f"{withdraw_amount}is debited from your account")
        print(f"your current balnce is {balance}")
        print("========================================")

     if option==3:
        depoist_amount=int(input("please enter depoist_amount"))
        balance=balance+depoist_amount
        print(f"{depoist_amount}is credited in your account")
        print(f"your updated balance is {balance}")
        print("========================================")
        
     if option==4:
     
      break
else:
    print("Invalid pin")