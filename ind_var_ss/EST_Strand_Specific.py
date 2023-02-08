from Main import load_json, get_data, highlighted_text, comments
from AttributeIDList import extended_how_output, time_Added_output, purpose_or_aim_output
from AttributeIDList import target_group_output, pupil_participation_output, activity_focus_output
from AttributeIDList import staff_kind_output, parental_involvement_output, digital_tech_output
from AttributeIDList import attendance_monitored_output

import pandas as pd

load_json()

# EXTENDED HOW?

# get extended how? data
extended_how = get_data(extended_how_output)
extended_how_df = pd.DataFrame(extended_how)
extended_how_df = extended_how_df.T
extended_how_df.columns = ["est_how"]

# Get extended how? highlighted text
extended_how_HT = highlighted_text(extended_how_output)
extended_how_HT_df = pd.DataFrame(extended_how_HT)
extended_how_HT_df = extended_how_HT_df.T
extended_how_HT_df.columns = ["est_how_ht"]

# Get extended how? user comments
extended_how_Comments = comments(extended_how_output)
extended_how_Comments_df = pd.DataFrame(extended_how_Comments)
extended_how_Comments_df = extended_how_Comments_df.T
extended_how_Comments_df.columns = ["est_how_info"]

# TIME ADDED

# get time added data
time_added = get_data(time_Added_output)
time_added_df = pd.DataFrame(time_added)
time_added_df = time_added_df.T
time_added_df.columns = ["est_time_added"]

# Get time added  highlighted text
time_added_HT = highlighted_text(time_Added_output)
time_added_HT_df = pd.DataFrame(time_added_HT)
time_added_HT_df = time_added_HT_df.T
time_added_HT_df.columns = ["est_time_added_ht"]

# Get time added  user comments
time_added_Comments = comments(time_Added_output)
time_added_Comments_df = pd.DataFrame(time_added_Comments)
time_added_Comments_df = time_added_Comments_df.T
time_added_Comments_df.columns = ["est_time_added_info"]

# PURPOSE OR AIM

# get purpose or aim data
purpose = get_data(purpose_or_aim_output)
purpose_df = pd.DataFrame(purpose)
purpose_df = purpose_df.T
purpose_df.columns = ["est_purpose"]

# Get purpose or aim highlighted text
purpose_HT = highlighted_text(purpose_or_aim_output)
purpose_HT_df = pd.DataFrame(purpose_HT)
purpose_HT_df = purpose_HT_df.T
purpose_HT_df.columns = ["est_purpose_ht"]

# Get purpose or aim user comments
purpose_Comments = comments(purpose_or_aim_output)
purpose_Comments_df = pd.DataFrame(purpose_Comments)
purpose_Comments_df = purpose_Comments_df.T
purpose_Comments_df.columns = ["est_purpose_info"]

# TARGET GROUP

# get target group data
target_group = get_data(target_group_output)
target_group_df = pd.DataFrame(target_group)
target_group_df = target_group_df.T
target_group_df.columns = ["est_target_group"]

# Get target group highlighted text
target_group_HT = highlighted_text(target_group_output)
target_group_HT_df = pd.DataFrame(target_group_HT)
target_group_HT_df = target_group_HT_df.T
target_group_HT_df.columns = ["est_target_group_ht"]

# Get target group user comments
target_group_Comments = comments(target_group_output)
target_group_Comments_df = pd.DataFrame(target_group_Comments)
target_group_Comments_df = target_group_Comments_df.T
target_group_Comments_df.columns = ["est_target_group_info"]

# PUPIL PARTICIPATION

# get pupil participation data
pupil_participation = get_data(pupil_participation_output)
pupil_participation_df = pd.DataFrame(pupil_participation)
pupil_participation_df = pupil_participation_df.T
pupil_participation_df.columns = ["est_pupil_participation"]

# Get pupil participation highlighted text
pupil_participation_HT = highlighted_text(pupil_participation_output)
pupil_participation_HT_df = pd.DataFrame(pupil_participation_HT)
pupil_participation_HT_df = pupil_participation_HT_df.T
pupil_participation_HT_df.columns = ["est_pupil_participation_ht"]

# Get pupil participation user comments
pupil_participation_Comments = comments(pupil_participation_output)
pupil_participation_Comments_df = pd.DataFrame(pupil_participation_Comments)
pupil_participation_Comments_df = pupil_participation_Comments_df.T
pupil_participation_Comments_df.columns = ["est_pupil_participation_info"]

# ACTIVITY FOCUS

# get activity focus data
activity_focus = get_data(activity_focus_output)
activity_focus_df = pd.DataFrame(activity_focus)
activity_focus_df = activity_focus_df.T
activity_focus_df.columns = ["est_activity_focus"]

