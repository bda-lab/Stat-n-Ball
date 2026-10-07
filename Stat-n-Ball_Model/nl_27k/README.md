# Stat-n-Ball

This directory contains the implementation of the **Stat-n-Ball** model.

## Setup

Create a directory for storing the generated embedding files:

```bash
mkdir -p Stat_n_Ball_results/EmEL_dir
```

## Running the Model

Run the model with:

```bash
python3 stats-n-ball.py <valid_file> <df_train_file> <owl_file> <save_file_name> <hyperparam_margin_loss> <hyperparam_dim>
```

## Arguments

- `valid_file`: Path to the validation dataset.
- `df_train_file`: Path to the training dataset.
- `owl_file`: Path to the OWL ontology file.
- `save_file_name`: Base name used for saving the generated embedding files.
- `hyperparam_margin_loss`: Margin-loss hyperparameter.
- `hyperparam_dim`: Number of embedding dimensions.

## Example

```bash
python3 stats-n-ball.py test_file.txt train.tsv cn_15k_axioms.owl cn15k_embed_outputs 0.1 50
```

For this example:

- Validation dataset: `test_file.txt`
- Training dataset: `train.tsv`
- OWL file: `cn_15k_axioms.owl`
- Output name: `cn15k_embed_outputs`
- Margin loss: `0.1`
- Embedding dimension: `50`

## Output

The generated embedding files are stored in:

```text
Stat_n_Ball_results/EmEL_dir
```

## Notes

The script uses **positional command-line arguments**. Therefore, arguments should be provided in the order shown above rather than as named flags such as `--valid_file` or `--df_train_file`.
