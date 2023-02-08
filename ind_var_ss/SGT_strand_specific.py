import pandas as pd

from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import group_size_output
from AttributeIDList import group_composition_output
from AttributeIDList import group_teaching_lead_output

load_json()

# get group size data
group_size = get_data(group_size_output)
group_size_df = pd.DataFrame(group_size)
group_size_df = group_size_df.T
group_size_df.columns = ["sgt_group_size"]

# Get group size highlighted text
group_size_HT = highlighted_text(group_size_output)
group_size_HT_df = pd.DataFrame(group_size_HT)
group_size_HT_df = group_size_HT_df.T
group_size_HT_df.columns = ["sgt_group_size_ht"]

# Get group size user comments
group_size_Comments = comments(group_size_output)
group_size_Comments_df = pd.DataFrame(group_size_Comments)
group_size_Comments_df = group_size_Comments_df.T
group_size_Comments_df.columns = ["sgt_group_size_info"]

# get group composition data
group_composition = get_data(group_composition_output)
group_composition_df = pd.DataFrame(group_composition)
group_composition_df = group_composition_df.T
group_composition_df.columns = ["sgt_group_composition"]

# Get group composition highlighted text
group_composition_HT = highlighted_text(group_composition_output)
group_composition_HT_df = pd.DataFrame(group_composition_HT)
group_composition_HT_df = group_composition_HT_df.T
group_composition_HT_df.columns = ["sgt_group_composition_ht"]

# Get group composition user comments
group_composition_Comments = comments(group_composition_output)
group_composition_Comments_df = pd.DataFrame(group_composition_Comments)
group_composition_Comments_df = group_composition_Comments_df.T
group_composition_Comments_df.columns = ["sgt_group_composition_info"]

# get group composition data
group_lead = get_data(group_teaching_lead_output)
group_lead_df = pd.DataFrame(group_lead)
group_lead_df = group_lead_df.T
group_lead_df.columns = ["sgt_group_lead"]

# Get group composition highlighted text
group_lead_HT = highlighted_text(group_teaching_lead_output)
group_lead_HT_df = pd.DataFrame(group_lead_HT)
group_lead_HT_df = group_lead_HT_df.T
group_lead_HT_df.columns = ["sgt_group_lead_ht"]

# Get group composition user comments
group_lead_Comments = comments(group_teaching_lead_output)
group_lead_Comments_df = pd.DataFrame(group_lead_Comments)
group_lead_Comments_df = group_lead_Comments_df.T
group_lead_Comments_df.columns = ["sgt_group_lead_info"]

sgt_ss_df = pd.concat([
    group_size_df,
    group_composition_df,
    group_lead_df,
], axis=1, sort=False)

# fill blanks with NA
sgt_ss_df.fillna("NA", inplace=True)

# save to disk
# sgt_ss_df.to_csv("small_group_tuition_ss_df.csv", index=False)