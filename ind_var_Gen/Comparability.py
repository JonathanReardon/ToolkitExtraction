from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import comparability_output
import pandas as pd

load_json()

# get comparability data
comparability = get_data(comparability_output)
comparability_df = pd.DataFrame(comparability)
comparability_df = comparability_df.T
comparability_df.columns = ["comp_anal_raw"]

# Get Baseline Differences highlighted text
comparability_HT = highlighted_text(comparability_output)
comparability_HT_df = pd.DataFrame(comparability_HT)
comparability_HT_df = comparability_HT_df.T
comparability_HT_df.columns = ["comp_anal_ht"]

# Get Educational Setting user comments
comparability_Comments = comments(comparability_output)
comparability_Comments_df = pd.DataFrame(comparability_Comments)
comparability_Comments_df = comparability_Comments_df.T
comparability_Comments_df.columns = ["comp_anal_info"]

# concatenate data frames
comparability_df = pd.concat([
    comparability_df, 
    comparability_HT_df, 
    comparability_Comments_df
], axis=1, sort=False)

# fill blanks with NA
comparability_df.fillna("NA", inplace=True)

# save to disk
# comparability_df.to_csv("comparability.csv", index=False)
