
cnt = 0
repeat_boolean = True
while repeat_boolean:
    print("%s while statement is running" % cnt)
    cnt = cnt+1
    if cnt == 30:
        repeat_boolean = False
        print("the end")
