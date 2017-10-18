
a = [34,560,101]
i = 0           
max = a[i]  
while i < len(a): 
    if a[i] > max: 
        max = i
        max = a[i]
    i = i + 1
print (max)