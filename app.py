#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime

import streamlit as st

from streamlit_jupyter import StreamlitPatcher, tqdm


# In[2]:


sp = StreamlitPatcher()
sp.jupyter()  # register patcher with streamlit


# In[3]:


st.title("Example")


# In[4]:


st.markdown(
    """

This is a test page demonstrating the use of `streamlit_jupyter`.

If you're seeing this in jupyter, then it's working!

"""
)


# In[5]:


sp.registered_methods


# In[6]:


name = st.text_input("What's your name?", "John")


# In[7]:


date = st.date_input("Choose a date", datetime.now().date())


# In[8]:


st.markdown(f"## Hello {name}!\n## The date is {date.strftime('%Y-%m-%d')}")


# In[ ]:





# In[9]:


import time

import pandas as pd


@st.cache(suppress_st_warning=True)
def get_data(date):
    for i in tqdm(range(10)):
        time.sleep(0.1)
    return pd.DataFrame(
        {"date": pd.date_range(date, periods=3), "c": [7, 8, 5], "d": [10, 11, 3]}
    ).set_index("date")


df = get_data(date)
st.write(df)


# In[ ]:





# In[ ]:





# In[10]:


# | exporti

st.metric("Speed", 300, 210, delta_color="normal", label_visibility="visible")


# In[11]:


# | exporti

st.metric("Speed", 300, 210)


# In[12]:


st.code("print(1+1)", language="python")


# In[13]:


show_code = st.checkbox("Show code", value=True)


# In[14]:


if show_code:
    st.code("[i**2 for i in range(100)]")


# In[15]:


option = st.radio("Choose one option", options=["foo", "bar"], index=1)


# In[16]:


option = st.selectbox("Selectbox: ", options=["Jane", "Bob", "Alice"], index=0)


# In[17]:


options = st.multiselect("Multiselect: ", options=["python", "golang", "julia", "rust"])


# In[18]:


options = st.multiselect(
    "Multiselect with defaults: ",
    options=["nbdev", "streamlit", "jupyter", "fastcore"],
    default=["jupyter", "streamlit"],
)


# In[19]:


# | exporti
st.subheader("st.text:")
st.text("This is a text")
st.text("This is \n multiline text")
st.code("This is multiline \n code", language=None)


# In[20]:




# In[ ]:




