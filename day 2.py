#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sets


# In[2]:


s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))


# In[3]:


#conditional statements
#if else


# In[5]:


#even - odd
a=int(input("enter number:"))
if(a%2==0):
    print("even")
else:
    print("odd")


# In[6]:


#prime
n=int(input())
if(n==1):
    print("neither prime nor composite")
elif(n==2):
    print("prime")
elif(n>2):
    for i in range(2,n):
        if(n%i==0):
            print("not prime")
            break
        else:
            print("prime")
            break
else:
    print("prime")
        
        


# In[7]:


##### week days
n=int(input())
if(n==1):
    print("monday")
elif(n==2):
    print("tuesday")
elif(n==3):
    print("wednesday")
elif(n==4):
    print("thursday")
elif(n==5):
    print("friday")
elif(n==6):
    print("saturday")
elif(n==7):
    print("sunday")
else:
    print("invalid range")


# In[8]:


#num greater than 0 and less than 20 if even-weird else normal
#num >=20 and less than 30normal
#num>30and  if odd normal else weird
n=int(input())
if(n>0 and n<20):
    if("n%2==0"):
        print("weird")
    else:
        print("normal")
elif(n>=20 and n<30):
    print("normal")
elif(n>=30 and n%2!=0):
    print("normal")
else:
    print("wierd")
    



# In[9]:


#dictionary
sd={}
sd.update({'201':'navya'})
sd.update({'202':'vineela'})
sd.update({'203':'bhuna'})
print(sd)
print(sd.get('201'))


# In[10]:


l=[2,3,4]
for i in l:
    print(i**2)


# In[11]:


#finding index of key
lst=[2,3,4,5,6]
k=int(input())
for i in range(0,(len(lst))):
    if(lst[i]==k):
        print(i)
        break
else:
    print("not found")
    


# In[12]:


#adding ele to empty list
l=[]
for i in range(0,10):
    l.append(i)
print(l)


# In[13]:


#adding ele to empty list in single line
list=[x for x in range(0,10)]
print(list)


# In[14]:


#printing even numbers
list=[x for x in range(0,51) if x%2==0]
print(list)


# In[15]:


list=[x for x in range(1,101) if x%7==0 and x%11==0]
print(list)


# In[16]:


list=[x for x in range(1,101) if x%7==0 or x%11==0]
print(list)


# In[17]:


lst=[1,2,3,4,5,6]
print(len(lst))
for i in range(len(lst)-1,0,-1):
    print(l[i])


# In[18]:


lst=[1,2,3,4,5]
print(lst[::-1])


# In[19]:


l=[1,-2,5,-7,-91,5,-4]
sum=0
sum1=0
for i in range(0,7):
    if(l[i]>0):
        k=l[i]
        sum=sum+k
    elif(l[i]<0):
        k1=l[i]
        sum1=sum1+k1
print(sum)
print(sum1)

    
        
   
        
        
    

