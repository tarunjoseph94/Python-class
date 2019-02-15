#lst=[1,2,5,4]
#lst.reverse()
#print(lst)
#lst.insert(3,9)
#print(lst)

# x=[0]*5
# for i in range (0,5):
#     x[i]=[0]*5
# x[1][2]=10
# x[4][4]=99
# print(x)



# x=[0]*5
# x=[1]*5
# for i in range (0,5):
# 	for j in range(0,5):
# 		x[i][j]=[0][0]*5
# x[1][2]=10
# x[4][4]=99
# print(x)

# lst=[1,2,3]
# This casuses lst to become none
# lst=lst.append(4)
# # print(lst.append(4))
# print(lst)

# lst=[]
# for i in range(0,5):
# 	lst.append(i)
# print(lst)

# lst1=list()
# for i in range(0,5):
# 	lst1.append(i)
# lst2=list()
# for i in range(1,6):
# 	lst2.append(i)
# for i in zip(lst1,lst2):
# 	print(i)

# lst1=list()
# for i in range(0,5):
# 	lst1.append(i)
# lst2=lst1
# lst2[1]=10
# print(lst1)
# print(lst2)

lst1=list()
for i in range(0,5):
	lst1.append(i)
lst2=lst1[:]
lst2[1]=10
print(lst1)
print(lst2)