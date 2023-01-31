from Main import load_json, get_outcome_lvl2
from AttributeIDList import out_out_type_CEDIL
import pandas as pd

# load json file
load_json()

# get outcome type data
outcome_type = get_outcome_lvl2(out_out_type_CEDIL)
outcometype_df = pd.DataFrame(outcome_type)

# name each column (number depends on outcome number)
outcometype_df.columns = [
    "out_type_"+'{}'.format(column+1) for column in outcometype_df.columns]

# fill blanks with NA
outcometype_df.fillna("NA", inplace=True)

# save to disk
""" outcometype_df.to_csv("outcometype.csv", index=False) """

print(outcometype_df)
