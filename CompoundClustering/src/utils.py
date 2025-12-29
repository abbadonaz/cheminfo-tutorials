from rdkit import DataStructs

def tanimoto_distance_matrix(fps):
    """Compute the Tanimoto distance matrix for a list of RDKit fingerprints."""
    n = len(fps)
    dists = []
    for i in range(1, n):
        sims = DataStructs.BulkTanimotoSimilarity(fps[i], fps[:i])
        dists.extend([1 - x for x in sims])
    return dists