import sys
valid_file = sys.argv[1]
df_train_file = sys.argv[2]
owl_file= sys.argv[3]
                            
save_file_name=sys.argv[4]
hyperparam_margin_loss=sys.argv[5]
hyperparam_dim=sys.argv[6]


valid_file=valid_file

import pandas as pd

df_train=pd.read_csv(df_train_file,sep='\t',header=None)
                               
df_train.columns=['entity1','relation','entity2','confidence']
                

df_train_or=df_train.copy()

list_entity_1=[]

for i in range(len(df_train)):
  term=df_train.iloc[i,0].split(':')[-1]
  list_entity_1.append(term)
                  

list_entity_2=[]

for i in range(len(df_train)):
  term=df_train.iloc[i,2].split(':')[-1]
  list_entity_2.append(term)
                  


list_rel_1=[]

for i in range(len(df_train)):
  term=df_train.iloc[i,1].split(':')[-1]
  list_rel_1.append(term)
list_rel_1[-1]


df_train['entity1_']=list_entity_1
df_train['entity2_']=list_entity_2
df_train['rel_']=list_rel_1

df_train_=df_train[['entity1_','entity2_','rel_','confidence']]
df_train_.rename(columns={'entity1_':'arg1_entity','entity2_':'arg2_entity','rel_':'relation'},inplace=True)

df_train4=df_train_.groupby(['arg1_entity','relation','arg2_entity'])['confidence'].mean().reset_index()
                      
                                        
                      

df_train=df_train4.copy()

df_train['arg1_entity']=df_train['arg1_entity'].str.replace(' ','_')
df_train['arg2_entity']=df_train['arg2_entity'].str.replace(' ','_')


cn_train_sc=df_train.copy()

sbc=cn_train_sc[cn_train_sc['relation'].isin(['subpartof','superpartof'])]
                  

for i in range(len(sbc)):
    if sbc.iloc[i,1]=='superpartof':
        k1=sbc.iloc[i,0]
        k2=sbc.iloc[i,2]
        sbc.iloc[i,0]=k2
        sbc.iloc[i,2]=k1


df_test3=sbc[['arg1_entity','relation','arg2_entity','confidence']]
df_test4=df_test3.groupby(['arg1_entity','relation','arg2_entity'])['confidence'].mean().reset_index()

df_test4['arg1_entity']=df_test4['arg1_entity'].str.replace(' ','_')
df_test4['arg2_entity']=df_test4['arg2_entity'].str.replace(' ','_')

sbs_list=[]
for i in range(len(df_test4)):
     aa='<'+df_test4.iloc[i,0]+'> <'+df_test4.iloc[i,2]+'> '+str(df_test4.iloc[i,3])
     sbs_list.append(aa)

ts='\n'.join(sbs_list)
file = open('train_subclass_jul5.txt', 'w')
file.write(ts)
file.close()


mod3=[]
with open(r'train_subclass_jul5.txt', 'r')  as fp:
                                                    
                                                              
    for line in fp:
                                              
                                                      

           x = line[:-1]
                                 

                                      
           mod3.append(x.split())

mod3[-1]=mod3[-1]
         


df=pd.DataFrame(mod3,columns=['Entity1','Entity2','Prob_Score'])
df['Prob_Score']=df['Prob_Score'].astype('float64')

df=df[~(df['Entity1'] == df['Entity2'])]

df1=df['Entity2'].value_counts().sort_values(ascending=False).reset_index()
df1.rename(columns={'Entity2':'count'},inplace=True)
df1.rename(columns={'index':'Entity2'},inplace=True)

df2=df1[df1['count']>1]

list_ent2=list(df2['Entity2'].unique())
              

list_ent3=[]

for i in list_ent2:
    max_score=df[df['Entity2']==i]['Prob_Score'].max()
    min_score=df[df['Entity2']==i]['Prob_Score'].min()

    if max_score!=min_score:
           list_ent3.append(i)


df_filt=df[df['Entity2'].isin(list_ent3)]


df_filt_s=df_filt.sort_values(['Entity2','Prob_Score'],ascending=False).groupby('Entity2').head(1000)


list_ent33=list(df_filt_s['Entity2'].unique())

list_ranks=[]
for i in list_ent33:
           
  rank_this=[]
  df_filt_s2=df_filt_s[df_filt_s['Entity2']==i]
  lista=df_filt_s2['Prob_Score'].tolist()
  listas=list(set(lista))
                
  min_r=1
  max_r=len(listas)
  for i in range(len(df_filt_s2)-1):
    flag1=False
                 
                 
                                 
    if df_filt_s2.iloc[i,-1]==df_filt_s2.iloc[i+1,-1]:
      if len(rank_this)==0 and flag1==True:
        rank_this.append(max_r)
        max_r-=1
      if len(rank_this)==0 and flag1==False:
        rank_this.append(max_r)
                 
      elif len(rank_this)>0 and flag1==False:
        rank_this.append(max_r)
      elif len(rank_this)>0 :
        rank_this.append(rank_this[-1])
    else:
                           
      rank_this.append(max_r)
      max_r-=1
      flag1=True
  if df_filt_s2.iloc[-1,-1]==df_filt_s2.iloc[-2,-1]:
                   
      rank_this.append(rank_this[-1])
  else:
                    
      rank_this.append(rank_this[-1]-1)
  list_ranks.extend(rank_this)


df_filt_s_c=df_filt_s.copy()
df_filt_s_c['Original_Rank']=list_ranks
df_filt_s_c2=df_filt_s_c.copy()


mod3=[]
with open(valid_file, 'r')  as fp:
    for line in fp:
           x = line[:-1]
           mod3.append(x.split())

mod3[-1]=mod3[-1]
                
                                      


import pandas as pd

df=pd.DataFrame(mod3,columns=['Entity1','Entity2','Prob_Score'])
df['Prob_Score']=df['Prob_Score'].astype('float64')
          


df=df[~(df['Entity1'] == df['Entity2'])]

df1=df['Entity2'].value_counts().sort_values(ascending=False).reset_index()
                   
                   
df1.rename(columns={'Entity2':'count'},inplace=True)
df1.rename(columns={'index':'Entity2'},inplace=True)
                   
                   
df2=df1[df1['count']>1]


list_ent2=list(df2['Entity2'].unique())

