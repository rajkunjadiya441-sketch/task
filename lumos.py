print("enter a string")
a=input()
count=0
s=set()
for c in a:
    count=count+1
    if(c=="l"or c=="o"or c=="u"or c=="m"or c=="s"):
     s.update(c)
     if(len(s)==5):
        print(count)
        break
if(len(s) !=5):
   print(-1)
