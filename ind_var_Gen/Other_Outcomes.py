from Main import load_json, get_data, comments, highlighted_text
from AttributeIDList import other_outcomes_output
from AttributeIDList import additional_outcomes_output
from AttributeIDList import other_participants_output
import pandas as pd

# load json file
load_json()

#################
# Other outcomes
#################

# get other outcomes data
other_outcomes = get_data(other_outcomes_output)
other_outcomes_df = pd.DataFrame(other_outcomes)
other_outcomes_df = other_outcomes_df.T
other_outcomes_df.columns = ["out_other_raw"]

# get other outcomes highlighted text
other_outcomes_HT = highlighted_text(other_outcomes_output)
other_outcomes_HT_df = pd.DataFrame(other_outcomes_HT)
other_outcomes_HT_df = other_outcomes_HT_df.T
other_outcomes_HT_df.columns = ["out_other_ht"]

# get other outcomes comments
other_outcomes_info = comments(other_outcomes_output)
other_outcomes_info_df = pd.DataFrame(other_outcomes_info)
other_outcomes_info_df = other_outcomes_info_df.T
other_outcomes_info_df.columns = ["out_other_info"]

######################
# Additional outcomes
######################

# get additional outcomes data
additional_outcomes = get_data(additional_outcomes_output)
additional_outcomes_df = pd.DataFrame(additional_outcomes)
additional_outcomes_df = additional_outcomes_df.T
additional_outcomes_df.columns = ["out_info_raw"]

# get additional outcomes highlighted text
additional_outcomes_ht = highlighted_text(additional_outcomes_output)
additional_outcomes_ht_df = pd.DataFrame(additional_outcomes_ht)
additional_outcomes_ht_df = additional_outcomes_ht_df.T
additional_outcomes_ht_df.columns = ["out_info_ht"]

# get additional outcomes comments
additional_outcomes_info = comments(additional_outcomes_output)
additional_outcomes_info_df = pd.DataFrame(additional_outcomes_info)
additional_outcomes_info_df = additional_outcomes_info_df.T
additional_outcomes_info_df.columns = ["out_info_info"]

#####################
# Other participants
#####################

# get other participants highlighted text
other_participants_ht = highlighted_text(other_participants_output)
other_participants_ht_df = pd.DataFrame(other_participants_ht)
other_participants_ht_df = other_participants_ht_df.T
other_participants_ht_df.columns = ["part_other_ht"]

# get other participants comments
other_participants_info = comments(other_participants_output)
other_participants_info_df = pd.DataFrame(other_participants_info)
other_participants_info_df = other_participants_info_df.T
other_participants_info_df.columns = ["part_other_info"]

# concatenate data frames
other_outcomes_df = pd.concat([
    other_outcomes_df, 
    other_outcomes_HT_df, 
    other_outcomes_info_df,
    additional_outcomes_df, 
    additional_outcomes_ht_df, 
    additional_outcomes_info_df,
    other_participants_ht_df, 
    other_participants_info_df
], axis=1, sort=False)

# fill blanks with NA
other_outcomes_df.fillna("NA", inplace=True)

# save to disk
""" other_outcomes_df.to_csv("other_outcomes.csv", index=False) """