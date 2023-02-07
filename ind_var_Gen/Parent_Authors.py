from Main import load_json, get_metadata
import pandas as pd

load_json()

# get abstract data
parentauthors = get_metadata("ParentAuthors")
parentauthors_df = pd.DataFrame(parentauthors)
parentauthors_df.columns = ["Parent_Authors"]
parentauthors_df.fillna("NA", inplace=True)

# save to disk
#parentauthors_df.to_csv("Parent_Authors.csv", index=False)
