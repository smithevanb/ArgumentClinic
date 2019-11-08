#A program that counts up to a certain number, and
#only prints out the primes between 1 and that number. 

list=[]
for x in range(2,10000):
    if x <= 2:
        list.append(x)    
    for n in list:
        if any(x % n == 0 for n in list):      
            continue
        elif x % n > 0:
            list.append(x)
            break
            
print(list)