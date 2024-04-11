num=input("whear you study: ")

if num=="goa":
    print(True)
else :
     print("your decision is wrong ")



num1=int(input("pls enter pirce"))
num2=int(input("pls enter your bughet"))

if num2 == num1 :
     print('you can buy') 

if num2>num1 :
   print("you can buy")

else  :
     print("you need more ")
     print(num1 - num2)


name=int(input("pls enter any number"))

if name == 5 and name > 5 :
    print(int(name * 2 )) 
    
elif name == 1 and name == 2  and name == 3 and name == 4 :  
     print(name * 4 )



bileti=10
yidva=input("how many bileti do you buy")

if yidva<5 :
    print(bileti * yidva)
elif yidva>5 :
    print()