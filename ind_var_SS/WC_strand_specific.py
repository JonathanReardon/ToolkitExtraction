from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import wcg_dir_grouping_change_output
from AttributeIDList import wcg_curr_taught_attain_grp_output
from AttributeIDList import wcg_pupils_affected_by_wcg_output
from AttributeIDList import wcg_attain_grouping_level
from AttributeIDList import wcg_follow_same_curr
from AttributeIDList import wcg_approach_name
from AttributeIDList import wcg_pupil_assignment

import pandas as pd

load_json()

# WITHIN CLASS GROUPING

# get grouping direction data
wc_grp_dir = get_data(wcg_dir_grouping_change_output)
wc_grp_dir_df = pd.DataFrame(wc_grp_dir)
wc_grp_dir_df = wc_grp_dir_df.T
wc_grp_dir_df.columns = ["wc_grp_dir"]

# get curriculum taught in attainment groups data
wc_curr_taught_att_grp = get_data(wcg_curr_taught_attain_grp_output)
wc_curr_taught_att_grp_df = pd.DataFrame(wc_curr_taught_att_grp)
wc_curr_taught_att_grp_df = wc_curr_taught_att_grp_df.T
wc_curr_taught_att_grp_df.columns = ["wc_curr_taught_att_grp"]

# get pupils affected by wcg data
wc_pup_affected = get_data(wcg_pupils_affected_by_wcg_output)
wc_pup_affected_df = pd.DataFrame(wc_pup_affected)
wc_pup_affected_df = wc_pup_affected_df.T
wc_pup_affected_df.columns = ["wc_pup_affected"]

# get attainment grouping levels data
wc_att_grping_levels = get_data(wcg_attain_grouping_level)
wc_att_grping_levels_df = pd.DataFrame(wc_att_grping_levels)
wc_att_grping_levels_df = wc_att_grping_levels_df.T
wc_att_grping_levels_df.columns = ["wc_attn_grouping_levels"]

# get follow same curriculum data
wc_follow_same_curr = get_data(wcg_follow_same_curr)
wc_follow_same_curr_df = pd.DataFrame(wc_follow_same_curr)
wc_follow_same_curr_df = wc_follow_same_curr_df.T
wc_follow_same_curr_df.columns = ["wc_follow_same_curr"]

# get approach name data
wc_approach_name = get_data(wcg_approach_name)
wc_approach_name_df = pd.DataFrame(wc_approach_name)
wc_approach_name_df = wc_approach_name_df.T
wc_approach_name_df.columns = ["wc_approach_name"]

# get pupil assignment data
wc_pup_assign = get_data(wcg_pupil_assignment)
wc_pup_assign_df = pd.DataFrame(wc_pup_assign)
wc_pup_assign_df = wc_pup_assign_df.T
wc_pup_assign_df.columns = ["wc_pup_assign"]

# concatenate data frames
wc_ss_df = pd.concat([
    wc_grp_dir_df,
    wc_curr_taught_att_grp_df,
    wc_pup_affected_df,
    wc_att_grping_levels_df,
    wc_follow_same_curr_df,
    wc_approach_name_df,
    wc_pup_assign_df,
], axis=1, sort=False)

# remove problematic text from outputs
wc_ss_df.replace('\r', ' ', regex=True, inplace=True)
wc_ss_df.replace('\n', ' ', regex=True, inplace=True)
wc_ss_df.replace(':', ' ',  regex=True, inplace=True)
wc_ss_df.replace(';', ' ',  regex=True, inplace=True)

wc_ss_df.to_csv("within_class_grouping_ss.csv", index=False, header=True)

print(wc_ss_df[0:50])