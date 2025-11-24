# Making a list by using constructor
lis1=list([2,4,6,8,10,12])
print(lis1)
print(type(lis1))
# Ways to Iterate over List
# 1)
for i in range (len(lis1)):  #Accessing Length of list using Len Function
    print(f"{i} >>  {lis1[i]}")
#  2)       
for i in lis1:
    print(i)