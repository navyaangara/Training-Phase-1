#!/usr/bin/env python
# coding: utf-8

# In[1]:


#single inheritance
class A:
    name="nivi"
    age=19
class B(A):
    age=10
obj=B()
print(obj.age)
print(obj.name)


# In[2]:


class A:
    name="nivi"
    age=19
class B(A):
    age=10
obj=B()
obj.name="navya"
print(obj.age)
print(obj.name)


# In[3]:


#multi level
class A:
    name="nivi"
    age=19
class B(A):
    age=10
class C(B):
    pass
class D(C):
    pass
obj=B()
print(obj.age)
print(obj.name)


# In[9]:


#multi level example 
class Vehicles:
    speed=120
    milage="60kmph"
class Bikes(Vehicles):
    speed=60
class Scooty(Bikes):
    name="activa"
    speed=80
class Electicscooty(Scooty):
    charge="2hrs"
    milage="40kmph"
obj=Scooty()
obj1=Electicscooty()
print(obj.speed)
print(obj.milage)
print(obj1.name)
print(obj1.milage)

    


# In[26]:


#hierarchial 
class Plants:
    name=""
    leaves="green"
class Floweringplants(Plants):
    color="red"
    def Need_water(self):
        print("yes")
class Thornybushes(Plants):
    def Need_water(self):
        print("no")
    def have_thorns(self):
        print("thorns")
obj=Floweringplants()
obj1=Thornybushes()
obj1.Need_water()
obj1.have_thorns()
print(obj.color)
print(obj.leaves)

        
        
    


# In[36]:


class P1:
    def m1(self):
        print("navya")
class P2:
    def m1(self):
        print("sri")
class C(P1,P2):
    pass
obj=C()
obj.m1()


# In[37]:


class P1:
    def m1(self):
        print("navya")
class P2:
    def m1(self):
        print("sri")
class C(P2,P1):
    pass
obj=C()
obj.m1()


# In[38]:


#multiple 2 parents and 1 child
class Mammals:
    def mammals_info(self):
        print("can give birth directly")
class Wingedmammals:
    def info(self):
        print("can flap")
class Bat(Mammals,Wingedmammals):
    def bat(self):
        print("can fly")
obj=Bat()
obj.info()
obj.mammals_info()
obj.bat()
    


# In[2]:


#hybrid combination of 2 inheritances
#common hybrid inheritance-hierarchial and multiple
class Restaurent:
    food_items=""
    bevarages="nb"
class veg(Restaurent):
    def veg_info(self):
        print("veg briyani")
class non_veg(Restaurent):
    staters="chicken"
class Customer(veg,non_veg):
    print("eat according to choice")
obj= Customer()
obj.veg_info()
print(obj.bevarages)
    


# In[4]:


from random import random,randint
a=randint(1,10)
id=random()*1000
print(id)


# In[7]:


from random import random,randint
a=randint(1,3)
print(a)


# In[7]:


from random import randint
choice=['rock','paper','scissor']
p_score=0
c_score=0
limit=3
while p_score!=limit and c_score!=limit:
    print(f"enter among the folloowing",choice)
    my_ch=input("Player choice:").lower()
    if my_ch not in choice:
        print("invalid input")
        continue
    sys_ch=choice[int(randint(0,2))]
    print(f"System choice: {sys_ch}")
    if my_ch==sys_ch:
        print("Draw")
        continue
    if my_ch=="rock" and sys_ch=="scissor":
        p_score+=1
    elif my_ch=="paper" and sys_ch=="rock":
        p_score+=1
    elif my_ch=="scissor" and sys_ch=="paper":  
        p_score+=1
    else:
        c_score+=1
    print(f"your score: {p_score},system score: {c_score}")
   
   
if p_score>c_score:
    print("you win the match")
else:
    print("system wins the match")


# In[2]:


#method overriding
class A:
    def method(self,a,b):
        print("sum of two numbers",a+b)
class B(A):
    def method(self,a,b):
        print("mul of two numbers",a*b)
obj=B()
obj.method(10,20)


# In[5]:


#method overloading
class A:
    def method(self,a,b):
        print("sum of two numbers",a+b)
class B(A):
    def method(self,a,b):
        print("mul of two numbers",a*b)
    def method(self,abc):
        print("value is",abc)
obj=B()
obj.method(10)


# In[4]:


a=int(input())
b=int(input())
a1=bin(a)[2:]
a2=bin(b)[2:]
ch=input()
if ch=='and':
    print(a1 and a2)
elif ch=='or':
    print(a1 or a2)
elif ch=='^':
    print(a1^a2)

else:
    print("invalid")


# In[1]:


a=int(input())
b=int(input())
print(a^b)


# In[5]:


def invert (string):
    res=""
    for i in string:
        if i=='0':
            res+=1
        else:
            res+=0
            a=int(input())
b=int(input())
a1=bin(a)[2:]
a2=bin(b)[2:]
ch=input()
print(a1,a2)

