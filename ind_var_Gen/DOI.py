from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
doi = get_metadata("DOI")
doi_df = pd.DataFrame(doi)
doi_df.columns = ["DOI"]
doi_df.fillna("NA", inplace=True)

# save to disk
#doi_df.to_csv("doi.csv", index=False)
