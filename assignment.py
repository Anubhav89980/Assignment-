#!/usr/bin/env python
# coding: utf-8

# In[4]:


" Use a for loop to iterate over an array. Use a for loop when you know the loop should execute n times. Use a while loop for reading a file into a variable. Use a while loop when asking for user input."


# In[1]:


l = [1,2,4,"anubhav",7,8,0]
for i in l :
    print(i)


# In[6]:


l1 = [1,2,3,4,5,6,7,8,9]
sum(l1)


# In[3]:


result = 0
for i in l1:
    result = result+ i
result


# In[25]:


bills = int(input("enter your bills as per unit"))
if bills <= 100 :
    print("user will pay 4.5 rs per unit")
elif bills > 100 and bills < 200 :
        print(" user will pay 6rs per unit ")
elif bills > 200 and bills < 300 :
        print ("user will pay 10 rs per unit")
else :
    print("user will pay 20rs per unit")


# In[47]:


p = list(range(1,100))
print(p)
l1 = []
for i in p :
    l1.append(i*i*i)
    print(l1)


# In[42]:


string=(" i want to become data scientist")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)


# In[45]:





# In[ ]:





# In[ ]:




