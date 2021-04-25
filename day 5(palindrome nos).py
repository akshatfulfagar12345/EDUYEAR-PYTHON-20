i= int(input('Enter no:'))
rev = 0
x = i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print('palindrome no')
else:
    print('not palindrome')


    