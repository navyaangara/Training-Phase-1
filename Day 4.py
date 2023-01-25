#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Packages


# In[ ]:


def add_two_num(a,b):
    return(a+b)
def add_n_nums(*arr):
    return  sum(arr)


# In[ ]:


#to import from other files
from myfile import add_two_nums
a=36
b=33
print(add_two_nums(a,b))
   OR
import myfile
a=22
b=3
print(myfile.add_two_nums(a,b))
    


# # OOPS

# In[ ]:


#class=blueprint (declare variables in class)
#to access first define object
#self-keyword (to link method to class)
#if method-keep self


# In[3]:


"""class Student:
    name="nivi"
    roll_num="3"
    branch="aiml"
    marks=0
    attendance=0.0
    is_using_transport=False  #boolean
    def view_marks(self):
        pass
    def view_attendance(self):
        pass
    def view_name(self):
        pass
    def update_name(self,new_name):
        pass"""
    


# In[ ]:


# default constructor
class Student:
    def __init__(self):
        pass


# In[5]:


# argumented constructor
class Student:
    student_name=""
    def __init__(self,name):
        print("object created")
        print(name)
s1=Student("mukesh")


# In[7]:


# argumented constructor
class Student:
    student_name=""
    def __init__(self,name):
        print("object created")
        print(name)
        print(student_name)
s1=Student("mukesh")


# In[11]:


# argumented constructor
class Student:
    student_name="nivi"
    def __init__(self,name):
        print("object created")
        print(name)
        print(self.student_name)
s1=Student("mukesh")


# In[18]:


class Student:
    student_name="nivi"
    def __init__(self,name):
        self.student_name=name
s1=Student("navya")
s2=Student("sri")
s3=Student("alekhya")
print(s2.student_name)
    
    


# In[19]:


class Student:
    student_name="nivi"
    def __init__(self,name):
        self.student_name=name
    def update_name(self,new_name):
        self.student_name=new_name
s1=Student("navya")
s2=Student("sri")
s3=Student("alekhya")
print(s2.student_name)  #before update
s2.update_name("navya good girl")
print(s2.student_name)  #after update

