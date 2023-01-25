#!/usr/bin/env python
# coding: utf-8

# In[5]:


l=[]
d={}
for i in range(3):
    d.update({
            'key1':input("enter value1 "),
            'key2':input("enter 2 ")
    })
    l.append(d)
print(l)


# In[6]:


l=[]
for i in range(3):
    d={
    'key1':input("enter value1:"),
    'key2':input("enter value2:")
    }
    l.append(d) 
    
print(l)


# In[4]:


db=[
    {'navya':'111'},
    {'sri':'222'},
    {'alekhya':'333'}
]
print(db)
username=input("username:")
password=input("passwprd:")
temp={username:password}
if temp in db:
    print(found)
else:
    print("not")


# In[3]:



l=[]
for i in range(2):
    d={
      input('usernames:'):input("passwords")
    }
    l.append(d)
    
print(l)
username=input("username:")
password=input("passwprd:")
temp={username:password}
if temp in l:
    print(found)
else:
    print("not")


# In[4]:


r=2
c=2
arr=[]
for i in range(r):
    ele=[]
    for j in range(c):
        ele.append((int(input("enter elements"))))
    arr.append(ele)
print(arr)


# In[19]:


n=int(input())
i=0
j=1
print(i)
print(j)
for k in range(0,n):
    sum=i+j
    print(sum)
    i,j=j,sum
        
        
        


# In[9]:


s='nivi sri'
s1='NAVYA'
print(s)
print(s.capitalize())
res=s.split(' ')
print(res)
print('-'.join(res))
print(s.title())
print(s1.lower())
print(s.upper())


# In[15]:


s1='hello world'
s2='ALEKHYA'
print(s1.count('l'))


# In[25]:


s1='HEllo worLD'
s2='nivi'
print(s1.swapcase())
print(s1.isalpha()) #false bcoz of space
print(s2.isalpha())


# In[31]:


name='alrkhya'
age=19
print(name+" age is "+str(age))


# In[26]:


num=6
print("square of {} is {}".format(num,num*num))


# In[42]:


num=6.88
print("square of {} is {}".format(num,num*num))


# In[33]:


num=6.88
print("square of {} is {:.2f}".format(num,num*num))


# In[36]:


num=62.88
print("square of {:10} is {:.2f}".format(num,num*num))


# In[40]:


num=6.88
print(f"square of {num} is {num*num}")


# In[41]:


num=6.88
print(f"square of {num} is {num*num:.6f}")


# In[45]:


#if denominator is 0
a=int(input())
b=int(input())
try:
    print(a/b)
except:
    print("b cannot be 0")
    print("after the error")


# In[1]:


a=int(input())
b=int(input())
op=input("enter op:")
try:
    if(op=='+'):
        print(a+b)
    elif(op=='-'):
        print(a-b)
    elif(op=='*'):
        print(a*b)
    elif(op=='/'):
        if(b!=0):
            print(a/b)
        else:
            print("cnnot b e0")
    else:
        print("invalid")
except:
    print("b cannot be 0")


# In[3]:


n=int(input())
for i in range(1,n+1):
    print(i)


# In[2]:


try:
    a=list(map(int,input().split()))
    print(a)
except:
    print("not an integer")


# In[1]:


print(eval("1+3/5+9"))


# # functions

# In[4]:


#regular function
#default value function
#key argument function
#variable length function


# In[5]:


#regular
def addition(n1,n2):
    sum=n1+n2
    return sum
print(addition (2,5))


# In[31]:


def prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==2:
        print("not")
    else:
        print("prime")
         
        
print(prime(2))


# In[ ]:


#m-1
for i in range(1,n+1):
    ststements
#m-2
for i in range(2,n):
    statements
#m-3
for i in range(2,n//2):  #half of number
    statements
#m-4
for i in range(2,int(n**0.5)+1):  #square root method
    statemnts

