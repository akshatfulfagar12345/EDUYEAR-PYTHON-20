string=input("Enter any string:")
c=input("Enter character to check frequency:")
count=0
for i in string:
    if i==c:
        count+=1
print(c,"occurs",count,"time(s)",)