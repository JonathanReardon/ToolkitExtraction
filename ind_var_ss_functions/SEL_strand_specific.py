import os
import sys

import pandas as pd

from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import sel_involvement_output
from AttributeIDList import sel_focus_output
from AttributeIDList import sel_location_output
from AttributeIDList import sel_invol_all_pupils
from AttributeIDList import sel_invol_targ_grp
from AttributeIDList import sel_invol_classes
from AttributeIDList import sel_invol_school
from AttributeIDList import sel_invol_teachers
from AttributeIDList import sel_invol_other_staff
from AttributeIDList import sel_invol_outside_experts
from AttributeIDList import sel_invol_other

load_json()

# get involvement data
sel_involvement = get_data(sel_involvement_output)
sel_involvement_df = pd.DataFrame(sel_involvement)
sel_involvement_df = sel_involvement_df.T
sel_involvement_df.columns = ["sel_involvement"]

# split involvement data (above) into individual columns

# get involvement pupils data
sel_invol_pupils = get_data(sel_invol_all_pupils)
sel_invol_pupils_df = pd.DataFrame(sel_invol_pupils)
sel_invol_pupils_df = sel_invol_pupils_df.T
sel_invol_pupils_df.columns = ["sel_invol_pupils"]

# get involvement target groups data
sel_invol_targ_groups = get_data(sel_invol_targ_grp)
sel_invol_targ_groups_df = pd.DataFrame(sel_invol_targ_groups)
sel_invol_targ_groups_df = sel_invol_targ_groups_df.T
sel_invol_targ_groups_df.columns = ["sel_invol_targ_grps"]

# get involvement classes data
sel_invol_classes = get_data(sel_invol_classes)
sel_invol_classes_df = pd.DataFrame(sel_invol_classes)
sel_invol_classes_df = sel_invol_classes_df.T
sel_invol_classes_df.columns = ["sel_invol_classes"]

# get involvement whole schools data
sel_invol_whole_school = get_data(sel_invol_school)
sel_invol_whole_school_df = pd.DataFrame(sel_invol_whole_school)
sel_invol_whole_school_df = sel_invol_whole_school_df.T
sel_invol_whole_school_df.columns = ["sel_invol_whole_school"]

# get involvement classroom teachers data
sel_invol_class_teachers = get_data(sel_invol_teachers)
sel_invol_class_teachers_df = pd.DataFrame(sel_invol_class_teachers)
sel_invol_class_teachers_df = sel_invol_class_teachers_df.T
sel_invol_class_teachers_df.columns = ["sel_invol_class_teachers"]

# get involvement other staff data
sel_invol_oth_staff = get_data(sel_invol_other_staff)
sel_invol_oth_staff_df = pd.DataFrame(sel_invol_oth_staff)
sel_invol_oth_staff_df = sel_invol_oth_staff_df.T
sel_invol_oth_staff_df.columns = ["sel_invol_oth_staff"]

# get involvement outside experts data
sel_invol_out_experts = get_data(sel_invol_outside_experts)
sel_invol_out_experts_df = pd.DataFrame(sel_invol_out_experts)
sel_invol_out_experts_df = sel_invol_out_experts_df.T
sel_invol_out_experts_df.columns = ["sel_invol_out_experts"]

# get involvement other data
sel_invol_other = get_data(sel_invol_other)
sel_invol_other_df = pd.DataFrame(sel_invol_other)
sel_invol_other_df = sel_invol_other_df.T
sel_invol_other_df.columns = ["sel_invol_other"]

# get focus data
sel_focus = get_data(sel_focus_output)
sel_focus_df = pd.DataFrame(sel_focus)
sel_focus_df = sel_focus_df.T
sel_focus_df.columns = ["sel_focus"]

# get location data
sel_location = get_data(sel_location_output)
sel_location_df = pd.DataFrame(sel_location)
sel_location_df = sel_location_df.T
sel_location_df.columns = ["sel_location"]

sel_ss_df = pd.concat([
    sel_involvement_df,

    sel_invol_pupils_df,
    sel_invol_targ_groups_df,
    sel_invol_classes_df,
    sel_invol_whole_school_df,
    sel_invol_class_teachers_df,
    sel_invol_oth_staff_df,
    sel_invol_out_experts_df,
    sel_invol_other_df,

    sel_focus_df,
    sel_location_df
], axis=1, sort=False)

# fill blanks with NA
sel_ss_df.fillna("NA", inplace=True)

# save to disk
#sel_ss_df.to_csv("social_emot_learning_ss_df.csv", index=False)