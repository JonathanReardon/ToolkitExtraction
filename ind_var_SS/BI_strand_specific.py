from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import bi_target_group_output, bi_intervention_approach_output, bi_intervention_components_output
from AttributeIDList import ind_comp_counselling, ind_comp_monitoring, ind_comp_self_management
from AttributeIDList import ind_comp_role_play, ind_comp_parental_involv, ind_comp_academic_focus
from AttributeIDList import ind_comp_digit_tech
import pandas as pd

load_json()

# BEHAVIOR INTERVENTION TARGET GROUP

# get target group data
bi_target_group = get_data(bi_target_group_output)
bi_target_group_df = pd.DataFrame(bi_target_group)
bi_target_group_df = bi_target_group_df.T
bi_target_group_df.columns = ["bi_targ_group"]

# get target group highlighted text
bi_target_group_HT = highlighted_text(bi_intervention_approach_output)
bi_target_group_HT_df = pd.DataFrame(bi_target_group_HT)
bi_target_group_HT_df = bi_target_group_HT_df.T
bi_target_group_HT_df.columns = ["bi_targ_group_ht"]

# get target group user comments
bi_target_group_Comments = comments(bi_intervention_components_output)
bi_target_group_Comments_df = pd.DataFrame(bi_target_group_Comments)
bi_target_group_Comments_df = bi_target_group_Comments_df.T
bi_target_group_Comments_df.columns = ["bi_targ_group_info"]

# BEHAVIOR INTERVENTION APPROACH

# get intervention approach data
bi_int_approach = get_data(bi_intervention_approach_output)
bi_int_approach_df = pd.DataFrame(bi_int_approach)
bi_int_approach_df = bi_int_approach_df.T
bi_int_approach_df.columns = ["bi_int_approach"]

# get intervention approach highlighted text
bi_int_approach_HT = highlighted_text(bi_intervention_approach_output)
bi_int_approach_HT_df = pd.DataFrame(bi_int_approach_HT)
bi_int_approach_HT_df = bi_int_approach_HT_df.T
bi_int_approach_HT_df.columns = ["bi_int_approach_ht"]

# get intervention approach user comments
bi_int_approach_Comments = comments(bi_intervention_approach_output)
bi_int_approach_Comments_df = pd.DataFrame(bi_int_approach_Comments)
bi_int_approach_Comments_df = bi_int_approach_Comments_df.T
bi_int_approach_Comments_df.columns = ["bi_int_approach_info"]

# BEHAVIOR INTERVENTION COMPONENTS

# get intervention components data
bi_int_components = get_data(bi_intervention_components_output)
bi_int_components_df = pd.DataFrame(bi_int_components)
bi_int_components_df = bi_int_components_df.T
bi_int_components_df.columns = ["bi_int_components"]

# get intervention components highlighted text
bi_int_components_HT = highlighted_text(bi_intervention_components_output)
bi_int_components_HT_df = pd.DataFrame(bi_int_components_HT)
bi_int_components_HT_df = bi_int_components_HT_df.T
bi_int_components_HT_df.columns = ["bi_int_components_ht"]

# get intervention components user comments
bi_int_components_Comments = comments(bi_intervention_components_output)
bi_int_components_Comments_df = pd.DataFrame(bi_int_components_Comments)
bi_int_components_Comments_df = bi_int_components_Comments_df.T
bi_int_components_Comments_df.columns = ["bi_int_components_info"]

# BEHAVIOR INTERVENTION COMPONENTS SPLIT

# get intervention components counselling data
bi_int_comp_counselling = get_data(ind_comp_counselling)
bi_int_comp_counselling_df = pd.DataFrame(bi_int_comp_counselling)
bi_int_comp_counselling_df = bi_int_comp_counselling_df.T
bi_int_comp_counselling_df.columns = ["bi_components_counselling"]

# get intervention components monitoring data
bi_int_comp_monitoring = get_data(ind_comp_monitoring)
bi_int_comp_monitoring_df = pd.DataFrame(bi_int_comp_monitoring)
bi_int_comp_monitoring_df = bi_int_comp_monitoring_df.T
bi_int_comp_monitoring_df.columns = ["bi_components_monitoring"]

# get intervention components self-manage data
bi_int_comp_self_man = get_data(ind_comp_self_management)
bi_int_comp_self_man_df = pd.DataFrame(bi_int_comp_self_man)
bi_int_comp_self_man_df = bi_int_comp_self_man_df.T
bi_int_comp_self_man_df.columns = ["bi_components_self"]

# get intervention components role-play data
bi_int_comp_role_play = get_data(ind_comp_role_play)
bi_int_comp_role_play_df = pd.DataFrame(bi_int_comp_role_play)
bi_int_comp_role_play_df = bi_int_comp_role_play_df.T
bi_int_comp_role_play_df.columns = ["bi_components_roleplay"]

# get intervention components parent-involv data
bi_int_comp_par_invol = get_data(ind_comp_parental_involv)
bi_int_comp_par_invol_df = pd.DataFrame(bi_int_comp_par_invol)
bi_int_comp_par_invol_df = bi_int_comp_par_invol_df.T
bi_int_comp_par_invol_df.columns = ["bi_components_parentalinv"]

# get intervention components ac-focus data
bi_int_comp_ac_focus = get_data(ind_comp_academic_focus)
bi_int_comp_ac_focus_df = pd.DataFrame(bi_int_comp_ac_focus)
bi_int_comp_ac_focus_df = bi_int_comp_ac_focus_df.T
bi_int_comp_ac_focus_df.columns = ["bi_academic"]

# get intervention components dig-tech data
bi_int_comp_dig_tech = get_data(ind_comp_digit_tech)
bi_int_comp_dig_tech_df = pd.DataFrame(bi_int_comp_dig_tech)
bi_int_comp_dig_tech_df = bi_int_comp_dig_tech_df.T
bi_int_comp_dig_tech_df.columns = ["bi_components_digital"]


bi_ss_df = pd.concat([
    bi_target_group_df,
    bi_int_approach_df,
    bi_int_components_df,

    bi_int_comp_counselling_df,
    bi_int_comp_monitoring_df,
    bi_int_comp_self_man_df,
    bi_int_comp_role_play_df,
    bi_int_comp_par_invol_df,
    bi_int_comp_ac_focus_df,
    bi_int_comp_dig_tech_df
], axis=1, sort=False)

# fill blanks with NA
bi_ss_df.fillna("NA", inplace=True)

# save to disk
bi_ss_df.to_csv("behavior_intervention_ss.csv", index=False)

print(bi_ss_df[0:50])