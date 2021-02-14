# like a map of JAVA
a_dict = {"key 1" : "value 1"
         ,"key 2" : "value 2"
         ,"key 3" : "value 3"}

print(type(a_dict))
print(a_dict)
print(a_dict['key 1'])

for key in a_dict:
    print('%s is key. %s is value.' % (key, a_dict[key]))

a_dict.update({"key 4" : "value 4", "key 5" : "value 5"})
print(a_dict)

for value in a_dict.keys():
    print("value : %s" % value)
    if value == "key 1":
        print("222222222222222222222")
    elif value == "key 2":
        print("33333333333333333333")
    else:
        print("44444444444444444444")


#like a map inner map of JAVA
b_dict = {"bkey 1" : 
            {"bkey 11" : "bvalue11"
            ,"bkey 12" : "bvalue122"
            }
         }

print(b_dict)
print(b_dict['bkey 1']['bkey 12'])


