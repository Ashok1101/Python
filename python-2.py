'''python'''
"""complete"""
#print
print("hello world")
print("hello world");  print('hello world','n',"j");
name="arvind"
print(type(name))
age=21
print(name),print(age)
print(name + str(age))
age1=input("enter ur age:\t")
print(int(age1) + age)       #type conversion
print(name.upper())
print(name)
name=name.upper()
print(name.lower())
print(name)
print(name.find('d'))
print(name.find('s'))
v=name + str(age)
print(v.find("nd21"))
print(name.replace("arvind","arvind patel"))
print(name)
print(v.replace("21"," patel"))
print('v' in name)
print("21" in name)
print(9+8)
print(9-8)
print(8*10)
print(9/2)
print(9//2)
print(9%2)
print(5**2)
print(9>=3)
print(1==0)
print(9!=2)
print(3>5 and 5<9)
print(3>5 or 5<9)
print(~ 5<9)
if int(age1) >= 18:
    print("u are adult")
    print ("u can vote")
elif int(age1) < 18:
    print("u are not adult")
else: 
    print ("u doesn't exist")
print ("Thk u")    

no = range(5) 
print(no)
i=1
while i<=5:
    print(i* '*')
    i+=1
for i in range(5):
        print(i+1)
l=[2,0,9, 90,"arvind","patel"]
print(l)
print(l[0])
print(l[-2])
print(l[0:3:2])
l.append(99)
print(l[::])
l.insert(2,5)
print(l)
print(len(l))
# l.clear()
print(l)
for m in l:
    if(m==90):
        break
    print(m)
i=0
while i<len(l):
    if l[i]==90:
        i=i+1
        continue
    print(l[i])
    i+=1
for m in l:
    if m==90:
        continue
    print(m)
l=(2,0,9, 90,90,90,"arvind","patel") 
l=2,0,9, 90,90,90,"arvind","patel"
print(l)
print(l.count(90))
print(l.index(9))
print(l.index(90))
l={2,0,9, 90,90,90,"arvind","patel"}    
print(l)
l={"m":1,"n":2,"k":3}
print(l["n"])
l["j"]=5
print(l)
l["j"]=4
print(l)
def sum(f,s):
    print(f+s)
sum(9,8)