list_ent3=[]

for i in list_ent2:
    max_score=df[df['Entity2']==i]['Prob_Score'].max()
    min_score=df[df['Entity2']==i]['Prob_Score'].min()

    if max_score!=min_score:
           list_ent3.append(i)

df_filt=df[df['Entity2'].isin(list_ent3)]
df_filt_s=df_filt.sort_values(['Entity2','Prob_Score'],ascending=False).groupby('Entity2').head(1000)

list_ent33=list(df_filt_s['Entity2'].unique())

list_ent33=list(df_filt_s['Entity2'].unique())

list_ranks=[]
for i in list_ent33:
           
  rank_this=[]
  df_filt_s2=df_filt_s[df_filt_s['Entity2']==i]
  lista=df_filt_s2['Prob_Score'].tolist()
  listas=list(set(lista))
                
  min_r=1
  max_r=len(listas)
  for i in range(len(df_filt_s2)-1):
    flag1=False
                 
                 
                                 
    if df_filt_s2.iloc[i,-1]==df_filt_s2.iloc[i+1,-1]:
      if len(rank_this)==0 and flag1==True:
        rank_this.append(max_r)
        max_r-=1
      if len(rank_this)==0 and flag1==False:
        rank_this.append(max_r)
                 
      elif len(rank_this)>0 and flag1==False:
        rank_this.append(max_r)
      elif len(rank_this)>0 :
        rank_this.append(rank_this[-1])
    else:
                           
      rank_this.append(max_r)
      max_r-=1
      flag1=True
  if df_filt_s2.iloc[-1,-1]==df_filt_s2.iloc[-2,-1]:
                   
      rank_this.append(rank_this[-1])
  else:
                    
      rank_this.append(rank_this[-1]-1)
  list_ranks.extend(rank_this)


df_filt_s_c=df_filt_s.copy()
df_filt_s_c['Original_Rank']=list_ranks


from scipy.stats import rankdata

def diffr(a,b):
     lista=[]
     for i,j in zip(a,b):
       if i==j:
          lista.append(0)
       else:
          lista.append(1)
     listb=list(range(1, len(lista)+1))
     listb.reverse()
                  
     listb2=[iaa/sum(listb) for iaa in listb]
     ws=sum([ia*ja for ia,ja in zip(lista,listb2)])
     return ws


def ranker(a,b):
 lista=[]
 for i,j in enumerate(zip(a,b)):
                         
  if j[0]==j[1]:
                          
     lista.append(0)
  else:
     list_hvv=[]
     for ia in range(0,i):
                     
      if j[0]==b[ia]:
        list_hvv.append(abs(ia-i))
                           
        break
     for ib in range(i+1,len(b)):
       if j[0]==b[ib]:
         list_hvv.append(abs(ib-i))
                            
         break
                                
     if len(list_hvv)>0:
       min_lista=min(list_hvv)
       lista.append(min_lista)
     else:
       lista.append(1)
                
  az=[(1.5)**iw for iw in range(1,len(b)+1)]
  azz=[iww/sum(az) for iww in az]
  listaa=sum([iwww*jwww for iwww,jwww in zip(lista,azz)])
 return [lista,listaa]


# Compute normalized hDMA for rank disagreement.
def hdma(a,b):
  suma=0
  for i,j in enumerate(zip(a,b)):
    if j[0]==j[1]:
      suma+=0
    else:
                              
      suma+=2**((len(a)-1)-i)
                       
  sumb=suma/(suma+1)
                     
  return sumb


# Load validation axioms and associated ranking information.
def load_valid_data(valid_data_file, classes, relations):
    data = []
    rel = f'SubClassOf'
    with open(valid_data_file, 'r') as f:
        for line in f:
            it = line.strip().split()
            id1 = it[0]
            id2 = it[1]
            id3=float(it[2])
            if id1 not in classes or id2 not in classes or rel not in relations and id1!=id2:
                continue
            dfcd=df_filt_s_c[df_filt_s_c['Entity2']==id2]
            dicta={}
            c_list=dfcd['Entity1'].tolist()
            rank_list=dfcd['Original_Rank'].tolist()
            for i,j in zip(c_list,rank_list):
              dicta[classes[i]]=j
            data.append((classes[id1], relations[rel], classes[id2],id3,dicta))
    return data


df_filt_s_c4=df_filt_s_c2.copy()
list_ent333=list(df_filt_s_c4['Entity2'].unique())


list_of_d={}
for i in list_ent333:
     df_sub=df_filt_s_c4[df_filt_s_c4['Entity2']==i]
     list_of_d[i]={ia:ja for ia,ja in zip(df_sub['Entity1'].tolist(),df_sub['Original_Rank'].tolist()) }


import pickle

with open('list_subclass_rank_jul5.pkl', 'wb') as handle:
    pickle.dump(list_of_d, handle)


import os
                               
                            
                                    
                         
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
                   
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.python.framework import function
import re
import math
                                
import logging
from tensorflow.keras.layers import (
    Input,
)
from tensorflow.keras import optimizers
from tensorflow.keras import initializers
from tensorflow.keras import constraints
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, CSVLogger
from tensorflow.keras import backend as K
from scipy.stats import rankdata
from tensorflow.python.keras.utils.data_utils import Sequence


        


config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
                              
                    
                                      
tf.compat.v1.keras.backend.set_session(tf.compat.v1.Session(config=config))

logging.basicConfig(level=logging.INFO)
""""

def load_valid_data(valid_data_file, classes, relations):
    data = []
    rel = f'SubClassOf'
    with open(valid_data_file, 'r') as f:
        for line in f:
            it = line.strip().split()
            id1 = it[0]
            id2 = it[1]
            if id1 not in classes or id2 not in classes or rel not in relations:
                continue
            data.append((classes[id1], relations[rel], classes[id2]))
    return data


# In[4]:


def load_cls(train_data_file):
    train_subs=list()
    counter=0
    with open(train_data_file,'r') as f:
        for line in f:
            counter+=1
            it = line.strip().split()
            #print(line)
            cls1 = it[0]
            cls2 = it[1]
            train_subs.append(cls1)
            train_subs.append(cls2)
    train_cls = list(set(train_subs))
    return train_cls,counter"""


# Load ontology axioms, build entity/relation indices, and prepare training data.
def load_data(filename):
    classes = {}
    relations = {}
    data = {'nf1': [], 'nf3': []}
    with open(filename) as f:
        for line in f:
                                        
            if line.startswith('SubObjectPropertyOf'):
                pass
                                 
            line = line.strip()[11:-1]
            if not line:
                continue
            if line.startswith('ObjectIntersectionOf('):
                                      
                it = line.split(' ')
                c = it[0][21:]
                d = it[1][:-1]
                e = it[2]
                f=float(it[3])
                if c not in classes:
                    classes[c] = len(classes)
                if d not in classes:
                    classes[d] = len(classes)
                if e not in classes:
                    classes[e] = len(classes)
                form = 'nf2'
                if e == 'owl:Nothing':
                    form = 'disjoint'
                                                                          

            elif line.find('ObjectSomeValuesFrom') != -1:
                                       
                it = line.split(' ')
                c = it[0]
                r = it[1][21:]
                d = it[2][:-1]
                f=float(it[3])
                if c not in classes:
                    classes[c] = len(classes)
                if d not in classes:
                    classes[d] = len(classes)
                if r not in relations:
                    relations[r] = len(relations)
                data['nf3'].append((classes[c], relations[r], classes[d],f))
            else:
                                
                            
                it = line.split(' ')
                c = it[0]
                d = it[1]
                e=float(it[2])
                r = 'SubClassOf'
                if r not in relations:
                    relations[r] = len(relations)
                if c not in classes:
                    classes[c] = len(classes)
                if d not in classes:
                    classes[d] = len(classes)
                data['nf1'].append((classes[c],relations[r],classes[d],e))

                                                           
    if 'owl:Thing' not in classes:
        classes['owl:Thing'] = len(classes)
                                                             

    prot_ids=[]
    for val in classes:
              prot_ids.append(classes[val])
    prot_ids=np.array(prot_ids)

                               
    n_classes = len(classes)
    data['nf3_neg'] = []
    for c, r, d,e in data['nf3']:
        x = np.random.choice(prot_ids)
        while x == c:
            x = np.random.choice(prot_ids)

        y = np.random.choice(prot_ids)
        while y == d:
             y = np.random.choice(prot_ids)
        data['nf3_neg'].append((c, r,x,0.99))
        data['nf3_neg'].append((y, r, d,0.99))

    data['radius'] = []
    for val in classes:
        data['radius'].append(classes[val])


    data['sub_info']=[]
    file = open("list_subclass_rank_jul5.pkl","rb")
    listt = pickle.load(file)

    for i in listt:
      list_final2=[np.float32(classes[i])]
              
                                       
      l1=list(listt[i].keys())
      l2=list(listt[i].values())
      for ia in range(len(l1)):
        list_final2.append(np.float32(classes[l1[ia]]))
        list_final2.append(np.float32(l2[ia]))
        list_final2.append(np.float32(1))
      data['sub_info'].append(list_final2)


    global numbaa
    numbaa=0
    for i in data['sub_info']:
          ca=len(i)
          if ca>numbaa:
                 numbaa=ca


    for i in data['sub_info']:
         if len(i)<numbaa:
            aa=numbaa-len(i)
            aa2=int(aa/3)
                       
            aaa=[99,99,0]*(aa2)
            i.extend(aaa)

             


    data['nf1'] = np.array(data['nf1'])
                                        
    data['nf3'] = np.array(data['nf3'])
                                        
                                                  
    data['top'] = np.array([classes['owl:Thing'],])
    data['nf3_neg'] = np.array(data['nf3_neg'])
                                                          
                                                  
    data['radius'] = np.array(data['radius'])
    data['sub_info']= np.array(data['sub_info'])

    for key, val in data.items():
        index = np.arange(len(data[key]))
        np.random.seed(seed=100)
        np.random.shuffle(index)
        data[key] = val[index]

    return data, classes, relations


gdata_file=owl_file
train_data_model, classes, relations = load_data(gdata_file)

varss=int((numbaa-1)/3)

# Compute the transformed hDMA ranking score.
def hdm_(a,b):
            
                               
                             
   ak=tf.where(tf.equal(a,b),0.0,1.)
   asa=[2.**((varss-1)-ip) for ip in range(varss)]
   asa=tf.convert_to_tensor(asa)
   asa=tf.reshape(asa,[1,-1])
   asa2=tf.repeat(asa,[256],axis=0)
   asa3=tf.math.reduce_sum(tf.math.multiply(asa2,ak),axis=1)
                                       
   asa4=tf.math.divide(asa3,asa3+1.)
   return asa4


def hdm_(a,b):
            
                               
                             
   ak=tf.where(tf.equal(a,b),0.0,1.)
                                                   
   asa=[2.**((len(a)-1)-ip) for ip in range(len(a))]
   asa=tf.convert_to_tensor(asa)
   asa=tf.reshape(asa,[1,-1])
                                    
   asa2=asa
                              
   asa3=tf.math.reduce_sum(tf.math.multiply(asa2,ak),axis=1)
                                       
   asa4=tf.math.exp(tf.math.exp(tf.math.divide(asa3,asa3+1.)))
                                                                    
   return asa4[0]

# Compute the transformed nDCG-based ranking score used by the model.
def ndcg_(a,b):
    t2=[a,b]
    t2=tf.convert_to_tensor(t2)
    t2=tf.cast(t2,tf.float32)
                       
                   
    a2=[*range(2,t2.shape[1]+2)]
    a2=tf.convert_to_tensor(a2)
    a2=tf.reshape(a2,[1,-1])
    a2=tf.cast(a2,tf.float32)
              
                 
    a3=tf.repeat(a2,[2],axis=0)
              
                    
                                            
    add=t2/((tf.math.log(a3)/tf.math.log(2.0)))
                
               
                    
    return tf.math.exp(tf.math.exp(tf.reduce_sum(add,axis=1)[1]/tf.reduce_sum(add,axis=1)[0]))


from scipy.stats import rankdata
@tf.py_function(Tout=tf.float32)
def py_log_huber(x):
                                         
  return(rankdata(x,axis=1,method='dense'))


def hdma(a,b):
  suma=0
  for i,j in enumerate(zip(a,b)):
    if j[0]==j[1]:
      suma+=0
    else:
                              
      suma+=2**((len(a)-1)-i)
                       
                     
  if suma>0:
                                                        
     sumb=suma/(suma+1)
                                      
                              
                              
  else:
     sumb=0.0
                           
                     
  return sumb


                          

