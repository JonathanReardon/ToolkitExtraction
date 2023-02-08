from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import ml_theor_output
from AttributeIDList import ml_age_group_output
from AttributeIDList import ml_ability_group_output
from AttributeIDList import ml_if_attain_what_grouping_type_output
from AttributeIDList import ml_goal_level
from AttributeIDList import ml_assess_detail
from AttributeIDList import ml_fb_detail_prov
from AttributeIDList import ml_mastery_level

import pandas as pd

load_json()

# MASTERY LEARNING

# get ml theorists data
ml_theor = get_data(ml_theor_output)
ml_theor_df = pd.DataFrame(ml_theor)
ml_theor_df = ml_theor_df.T
ml_theor_df.columns = ["ml_theor"]

# get ml age group data
ml_age_grp = get_data(ml_age_group_output)
ml_age_grp_df = pd.DataFrame(ml_age_grp)
ml_age_grp_df = ml_age_grp_df.T
ml_age_grp_df.columns = ["ml_age_grp"]

# get ml ability group data
ml_ability_grp = get_data(ml_ability_group_output)
ml_ability_grp_df = pd.DataFrame(ml_ability_grp)
ml_ability_grp_df = ml_ability_grp_df.T
ml_ability_grp_df.columns = ["ml_ability_grp"]

# get ml if attainment grouping, what group type data
ml_attain_group_type = get_data(ml_if_attain_what_grouping_type_output)
ml_attain_group_type_df = pd.DataFrame(ml_attain_group_type)
ml_attain_group_type_df = ml_attain_group_type_df.T
ml_attain_group_type_df.columns = ["ml_attain_grouping"]

# get ml goal level type data
ml_goal_level = get_data(ml_goal_level)
ml_goal_level_df = pd.DataFrame(ml_goal_level)
ml_goal_level_df = ml_goal_level_df.T
ml_goal_level_df.columns = ["ml_goal_level"]

# get ml assess detail data
ml_asess_det = get_data(ml_assess_detail)
ml_asess_det_df = pd.DataFrame(ml_asess_det)
ml_asess_det_df = ml_asess_det_df.T
ml_asess_det_df.columns = ["ml_assess_det"]

# get ml feedback detail provided data
ml_fb_det_prov = get_data(ml_fb_detail_prov)
ml_fb_det_prov_df = pd.DataFrame(ml_fb_det_prov)
ml_fb_det_prov_df = ml_fb_det_prov_df.T
ml_fb_det_prov_df.columns = ["ml_fb_detail_prov"]

# get ml mastery level data
ml_mast_lev = get_data(ml_mastery_level)
ml_mast_lev_df = pd.DataFrame(ml_mast_lev)
ml_mast_lev_df = ml_mast_lev_df.T
ml_mast_lev_df.columns = ["ml_mastery_lev"]

ml_ss_df = pd.concat([
    ml_theor_df,
    ml_age_grp_df,
    ml_ability_grp_df,
    ml_attain_group_type_df,
    ml_goal_level_df,
    ml_asess_det_df,
    ml_fb_det_prov_df,
    ml_mast_lev_df
], axis=1, sort=False)

# fill blanks with NA
ml_ss_df.fillna("NA", inplace=True)

# save to disk
""" ml_ss_df.to_csv("mastery_learning_ss.csv", index=False) """