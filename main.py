#1
import random
l=[random.randint(0, 10) for i in range(10)]
print(l)
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(s)
print("\n")




#2
k=[random.randint(-5, 5) for i in range(10)]
print(k)
j=[]
j=k
print(j)
print("\n")




#3
o=[random.randint(1, 10) for i in range(5)]
g=[random.randint(1, 10) for i in range(5)]
print(o)
print(g)
f=[]
k=list(set(o)-set(g))
h=list(set(g)-set(o))
f=k+h
print(f)
print("\n")




#4
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
#{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic4={}
for i in (dic1, dic2, dic3):
    dic4.update(i)
print(dic4)
print("\n")




#5
d=dict()
for i in range(1, 16):
   d[i]=i**2
print(d)






