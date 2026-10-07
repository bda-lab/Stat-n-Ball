                       

    

import sys
test_file = sys.argv[1]
cls_file= sys.argv[2]
rel_file=sys.argv[3]
dataset_dets=sys.argv[4]
output_file_name=sys.argv[5]
import pandas as pd

                                
                                                  
                                                  
                     


# Load trained class and relation embeddings.
df_cls_cn=pd.read_pickle(cls_file)
df_rel_cn=pd.read_pickle(rel_file)

# Load and parse the test axioms.
mod3=[]
                                                        
                                                           
                                                                    
                                                                         
with open(test_file, 'r') as fp:
    for line in fp:
                                              
                                                      

           x = line[:-1]
                                 

                                      
           mod3.append(x)

mod3[-1]=mod3[-1]

import numpy as np

# Evaluate ball overlap and count good/valid axioms.
hv_save_prob=[]
mu_save=[]
mu_bb=[]
c_good=0
c_bad=0

all_test_v=[]
for i in mod3:
               
      all_test_v.append(i.split())
               
cac=0

for j in all_test_v:
 try:
  cac+=1
                                                                                                                                                                                                                                                                             
              
           
  c=np.array(df_cls_cn[df_cls_cn['classes']==j[0]]['embeddings'])[0][:-1]
  d=np.array(df_cls_cn[df_cls_cn['classes']==j[1]]['embeddings'])[0][:-1]
  rel=np.array(df_rel_cn[df_rel_cn['relations']==j[2]]['embeddings'])[0]
  c=c+rel

  cr=np.array(df_cls_cn[df_cls_cn['classes']==j[0]]['embeddings'])[0][-1]
  dr=np.array(df_cls_cn[df_cls_cn['classes']==j[1]]['embeddings'])[0][-1]

  if dr>cr and dr>0 and cr>0:
      dist_bada=np.linalg.norm(c-d)
      rad_diff=dr-cr
      rad_sum=dr+cr
                            
                                
                              
      mu_val=dist_bada/rad_diff
      mu_save.append(mu_val)
                            
      p=float(j[3])
      if dist_bada<=rad_sum and dist_bada>rad_diff:
              mu_b=rad_sum/rad_diff
                                 
                                                     
              val_fr_conversion=1+(((mu_val-1)*(0-1))/(mu_b-1))
                                                 
                                     
                                   
              mu_bb.append((mu_val,mu_b))
              c_good+=1
      elif dist_bada>rad_sum:
              val_fr_conversion=0.
              c_bad+=1
      elif dist_bada<rad_diff:
              val_fr_conversion=1.
              c_good+=1
  elif dr<=cr and dr>0 and cr>0:
               dist_bada=np.linalg.norm(c-d)
               rad_diff=dr-cr
               rad_sum=dr+cr
                                     
                                              
                                       
               mu_val=dist_bada/rad_diff
               mu_save.append(mu_val)
                                     
               p=float(j[3])
               if dist_bada<=rad_sum and dist_bada>rad_diff:
                    mu_b=rad_sum/rad_diff
                                       
                                                           
                    val_fr_conversion=1+(((mu_val-1)*(0-1))/(mu_b-1))
                                                       
                                            
                    mu_bb.append((mu_val,mu_b))
                    c_good+=1
               elif dist_bada>rad_sum:
                    val_fr_conversion=0.
                    c_bad+=1
               elif dist_bada<rad_diff:
                    val_fr_conversion=1.
                    c_good+=1

 except:
  pass

                    
                           
                                           
                                        


# Write geometric validity counts to the output file.
with open(output_file_name, "w") as f:
    f.writelines([F"Dataset Details: {dataset_dets} \n","=============== \n",F"Good Balls: {c_good}, Valid Balls: {c_bad} \n"])

hv_save_prob=[]
hv_save_prob_case2=[]
mu_save=[]
mu_bb=[]
c_good=0
c_bad=0
hava=[]

case1=0
case2=0
sum_check=0
                                     
                   

all_test_v=[]
for i in mod3:
      all_test_v.append(i.split())
                 