# Get activity focus highlighted text
activity_focus_HT = highlighted_text(activity_focus_output)
activity_focus_HT_df = pd.DataFrame(activity_focus_HT)
activity_focus_HT_df = activity_focus_HT_df.T
activity_focus_HT_df.columns = ["est_activity_focus_ht"]

# Get activity focus user comments
activity_focus_Comments = comments(activity_focus_output)
activity_focus_Comments_df = pd.DataFrame(activity_focus_Comments)
activity_focus_Comments_df = activity_focus_Comments_df.T
activity_focus_Comments_df.columns = ["est_activity_focus_info"]

# STAFF KIND

# get staff kind data
staff_kind = get_data(staff_kind_output)
staff_kind_df = pd.DataFrame(staff_kind)
staff_kind_df = staff_kind_df.T
staff_kind_df.columns = ["est_staff_kind"]

# Get staff kind highlighted text
staff_kind_HT = highlighted_text(staff_kind_output)
staff_kind_HT_df = pd.DataFrame(staff_kind_HT)
staff_kind_HT_df = staff_kind_HT_df.T
staff_kind_HT_df.columns = ["est_staff_kind_ht"]

# Get staff kind user comments
staff_kind_Comments = comments(staff_kind_output)
staff_kind_Comments_df = pd.DataFrame(staff_kind_Comments)
staff_kind_Comments_df = staff_kind_Comments_df.T
staff_kind_Comments_df.columns = ["est_staff_kind_info"]

# PARENTAL INVOLVEMENT

# get parental involvement data
parent_involved = get_data(parental_involvement_output)
parent_involved_df = pd.DataFrame(parent_involved)
parent_involved_df = parent_involved_df.T
parent_involved_df.columns = ["est_parental_involvement"]

# Get parental involvement highlighted text
parent_involved_HT = highlighted_text(parental_involvement_output)
parent_involved_HT_df = pd.DataFrame(parent_involved_HT)
parent_involved_HT_df = parent_involved_HT_df.T
parent_involved_HT_df.columns = ["est_parental_involvement_ht"]

# Get parental involvementuser comments
parent_involved_Comments = comments(parental_involvement_output)
parent_involved_Comments_df = pd.DataFrame(parent_involved_Comments)
parent_involved_Comments_df = parent_involved_Comments_df.T
parent_involved_Comments_df.columns = ["est_parental_involvement_info"]

# DIGITAL TECHNOLOGY

# get digital technology data
digit_tech = get_data(digital_tech_output)
digit_tech_df = pd.DataFrame(digit_tech)
digit_tech_df = digit_tech_df.T
digit_tech_df.columns = ["est_digital_tech"]

# Get digital technology highlighted text
digit_tech_HT = highlighted_text(digital_tech_output)
digit_tech_HT_df = pd.DataFrame(digit_tech_HT)
digit_tech_HT_df = digit_tech_HT_df.T
digit_tech_HT_df.columns = ["est_digital_tech_ht"]

# Get digital technology user comments
digit_tech_Comments = comments(digital_tech_output)
digit_tech_Comments_df = pd.DataFrame(digit_tech_Comments)
digit_tech_Comments_df = digit_tech_Comments_df.T
digit_tech_Comments_df.columns = ["est_digital_tech_info"]

# ATTENDANCE MONITORED

# get attendance monitored data
attend_mon = get_data(attendance_monitored_output)
attend_mon_df = pd.DataFrame(attend_mon)
attend_mon_df = attend_mon_df.T
attend_mon_df.columns = ["est_attend_monitored"]

# Get attendance monitored highlighted text
attend_mon_HT = highlighted_text(attendance_monitored_output)
attend_mon_HT_df = pd.DataFrame(attend_mon_HT)
attend_mon_HT_df = attend_mon_HT_df.T
attend_mon_HT_df.columns = ["est_attend_monitored_ht"]

# Get attendance monitored user comments
attend_mon_Comments = comments(attendance_monitored_output)
attend_mon_Comments_df = pd.DataFrame(attend_mon_Comments)
attend_mon_Comments_df = attend_mon_Comments_df.T
attend_mon_Comments_df.columns = ["est_attendance_monitored_info"]

# concatenate data frames
est_ss_df = pd.concat([
    extended_how_df,
    time_added_df,
    time_added_Comments_df,
    purpose_df,
    target_group_df,
    pupil_participation_df,
    activity_focus_df,
    staff_kind_df,
    parent_involved_df,
    digit_tech_df,
    attend_mon_df,
], axis=1, sort=False)

# remove problematic text from outputs
est_ss_df.replace('\r', ' ', regex=True, inplace=True)
est_ss_df.replace('\n', ' ', regex=True, inplace=True)
est_ss_df.replace(':', ' ',  regex=True, inplace=True)
est_ss_df.replace(';', ' ',  regex=True, inplace=True)

""" est_ss_df.to_csv("extended_school_time_ss.csv", index=False, header=True) """