from sklearn.metrics import ndcg_score
                                      
import numpy as np

# Stat-n-Ball embedding model and loss functions.
class ELModel(tf.keras.Model):

    def __init__(self, nb_classes, nb_relations, embedding_size, batch_size, margin, reg_norm=1):
        super(ELModel, self).__init__()
        self.nb_classes = nb_classes
        self.nb_relations = nb_relations
        self.margin = margin
        self.reg_norm = reg_norm
        self.batch_size = batch_size
        self.inf = 5.0                 
                                                   
        csample_weights = np.random.uniform(low=-1, high=1, size=(nb_classes, embedding_size))
        radius_wts = np.random.uniform(low=0, high=1, size=(nb_classes,))
        cls_weights = np.column_stack((csample_weights,radius_wts))
        cls_weights = cls_weights / np.linalg.norm(
            cls_weights, axis=1).reshape(-1, 1)
        rel_weights = np.random.uniform(low=-1, high=1, size=(nb_relations, embedding_size))
        rel_weights = rel_weights / np.linalg.norm(
            rel_weights, axis=1).reshape(-1, 1)
        self.cls_embeddings = tf.keras.layers.Embedding(
            nb_classes,
            embedding_size + 1,
            input_length=1,
            weights=[cls_weights,])
        self.rel_embeddings = tf.keras.layers.Embedding(
            nb_relations,
            embedding_size,
            input_length=1,
            weights=[rel_weights,])


    def call(self, input):
        nf1,  nf3,  top, nf3_neg,radius, sub_info = input
        loss1 = self.nf1_loss(nf1)
                                   
        loss3 = self.nf3_loss(nf3)
                                   
                                      
        loss_top = self.top_loss(top)
        loss_nf3_neg = self.nf3_neg_loss(nf3_neg)
                                                  
                                                  
                                                  
                                          
        loss7 = self.radius_loss(radius)
        loss8=self.sub_info_loss(sub_info)
                   
        loss = loss1 +loss3+  loss_top + loss_nf3_neg-loss8-loss7
                   
        return loss


    def reg(self, x):
        res = tf.abs(tf.norm(x, axis=1) - self.reg_norm)
        res = tf.reshape(res, [-1, 1])
        return res

    # NF1: confidence-aware subclass loss (C ⊑ D).
    def nf1_loss(self, input):
        c = input[:, 0]
        r = input[:,1]
        d = input[:, 2]
        e=input[:,3]
        c = self.cls_embeddings(c)
        d = self.cls_embeddings(d)
        r = self.rel_embeddings(r)

        rc = tf.math.maximum(0.0,c[:, -1])
        rd = tf.math.maximum(0.0,d[:, -1])
        x1 = c[:, 0:-1]
        x2 = d[:, 0:-1]
                                                           
                                                           
                    
                      
        x3=x1
        euc = tf.norm(x3 - x2, axis=1)
        rdiff=rd-rc
        rsum=rd+rc
        mu_high=tf.math.divide_no_nan(rsum, rdiff)
        hlf=((tf.cast(e,tf.float32)-1.0)*(mu_high-1.0))/(0.0-1.0)
        tot=1.0+hlf
        reduction_factor=  tf.math.divide_no_nan(rc, rd)
        tot=tf.where(tf.math.greater(rd,rc),tot,tot*reduction_factor)
        timea=tf.clip_by_value(tot, clip_value_min=1,clip_value_max=mu_high)   
                         
                                                                                                                                                                                    
                                                                                   
                                                                                                                        
        dst=tf.where(tf.equal(euc + rc - rd - margin,0.0),tf.where(tf.equal(timea,0.0),0.0,tf.nn.relu(timea)),tf.nn.relu(timea*(euc + rc - rd - margin)))
        dst=tf.reshape(dst,[-1,1])
        return dst + self.reg(x1) + self.reg(x2)

    # Negative NF1 loss for corrupted subclass axioms.
    def nf1_neg_loss(self, input):
        c = input[:, 0]
        r = input[:,1]
        d = input[:, 2]
        e=input[:,3]
        c = self.cls_embeddings(c)
        d = self.cls_embeddings(d)
        r = self.rel_embeddings(r)
        rc = tf.math.maximum(0.0,c[:, -1])
        rd = tf.math.maximum(0.0,d[:, -1])
        x3 = c[:, 0:-1]
        x2 = d[:, 0:-1]
        euc = tf.norm(x3 - x2, axis=1)
        rdiff=rd-rc
        rsum=rd+rc
        mu_high=tf.math.divide_no_nan(rsum, rdiff)
        hlf=((tf.cast(e,tf.float32)-1.0)*(mu_high-1.0))/(0.0-1.0)
        tot=1.0+hlf
        timea=tf.clip_by_value(tot, clip_value_min=1,clip_value_max=mu_high)   
                         
                                                                                                                                                                                    
                                                                                   
        dst=tf.where(tf.equal(euc + rc - rd - margin,0.0),tf.nn.relu(timea),tf.nn.relu(timea*(euc + rc - rd - margin)))
        dst=tf.reshape(dst,[-1,1])
        return dst + self.reg(x3) + self.reg(x2)

    # NF2: confidence-aware intersection loss (C ⊓ D ⊑ E).
    def nf2_loss(self, input):
        c = input[:, 0]
        d = input[:, 1]
        e = input[:, 2]
        c = self.cls_embeddings(c)
        d = self.cls_embeddings(d)
        e = self.cls_embeddings(e)
        f=input[:,3]
        rc = tf.reshape(tf.math.maximum(0.0,c[:, -1]), [-1, 1])
        rd = tf.reshape(tf.math.maximum(0.0,d[:, -1]), [-1, 1])
        re = tf.reshape(tf.math.maximum(0.0,e[:, -1]), [-1, 1])
        sr = rc + rd
        x1 = c[:, 0:-1]
        x2 = d[:, 0:-1]
        x3 = e[:, 0:-1]

        x = x2 - x1
        dst = tf.reshape(tf.norm(x, axis=1), [-1, 1])
        dst2 = tf.reshape(tf.norm(x3 - x1, axis=1), [-1, 1])
        dst3 = tf.reshape(tf.norm(x3 - x2, axis=1), [-1, 1])
        rdst = tf.nn.relu(tf.math.minimum(rc, rd) - re - self.margin)
        dst_loss = (tf.nn.leaky_relu(dst - sr - self.margin)
                    + tf.nn.leaky_relu(dst2 - rc - self.margin)
                    + tf.nn.leaky_relu(dst3 - rd - self.margin)
                    + rdst)

        rdiff=rd-rc
        rsum=rd+rc
        mu_high=tf.math.divide_no_nan(rsum, rdiff)
        hlf=((tf.cast(f,tf.float32)-1.0)*(mu_high-1.0))/(0.0-1.0)
        tot=1.0+hlf
        timea=tf.clip_by_value(tot, clip_value_min=1,clip_value_max=mu_high)   
                         
        dst_loss2=tf.where(tf.equal(dst_loss,0),timea,timea*dst_loss)
                                                                           
        return dst_loss2 + self.reg(x1) + self.reg(x2) + self.reg(x3)

    # Negative NF2 loss for corrupted intersection axioms.
    def nf2_neg_loss(self, input):
        c = input[:, 0]
        d = input[:, 1]
        e = input[:, 2]
        c = self.cls_embeddings(c)
        d = self.cls_embeddings(d)
        e = self.cls_embeddings(e)
        f=input[:,3]
        rc = tf.reshape(tf.math.maximum(0.0,c[:, -1]), [-1, 1])
        rd = tf.reshape(tf.math.maximum(0.0,d[:, -1]), [-1, 1])
        re = tf.reshape(tf.math.maximum(0.0,e[:, -1]), [-1, 1])
        sr = rc + rd
        x1 = c[:, 0:-1]
        x2 = d[:, 0:-1]
        x3 = e[:, 0:-1]
                    
        dst = tf.reshape(tf.norm(x1-x2, axis=1), [-1, 1])
        dst2 = tf.reshape(tf.norm(x3 - x1, axis=1), [-1, 1])
        dst3 = tf.reshape(tf.norm(x3 - x2, axis=1), [-1, 1])
                                                                      

        dst_loss=(tf.nn.leaky_relu(-rc-rd+dst-self.margin)+tf.nn.leaky_relu(rc-dst2+self.margin)+\
                 tf.nn.leaky_relu(rd-dst3+self.margin))

        rdiff=rd-rc
        rsum=rd+rc
        mu_high=tf.math.divide_no_nan(rsum, rdiff)
        hlf=((tf.cast(f,tf.float32)-1.0)*(mu_high-1.0))/(0.0-1.0)
        tot=1.0+hlf
        timea=tf.clip_by_value(tot, clip_value_min=1,clip_value_max=mu_high)   
                         
        dst_loss2=tf.where(tf.equal(dst_loss,0),timea,timea*dst_loss)
                                                                           
        return dst_loss2 + self.reg(x1) + self.reg(x2) + self.reg(x3)


    # NF3: confidence-aware existential loss (C ⊑ ∃R.D).
    def nf3_loss(self, input):
                               
        c = input[:, 0]
        r = input[:, 1]
        d = input[:, 2]
        e=input[:,3]
        c = self.cls_embeddings(c)
        d = self.cls_embeddings(d)
        r = self.rel_embeddings(r)
        x1 = c[:, 0:-1]
        x2 = d[:, 0:-1]
        x3 = x1 + r

        rc = tf.math.maximum(0.0,c[:, -1])
        rd = tf.math.maximum(0.0,d[:, -1])
        euc = tf.norm(x3 - x2, axis=1)
        rdiff=rd-rc
        rsum=rd+rc
        mu_high=tf.math.divide_no_nan(rsum, rdiff)
        hlf=((tf.cast(e,tf.float32)-1.0)*(mu_high-1.0))/(0.0-1.0)
        tot=1.0+hlf
        reduction_factor=  tf.math.divide_no_nan(rc, rd)
        tot=tf.where(tf.math.greater(rd,rc),tot,tot*reduction_factor)
        timea=tf.clip_by_value(tot, clip_value_min=1,clip_value_max=mu_high)   
                         
                                                                                   
                                                                                                                                                                                    
                                                                                                                        
        dst=tf.where(tf.equal(euc + rc - rd - margin,0.0),tf.where(tf.equal(timea,0.0),0.0,tf.nn.relu(timea)),tf.nn.relu(timea*(euc + rc - rd - margin)))
        dst=tf.reshape(dst,[-1,1])
        return dst + self.reg(x1) + self.reg(x2)

    # Negative NF3 loss for corrupted existential axioms.
    def nf3_neg_loss(self, input):
                               
        c = input[:, 0]
        r = input[:, 1]
        d = input[:, 2]
        e=input[:,3]
        c = self.cls_embeddings(c)
        d = self.cls_embeddings(d)
        r = self.rel_embeddings(r)
        x1 = c[:, 0:-1]
        x2 = d[:, 0:-1]
        rc = tf.math.maximum(0.0,c[:, -1])
        rd = tf.math.maximum(0.0,d[:, -1])
        x3 = x1 + r
        rdiff=rd-rc
        rsum=rd+rc
        mu_high=tf.math.divide_no_nan(rsum, rdiff)
        hlf=((tf.cast(e,tf.float32)-1.0)*(mu_high-1.0))/(0.0-1.0)
        tot=1.0+hlf
        reduction_factor=  tf.math.divide_no_nan(rc, rd)
        tot=tf.where(tf.math.greater(rd,rc),tot,tot*reduction_factor)
        timea=tf.clip_by_value(tot, clip_value_min=1,clip_value_max=mu_high)    
                                           
                                           
                         
        euc = tf.norm(x3 - x2, axis=1)

                                                                            
                                                                                                                                      
        dst=tf.where(tf.equal(-(euc - rc - rd) + self.margin,0.0),tf.where(tf.equal(timea,0.0),0.0,tf.nn.relu(timea)),tf.nn.relu(timea*(-(euc - rc - rd) + self.margin)))
        dst=tf.reshape(dst,[-1,1])
        return dst + self.reg(x1) + self.reg(x2)


    # Disjointness loss for C ⊓ D ⊑ ⊥.
    def dis_loss(self, input):
        c = input[:, 0]
        d = input[:, 1]
        c = self.cls_embeddings(c)
        d = self.cls_embeddings(d)
        e=input[:,3]
                
                                                                
                                                                
        rc = tf.math.maximum(0.0,c[:, -1])
        rd = tf.math.maximum(0.0,d[:, -1])
        sr = rc + rd
        x1 = c[:, 0:-1]
        x2 = d[:, 0:-1]
        rdiff=rd-rc
        rsum=rd+rc
        mu_high=tf.math.divide_no_nan(rsum, rdiff)
        hlf=((tf.cast(e,tf.float32)-1.0)*(mu_high-1.0))/(0.0-1.0)
        tot=1.0+hlf
        timea=tf.clip_by_value(tot, clip_value_min=1,clip_value_max=mu_high)    
                         
        euc = tf.norm(x2 - x1, axis=1)
                                                                           
                                                            
        dst=tf.where(tf.equal(sr - euc + self.margin,0),tf.reshape(tf.nn.leaky_relu(timea),[-1,1]),tf.reshape(tf.nn.leaky_relu(timea*(sr - euc + self.margin)), [-1, 1]))
                                                                                        
                                                                          

        return dst + self.reg(x1) + self.reg(x2)

    # Constrain owl:Thing to the designated top radius.
    def top_loss(self, input):
        d = input[:, 0]
        d = self.cls_embeddings(d)
        rd = tf.reshape(tf.math.maximum(0.0,d[:, -1]), [-1, 1])
        return tf.math.abs(rd - self.inf)

    # Relation inclusion loss.
    def inclusion_loss(self,input):
        r1 = input[:, 0]
        r2 = input[:, 1]
        r1 = self.rel_embeddings(r1)
        r2 = self.rel_embeddings(r2)
                                         

        euc = tf.norm(r2 - r1, axis=1)

        normalize_a = tf.nn.l2_normalize(r1,0)
        normalize_b = tf.nn.l2_normalize(r2,0)
        direction=tf.reduce_sum(tf.multiply(normalize_a,normalize_b))
        dir_loss = tf.abs(1 - direction)
        dir_loss = tf.reshape(dir_loss, [-1, 1])
        dst = tf.reshape(tf.nn.leaky_relu(euc - self.margin), [-1, 1])

        return dst + self.reg(r1) + self.reg(r2) + dir_loss

    # Relation-chain loss.
    def chain_loss(self,input):
        r1 = input[:, 0]
        r2 = input[:, 1]
        r3 = input[:, 2]
        c = self.rel_embeddings(r1)
        d = self.rel_embeddings(r2)
        e = self.rel_embeddings(r3)
        s = e - c

        dst = tf.reshape(tf.norm(c - d, axis=1), [-1, 1])
        dst2 = tf.reshape(tf.norm(e - c, axis=1), [-1, 1])
        dst3 = tf.reshape(tf.norm(e - d, axis=1), [-1, 1])
        dst_dir = tf.reshape(tf.norm(s - d, axis=1), [-1, 1])
        dst_loss = (tf.nn.relu(dst_dir - self.margin))

        res_vec = c + d
        normalize_a = tf.nn.l2_normalize(res_vec,0)
        normalize_b = tf.nn.l2_normalize(e,0)
        direction=tf.reduce_sum(tf.multiply(normalize_a,normalize_b))
        dir_loss = tf.abs(1 - direction)
        dir_loss = tf.reshape(dir_loss, [-1, 1])
        return dst_loss + self.reg(c) + self.reg(d) + self.reg(e) + dir_loss

    # Ranking loss over subconcepts using overlap-derived ranks.
    def sub_info_loss(self,input):
        da=input[:,0]
        d=self.cls_embeddings(da)
        ind_c=[i for i in range(1,numbaa,3)]
        rank_c=[i for i in range(2,numbaa,3)]
        flag_c=[i for i in range(3,numbaa,3)]
                          
        acc=[]
        for iia in ind_c:
            acc.append(input[:,iia])
        ac=tf.transpose(tf.convert_to_tensor(acc))

        rcc=[]
        for iia in rank_c:
            rcc.append(input[:,iia])
        c_rank_tf=tf.transpose(tf.convert_to_tensor(rcc))

        fcc=[]
        for iia in flag_c:
            fcc.append(input[:,iia])
        c_flag_tf=tf.transpose(tf.convert_to_tensor(fcc))
        c_flag_tf=tf.cast(c_flag_tf,tf.float32)
        c_rank_tf=tf.cast(c_rank_tf,tf.float32)
        c=self.cls_embeddings(ac)
        dr=tf.math.maximum(0.0,d[:,-1])
        cr=tf.math.maximum(0.0,c[:,:,-1])

        dd=d[:,:-1]
        cc=c[:,:,:-1]
        dd=tf.repeat(dd,[varss],axis=0)
        dd=tf.reshape(dd,[256,varss,int(hyperparam_dim)])   
        tf_dist=tf.reduce_sum(tf.abs(dd-cc)**2, -1)**(1./2)
        dr_x=tf.repeat(dr,[varss],axis=0)
        dr_x=tf.reshape(dr_x,[256,varss])
                                       
                                        
        tf_radsum=dr_x+cr
        tf_raddiff=dr_x-cr


                                                                            
        dr=(tf_radsum+tf_raddiff)/2
        cr=(tf_radsum-tf_raddiff)/2
        reduction_factor=  tf.math.divide_no_nan(cr, dr)
                                                                                                                                              
                                                                                                                              

                                                                  
                                                                        
        ab=tf.math.divide_no_nan(tf_dist, tf.abs(tf_raddiff))*reduction_factor
        ab_or=tf.math.divide_no_nan(tf_dist, tf.abs(tf_raddiff))
                                                                                                                                                 
        aff=tf.where(tf.less_equal(tf_raddiff,0),tf.where(tf.greater(tf_radsum,0),tf.where(tf.greater(dr*cr,0),ab,0),  0.0  ),tf.where(tf.greater(dr*cr,0),ab_or,0))                  
                         
                  
                     
                                         
        affa_num=py_log_huber(aff)
                                 
        affa_num=tf.cast(affa_num,tf.float32)
        affa_num=tf.math.multiply(affa_num,c_flag_tf)
                              
                      
        rank_full= 100-(tf.broadcast_to(tf.reshape(tf.reduce_max(affa_num, axis=1),[-1,1]),[256,varss])-affa_num)
        rank_full= tf.multiply(rank_full,c_flag_tf)
        rnk_flg_tf=tf.multiply(c_rank_tf,c_flag_tf)
        rnk_flg_tf2=100-(tf.broadcast_to(tf.reshape(tf.reduce_max(rnk_flg_tf, axis=1),[-1,1]),[256,varss])-rnk_flg_tf)
        rnk_flg_tf3=tf.multiply(rnk_flg_tf2,c_flag_tf)

                                                                                    

        ind_ndcg=[i for i in range(0,256)]


        abc=[]
        for iiv in ind_ndcg:
               b=rnk_flg_tf3[iiv]
               a=rank_full[iiv]
               hv_k_2=tf.where(tf.greater_equal(tf.reduce_sum(rnk_flg_tf3[iiv]),tf.reduce_sum(rank_full[iiv])),ndcg_(b,a),-hdm_(b,a))
                                                                  
               abc.append(hv_k_2)


                                         
        azi=tf.convert_to_tensor(abc)
                     
                                      
                                          
                                   

                                                            
                                                                              
        azi=tf.where(tf.math.is_nan(azi), tf.zeros_like(azi), azi)
                                          
                             
        azi=tf.reshape(azi,[-1,1])
                                                       
                                                    
        return azi
                                                           
                                                                   
                   
                      
                                                                                               
                                
                                     


    # Penalize negative class radii.
    def radius_loss(self, input):
        d = input[:, 0]
        d = self.cls_embeddings(d)
        rd = tf.reshape(d[:, -1], [-1, 1])
                   
        return tf.math.minimum(0.0,rd)


         


