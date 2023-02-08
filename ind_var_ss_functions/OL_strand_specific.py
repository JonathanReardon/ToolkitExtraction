from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import ol_focus
from AttributeIDList import ol_target
from AttributeIDList import ol_imp_comp_type
from AttributeIDList import ol_activity_invol

import pandas as pd

load_json()

# ORAL LANGUAGE

# get focus data
ol_focus = get_data(ol_focus)
ol_focus_df = pd.DataFrame(ol_focus)
ol_focus_df = ol_focus_df.T
ol_focus_df.columns = ["ol_focus"]

# get target data
ol_target = get_data(ol_target)
ol_target_df = pd.DataFrame(ol_target)
ol_target_df = ol_target_df.T
ol_target_df.columns = ["ol_target"]

# get improved comprehension type (nested frop target option) data
ol_target_comp_type = get_data(ol_imp_comp_type)
ol_target_comp_type_df = pd.DataFrame(ol_target_comp_type)
ol_target_comp_type_df = ol_target_comp_type_df.T
ol_target_comp_type_df.columns = ["ol_target_comp_type"]

# get activity invol data
ol_act_invol = get_data(ol_activity_invol)
ol_act_invol_df = pd.DataFrame(ol_act_invol)
ol_act_invol_df = ol_act_invol_df.T
ol_act_invol_df.columns = ["ol_activity_invol"]

ol_ss_df = pd.concat([
    ol_focus_df,
    ol_target_df,
    ol_target_comp_type_df,
    ol_act_invol_df,
], axis=1, sort=False)

# fill blanks with NA
ol_ss_df.fillna("NA", inplace=True)

# save to disk
""" ol_ss_df.to_csv("oral_language_ss.csv", index=False) """