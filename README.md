# Stat-n-Ball: Enhancing Probabilistic Knowledge Graph Embeddings with Geometric and Confidence-Aware Models

[Paper Link](https://dl.acm.org/doi/10.1145/3701716.3715487)

## Abstract

Region-based Knowledge Graph Embedding (R-KGE) models, which represent entities as convex shapes (e.g., balls) and relations as geometric transformations in vector space, offer a promising approach for explainable and accurate reasoning over ontologies. However, existing R-KGE models assume perfect reliability of Knowledge Graphs (KGs), which is often unrealistic as real-world KGs are noisy and incomplete. To address this, Probabilistic Knowledge Graphs (P-KGs) associate axioms with confidence scores, capturing the uncertainty of their truthfulness.

We propose *Stat-n-Ball*, a novel R-KGE framework that incorporates confidence scores by representing axioms' certainty as overlapping volumes between entities in vector space. Our approach enhances the geometric representation of KGs, enabling accurate link prediction and confidence estimation in probabilistic settings. Experimental evaluations on standard P-KG datasets demonstrate that *Stat-n-Ball* achieves at least a **2× improvement** in entity association detection and a **minimum 5% reduction** in confidence prediction error compared to state-of-the-art models. These results underscore its effectiveness in handling noisy and uncertain KGs while preserving logical and semantic integrity.

## Authors

- Aniket Mitra
- Vinu E Venugopal

## Open Data Used for Testing

We evaluate our approach using three probabilistic knowledge graph datasets:

1. **cn15k**: A subgraph of the commonsense knowledge graph **ConceptNet**, which represents general human knowledge.
2. **nl27k**: Extracted from **NELL** (*Never-Ending Language Learning*), a dataset that continuously collects data.
3. **ppi5k**: A subset of the STRING dataset that assigns probabilities to protein-protein interactions.

## Ontology Normalization

Before training Stat-n-Ball, the ontology must be converted into the EL normal forms used by the embedding model.

The normalization procedure follows the approach used in the [EL Embeddings repository](https://github.com/bio-ontology-research-group/el-embeddings). The repository provides a `Normalizer.groovy` script based on the `jcel` reasoner for converting an OWL 2 EL ontology into normalized axioms in OWL functional syntax.

### 1. Set up the normalizer

Clone the EL Embeddings repository together with its submodules:

```bash
git clone --recurse-submodules https://github.com/bio-ontology-research-group/el-embeddings
```

If building `jcel` from source, move into the `jcel` directory and install it using Maven:

```bash
cd el-embeddings/jcel
mvn install
```

The EL Embeddings repository also provides the required JAR files in its `jar/` directory, which can be added to the Java `CLASSPATH`.

### 2. Normalize the ontology

Run the normalization script with the input OWL ontology and the desired normalized output file:

```bash
groovy Normalizer.groovy -i <input_ontology.owl> -o <normalized_ontology.owl>
```

For example:

```bash
groovy Normalizer.groovy -i ontology.owl -o ontology_normalized.owl
```

The normalized file produced by this step is then used as the OWL/axiom input for Stat-n-Ball training.

The normalization script supports:

```text
usage: groovy Normalizer.groovy -i INPUT -o OUTPUT [-h]

-h, --help          Show help information
-i, --input <arg>   Input OWL ontology
-o, --output <arg>  Output file containing normalized axioms
```

## Features

- **Geometric Representations**: Entities are modeled as convex shapes (balls) and relations as transformations, allowing intuitive and explainable embeddings.
- **Confidence-Aware Modeling**: Handles uncertainty by associating confidence scores with axioms and representing them as overlapping volumes in vector space.
- **Enhanced Reasoning**: Enables accurate link prediction and confidence estimation in noisy and incomplete knowledge graphs.
- **State-of-the-Art Performance**: Achieves significant improvements in entity association detection and confidence prediction error.

## Results

- **Entity Association Detection**: At least **2× improvement** over existing models.
- **Confidence Prediction Error**: Reduced by a **minimum of 5%**.

## Citation

If you use *Stat-n-Ball* in your research, please cite:

```bibtex
@article{mitra2024statnball,
  title={Stat-n-Ball: Enhancing Probabilistic Knowledge Graph Embeddings with Geometric and Confidence-Aware Models},
  author={Mitra, Aniket and Venugopal, Vinu E},
  year={2024}
}
```

## Acknowledgments

Special thanks to the contributors of the datasets used in this project: ConceptNet, NELL, and STRING.

The ontology normalization procedure is adapted from the [EL Embeddings](https://github.com/bio-ontology-research-group/el-embeddings) implementation.
