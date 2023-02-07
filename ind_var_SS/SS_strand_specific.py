import pandas as pd

from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import ss_aim_output

from AttributeIDList import ss_aim_output_catch_up
from AttributeIDList import ss_aim_output_enrich
from AttributeIDList import ss_aim_output_school_trans
from AttributeIDList import ss_aim_output_gifted
from AttributeIDList import ss_aim_output_unclear
from AttributeIDList import ss_pupil_part_output
from AttributeIDList import ss_resid_comp_output
from AttributeIDList import ss_group_size_output
from AttributeIDList import ss_activity_focus_output
from AttributeIDList import ss_staff_kind_output
from AttributeIDList import ss_parent_invol
from AttributeIDList import ss_digit_tech
from AttributeIDList import ss_attendance

load_json()

# SUMMER SHCOOL

# get summer school aim data
ss_aim = get_data(ss_aim_output)
ss_aim_df = pd.DataFrame(ss_aim)
ss_aim_df = ss_aim_df.T
ss_aim_df.columns = ["ss_aim"]

# individual column extraction for summer school aim options
ss_aim_catch_up = get_data(ss_aim_output_catch_up)
ss_aim_catch_up_df = pd.DataFrame(ss_aim_catch_up)
ss_aim_catch_up_df = ss_aim_catch_up_df.T
ss_aim_catch_up_df.columns = ["ss_aim_catch_up"]

ss_aim_enrich = get_data(ss_aim_output_enrich)
ss_aim_enrich_df = pd.DataFrame(ss_aim_enrich)
ss_aim_enrich_df = ss_aim_enrich_df.T
ss_aim_enrich_df.columns = ["ss_aim_enrich"]

ss_aim_trans = get_data(ss_aim_output_school_trans)
ss_aim_trans_df = pd.DataFrame(ss_aim_trans)
ss_aim_trans_df = ss_aim_trans_df.T
ss_aim_trans_df.columns = ["ss_aim_trans"]

ss_aim_gifted = get_data(ss_aim_output_gifted)
ss_aim_gifted_df = pd.DataFrame(ss_aim_gifted)
ss_aim_gifted_df = ss_aim_gifted_df.T
ss_aim_gifted_df.columns = ["ss_aim_gifted"]

ss_aim_unclear = get_data(ss_aim_output_unclear)
ss_aim_unclear_df = pd.DataFrame(ss_aim_unclear)
ss_aim_unclear_df = ss_aim_unclear_df.T
ss_aim_unclear_df.columns = ["ss_aim_unclear"]

#^^ end of individual column extraction for summer school aim options^^

# get summer school pupil participation data
ss_pupil_part = get_data(ss_pupil_part_output)
ss_pupil_part_df = pd.DataFrame(ss_pupil_part)
ss_pupil_part_df = ss_pupil_part_df.T
ss_pupil_part_df.columns = ["ss_pupil_part"]

# get summer school residential component data
ss_resid_comp = get_data(ss_resid_comp_output)
ss_resid_comp_df = pd.DataFrame(ss_resid_comp)
ss_resid_comp_df = ss_resid_comp_df.T
ss_resid_comp_df.columns = ["ss_resid_comp"]

# get summer school group size data
ss_grp_size = get_data(ss_group_size_output)
ss_grp_size_df = pd.DataFrame(ss_grp_size)
ss_grp_size_df = ss_grp_size_df.T
ss_grp_size_df.columns = ["ss_grp_size"]

# get summer school activity focus data
ss_act_focus = get_data(ss_activity_focus_output)
ss_act_focus_df = pd.DataFrame(ss_act_focus)
ss_act_focus_df = ss_act_focus_df.T
ss_act_focus_df.columns = ["ss_act_focus"]

# get summer school activity focus data
ss_staff_kind = get_data(ss_staff_kind_output)
ss_staff_kind_df = pd.DataFrame(ss_staff_kind)
ss_staff_kind_df = ss_staff_kind_df.T
ss_staff_kind_df.columns = ["ss_staff_kind"]

# get summer school parental involvement data
ss_par_invol = get_data(ss_parent_invol)
ss_par_invol_df = pd.DataFrame(ss_par_invol)
ss_par_invol_df = ss_par_invol_df.T
ss_par_invol_df.columns = ["ss_par_invol"]

# get summer school digital tech data
ss_dig_tech = get_data(ss_digit_tech)
ss_dig_tech_df = pd.DataFrame(ss_dig_tech)
ss_dig_tech_df = ss_dig_tech_df.T
ss_dig_tech_df.columns = ["ss_dig_tech"]

# get summer school attendance data
ss_atten = get_data(ss_attendance)
ss_atten_df = pd.DataFrame(ss_atten)
ss_atten_df = ss_atten_df.T
ss_atten_df.columns = ["ss_attendance"]

SS_ss_df = pd.concat([
    ss_aim_df,

    ss_aim_catch_up_df,
    ss_aim_enrich_df,
    ss_aim_trans_df,
    ss_aim_gifted_df,
    ss_aim_unclear_df,
    ss_pupil_part_df,
    ss_resid_comp_df,
    ss_grp_size_df,
    ss_act_focus_df,
    ss_staff_kind_df,
    ss_par_invol_df,
    ss_dig_tech_df,
    ss_atten_df
], axis=1, sort=False)

# fill blanks with NA
SS_ss_df.fillna("NA", inplace=True)

# save to disk
""" SS_ss_df.to_csv("summer_school_ss.csv", index=False) """