# Mini-batch generator for training inputs.
class Generator(object):

    def __init__(self, data, batch_size, steps=100):
        self.data = data
        self.batch_size = batch_size
        self.steps = steps
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def reset(self):
        self.start = 0

    def next(self):
        if self.start < self.steps:
            nf1_index = np.random.choice(
                self.data['nf1'].shape[0], self.batch_size)
                                              
                                                                
                                          
                                                            
                                              
                                                                
            nf3_index = np.random.choice(
                self.data['nf3'].shape[0], self.batch_size)
                                          
                                                            
                                          
                                                                 
            top_index = np.random.choice(
                self.data['top'].shape[0], self.batch_size)
            nf3_neg_index = np.random.choice(
                self.data['nf3_neg'].shape[0], self.batch_size)
                                                                                                      
                                                                                              
            radius_index = np.random.choice(
                self.data['radius'].shape[0], self.batch_size)
            sub_info_index=np.random.choice(self.data['sub_info'].shape[0],self.batch_size)

            nf1 = self.data['nf1'][nf1_index]
                                                          
                                              
                                                           
            nf3 = self.data['nf3'][nf3_index]
                                              
                                                   
            top = self.data['top'][top_index]
            nf3_neg = self.data['nf3_neg'][nf3_neg_index]
                                                                         
                                                             
            radius = self.data['radius'][radius_index]
            sub_info=self.data['sub_info'][sub_info_index]
            labels = np.zeros((self.batch_size, 1), dtype=np.float32)
            self.start += 1
            return ([nf1,  nf3,  top, nf3_neg,radius,sub_info], labels)
        else:
            self.reset()

                
