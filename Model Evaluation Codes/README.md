To run the evaluator file for **ppi** dataset: <br />
<br />
```python3 evaluator_ppi.py --test_file --cls_file --rel_file --dataset_dets --output_file_name```
<br />
**test_file** = file containing test axioms. <br />
**cls_file** = file containing embeddings of concept <br />
**rel_file** = file containing embeddings of relations <br />
**dataset_dets** = details about dataset being evaluated <br />
**output_file_name** = name of output file where the metric values will be stored. <br />
<br />
Eg:
<br />
```python3 evaluator_ppi.py ppi_test.txt  ppi_cls_embeddings.pkl ppi_rel_embeddings.pkl ppi --output_ppi.txt```

Similarly for **cn** and **nl** datasets,
```python3 evaluator_nl_cn_data.py --test_file --cls_file --dataset_dets --output_file_name```
