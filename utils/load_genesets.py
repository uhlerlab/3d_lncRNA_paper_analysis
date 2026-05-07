import os
import pandas as pd
import json

def load_aging_genesets():
    # Load adhesome.org data
    components_df = pd.read_csv( "../data/genesets/adhesome/components.csv", header=0, index_col=None)
    adhesome_df = components_df[
        ["Official Symbol", "Protein name", "Functional Category", "FA"]
    ]
    adhesome_df.columns = ["hgnc_id", "protein", "functional_category", "FA"]
    
    # Function to load gene sets
    def load_geneset_from_json(file, entry="geneSymbols"):
        data = json.load(open(file))
        genes = data[list(data.keys())[0]][entry]
        return genes
    
    dir_ref = '../data/genesets/custom_aging/'
    # Load gene sets
    geneset_files = [
        dir_ref + "SAUL_SEN_MAYO.v2023.2.Hs.json",
        dir_ref + "REACTOME_CELLULAR_SENESCENCE.v2023.2.Hs.json",
        dir_ref
        + "REACTOME_SENESCENCE_ASSOCIATED_SECRETORY_PHENOTYPE_SASP.v2023.2.Hs.json",
        dir_ref + "KEGG_TGF_BETA_SIGNALING_PATHWAY.v2023.2.Hs.json",
        dir_ref + "HALLMARK_TGF_BETA_SIGNALING.v2023.2.Hs.json",
        dir_ref + "REACTOME_TGF_BETA.json",
        dir_ref + "HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION.v2023.2.Hs.json",
        dir_ref + "HALLMARK_TNFA_SIGNALING_VIA_NFKB.v2023.2.Hs.json",
        dir_ref + "REACTOME_TNF_SIGNALING.v2023.2.Hs.json",
    ]
    aging_genesets = {}
    for file in geneset_files:
        gs = os.path.split(file)[1]
        gs = gs[: gs.index(".")]
        aging_genesets[gs] = load_geneset_from_json(file)
    aging_genesets["ADHESOME"] = adhesome_df["hgnc_id"].unique().tolist()
    
    return aging_genesets