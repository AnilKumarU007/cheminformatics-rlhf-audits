# Cheminformatics & AI Scientific Audit Portfolio
**Author:** Anil Kumar (IIT Bombay B.Tech | AI Scientific Auditor & Cheminformatics Specialist)
This repository contains production-grade, warning-free Python and RDKit scripts designed for high-throughput molecular data processing, sparse matrix vectorization, and rigorous RLHF evaluation of frontier Large Language Models (LLMs).
## Repository Structure
1. **`rdkit_similarity_pipeline.py`** — High-performance Tanimoto similarity matrix computation using Morgan fingerprints and sparse CSR matrices (`scipy.sparse`), optimized for million-molecule datasets.
2. **`smarts_substructure_filter.py`** — Robust molecular parsing script handling SMILES sanitization, tautomer deduplication, and strict SMARTS substructure matching with defensive null-checks.
3. **`llm_chemical_audit_rubric.md`**— A sample Process-Supervised Reward Modeling (PRM) rubric used to audit LLM outputs for thermodynamic vs. kinetic control and mechanistic validity.
## Quick Start / Usage Example
You can easily import and run the similarity pipeline directly in your Python environment:
```python
from rdkit_similarity_pipeline import compute_sparse_tanimoto
smiles = ["CCO", "CC", "CCCO", "c1ccccc1"]
matrix, valid = compute_sparse_tanimoto(smiles)
print(f"Computed matrix shape: {matrix.shape}")
