from rdkit import Chem
from rdkit.Chem.MolStandardize import rdMolStandardize

def standardize_smiles(smiles):
    """Standardize a SMILES string and return an RDKit Mol (or None on failure).

    Steps: cleanup, fragment parent, uncharge, and tautomer canonicalization.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    clean = rdMolStandardize.Cleanup(mol)
    parent = rdMolStandardize.FragmentParent(clean)
    uncharger = rdMolStandardize.Uncharger()
    uncharged = uncharger.uncharge(parent)
    te = rdMolStandardize.TautomerEnumerator()
    taut = te.Canonicalize(uncharged)
    return taut