a = [10,20,30,20,10,50,60,40,80,50,40]
reduced_a=[]
[reduced_a.append(x) for x in a if x not in reduced_a]
print(reduced_a)