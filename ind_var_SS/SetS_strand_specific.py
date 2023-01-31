from Main import load_json, get_data, highlighted_text, comments

from AttributeIDList import sets_dir_grouping_change
from AttributeIDList import sets_dir_grouping_type_regroup
from AttributeIDList import sets_curr_taught_in_regroup
from AttributeIDList import sets_dir_grouping_stream
from AttributeIDList import sets_dir_grouping_gifted
from AttributeIDList import sets_school_groupings
from AttributeIDList import sets_attain_grouping_level
from AttributeIDList import sets_follow_same_curr
from AttributeIDList import sets_approach_name
from AttributeIDList import sets_pupil_assignment

import pandas as pd

load_json()

# SETTING OR STREAMING

# get grouping change data
sets_dir_grp_change = get_data(sets_dir_grouping_change)
sets_dir_grp_change_df = pd.DataFrame(sets_dir_grp_change)
sets_dir_grp_change_df = sets_dir_grp_change_df.T
sets_dir_grp_change_df.columns = ["sets_dir_grp_change"]

""" # get grouping type within attainment data
sets_grp_type_within_attain = get_data(sets_dir_grouping_type_within_attain)
sets_grp_type_within_attain_df = pd.DataFrame(sets_grp_type_within_attain)
sets_grp_type_within_attain_df = sets_grp_type_within_attain_df.T
sets_grp_type_within_attain_df.columns = ["sets_grp_type_within_attain"] """

""" # nested within grp type within attain ^
# get curriculum taight within attainment data
sets_curr_taught_attain = get_data(sets_curr_taught_in_attain_grp)
sets_curr_taught_attain_df = pd.DataFrame(sets_curr_taught_attain)
sets_curr_taught_attain_df = sets_curr_taught_attain_df.T
sets_curr_taught_attain_df.columns = ["sets_curr_taught_in_attain"] """

# get grouping type regroup data
sets_dir_grp_type_regroup = get_data(sets_dir_grouping_type_regroup)
sets_dir_grp_type_regroup_df = pd.DataFrame(sets_dir_grp_type_regroup)
sets_dir_grp_type_regroup_df = sets_dir_grp_type_regroup_df.T
sets_dir_grp_type_regroup_df.columns = ["sets_dir_grp_type_regroup"]

# nested within grp type regroup ^
# get curr taught in regroup data
sets_curr_taught_regroup = get_data(sets_curr_taught_in_regroup)
sets_curr_taught_regroup_df = pd.DataFrame(sets_curr_taught_regroup)
sets_curr_taught_regroup_df = sets_curr_taught_regroup_df.T
sets_curr_taught_regroup_df.columns = ["sets_curr_taught_in_regroup"]

# get dir grouping stream data
sets_dir_grp_stream = get_data(sets_dir_grouping_stream)
sets_dir_grp_stream_df = pd.DataFrame(sets_dir_grp_stream)
sets_dir_grp_stream_df = sets_dir_grp_stream_df.T
sets_dir_grp_stream_df.columns = ["sets_dir_grp_type_streaming"]

# get dir grouping gifted data
sets_dir_grp_gifted = get_data(sets_dir_grouping_gifted)
sets_dir_grp_gifted_df = pd.DataFrame(sets_dir_grp_gifted)
sets_dir_grp_gifted_df = sets_dir_grp_gifted_df.T
sets_dir_grp_gifted_df.columns = ["sets_dir_grp_type_gifted"]

# get school groupings data
sets_schl_groupings = get_data(sets_school_groupings)
sets_schl_groupings_df = pd.DataFrame(sets_schl_groupings)
sets_schl_groupings_df = sets_schl_groupings_df.T
sets_schl_groupings_df.columns = ["sets_school_groupings"]

# get attainment grouping levels data
sets_attain_grp_levels = get_data(sets_attain_grouping_level)
sets_attain_grp_levels_df = pd.DataFrame(sets_attain_grp_levels)
sets_attain_grp_levels_df = sets_attain_grp_levels_df.T
sets_attain_grp_levels_df.columns = ["sets_attain_grouping_levels"]

# get attainment grouping levels data
sets_foll_same_curr = get_data(sets_follow_same_curr)
sets_foll_same_curr_df = pd.DataFrame(sets_foll_same_curr)
sets_foll_same_curr_df = sets_foll_same_curr_df.T
sets_foll_same_curr_df.columns = ["sets_follow_same_curr"]

# get approach name data
sets_appr_name = get_data(sets_approach_name)
sets_appr_name_df = pd.DataFrame(sets_appr_name)
sets_appr_name_df = sets_appr_name_df.T
sets_appr_name_df.columns = ["sets_approach_name"]

# get pupil assignment data
sets_pup_assignment = get_data(sets_pupil_assignment)
sets_pup_assignment_df = pd.DataFrame(sets_pup_assignment)
sets_pup_assignment_df = sets_pup_assignment_df.T
sets_pup_assignment_df.columns = ["sets_pup_assign"]

sets_ss_df = pd.concat([
    sets_dir_grp_change_df,

    sets_dir_grp_type_regroup_df,

    sets_curr_taught_regroup_df,

    sets_dir_grp_stream_df,
    sets_dir_grp_gifted_df,

    sets_schl_groupings_df,
    sets_attain_grp_levels_df,
    sets_foll_same_curr_df,
    sets_appr_name_df,
    sets_pup_assignment_df
], axis=1, sort=False)

# fill blanks with NA
sets_ss_df.fillna("NA", inplace=True)

# save to disk
sets_ss_df.to_csv("setting_or_streaming_ss.csv", index=False)

print(sets_ss_df[0:50])