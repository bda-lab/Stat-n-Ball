To run stats-n-ball model:

python3 stats-n-ball.py --valid_file --df_train_file --owl_file --save_file_name --hyperparam_margin_loss --hyperparam_dim

valid_file=validation dataset
df_train_file=training dataset
owl_file=owl file
save_file_file=file name where the embeddings will be saved
hyperparam_margin_loss= margin loss
hyperparam_dim= no. of dimensions

Eg:


python3 stats-n-ball.py test_file.txt train.tsv nl_27k_axioms.owl nl27k_embed_outputs 0.1 50
