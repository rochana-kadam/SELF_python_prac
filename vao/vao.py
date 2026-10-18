
# * highest occurring element in an array

# nums=[4,4,5,5,6,7]
# freq={}
# for no in nums:
#     if no in freq:
#         freq[no]+=1
#     else:
#         freq[no]=1
# max_cnt=0
# highest=None
# for no in freq:
#     if freq[no]>max_cnt:
#         max_cnt=freq[no]
#         highest=no
# print(highest) 

# ? another way to solve
nums=[4,4,5,5,6,7]
freq={}
for no in nums:
    if no in freq:
        freq[no]+=1
    else:
        freq[no]=1

highest=max(freq, key=freq.get)
print(highest)
