#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
data_tanaya = pd.read_clipboard()
# Menampilkan data
print(data_tanaya)


# In[6]:


tanaya = data_tanaya[data_tanaya["Tinggi Badan"] > 160]

# Menampilkan nama
print(tanaya)


# In[7]:


data_tanaya['Tinggi Badan'] = pd.to_numeric(data_tanaya['Tinggi Badan'])

import numpy as np

data_tanaya['Tinggi Badan'] = data_tanaya['Tinggi Badan'].apply(lambda x: 'Tinggi' if x > 160 else 'Pendek')

# Menampilkan DataFrame setelah modifikasi
print(data_tanaya)


# In[10]:


data_tanaya["Jurusan"] = "Infor23"
data_tanaya["Fakultas"] = "FTI"

print(data_tanaya)


# In[11]:


data_tanaya = data_tanaya.drop(columns = ["Fakultas"])
print(data_tanaya)


# In[14]:


NamaGender = data_tanaya.iloc[:, [0,1]]
print(NamaGender)


# In[15]:


AngkatanTinggi = data_tanaya.iloc[:, [2,3]]
print(AngkatanTinggi)


# In[16]:


Gabung = pd.concat([NamaGender, AngkatanTinggi], axis = 1)
print(Gabung)


# In[21]:


bar15 = data_tanaya.iloc[0:5, :]
bar2530 = data_tanaya.iloc[5:30, :]
baris = bar15.append(bar2530)
print(baris)


# In[24]:


data_tanaya_sort = data_tanaya.sort_values(by = "Tinggi Badan")

print(data_tanaya_sort)


# In[ ]:




