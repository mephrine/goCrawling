
# like a javascript array
# tuple is not able to add or update
a_tuple = {"kiumn","daesin", "kakao"}
print(a_tuple)

a_len = len(a_tuple)
print(a_len)

a_type = type(a_tuple)
print(a_type)

for value in a_tuple:
    print(value)

for index, value in enumerate(a_tuple):
    print("%s is index, %s is value" % (index, value))

