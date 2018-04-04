
# coding: utf-8

# In[48]:


import pandas as pd
import numpy as np


# In[49]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                  'Budapest_PaRis', 'Brussels_londOn'],
                  'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                  'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                  'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                  '12. Air France', '"Swiss Air"']})


# In[50]:


# 1.Some values in the the FlightNumber column are missing.
#These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place.
#Fill in these missing numbers and make the column an integer column.


# In[51]:


df['FlightNumber'].loc[1] = (df['FlightNumber'].iloc[0] + 10)
df['FlightNumber'].loc[3] = (df['FlightNumber'].iloc[2] + 10)
df['FlightNumber'] = df['FlightNumber'].astype(int)


# In[52]:


print(df['FlightNumber'])


# In[53]:


#2.The From_To column would be better as two separate columns.
#Split each string on the underscore delimiter _ to give a new temporary DataFrame with the correct values.
#Assign the correct column names to this temporary DataFrame.


# In[54]:


tDF = pd.DataFrame(df.From_To)
tDF['From'] = tDF['From_To'].str.split('_').str.get(0)
tDF['To'] = tDF['From_To'].str.split('_').str.get(1)
tDF = tDF.drop('From_To', 1)


# In[55]:


#3.Standardise the strings in the temporary DataFrame, so that only the first letter is uppercase. 


# In[56]:


tDF['From'] = tDF.From.str.title()
tDF['To'] = tDF.To.str.title()


# In[57]:


print(tDF['From'])


# In[58]:


print(tDF['To'])


# In[59]:


#4.Delete the From_To column from df, and attach the temporary DataFrame from the previous questions.


# In[60]:


df = df.drop('From_To', 1)
df = pd.concat([tDF,df], axis = 1)


# In[61]:


# 5.Expand the series of delays into a DataFrame named "delays". 
#Each delay value should be in its own column. Missing values should be NaN. 
#Rename the columns: delay_1, delay_2, etc. Replace RecentDelays with this DataFrame. 


# In[62]:


tDelay = pd.DataFrame(df.RecentDelays)
tDelay = pd.DataFrame(df['RecentDelays'].values.tolist())
tDelay.columns = ['Delay_1', 'Delay_2', 'Delay_3']
df = df.drop('RecentDelays', 1)
df.insert(3, "Delay_1", tDelay['Delay_1'])
df.insert(4, "Delay_2", tDelay['Delay_2'])
df.insert(5, "Delay_3", tDelay['Delay_3'])



# In[63]:


print(df)

