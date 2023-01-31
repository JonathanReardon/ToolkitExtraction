from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import hw_dur_info_output
from AttributeIDList import hw_total_time
from AttributeIDList import hw_who_involved_output
from AttributeIDList import hw_if_parents_describe_role_output
from AttributeIDList import hw_completed_where_output
from AttributeIDList import hw_mark_method_info_output

import pandas as pd

load_json()

# HOMEWORK

# get hw duration data
hw_dur = get_data(hw_dur_info_output)
hw_dur_df = pd.DataFrame(hw_dur)
hw_dur_df = hw_dur_df.T
hw_dur_df.columns = ["hw_dur"]

# get hw duration information data
hw_dur_info = comments(hw_dur_info_output)
hw_dur_info_df = pd.DataFrame(hw_dur_info)
hw_dur_info_df = hw_dur_info_df.T
hw_dur_info_df.columns = ["hw_dur_info"]

# get hw duration total time data
hw_dur_tot_time = comments(hw_total_time)
hw_dur_tot_time_df = pd.DataFrame(hw_dur_tot_time)
hw_dur_tot_time_df = hw_dur_tot_time_df.T
hw_dur_tot_time_df.columns = ["hw_dur_tot_time"]

# get hw who was involved data
hw_who_invol = get_data(hw_who_involved_output)
hw_who_invol_df = pd.DataFrame(hw_who_invol)
hw_who_invol_df = hw_who_invol_df.T
hw_who_invol_df.columns = ["hw_who_involved"]

# get hw if parentes involved, describe role data
hw_par_role = get_data(hw_if_parents_describe_role_output)
hw_par_role_df = pd.DataFrame(hw_par_role)
hw_par_role_df = hw_par_role_df.T
hw_par_role_df.columns = ["hw_par_role"]

# get hw completed where data
hw_where = get_data(hw_completed_where_output)
hw_where_df = pd.DataFrame(hw_where)
hw_where_df = hw_where_df.T
hw_where_df.columns = ["hw_where"]

# get hw marking method data
hw_mark_method = get_data(hw_mark_method_info_output)
hw_mark_method_df = pd.DataFrame(hw_mark_method)
hw_mark_method_df = hw_mark_method_df.T
hw_mark_method_df.columns = ["hw_mark_method_info"]

hw_ss_df = pd.concat([
    hw_dur_df,
    hw_dur_info_df,
    hw_dur_tot_time_df,
    hw_who_invol_df,
    hw_par_role_df,
    hw_where_df,
    hw_mark_method_df
], axis=1, sort=False)

# fill blanks with NA
hw_ss_df.fillna("NA", inplace=True)

# save to disk
hw_ss_df.to_csv("homework_ss.csv", index=False)

print(hw_ss_df[0:50])