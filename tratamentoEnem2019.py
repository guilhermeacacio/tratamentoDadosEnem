#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


dados = pd.read_csv('microdados_enem_2019_sp.csv', sep=';', encoding='iso-8859-1')
dados.head(3)


# In[3]:


dados1 = dados.drop(columns=['CO_MUNICIPIO_RESIDENCIA'])


# In[4]:


dados1.head(3)


# In[5]:


dados1 = dados1.drop(columns=['CO_UF_RESIDENCIA', 'SG_UF_RESIDENCIA', 'CO_MUNICIPIO_NASCIMENTO'],)


# In[6]:


dados1.head(3)


# In[7]:


dados1.shape


# In[8]:


dados1 = dados1.drop(columns=['NO_MUNICIPIO_NASCIMENTO', 'CO_UF_NASCIMENTO', 'SG_UF_NASCIMENTO',
                              'TP_ANO_CONCLUIU', 'TP_ENSINO', 'CO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC'], )
dados1.head(3)


# In[9]:


dados1.loc[:,'NU_NOTA_CN'] /= 10
dados1.loc[:,'NU_NOTA_CH'] /= 10
dados1.loc[:,'NU_NOTA_LC'] /= 10
dados1.loc[:,'NU_NOTA_MT'] /= 10

dados1.head(3)


# In[10]:


dados1 = dados1.rename(columns={'NU_NOTA_CN': 'NOTA_CN' ,
                                'NU_NOTA_CH': 'NOTA_CH',
                                'NU_NOTA_LC': 'NOTA_LC',
                                'NU_NOTA_MT': 'NOTA_MT'})
dados1.head(3)


# In[11]:


dados1 = dados1.rename(columns={'NU_NOTA_COMP1': 'NOTA_COMP1' ,
                                'NU_NOTA_COMP2': 'NOTA_COMP2',
                                'NU_NOTA_COMP3': 'NOTA_COMP3',
                                'NU_NOTA_COMP4': 'NOTA_COMP4'})
dados1.head(3)


# In[12]:


dados1 = dados1.rename(columns={'NU_IDADE': 'IDADE' ,
                                'TP_SEXO': 'SEXO',
                                'TP_COR_RACA': 'RACA',
                                'Q025': 'INTERNET',
                                'TP_ESCOLA': 'ESCOLA'})
dados1.head(3)


# In[18]:


dados1['RACA'] = dados1['RACA'].replace({0: 'Não Declarado',
                                 1: 'Branca',
                                 2: 'Preta',
                                 3: 'Parda',
                                 4: 'Amarela',
                                 5: 'Indigena'})


# In[20]:


dados1.head(10)


# In[23]:


dados1['TP_LINGUA'] = dados1['TP_LINGUA'].replace([0, 1], ['Ingles', 'Espanhol'])

dados1.head(10)


# In[31]:


dados1['IDADE'].value_counts(sort=False)


# In[35]:


menores_12 = dados1.query('IDADE <= 12')['NO_MUNICIPIO_RESIDENCIA'].value_counts()
menores_12


# In[40]:


dados_maiores_11 = dados1.loc[dados1.IDADE > 11]
dados_maiores_11['IDADE'].value_counts(sort=False)


# In[41]:


dados_maiores_11.query('IN_TREINEIRO == 1')['IN_TREINEIRO'].value_counts()


# In[42]:


treineiros = dados_maiores_11.loc[dados_maiores_11.IN_TREINEIRO == 1]


# In[44]:


treineiros.head(10)


# In[45]:


treineiros.to_csv('treineiros_enem_2019_sp.csv', encoding='iso-8859-1', index=False)


# In[48]:


vestibulandos = dados_maiores_11.loc[dados_maiores_11.IN_TREINEIRO == 0]


# In[50]:


vestibulandos.head(20)


# In[51]:


vestibulandos['TP_PRESENCA_CN'].value_counts() 


# In[52]:


vestibulandos['TP_PRESENCA_CH'].value_counts() 


# In[53]:


vestibulandos['TP_PRESENCA_MT'].value_counts() 


# In[54]:


vestibulandos['TP_PRESENCA_LC'].value_counts() 


# In[57]:


vestibulandos.describe()


# In[62]:


provas = ['NU_NOTA_REDACAO', 'NOTA_CN', 'NOTA_CH', 'NOTA_LC', 'NOTA_MT']


# In[63]:


vestibulandos[provas].isnull().sum()


# In[ ]:




