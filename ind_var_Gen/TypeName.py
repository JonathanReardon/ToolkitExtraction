from Main import load_json, get_metadata
import pandas as pd

load_json()

# get author data
typename = get_metadata("TypeName")
typename_df = pd.DataFrame(typename)
typename_df.columns = ["typename"]
typename_df.fillna("NA", inplace=True)

# save to disk
#typename_df.to_csv("typename.csv", index=False)

""" print(typename_df) """
