# len=int(input("enter length: "))
# width=int(input("enter width: "))
# area=len*width
# print(f"area of rectangle is {area}cm")

# item=input("wht would u like to buy?: ")
# price=float(input("wht is the price? : "))
# quantity=int(input("how many would u like to buy?: "))
# total=price*quantity
# print(f"u have bought {item}*{quantity}")
# print(f"ur total is: {total}")

# import math

# radius=float(input("enter the radius of the circle: "))
# cir=2*math.pi*radius
# print(f"the circumference of the circle is : {round(cir,2)}")

# name=""
# print(bool(name))

# while True:
#     n1=float(input("Enter number 1: "))
#     n2=float(input("Enter number 2: "))
#     op=input("enter operator(+,-,*,%,/,**): ")
#     if op=="+":
#         result=n1+n2
#     elif op=="-":
#         result=n1-n2
#     elif op=="*":
#         result=n1*n2
#     elif op=="/":
#         result=n1/n2
#     elif op=="%":
#         result=n1%n2
#     elif op=="**":
#         result=n1**n2
#     else:
#         False
#     print(result)

# import time
# for x in range(3,0,-1):
#     print(x)
#     time.sleep(1)
# print("time's up")

# for x in range (1,6):
#     for j in range(1,x+1):
#         print(j,end=" ")
#     print()

# cnt=0
# for x in range(1,6):
#     for j in range(1,x+1):
#         cnt+=1
#         print(cnt,end=" ")
#     print()

# cnt=0
# for x in range (5,0,-1):
#     for y in range(x,0,-1):
#         cnt+=1
#         print(cnt, end=" ")
#     print()


# fruits=["apple", "mangoes", "cherry", "pear", "orange"]
# print(dir(fruits))


# nums=[0,1,0,3,12]
# for i in range (len(nums)):
#     if nums[i]==0:
#         for j in range(i+1,len(nums)):
#             if nums[j]!=0:
#                 nums[i],nums[j]=nums[j],nums[i]
#                 break
# print(nums)

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# new=[]
# for i in range (len(list1)):
#     for j in range (len(list2)):
#         if list1[i]==list2[j]:
#             new.append(list1[i])
# print(new) 


# list=["flowers","flewings","flight"]
# print(max(list, key=len))


# num_pad=((1 ,2 ,3 ),
#          (4 ,5 ,6),
#          (7 ,8 ,9),
#          ("*",0,"#"))
# for row in num_pad:
#     for item in row:
#         print(item , end=" ")
#     print()


# food={"pizza":100,"burger":90,"cake":120,"soup":80}
# print(food.get("dog"))
