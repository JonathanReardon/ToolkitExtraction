import pandas as pd

from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import ta_description_output
from AttributeIDList import ta_role_output
from AttributeIDList import ta_group_size_output

load_json()

# TEACHING ASSISTANTS DESCRIPTION

# get teaching assistants description data
ta_desc = get_data(ta_description_output)
ta_desc_df = pd.DataFrame(ta_desc)
ta_desc_df = ta_desc_df.T
ta_desc_df.columns = ["ta_desc"]

# Get teaching assistants description highlighted text
ta_desc_HT = highlighted_text(ta_description_output)
ta_desc_HT_df = pd.DataFrame(ta_desc_HT)
ta_desc_HT_df = ta_desc_HT_df.T
ta_desc_HT_df.columns = ["ta_desc_ht"]

# Get teaching assistants description user comments
ta_desc_Comments = comments(ta_description_output)
ta_desc_Comments_df = pd.DataFrame(ta_desc_Comments)
ta_desc_Comments_df = ta_desc_Comments_df.T
ta_desc_Comments_df.columns = ["ta_desc_info"]

# TEACHING ASSISTANTS ROLE

# get teaching assistants description data
ta_role = get_data(ta_role_output)
ta_role_df = pd.DataFrame(ta_role)
ta_role_df = ta_role_df.T
ta_role_df.columns = ["ta_role"]

# Get teaching assistants description highlighted text
ta_role_HT = highlighted_text(ta_role_output)
ta_role_HT_df = pd.DataFrame(ta_role_HT)
ta_role_HT_df = ta_role_HT_df.T
ta_role_HT_df.columns = ["ta_role_ht"]

# Get teaching assistants description user comments
ta_role_Comments = comments(ta_role_output)
ta_desc_Comments_df = pd.DataFrame(ta_role_Comments)
ta_desc_Comments_df = ta_desc_Comments_df.T
ta_desc_Comments_df.columns = ["ta_role_info"]

# TEACHING GROUP SIZE

# get teaching assistants group size data
ta_group_size = get_data(ta_group_size_output)
ta_group_size_df = pd.DataFrame(ta_group_size)
ta_group_size_df = ta_group_size_df.T
ta_group_size_df.columns = ["ta_group_size"]

# get teaching assistants group size highlighted text
ta_group_size_HT = highlighted_text(ta_group_size_output)
ta_group_size_HT_df = pd.DataFrame(ta_group_size_HT)
ta_group_size_HT_df = ta_group_size_HT_df.T
ta_group_size_HT_df.columns = ["ta_group_size_ht"]

# get teaching assistants group size user comments
ta_group_size_Comments = comments(ta_group_size_output)
ta_group_size_Comments_df = pd.DataFrame(ta_group_size_Comments)
ta_group_size_Comments_df = ta_group_size_Comments_df.T
ta_group_size_Comments_df.columns = ["ta_group_size_info"]

# concatenate data frames
ta_ss_df = pd.concat([
    ta_desc_df,
    ta_role_df,
    ta_group_size_df,

], axis=1, sort=False)

# remove problematic text from outputs
ta_ss_df.replace('\r', ' ', regex=True, inplace=True)
ta_ss_df.replace('\n', ' ', regex=True, inplace=True)
ta_ss_df.replace(':', ' ',  regex=True, inplace=True)
ta_ss_df.replace(';', ' ',  regex=True, inplace=True)

""" ta_ss_df.to_csv("ta_ss.csv", index=False, header=True) """
