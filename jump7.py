num=0
a = 0
for num in range(101):
    if num%7==0:
        continue
    elif num%10==7:
        continue  
    elif num//10==7:
        continue
    print(num)

                    
