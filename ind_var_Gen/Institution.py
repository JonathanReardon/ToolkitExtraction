from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
institution = get_metadata("Institution")
institution_df = pd.DataFrame(institution)
institution_df.columns = ["Institution"]
institution_df.fillna("NA", inplace=True)

# save to disk
#institution_df.to_csv("Institution.csv", index=False)

""" print(institution_df) """
