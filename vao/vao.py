
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
# nums=[4,4,5,5,6,7]
# freq={}
# for no in nums:
#     if no in freq:
#         freq[no]+=1
#     else:
#         freq[no]=1

# highest=max(freq, key=freq.get)
# print(highest)


# * second highest occuring element

# nums=[1,1,2,3,3,3]
# freq={}
# for i in nums:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1

# unique_freq=sorted(set(freq.values()),reverse=True)
# second_highest=unique_freq[1]

# for key, value in freq.items():
#     if value==second_highest:
#         print(key)

# * sum of highest and lowest frequencies

nums=[1,1,2,3,3,3]
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

highest=max(freq.values())
lowest=min(freq.values())
print(highest+lowest)