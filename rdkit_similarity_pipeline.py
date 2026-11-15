"""
High-Performance Tanimoto Similarity Pipeline for Large Molecular Libraries
Author: Anil Kumar (IIT Bombay B.Tech)
"""

import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.DataStructs import ConvertToNumpyArray
from scipy.sparse import csr_matrix

def compute_sparse_tanimoto(smiles_list, radius=2, n_bits=2048):
    """
    Computes pairwise Tanimoto similarity matrix efficiently using scipy.sparse 
    CSR matrices to prevent out-of-memory errors on large datasets.
    """
    fps = []
    valid_smiles = []
    
    # Use the legacy generator method which natively supports Numpy array conversion
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            continue  # Defensive null-check for parsing failures
            
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=radius, nBits=n_bits)
        arr = np.zeros((n_bits,), dtype=np.int8)
        ConvertToNumpyArray(fp, arr)
        fps.append(arr)
        valid_smiles.append(smi)
        
    if not fps:
        raise ValueError("No valid molecules parsed from SMILES list.")
        
    X = np.array(fps, dtype=np.float32)
    X_sparse = csr_matrix(X)
    
    # Vectorized Tanimoto calculation via sparse dot product
    intersection = X_sparse.dot(X_sparse.T).toarray()
    row_sums = X.sum(axis=1)
    union = row_sums[:, None] + row_sums[None, :] - intersection
    
    # Avoid division by zero
    with np.errstate(divide='ignore', invalid='ignore'):
        tanimoto_matrix = np.where(union > 0, intersection / union, 0.0)
        
    return tanimoto_matrix, valid_smiles

if __name__ == "__main__":
    test_smiles = ["CCO", "CC", "CCCO", "c1ccccc1"]
    matrix, valid = compute_sparse_tanimoto(test_smiles)
    print(f"Successfully computed Tanimoto matrix of shape {matrix.shape} for {len(valid)} molecules.")
