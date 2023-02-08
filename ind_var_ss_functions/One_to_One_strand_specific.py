from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import comparisons_available
import pandas as pd

load_json()

# ONE TO ONE

# get one-to-one comparisons data
comp_avail = get_data(comparisons_available)
comp_avail_df = pd.DataFrame(comp_avail)
comp_avail_df = comp_avail_df.T
comp_avail_df.columns = ["1_1_comparisons_Available"]

# Get one-to-one comparisons highlighted text
comp_avail_HT = highlighted_text(comparisons_available)
comp_avail_HT_df = pd.DataFrame(comp_avail_HT)
comp_avail_HT_df = comp_avail_HT_df.T
comp_avail_HT_df.columns = ["1_1_comparisons_Available_SS_ht"]

# Get one-to-one comparisons user comments
comp_avail_Comments = comments(comparisons_available)
comp_avail_Comments_df = pd.DataFrame(comp_avail_Comments)
comp_avail_Comments_df = comp_avail_Comments_df.T
comp_avail_Comments_df.columns = ["1_1_comparisons_Available_SS_info"]

# concatenate data frames
one_to_one_ss_df = pd.concat([
    comp_avail_df,
], axis=1, sort=False)

# fill blanks with NA
one_to_one_ss_df.fillna("NA", inplace=True)

# remove problematic text from outputs
one_to_one_ss_df.replace('\r', ' ', regex=True, inplace=True)
one_to_one_ss_df.replace('\n', ' ', regex=True, inplace=True)
one_to_one_ss_df.replace(':', ' ',  regex=True, inplace=True)
one_to_one_ss_df.replace(';', ' ',  regex=True, inplace=True)

# save to disk
# one_to_one_ss_df.to_csv("one_to_one_ss_df.csv", index=False)