class MyModelCheckpoint(ModelCheckpoint):

    def __init__(self, *args, **kwargs):
        super(ModelCheckpoint, self).__init__()
        self.out_classes_file = kwargs.pop('out_classes_file')
        self.out_relations_file = kwargs.pop('out_relations_file')
        self.monitor = kwargs.pop('monitor')
        self.cls_list = kwargs.pop('cls_list')
        self.rel_list = kwargs.pop('rel_list')
        self.valid_data = kwargs.pop('valid_data')
        self.proteins = kwargs.pop('proteins')
        self.prot_index = list(self.proteins.values())
        self.prot_dict = {v: k for k, v in enumerate(self.prot_index)}
        self.load_weights_on_restart = False
          
        self.save_freq='epoch'
        self.best_rank = 100000
        self.valid_count=0

    def on_epoch_end(self, epoch, logs=None):
                                         
        current_loss = logs.get(self.monitor)
        if math.isnan(current_loss):
            self.model.stop_training = True
            return
        el_model = self.model.layers[-1]
        cls_embeddings = el_model.cls_embeddings.get_weights()[0]
        rel_embeddings = el_model.rel_embeddings.get_weights()[0]

        prot_embeds = cls_embeddings[self.prot_index]
                                            
        prot_rs = prot_embeds[:, -1].reshape(-1, 1)
        prot_embeds = prot_embeds[:, :-1]
                                             
                              
        mean_rank = 0
        n = len(self.valid_data)

        for c, r, d,e,f in self.valid_data:

            c, r, d = self.prot_dict[c], r, self.prot_dict[d]
            ec = prot_embeds[c, :]
            rc = prot_rs[c, :]
            dd=prot_embeds[d,:]
            er = rel_embeddings[r, :]
                     
            rdd=prot_rs[d,:]


            r2new=np.maximum(0,rc)
            prot_rsnew=np.maximum(0,rdd)

            rd=prot_rsnew-r2new
            sr=prot_rsnew+r2new
            dst2 = np.linalg.norm(dd.reshape(1,-1) - ec.reshape(1,-1),axis=1)
            mu_curr = np.divide(dst2, rd, out=np.zeros_like(dst2), where=rd!=0)

            mu_high = np.divide(sr, rd, out=np.zeros_like(sr), where=rd!=0)

               
                                                                             
               

            e=np.reshape(e,[-1,1])

            a1=((mu_curr-1.0)*(0.0-1.0))
            a2=(mu_high-1.0)
            hlf=np.divide(a1, a2, out=np.zeros_like(a1), where=a2!=0)
            tot=1.0+hlf
                    
            if len(f)==0:
               res=np.linalg.norm(e-tot, axis=1)
               res=np.abs(res)

            else:
               res=np.linalg.norm(e-tot, axis=1)
               res=np.abs(res)
               keys_d=list(f.keys())
               vals_d=list(f.values())
                             
               ddks=prot_embeds[keys_d,:]
               rdd2=prot_rs[keys_d]
               r2new=np.maximum(0,rc)
                              
               prot_rsnew=np.maximum(0,rdd2)
                                             
               rd=prot_rsnew-r2new
               sr=prot_rsnew+r2new

               dst2 = np.linalg.norm(ddks - ec.reshape(1, -1), axis=1)
               dst2=dst2.reshape(-1, 1)
                                   

               mu_curr = np.divide(dst2, rd, out=np.zeros_like(dst2), where=rd!=0)

               mu_high = np.divide(sr, rd, out=np.zeros_like(sr), where=rd!=0)
                                        

               e=np.reshape(e,[-1,1])

               a1=((mu_curr-1.0)*(0.0-1.0))
               a2=(mu_high-1.0)
               hlf=np.divide(a1, a2, out=np.zeros_like(a1), where=a2!=0)
                                 
               tot=1.0+hlf
               tot=np.abs(tot)
               tot_rank=rankdata(tot, method='dense')
                                
                                                      

               c=0
               ndcg_={}
               rank_ndcg={}
               hdm={}
               sums=[]
                                                      
                                                     
                                  

               a=vals_d
               b=tot_rank

               if sum(a)>=sum(b):
                        true_relevance=np.asarray([a])
                        relevance_score=np.asarray([b])
                        ndcg=ndcg_score(true_relevance,relevance_score)
                              
                                                             
                             
                                                  
                                                   
                        resa=-ndcg
                        resb=diffr(a,b)
                        resc=ranker(a,b)[1]
                        res12=resa+resb+resc
                        res+=res12
                                 
               else:

                        hdm=diffr(a,b)
                        sums=ranker(a,b)[1]
                        res11=hdm+sums
                        res11+=hdma(a,b)
                                      
                                                       
                        res+=res11
                             

            mean_rank += res
        mean_rank=np.max([mean_rank[0],0])
        mean_rank /= n
                              
                         

        if mean_rank < self.best_rank:
            self.valid_count = 0
            self.best_rank = mean_rank
            cls_file = self.out_classes_file
            rel_file = self.out_relations_file
                                                      
                                         
                                                      
                                                      

            df = pd.DataFrame(
                {'classes': self.cls_list, 'embeddings': list(cls_embeddings)})
            df.to_pickle(cls_file)

            df = pd.DataFrame(
                {'relations': self.rel_list, 'embeddings': list(rel_embeddings)})
            df.to_pickle(rel_file)
        else:
            if self.valid_count < 60:
                self.valid_count+=1
            else:
                self.model.stop_training = True


         


