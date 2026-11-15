"""
Defensive SMARTS Substructure Filtering & Sanitization Script
Author: Anil Kumar (IIT Bombay B.Tech)
"""

from rdkit import Chem
from rdkit import RDLogger

# Suppress verbose C++ stderr warnings in batch pipelines
RDLogger.DisableLog('rdApp.*')

def filter_molecules_by_smarts(smiles_list, smarts_query):
    """
    Parses SMILES, sanitizes molecules, and filters using a compiled SMARTS query.
    """
    query = Chem.MolFromSmarts(smarts_query)
    if query is None:
        raise ValueError(f"Invalid SMARTS query: {smarts_query}")
        
    matched_molecules = []
    
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            continue  # Strict defensive check against structural/valency hallucinations
            
        if mol.HasSubstructMatch(query):
            matched_molecules.append(Chem.MolToSmiles(mol))
            
    return matched_molecules

if __name__ == "__main__":
    library = ["CC(=O)C", "CC(=O)H", "c1ccccc1", "CCO"]
    # Target exact aldehyde query using explicit hydrogen count [C;H1]
    aldehyde_smarts = "[C;H1](=O)[#6]"
    results = filter_molecules_by_smarts(library, aldehyde_smarts)
    print(f"Filtered aldehydes: {results}")
