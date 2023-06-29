cost = [100,20,10,5,1]
count = 0 
a = 125
while(a!=25):
    print(a)
    for i in cost:
        print(i)
        if(a>=i):
            a = a-i
            count += 1
            print(count)
            break
print(count)