save_inds_true=[]
kk=-1
for j in all_test_v:
     kk+=1
     c=np.array(df_cls_cn[df_cls_cn['classes']==j[0]]['embeddings'])[0][:-1]
     d=np.array(df_cls_cn[df_cls_cn['classes']==j[1]]['embeddings'])[0][:-1]
     rel=np.array(df_rel_cn[df_rel_cn['relations']==j[2]]['embeddings'])[0]
     c=c+rel

                           
                           

     cr=np.array(df_cls_cn[df_cls_cn['classes']==j[0]]['embeddings'])[0][-1]
     dr=np.array(df_cls_cn[df_cls_cn['classes']==j[1]]['embeddings'])[0][-1]

     val_fr_conversion=0
     if dr<=cr and dr>0 and cr>0:
               


      reduction_factor=dr/cr
      save_inds_true.append(kk)
      dist_bada=np.linalg.norm(c-d)
                            
                     
      rad_diff=abs(dr-cr)
      rad_sum=dr+cr
                            
                                
                              
      mu_val=dist_bada/rad_diff
      mu_save.append(mu_val)
                            
      p=float(j[3])
      if dist_bada<=rad_sum and dist_bada>rad_diff:
              sum_check+=1
              mu_b=rad_sum/rad_diff
                                 
                                                     
              val_fr_conversion=(1+(((mu_val-1)*(0-1))/(mu_b-1)))*reduction_factor
              if mu_val==np.inf or mu_b==np.inf:
                val_fr_conversion=0.
                                                          
              mu_bb.append((mu_val,mu_b))
              c_good+=1
              hv_save_prob.append([val_fr_conversion,p])
      elif dist_bada>rad_sum:
              sum_check+=1
              val_fr_conversion=0.
              c_bad+=1
                        
              hv_save_prob.append([val_fr_conversion,p])
      elif dist_bada<rad_diff:
              sum_check+=1
              val_fr_conversion=reduction_factor
              c_good+=1
              hv_save_prob.append([val_fr_conversion,p])

                                                       
     elif dr>cr and dr>0 and cr>0:
      case2+=1
      dist_bada=np.linalg.norm(d-c)
                            
                     
      rad_diff=dr-cr
      rad_sum=dr+cr
      if rad_sum<=rad_diff:
          pass
                              
      mu_val=dist_bada/rad_diff
      mu_save.append(mu_val)
                            
      p=float(j[3])
      if dist_bada<=rad_sum and dist_bada>rad_diff:
              sum_check+=1
              mu_b=rad_sum/rad_diff
                                 
                                                     
              val_fr_conversion=1+(((mu_val-1)*(0-1))/(mu_b-1))
              if mu_val==np.inf or mu_b==np.inf:
                val_fr_conversion=0.
              mu_bb.append((mu_val,mu_b))
              c_good+=1
              hv_save_prob.append([val_fr_conversion,p])
      elif dist_bada>rad_sum:
              sum_check+=1
              val_fr_conversion=0.
              c_bad+=1
                        
              hv_save_prob.append([val_fr_conversion,p])
      elif dist_bada<rad_diff:
              sum_check+=1
              val_fr_conversion=1.
              c_good+=1
              hv_save_prob.append([val_fr_conversion,p])

                                                 

     else:
      c_bad+=1
      val_fr_conversion=0.
      p=float(j[3])
      hv_save_prob.append([val_fr_conversion,p])


                                       
w1=c_good/(c_good+c_bad)
w2=c_bad/(c_good+c_bad)
                         
                   

a1=[]
for i in hv_save_prob:
              
             
    a1.append(i)


a2=[]
for i in hv_save_prob_case2:
              
             
    a2.append(i)

# Compute confidence prediction errors.
diff=[]
                       
for i in a1:
  diff.append(abs(i[0]-i[1]))

diff_case2=[]
diff_case3=[]
                       
for i in a1:
  diff_case2.append(abs(i[0]-i[1]))
  diff_case3.append((i[0]-i[1])**2)

                                                 
mae=sum(diff_case2)/(c_good+c_bad)

                                                              
mse=np.sqrt(np.sum(diff_case3)/(c_good+c_bad))

with open(output_file_name, "a") as f:
    f.write(F"MAE: {mae}, MSE: {mse} \n")

                                   
          
                                                        

mod3=[]
with open(test_file, 'r')  as fp:
                                               
                                                         
                                                       
    for line in fp:
                                              
                                                      

           x = line[:-1]
                                 

                                      
           mod3.append(x.split())

mod3[-1]=mod3[-1]
mod3[-1]

import pandas as pd

# Build ground-truth ranking groups from test confidences.
df=pd.DataFrame(mod3,columns=['Entity1','Entity2','Rel','Prob_Score'])
df['Prob_Score']=df['Prob_Score'].astype('float64')

df=df[~(df['Entity1'] == df['Entity2'])]

df1=df[['Entity2','Rel']].value_counts().sort_values(ascending=False).reset_index()
           
df1.rename(columns={0:'count'},inplace=True)
                                                     
df2=df1[df1['count']>1]

list_ent2=list(df2['Entity2'].unique())
list_rel2=list(df2['Rel'].unique())
              

list_ent3_=[]
list_ent3=[]
list_rel3=[]

for i in list_ent2:
  for j in list_rel2:
   if len(df[(df['Entity2']==i) & (df['Rel']==j)])>1:
    max_score=df[(df['Entity2']==i) & (df['Rel']==j)]['Prob_Score'].max()
    min_score=df[(df['Entity2']==i) & (df['Rel']==j)]['Prob_Score'].min()

    if max_score!=min_score:
           list_ent3_.append([i,j])
           list_ent3.append(i)
           list_rel3.append(j)


df_filt=df[(df['Entity2'].isin(list_ent3)) & df['Rel'].isin(list_rel3)]
df_filt_s=df_filt.sort_values(['Entity2','Rel','Prob_Score'],ascending=False).groupby(['Entity2','Rel']).head(1000)

save_metas=[]
list_ranks=[]
for ii in list_ent3_:
   rank_this=[]
                 
   df_filt_s2=df_filt_s[(df_filt_s['Entity2']==ii[0]) & (df_filt_s['Rel']==ii[1])]
                      
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
                               
                                
   list_ranks.append(rank_this)
   save_metas.append(ii)


df_a=pd.DataFrame()

for ii,j in zip(save_metas,list_ranks):
  df_hv_filt=df_filt_s[(df_filt_s['Entity2']==ii[0]) & (df_filt_s['Rel']==ii[1])]
  df_hv_filt['Original_Rank']=j
  df_a=pd.concat([df_a,df_hv_filt],axis=0)


df_filt_s_c=df_a.copy()


ca=0
import numpy as np
probs_to_save=[]
save_nums=[]

# Predict overlap-based confidence scores for ranking evaluation.
for i in range(len(df_filt_s_c)):
                                                                                                                                                                                                                                                                                                                                                                                                                        
 try:
  ca+=1
  c=np.array(df_cls_cn[df_cls_cn['classes']==df_filt_s_c.iloc[i,0]]['embeddings'])[0][:-1]
  d=np.array(df_cls_cn[df_cls_cn['classes']==df_filt_s_c.iloc[i,1]]['embeddings'])[0][:-1]
                               
  rel=np.array(df_rel_cn[df_rel_cn['relations']==df_filt_s_c.iloc[i,2]]['embeddings'])[0][:]
  c=c+rel

  cr=np.array(df_cls_cn[df_cls_cn['classes']==df_filt_s_c.iloc[i,0]]['embeddings'])[0][-1]
  dr=np.array(df_cls_cn[df_cls_cn['classes']==df_filt_s_c.iloc[i,1]]['embeddings'])[0][-1]

  val_fr_conversion=0

  if dr<=cr and dr>0 and cr>0:
               
                          
      reduction_factor=dr/cr
                                
      dist_bada=np.linalg.norm(c-d)
      rad_diff=abs(dr-cr)
      rad_sum=dr+cr
                            
                                
                              
                                

      if rad_diff!=0:
        mu_val=dist_bada/rad_diff
      else:
        mu_val=0
                             
                            
                    
      if dist_bada<=rad_sum and dist_bada>rad_diff:
                           
              save_nums.append(i)
              mu_b=rad_sum/rad_diff
                                 
                                                     
              val_fr_conversion=(1+(((mu_val-1)*(0-1))/(mu_b-1)))*reduction_factor
              if mu_val==np.inf or mu_b==np.inf:
                val_fr_conversion=0.
                                          
                        
              probs_to_save.append(val_fr_conversion)
      elif dist_bada>rad_sum:
                           
              save_nums.append(i)
              val_fr_conversion=0.
                       
              probs_to_save.append(val_fr_conversion)
      elif dist_bada<rad_diff:
                           
              save_nums.append(i)
              val_fr_conversion=reduction_factor
                        
              probs_to_save.append(reduction_factor)
      else:
              probs_to_save.append(1.)
                                                       
  elif dr>cr and dr>0 and cr>0:
               
               
                          
      dist_bada=np.linalg.norm(d-c)
      rad_diff=dr-cr
      rad_sum=dr+cr
      if rad_sum<=rad_diff:
          pass
                              
                                

      if rad_diff!=0:
        mu_val=dist_bada/rad_diff
      else:
        mu_val=0
                             
                            
                    
      if dist_bada<=rad_sum and dist_bada>rad_diff:
                           
              save_nums.append(i)
              mu_b=rad_sum/rad_diff
                                 
                                                     
              val_fr_conversion=1+(((mu_val-1)*(0-1))/(mu_b-1))
              if mu_val==np.inf or mu_b==np.inf:
                val_fr_conversion=0.
                                          
                        
              probs_to_save.append(val_fr_conversion)
      elif dist_bada>rad_sum:
              save_nums.append(i)
                           
              val_fr_conversion=0.
                       
              probs_to_save.append(0.)
      elif dist_bada<rad_diff:
                           
              save_nums.append(i)
              val_fr_conversion=1.
                        
              probs_to_save.append(1.)
      else:
              probs_to_save.append(1.)
  else:
                       
                                  
              probs_to_save.append(0.)
              save_nums.append(i)
 except:
  pass