def build_model(device,train_data,classes,relations,valid_data):
    proteins = {}                                          
    for val in classes:
        proteins[val] = classes[val]
    nb_classes = len(classes)
    nb_relations = len(relations)
    nb_train_data = 0
    for key, val in train_data.items():
        nb_train_data = max(len(val), nb_train_data)
    train_steps = int(math.ceil(nb_train_data / (1.0 * batch_size)))
    train_generator = Generator(train_data, batch_size, steps=train_steps)

    cls_dict = {v: k for k, v in classes.items()}
    rel_dict = {v: k for k, v in relations.items()}

    cls_list = []
    rel_list = []
    for i in range(nb_classes):
        cls_list.append(cls_dict[i])
    for i in range(nb_relations):
        rel_list.append(rel_dict[i])

    with tf.device('/' + device):
        nf1 = Input(shape=(4,), dtype=np.float32)      
                                                      
                                                  
                                                      
        nf3 = Input(shape=(4,), dtype=np.float32)
                                                
                                                  
        top = Input(shape=(1,), dtype=np.float32)
        nf3_neg = Input(shape=(4,), dtype=np.float32)
                                                         
                                                     
        radius = Input(shape=(1,), dtype=np.float32)
        sub_info=Input(shape=(numbaa,),dtype=np.float32)


        el_model = ELModel(nb_classes, nb_relations, embedding_size, batch_size, margin, reg_norm)
        out = el_model([nf1,  nf3,  top, nf3_neg,radius,sub_info])
        model = tf.keras.Model(inputs=[nf1,  nf3,  top, nf3_neg,radius,sub_info], outputs=out)
        optimizer = optimizers.legacy.Adam(lr=learning_rate)
        model.compile(optimizer=optimizer, loss='mse')
                   
        top = classes.get('owl:Thing', None)
        checkpointer = MyModelCheckpoint(
            out_classes_file=out_classes_file,
            out_relations_file=out_relations_file,
            cls_list=cls_list,
            rel_list=rel_list,
            valid_data=valid_data,
                                                                      
            proteins=proteins,
            monitor='loss')

        logger = CSVLogger(loss_history_file)

                                 
        cls_embeddings = el_model.cls_embeddings.get_weights()[0]
        rel_embeddings = el_model.rel_embeddings.get_weights()[0]

        cls_file = out_classes_file
        rel_file = out_relations_file

        df = pd.DataFrame(
            {'classes': cls_list, 'embeddings': list(cls_embeddings)})
        df.to_pickle(cls_file)

        df = pd.DataFrame(
            {'relations': rel_list, 'embeddings': list(rel_embeddings)})
        df.to_pickle(rel_file)
                                                             
                                                          
        model.fit_generator(
            train_generator,
            steps_per_epoch=train_steps,
            epochs=epochs,
            workers=12,
            callbacks=[logger, checkpointer])


         


                    
                                                             


         


valid_data_file=valid_file
valid_data_model = load_valid_data(valid_data_file, classes, relations)


         


margins = [float(hyperparam_margin_loss)]
embed_dims = [int(hyperparam_dim)]
batch_size =  256
device='gpu:0'
reg_norm=1
learning_rate=3e-4
                   
epochs=1000
for d in embed_dims:
    embedding_size = d
    for m in margins:
        margin = m
        out_classes_file = f'Stat_n_Ball_results/EmEL_dir/GO_{embedding_size}_{margin}_{epochs}_{save_file_name}_cls.pkl'
        out_relations_file = f'Stat_n_Ball_results/EmEL_dir/GO_{embedding_size}_{margin}_{epochs}_{save_file_name}_rel.pkl'
        loss_history_file= f'Stat_n_Ball_results/EmEL_dir/GO_lossHis_{embedding_size}_{margin}_{epochs}.csv'
        build_model(device,train_data_model,classes,relations,valid_data_model)

