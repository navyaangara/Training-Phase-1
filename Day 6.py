#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install translate


# In[5]:


from translate import Translator


# In[6]:


obj=Translator(from_lang="english",to_lang="hindi")
new_name=obj.translate("navya")
print(new_name)


# In[7]:


obj=Translator(from_lang="english",to_lang="tamil")
new_name=obj.translate("navya")
print(new_name)


# In[13]:


obj=Translator(from_lang="english",to_lang="marati")
new_name=obj.translate("navya")
print(new_name)


# In[20]:


#method overriding
class Animal():
    def speak(self):
        print("every animal speaks")
class Dog(Animal):
    def speak(self):
        print("bark")
class Cat(Animal):
    def speak(self):
        print("meow")
class Cow(Animal):
    def speak(self):
        print("vinni says ambaa")
obj=Vineela()
obj.speak()
        
        


# In[21]:


#Abstraction
#for Abstraction we have a package called abc
#import a package called  abc - called abstract base class
# ABC - class in abc
#they dont have method body , have only definition


# In[22]:


#Annotations-start with @
#@override   @overload   @request   @abstarctmethod


# In[28]:


from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Square(Area):
    def calculate_area(self):
        print("square")
class Rectangle(Area):
    pass
obj=Square()
obj.calculate_area()
    


# In[32]:


from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def calculate_speed(self):
        pass
class Bike(Vehicle):
    def calculate_speed(self):
        print("speed is 60kmph")
obj=Bike()
obj.calculate_speed()


# In[1]:


#left shift
print(7<<3) #multiply 7 - 3 times with 2


# In[2]:


#right shift
print(8>>3) #divide 8 - 3 times with 2 

