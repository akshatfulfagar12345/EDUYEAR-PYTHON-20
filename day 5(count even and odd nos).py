num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
odd = 0
even = 0
for i in num:
    if not i%2:
        even+=1
    else:
        odd+=1
print('total even num is',even)
print('total odd num is',odd)
    