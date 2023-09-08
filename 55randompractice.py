'''
values=[[3,4,5,1],[33,6,1,2]]
v = values[0][0]
for Ist in values:
    for element in Ist:
        if v>element:
            v=element

print(v)

'''

# importing copy module
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]
print("li1 ID: ", id(li1), "Value: ", li1)

# using copy for shallow copy
li2 = copy.copy(li1)
print("li2 ID: ", id(li2), "Value: ", li2)
# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)
