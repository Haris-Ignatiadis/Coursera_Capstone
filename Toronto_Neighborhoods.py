#!/usr/bin/env python
# coding: utf-8

# # Explore and cluster the neighborhoods in Toronto

# In[19]:


#Import and prepare dataset
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
data = pd.read_html(url, header=0)
df = data[0]
df.head()


# In[20]:


#Removing not_assigned boroughs
df = df[(df.Borough != 'Not assigned')]
df.head()


# In[22]:


#Combine the neighborhoods with identical postcode
df['Neighborhood'] = df.groupby(['Postal code','Borough'])['Neighborhood'].transform(lambda x: ','.join(x))
df.drop_duplicates()
df.reset_index(drop = True, inplace=True)
df.head()


# In[33]:


#Rename not_assigned neighborhoods
df.Neighborhood[df['Neighborhood'] == 'Not assigned'] = df.Borough[df['Neighborhood']=='Not assigned']
df.rename(index=str, columns={"Postcode": "PostalCode", "Neighbourhood":"Neighborhood"}, inplace = True)
print(df.shape)
df.head()


# In[ ]:




