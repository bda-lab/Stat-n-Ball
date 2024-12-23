To run stats-n-ball model: <br />
<br />
```python3 stats-n-ball.py --valid_file --df_train_file --owl_file --save_file_name --hyperparam_margin_loss --hyperparam_dim```
<br />
<br />
**valid_file**=validation dataset <br />
**df_train_file**=training dataset <br />
**owl_file**=owl file <br />
**save_file_file**=file name where the embeddings will be saved <br />
**hyperparam_margin_loss**= margin loss <br />
**hyperparam_dim**= no. of dimensions <br />
<br />
Eg:
<br />
<br />


```python3 stats-n-ball.py test_file.txt train.tsv cn_15k_axioms.owl cn15k_embed_outputs 0.1 50```
