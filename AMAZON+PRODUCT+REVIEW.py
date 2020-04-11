
# coding: utf-8

# In[1]:


import bokeh
import bs4
import bs4
import requests


# In[3]:


rs=requests.get("https://www.amazon.in/Spotzero-Milton-Bigger-Cleaning-Refills/product-reviews/B01MA1JLOM/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&pageNumber=3&reviewerType=all_reviews")
rs


# In[4]:


c=rs.content
c


# In[5]:


from bs4 import BeautifulSoup


# In[6]:


soup=BeautifulSoup(c,"html.parser")


# In[9]:


soup


# In[11]:


data=soup.find_all("a");data


# In[23]:


da=soup.find_all("a",{'class':'a-size-base a-link-normal author'})
da


# In[29]:


dd=soup.find_all("a",{'class':'a-size-base a-link-normal author'})[0].text
dd


# In[62]:


import numpy as np
import pandas as pd


# In[63]:


g=[]
for i in da:
    g.append(i.find_all("a")[0].text)
df2=pd.DataFrame(g,columns=['NAME'])    
df2  


# In[64]:


dff=pd.DataFrame(columns=['NAME'])


i=0.
for k in da:
    dff.loc[i]=[k.find_all("a")[0].text]
    i+=1
dff


# In[78]:


h=[]
for i in range(10):
    dd=soup.find_all("a",{'class':'a-size-base a-link-normal author'})[i].text
    print(dd)
    h.append(dd)


# In[79]:


h


# In[81]:


c


# In[84]:


dp=soup.find_all("span",{'class':'a-size-base a-color-secondary review-date'})[0].text
dp


# In[86]:


g=[]
for i in range(10):
    dp=soup.find_all("span",{'class':'a-size-base a-color-secondary review-date'})[i].text
    print(dp)
    g.append(dp)


# In[90]:


dp=soup.find_all("span",{ 'class':'a-icon-alt'})[0].text
dp


# In[91]:


for i in range(10):
    dp=soup.find_all("span",{ 'class':'a-icon-alt'})[i].text
    print(dp)


# In[92]:


for i in range(10):
    dp=soup.find_all("span",{ 'class':'a-size-mini a-color-state a-text-bold'})[i].text
    print(dp)


# In[99]:


for i in range(10):
    dp=soup.find_all("a",{ 'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'})[i].text
    print(dp)


# In[103]:


for i in range(10):
    dp=soup.find_all("span",{ 'class':'a-size-base review-text'})[i].text
    print(dp)
    print( )
    print("_________________*****************************************************************************____________________")

