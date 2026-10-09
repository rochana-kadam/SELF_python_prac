
# * create a hetrogenous list and split the list at the highest number

# list = ["Amit", 25, "Riya", 10, "Rahul", 50, "Priya", 30]
# highest=0
# for i in list:
#     if str(i).isdigit() and int(i)>highest:
#         highest=i

# index=list.index(highest)

# before=list[:index]
# after=list[index:]
# print(before)
# print(after)

# * print the pattern 
# *      *
# *     # #
# *    * * *
# *   # # # #


for i in range(5):
    print(" "*(4-i), end="")
    for j in range(i):
        if i%2==0:
            print("# ", end="")
        else:
            print("* ", end="")
    print()