a1=[i for i in probs_to_save if i>0]

# Compare original and predicted subconcept rankings.
if len(a1)>=100:
    df_filt_s_c['Prob_Ball']=probs_to_save
    df_filt_s_c2=df_filt_s_c.copy()
    df_filt_s_c3=df_filt_s_c2[['Entity1','Entity2','Rel','Prob_Ball']]
    df_filt_s_c4=df_filt_s_c3.sort_values(['Entity2','Rel','Prob_Ball'],ascending=False).groupby(['Entity2','Rel']).head(10000)
    df_filt_s_c_copy= df_filt_s_c.copy()
    save_metas=[]
    list_ranks=[]
    for ii in list_ent3_:
       rank_this=[]
                     
       df_filt_s2=df_filt_s_c4[(df_filt_s_c4['Entity2']==ii[0]) & (df_filt_s_c4['Rel']==ii[1])]
                          
       lista=df_filt_s2['Prob_Ball'].tolist()
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
                                       
                                    
       list_ranks.append(rank_this)
       save_metas.append(ii)

    df_a=pd.DataFrame()
    for ii,j in zip(save_metas,list_ranks):
       df_hv_filt=df_filt_s_c4[(df_filt_s_c4['Entity2']==ii[0]) & (df_filt_s_c4['Rel']==ii[1])]
       df_hv_filt['Pred_Rank']=j
       df_a=pd.concat([df_a,df_hv_filt],axis=0)

    df_filt_s_c2=df_a.copy()

    unique_entities=list(df['Entity2'].unique())
    unique_relations=list(df['Rel'].unique())

    mer_final=pd.merge(left=df_filt_s_c,right=df_filt_s_c2,on=['Entity1','Entity2','Rel'],how='inner')
    mer_final.to_csv('mer_final25jun.csv',index=None)
                        
    dfm=pd.read_csv('mer_final25jun.csv')
    df=dfm.copy()

    # Weighted rank-disagreement score.
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


    # Rank displacement score used by the hDMA evaluation.
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
             azz.reverse()
             listaa=sum([iwww*jwww for iwww,jwww in zip(lista,azz)])

        return [lista,listaa]


    c=0
    ndcg_={}
    rank_ndcg={}
    hdm_res={}
    sums=[]
    from sklearn.metrics import ndcg_score
    from ranking_measures import measures

                       
    # Compute nDCG or hDMA for each superconcept/relation group.
    for i in unique_entities:
      for j in unique_relations:
           df_subs=df[(df['Entity2']==i) & (df['Rel']==j)]
           if len(df_subs)>0:
               a=df_subs['Original_Rank'].tolist()
               b=df_subs['Pred_Rank'].tolist()
               if sum(a)>=sum(b):
                    true_relevance=np.asarray([a])
                    relevance_score=np.asarray([b])
                    ndcg=ndcg_score(true_relevance,relevance_score)
                    ndcg_[i]=ndcg
                    rank_ndcg[i]=measures.find_rankdcg(a,b)
                    c+=1
               else:
                     hdm_res[i]=diffr(a,b)
                     sums.append(ranker(a,b)[1])


    ndcg_mean=np.mean(list(ndcg_.values()))
    ndcg_med=np.median(list(ndcg_.values()))

    hdm_vals_mean=np.mean(list(hdm_res.values()))
    hdm_vals_med=np.median(list(hdm_res.values()))

    with open(output_file_name, "a") as f:
         f.write(F"\n HDMA_mean: {hdm_vals_mean}, HDMA_median: {hdm_vals_med},  NDCG_mean: {ndcg_mean}, NDCG_median: {ndcg_med}, total_subconcept_ndcg_applied: {c}, total_multiple_superconcepts: {len(unique_entities)}")


