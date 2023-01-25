#!/usr/bin/env python
# coding: utf-8

# In[1]:


#list

l=[]
l.append("navya")
l.append(19)
l.append(2003.04)
l.append(1)
l.append(15)
l.append(199)
print(l)


# In[9]:
print(len(l))
# In[10]:

l.pop(0)#index value


# In[11]:


print(l)


# In[12]:


l.remove(19)#ele value


# In[13]:


print(l)


# In[14]:


l.pop()#removes last ele
print(l)


# In[15]:


l.remove()


# In[16]:


print(l.pop(2))#shows ele thai is removed
print(l)


# In[17]:


print(l.remove(1))
print(l)


# In[18]:


print(l.insert(0,12))
print(l)


# In[19]:


l.insert(1,16)#inserting ele at specific index
print(l)


# In[23]:


a=[10,20,30,40]
b=[5,15,25,35]
a.extend(b)#adds ele from b to a
print(a)
print(b)


# In[25]:


a1=[10,10,10,20,20,30,30,50,40]
print(a1.count(10))


# In[26]:


print(a1.count(60))


# In[27]:


c=a.copy()
print(c)


# In[28]:


b.clear()
print(b)


# In[30]:


c.reverse()
print(c)


# In[33]:


d=a.sort()
print(d)# default ascending order ,sort existing list
print(a)


# In[31]:


a.sort(reverse=True)#descending order
print(a)


# In[37]:


a2=[6,8,4]
e=sorted(a2)
print(e)
print(a2)


# In[38]:


a2=[6,8,4]
e=sorted(a2,reverse=True)
print(e)
print(a2)


# In[6]:


#string to list
l='12345'
l=list('12345')
print(l) #['1', '2', '3', '4', '5']
l=map(int,l)
print(l) #<map object at 0x000002013C269400>
l=list(map(int,l))
print(l) #[1, 2, 3, 4, 5]


# In[ ]:




