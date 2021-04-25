maximum= int(input('Please enter maximum:'))
minimum= int=1
print("palindrome numbers between %d to %d are:"%(minimum,maximum))
for num in range(1,maximum+1):
    temp=num
    reverse=0
    while(temp>0):
        reminder=temp%10
        reverse=(reverse*10)+reminder
        temp=temp//10
        if(num==reverse):
           print("%d",%num,end = ' ')



    