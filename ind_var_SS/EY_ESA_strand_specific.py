from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import ey_esa_prev_starting_age
from AttributeIDList import ey_esa_new_starting_age
from AttributeIDList import ey_esa_addit_time_f_pt
from AttributeIDList import ey_esa_addit_time_struct
from AttributeIDList import ey_esa_earlier_child_addit_time
from AttributeIDList import ey_esa_earlier_child_addit_time_other
from AttributeIDList import ey_esa_setting_type

import pandas as pd
import os
import sys

load_json()

""" data_files = sys.argv[1] """

# get prev starting age data
prev_start_age = get_data(ey_esa_prev_starting_age)
prev_start_age_df = pd.DataFrame(prev_start_age)
prev_start_age_df = prev_start_age_df.T
prev_start_age_df.columns = ["prev_start_age"]

# get new starting age data
new_start_age = get_data(ey_esa_new_starting_age)
new_start_age_df = pd.DataFrame(new_start_age)
new_start_age_df = new_start_age_df.T
new_start_age_df.columns = ["new_start_age"]

# get additional tikme (f/pt) data
addit_time_f_pt = get_data(ey_esa_addit_time_f_pt)
addit_time_f_pt_df = pd.DataFrame(addit_time_f_pt)
addit_time_f_pt_df = addit_time_f_pt_df.T
addit_time_f_pt_df.columns = ["addit_time_f_pt"]

# get additional time structure data
add_time_struct = get_data(ey_esa_addit_time_struct)
add_time_struct_df = pd.DataFrame(add_time_struct)
add_time_struct_df = add_time_struct_df.T
add_time_struct_df.columns = ["addit_time_struct"]

# get earlier child additional time data
earl_child_addit_time = get_data(ey_esa_earlier_child_addit_time)
earl_child_addit_time_df = pd.DataFrame(earl_child_addit_time)
earl_child_addit_time_df = earl_child_addit_time_df.T
earl_child_addit_time_df.columns = ["early_child_addit_time"]





# get earlier child additional time data
earl_child_addit_time_info = comments(ey_esa_earlier_child_addit_time_other)
earl_child_addit_time_info_df = pd.DataFrame(earl_child_addit_time_info)
earl_child_addit_time_info_df = earl_child_addit_time_info_df.T
earl_child_addit_time_info_df.columns = ["early_child_addit_time_info"]



# get setting type data
setting_type = get_data(ey_esa_setting_type)
setting_type_df = pd.DataFrame(setting_type)
setting_type_df = setting_type_df.T
setting_type_df.columns = ["setting_type"]

ey_esa_df = pd.concat([
    prev_start_age_df,
    new_start_age_df,
    addit_time_f_pt_df,
    add_time_struct_df,
    earl_child_addit_time_df,
    earl_child_addit_time_info_df,
    setting_type_df,
], axis=1, sort=False)

# fill blanks with NA
ey_esa_df.fillna("NA", inplace=True)

# save to disk
#ey_esa_df.to_csv("ey_pbl_ss_df.csv", index=False)