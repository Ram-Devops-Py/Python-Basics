#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Print String value
a = 'Ram Paritala'
print(a)


# In[24]:


#Print String in double quotes
b = " This is a string with double quotes "
print(b)
print(b.strip())


# In[26]:


#Print String in Triple quotes
c = '''Python modules are files that have a .py extension and are capable of implementing a set of \nvariables, functions, and classes.'''
print(c)


# In[42]:


#Print the required info from given string using indexing
Iam = "Indian"
print(Iam[0:5])
print(Iam[0:5]+'is my country.')


# In[44]:


#Data manipulation with methods() 
#Title()
name = 'ram'
print(name)
print(name.title())


# In[66]:


#Upper()
A = 'python is'
B = ' more powerful language '
print(A.upper() + B.upper())


# In[71]:


#Lower()
name = "RAM"
surname = " PARITALA "
print(name.lower() + surname.lower())


# In[69]:


#Place holders using f strings. 
fname = 'Ram'
lname = 'Paritala'
full_name = f"{fname}{lname}"
print(full_name)


# In[72]:


#Adding white spaces to string with tabs/new lines
print("Designations: \nAssosiate\nSoftware\nSeniorSoftware\nBA\nLead\nSME\nManager\nDelivery Manager")


# In[ ]:




