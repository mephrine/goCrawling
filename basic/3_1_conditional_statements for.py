count = 0
for i in range(0, 10):
    count = count + 1

print(count)

for i, value in enumerate(['kium', 'samsung', 'kakao']):
    print("%s is numeric, %s is value" % (i,value))