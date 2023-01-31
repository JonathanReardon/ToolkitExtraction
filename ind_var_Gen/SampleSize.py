from random import sample
from Main import load_json, comments, highlighted_text
from AttributeIDList import sample_size_output
import pandas as pd

# load json file
load_json()

# get sample size comments
sample_size_Comments = comments(sample_size_output)
sample_size_Comments_df = pd.DataFrame(sample_size_Comments)
sample_size_Comments_df = sample_size_Comments_df.T
sample_size_Comments_df.columns = ["sample_analysed_info"]

# get sample size highlighted text
sample_size_HT = highlighted_text(sample_size_output)
sample_size_HT_df = pd.DataFrame(sample_size_HT)
sample_size_HT_df = sample_size_HT_df.T
sample_size_HT_df.columns = ["sample_analysed_ht"]

# concatenate dataframes
sample_size_df = pd.concat([
    sample_size_Comments_df,
    sample_size_HT_df
], axis=1, sort=False)

# remove problematic text
sample_size_df.replace('\r', ' ', regex=True, inplace=True)
sample_size_df.replace('\n', ' ', regex=True, inplace=True)

# fill blanks with NA
sample_size_df.fillna("NA", inplace=True)

# save to disk
sample_size_df.to_csv("sample_size.csv", index=False)

""" print(sample_size_df) """