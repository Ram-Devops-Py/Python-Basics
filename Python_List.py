#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Print the list
Countries = ['India','United Kingdom','United States','Australia','New Zealand']
print(Countries)


# In[5]:


# Replace the US with UAE using index value
Countries[2] = 'UAE'
print(Countries)


# In[12]:


#Add SA to the existing list
Countries.append('South Africa')
print(Countries)


# In[31]:


Length_of_list = len(Countries)
print(Length_of_list)


# In[30]:


#Print selected values using index range
print(Countries[0:5])
print(Countries[5:10])


# In[37]:


#Remove a value from list using remove() function
Countries.remove("South Africa")
print(Countries)


# In[40]:


#Remove a value from list using pop() function
poped_Countries = Countries.pop()
print(Countries)


# In[ ]:




