# (complete code will be added by Dec 21/22 AOE) (Code upload in progress. Sorry for the inconvenience).

# Stat-n-Ball: Enhancing Probabilistic Knowledge Graph Embeddings with Geometric and Confidence-Aware Models

## Abstract
Region-based Knowledge Graph Embedding (R-KGE) models, which represent entities as convex shapes (e.g., balls) and relations as geometric transformations in vector space, offer a promising approach for explainable and accurate reasoning over ontologies. However, existing R-KGE models assume perfect reliability of Knowledge Graphs (KGs), which is often unrealistic as real-world KGs are noisy and incomplete. To address this, Probabilistic Knowledge Graphs (P-KGs) associate axioms with confidence scores, capturing the uncertainty of their truthfulness.

We propose *Stat-n-Ball*, a novel R-KGE framework that incorporates confidence scores by representing axioms' certainty as overlapping volumes between entities in vector space. Our approach enhances the geometric representation of KGs, enabling accurate link prediction and confidence estimation in probabilistic settings. Experimental evaluations on standard P-KG datasets demonstrate that *Stat-n-Ball* achieves at least a **2× improvement** in entity association detection and a **minimum 10% reduction** in confidence prediction error compared to state-of-the-art models. These results underscore its effectiveness in handling noisy and uncertain KGs while preserving logical and semantic integrity.

## Authors
- Aniket Mitra
- Vinu E Venugopal

## Open Data Used for Testing
We evaluate our approach using three probabilistic knowledge graph datasets:

1. **cn15k**: A subgraph of the commonsense knowledge graph **ConceptNet**, which represents general human knowledge.
2. **nl27k**: Extracted from **NELL** (*Never-Ending Language Learning*), a dataset that continuously collects data.
3. **ppi5k**: A subset of the STRING dataset that assigns probabilities to protein-protein interactions.

## Features
- **Geometric Representations**: Entities are modeled as convex shapes (balls) and relations as transformations, allowing intuitive and explainable embeddings.
- **Confidence-Aware Modeling**: Handles uncertainty by associating confidence scores with axioms and representing them as overlapping volumes in vector space.
- **Enhanced Reasoning**: Enables accurate link prediction and confidence estimation in noisy and incomplete knowledge graphs.
- **State-of-the-Art Performance**: Achieves significant improvements in entity association detection and confidence prediction error.

## Getting Started
### Prerequisites
Ensure you have the following libraries installed:
- Python 3.8+
- NumPy
- PyTorch
- Scikit-learn

### Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/yourusername/stat-n-ball.git
cd stat-n-ball
pip install -r requirements.txt
```

### Usage
1. Prepare your dataset in the supported format.
2. Configure the settings in `config.yaml`.
3. Train the model:
   ```bash
   python train.py --config config.yaml
   ```
4. Evaluate the model:
   ```bash
   python evaluate.py --config config.yaml
   ```

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

