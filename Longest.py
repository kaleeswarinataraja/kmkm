a=int(input())
b=[]
for i in range(0,a):  
    c=input()
    b.append(c)
list=[]
for i in zip(*b):
    if i.count(i[0])==len(i): 
        list.append(i[0])
    else:
        break
print(''.join(list))
