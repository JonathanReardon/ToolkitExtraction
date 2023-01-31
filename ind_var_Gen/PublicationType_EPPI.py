from Main import load_json, get_metadata
import pandas as pd

# load json file
load_json()

# get pubtype eppi data
pubtype_eppi = get_metadata("TypeName")
pubtype_eppi_df = pd.DataFrame(pubtype_eppi)
pubtype_eppi_df.columns = ["pub_eppi"]

# fill blanks with NA
pubtype_eppi_df.fillna("NA", inplace=True)

# save to risk
""" pubtype_eppi_df.to_csv("pubtype_eppi.csv", index=False) """

""" print(pubtype_eppi_df) """
