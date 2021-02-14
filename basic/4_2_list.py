a_list = ["list1", "list2", "list3"]

print(a_list)

for index,value in enumerate(a_list):
    print("%s, %s" %(index,value))


a_list = ["a_list1", "a_list2", "a_list3"]
b_list = ["b_list1", "b_list2"]

a_list.append(b_list)

print(a_list)