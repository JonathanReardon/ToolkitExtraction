#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Jonathan Reardon
"""

# Standard imports
import os
import sys

# Third party imports
import pandas as pd
import numpy as np
from toolz import interleave

# Local imports
from Main import getOutcomeData
from Main import verbose_display
from Main import save_dataframe
from Main import verbose_display
from Main import save_dataframe
from Main import clean_up
from Main import load_json, get_data
from Main import highlighted_text, comments

def arts_participation_ss():
    from AttributeIDList import ap_focus_output
    from AttributeIDList import ap_who_output
    from AttributeIDList import ap_where_output
    # get focus data
    ap_focus = get_data(ap_focus_output)
    ap_focus_df = pd.DataFrame(ap_focus)
    ap_focus_df = ap_focus_df.T
    ap_focus_df.columns = ["ap_focus"]

    # get who involved data
    ap_who_invol = get_data(ap_who_output)
    ap_who_invol_df = pd.DataFrame(ap_who_invol)
    ap_who_invol_df = ap_who_invol_df.T
    ap_who_invol_df.columns = ["ap_involved"]

    # get where data
    ap_where = get_data(ap_where_output)
    ap_where_df = pd.DataFrame(ap_where)
    ap_where_df = ap_where_df.T
    ap_where_df.columns = ["ap_where"]

    ap_ss_df = pd.concat([
        ap_focus_df,
        ap_who_invol_df,
        ap_where_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    ap_ss_df.fillna("NA", inplace=True)

    return ap_ss_df

def behaviour_int_ss():

    from AttributeIDList import bi_target_group_output, bi_intervention_approach_output, bi_intervention_components_output
    from AttributeIDList import ind_comp_counselling, ind_comp_monitoring, ind_comp_self_management
    from AttributeIDList import ind_comp_role_play, ind_comp_parental_involv, ind_comp_academic_focus
    from AttributeIDList import ind_comp_digit_tech
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

    return bi_ss_df

def collab_learning_ss():

    from AttributeIDList import cl_approach_spec_output
    from AttributeIDList import cl_group_size_output
    from AttributeIDList import cl_collab_kind_output
    from AttributeIDList import cl_stud_collab_output
    from AttributeIDList import cl_extr_rewards_output
    from AttributeIDList import cl_if_yes_rewards_output
    from AttributeIDList import cl_comp_elem_output
    from AttributeIDList import cl_teacher_role_info_output
    from AttributeIDList import cl_pupil_feedback_output
    from AttributeIDList import cl_pupil_feedback_who_output
    # COLLABORATIVE LEARNING

    # get approach specified data
    cl_approach_spec = get_data(cl_approach_spec_output)
    cl_approach_spec_df = pd.DataFrame(cl_approach_spec)
    cl_approach_spec_df = cl_approach_spec_df.T
    cl_approach_spec_df.columns = ["cl_approach_spec"]

    # get group size data
    cl_grp_size = get_data(cl_group_size_output)
    cl_grp_size_df = pd.DataFrame(cl_grp_size)
    cl_grp_size_df = cl_grp_size_df.T
    cl_grp_size_df.columns = ["cl_grp_size"]

    # get collab kind data
    cl_collab_kind = get_data(cl_collab_kind_output)
    cl_collab_kind_df = pd.DataFrame(cl_collab_kind)
    cl_collab_kind_df = cl_collab_kind_df.T
    cl_collab_kind_df.columns = ["cl_collab_kind"]

    # get student collab data
    cl_stud_collab = get_data(cl_stud_collab_output)
    cl_stud_collab_df = pd.DataFrame(cl_stud_collab)
    cl_stud_collab_df = cl_stud_collab_df.T
    cl_stud_collab_df.columns = ["cl_stud_collab"]

    # get student collab highlighted text
    cl_stud_collab_HT = highlighted_text(cl_stud_collab_output)
    cl_stud_collab_HT_df = pd.DataFrame(cl_stud_collab_HT)
    cl_stud_collab_HT_df = cl_stud_collab_HT_df.T
    cl_stud_collab_HT_df.columns = ["cl_stud_collab_HT"]

    # get extrinsic rewards data
    cl_extr_rewards = get_data(cl_extr_rewards_output)
    cl_extr_rewards_df = pd.DataFrame(cl_extr_rewards)
    cl_extr_rewards_df = cl_extr_rewards_df.T
    cl_extr_rewards_df.columns = ["cl_extr_rewards"]

    # get extrinsic rewards highlighted text
    cl_extr_rewards_HT = highlighted_text(cl_extr_rewards_output)
    cl_extr_rewards_HT_df = pd.DataFrame(cl_extr_rewards_HT)
    cl_extr_rewards_HT_df = cl_extr_rewards_HT_df.T
    cl_extr_rewards_HT_df.columns = ["cl_extr_rewards_HT"]

    # get if yes rewards, where they.. data
    cl_if_yes_rewards = get_data(cl_if_yes_rewards_output)
    cl_if_yes_rewards_df = pd.DataFrame(cl_if_yes_rewards)
    cl_if_yes_rewards_df = cl_if_yes_rewards_df.T
    cl_if_yes_rewards_df.columns = ["cl_what_rewards"]

    # get if yes rewards, where they.. highlighted text
    cl_if_yes_rewards_HT = highlighted_text(cl_if_yes_rewards_output)
    cl_if_yes_rewards_HT_df = pd.DataFrame(cl_if_yes_rewards_HT)
    cl_if_yes_rewards_HT_df = cl_if_yes_rewards_HT_df.T
    cl_if_yes_rewards_HT_df.columns = ["cl_what_rewards_HT"]

    # get competitive element data
    cl_comp_elem = get_data(cl_comp_elem_output)
    cl_comp_elem_df = pd.DataFrame(cl_comp_elem)
    cl_comp_elem_df = cl_comp_elem_df.T
    cl_comp_elem_df.columns = ["cl_comp_elem"]

    # get competitive element highlighted text
    cl_comp_elem_HT = highlighted_text(cl_comp_elem_output)
    cl_comp_elem_HT_df = pd.DataFrame(cl_comp_elem_HT)
    cl_comp_elem_HT_df = cl_comp_elem_HT_df.T
    cl_comp_elem_HT_df.columns = ["cl_comp_elem_HT"]

    # get teacher role info data
    cl_teach_role_info = get_data(cl_teacher_role_info_output)
    cl_teach_role_info_df = pd.DataFrame(cl_teach_role_info)
    cl_teach_role_info_df = cl_teach_role_info_df.T
    cl_teach_role_info_df.columns = ["cl_teacher_role_info"]

    # get teacher role info highlighted text
    cl_teach_role_info_HT = highlighted_text(cl_teacher_role_info_output)
    cl_teach_role_info_HT_df = pd.DataFrame(cl_teach_role_info_HT)
    cl_teach_role_info_HT_df = cl_teach_role_info_HT_df.T
    cl_teach_role_info_HT_df.columns = ["cl_teacher_role_info_HT"]

    # get pupil feedback data
    cl_pup_feedback = get_data(cl_pupil_feedback_output)
    cl_pup_feedback_df = pd.DataFrame(cl_pup_feedback)
    cl_pup_feedback_df = cl_pup_feedback_df.T
    cl_pup_feedback_df.columns = ["cl_pup_feedback"]

    # get pupil feedback highlighted text
    cl_pup_feedback_HT = highlighted_text(cl_pupil_feedback_output)
    cl_pup_feedback_HT_df = pd.DataFrame(cl_pup_feedback_HT)
    cl_pup_feedback_HT_df = cl_pup_feedback_HT_df.T
    cl_pup_feedback_HT_df.columns = ["cl_pup_feedback_HT"]

    # get pupil feedback who data
    cl_pup_feedback_who = get_data(cl_pupil_feedback_who_output)
    cl_pup_feedback_who_df = pd.DataFrame(cl_pup_feedback_who)
    cl_pup_feedback_who_df = cl_pup_feedback_who_df.T
    cl_pup_feedback_who_df.columns = ["cl_pup_feedback_who"]

    # get pupil feedback who highlighted text
    cl_pup_feedback_who_HT = highlighted_text(cl_pupil_feedback_who_output)
    cl_pup_feedback_who_HT_df = pd.DataFrame(cl_pup_feedback_who_HT)
    cl_pup_feedback_who_HT_df = cl_pup_feedback_who_HT_df.T
    cl_pup_feedback_who_HT_df.columns = ["cl_pup_feedback_who_HT"]

    cl_ss_df = pd.concat([
        cl_approach_spec_df,
        cl_grp_size_df,
        cl_collab_kind_df,
        cl_stud_collab_df,
        cl_extr_rewards_df,
        cl_if_yes_rewards_df,
        cl_comp_elem_df,
        cl_teach_role_info_df,
        cl_pup_feedback_df,
        cl_pup_feedback_who_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    cl_ss_df.fillna("NA", inplace=True)

    return cl_ss_df

def ey_early_lit_approaches_ss():
    # EARLY LITERACY APPROACHES

    from AttributeIDList import ela_literacy_activities
    from AttributeIDList import ela_comprehensive
    from AttributeIDList import ela_prog_desc

    # literacy acticivities data
    lit_act = get_data(ela_literacy_activities)
    lit_act_df = pd.DataFrame(lit_act)
    lit_act_df = lit_act_df.T
    lit_act_df.columns = ["lit_activities"]

    # literacy activities highlighted text
    lit_act_HT = highlighted_text(ela_literacy_activities)
    lit_act_HT_df = pd.DataFrame(lit_act_HT)
    lit_act_HT_df = lit_act_HT_df.T
    lit_act_HT_df.columns = ["lit_activities_HT"]

    # comprehensive prog data
    prog_comp = get_data(ela_comprehensive)
    prog_comp_df = pd.DataFrame(prog_comp)
    prog_comp_df = prog_comp_df.T
    prog_comp_df.columns = ["prog_comp"]

    # comprehensive prog highlighted text
    prog_comp_HT = highlighted_text(ela_comprehensive)
    prog_comp_HT_df = pd.DataFrame(prog_comp_HT)
    prog_comp_HT_df = prog_comp_HT_df.T
    prog_comp_HT_df.columns = ["prog_comp_HT"]

    # comprehensive prog data
    prog_desc = get_data(ela_prog_desc)
    prog_desc_df = pd.DataFrame(prog_desc)
    prog_desc_df = prog_desc_df.T
    prog_desc_df.columns = ["prog_desc"]

    # comprehensive prog highlighted text
    prog_desc_HT = highlighted_text(ela_prog_desc)
    prog_desc_HT_df = pd.DataFrame(prog_desc_HT)
    prog_desc_HT_df = prog_desc_HT_df.T
    prog_desc_HT_df.columns = ["prog_desc_HT"]

    # concatenate data frames
    ela_ss_df = pd.concat([
        lit_act_df,
        #lit_act_HT_df,
        prog_comp_df,
        #prog_comp_HT_df,
        prog_desc_df,
        #prog_desc_HT_df,
    ], axis=1, sort=False)

    return ela_ss_df

def ey_early_num_approaches_ss():
    # EARLY NUMERACY APPROACHES
    from AttributeIDList import ena_maths_included
    from AttributeIDList import ena_prog_comp
    from AttributeIDList import ena_prog_activities
    # maths included data
    math_incl = get_data(ena_maths_included)
    math_incl_df = pd.DataFrame(math_incl)
    math_incl_df = math_incl_df.T
    math_incl_df.columns = ["math_incl"]

    # maths included highlighted text
    math_incl_HT = highlighted_text(ena_maths_included)
    math_incl_HT_df = pd.DataFrame(math_incl_HT)
    math_incl_HT_df = math_incl_HT_df.T
    math_incl_HT_df.columns = ["math_incl_ht"]

    # how comprehensive was the data, data
    prog_comp = get_data(ena_prog_comp)
    prog_comp_df = pd.DataFrame(prog_comp)
    prog_comp_df = prog_comp_df.T
    prog_comp_df.columns = ["prog_comp"]

    # how comprehensive activities, data
    prog_act = get_data(ena_prog_activities)
    prog_act_df = pd.DataFrame(prog_act)
    prog_act_df = prog_act_df.T
    prog_act_df.columns = ["prog_act"]

    # concatenate data frames
    ena_ss_df = pd.concat([
        math_incl_df,
        #math_incl_HT_df,
        prog_comp_df,
        prog_act_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    ena_ss_df.fillna("NA", inplace=True)

    return ena_ss_df

def ext_school_time_ss():

    from AttributeIDList import extended_how_output, time_Added_output, purpose_or_aim_output
    from AttributeIDList import target_group_output, pupil_participation_output, activity_focus_output
    from AttributeIDList import staff_kind_output, parental_involvement_output, digital_tech_output
    from AttributeIDList import attendance_monitored_output

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
    clean_up(est_ss_df)
    
    return est_ss_df

def ey_earlier_start_age_ss():
    from AttributeIDList import ey_esa_prev_starting_age
    from AttributeIDList import ey_esa_new_starting_age
    from AttributeIDList import ey_esa_addit_time_f_pt
    from AttributeIDList import ey_esa_addit_time_struct
    from AttributeIDList import ey_esa_earlier_child_addit_time
    from AttributeIDList import ey_esa_earlier_child_addit_time_other
    from AttributeIDList import ey_esa_setting_type

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

    return ey_esa_df

def ey_extra_hours_ss():
    from AttributeIDList import time_organsised
    from AttributeIDList import addit_time_struct
    # get additional time organised data
    time_org = get_data(time_organsised)
    time_org_df = pd.DataFrame(time_org)
    time_org_df = time_org_df.T
    time_org_df.columns = ["time_org"]

    # get structure of additional time data
    addit_time_struc= get_data(addit_time_struct)
    addit_time_struc_df = pd.DataFrame(addit_time_struc)
    addit_time_struc_df = addit_time_struc_df.T
    addit_time_struc_df.columns = ["addit_time_struct"]

    ey_eh_df = pd.concat([
        time_org_df,
        addit_time_struc_df
    ], axis=1, sort=False)

    # fill blanks with NA
    ey_eh_df.fillna("NA", inplace=True)
    return ey_eh_df

def ey_play_based_learning_ss():
    from AttributeIDList import kind_of_play
    from AttributeIDList import who_involved
    from AttributeIDList import play_focus
    
    # get kind if play data
    kind_play = get_data(kind_of_play)
    kind_play_df = pd.DataFrame(kind_play)
    kind_play_df = kind_play_df.T
    kind_play_df.columns = ["kind_of_play"]

    # get who involved data
    who_invol = get_data(who_involved)
    who_invol_df = pd.DataFrame(who_invol)
    who_invol_df = who_invol_df.T
    who_invol_df.columns = ["who_involved"]

    # get play focus data
    play_foc = get_data(play_focus)
    play_foc_df = pd.DataFrame(play_foc)
    play_foc_df = play_foc_df.T
    play_foc_df.columns = ["play_focus"]

    ey_pbl_df = pd.concat([
        kind_play_df,
        who_invol_df,
        play_foc_df
    ], axis=1, sort=False)

    # fill blanks with NA
    ey_pbl_df.fillna("NA", inplace=True)
    return ey_pbl_df

def feedback_ss():
    from AttributeIDList import feedback_source_output
    from AttributeIDList import feedback_directed_output
    from AttributeIDList import feedback_form_output
    from AttributeIDList import feedback_when_output
    from AttributeIDList import feedback_kind_output
    from AttributeIDList import feedback_emo_tone
    from AttributeIDList import feedback_about_outcome_output

    # feedback source options for ind column extraction
    from AttributeIDList import fsource_teacher
    from AttributeIDList import fsource_ta
    from AttributeIDList import fsource_volunteer
    from AttributeIDList import fsource_parent
    from AttributeIDList import fsource_researcher
    from AttributeIDList import fsource_peer_sameage_class
    from AttributeIDList import fsource_peer_group
    from AttributeIDList import fsource_peer_older
    from AttributeIDList import fsource_dig_aut
    from AttributeIDList import fsource_other_nonhuman
    from AttributeIDList import fsource_self
    from AttributeIDList import fsource_other

    # FEEDBACK SOURCE

    # get feedback source data
    feedb_source = get_data(feedback_source_output)
    feedb_source_df = pd.DataFrame(feedb_source)
    feedb_source_df = feedb_source_df.T
    feedb_source_df.columns = ["feedback_Source"]

    # Get feedback source highlighted text
    feedb_source_HT = highlighted_text(feedback_source_output)
    feedb_source_HT_df = pd.DataFrame(feedb_source_HT)
    feedb_source_HT_df = feedb_source_HT_df.T
    feedb_source_HT_df.columns = ["feedback_Source_ht"]

    # Get feedback source user comments
    feedb_source_Comments = comments(feedback_source_output)
    feedb_source_Comments_df = pd.DataFrame(feedb_source_Comments)
    feedb_source_Comments_df = feedb_source_Comments_df.T
    feedb_source_Comments_df.columns = ["feedback_Source_info"]

    # FEEDBACK SOURCE COMPONENTS SPLIT

    # get feedback source teacher data
    fsource_teacher = get_data(fsource_teacher)
    fsource_teacher_df = pd.DataFrame(fsource_teacher)
    fsource_teacher_df = fsource_teacher_df.T
    fsource_teacher_df.columns = ["fb_source_teacher"]

    # get feedback source teaching assistant data
    fsource_ta = get_data(fsource_ta)
    fsource_ta_df = pd.DataFrame(fsource_ta)
    fsource_ta_df = fsource_ta_df.T
    fsource_ta_df.columns = ["fb_source_ta"]

    # get feedback source volunteer data
    fsource_volunteer = get_data(fsource_volunteer)
    fsource_volunteer_df = pd.DataFrame(fsource_volunteer)
    fsource_volunteer_df = fsource_volunteer_df.T
    fsource_volunteer_df.columns = ["fb_source_volunteer"]

    # get feedback source parent data
    fsource_parent = get_data(fsource_parent)
    fsource_parent_df = pd.DataFrame(fsource_parent)
    fsource_parent_df = fsource_parent_df.T
    fsource_parent_df.columns = ["fb_source_parent"]

    # get feedback source researcher data
    fsource_researcher = get_data(fsource_researcher)
    fsource_researcher_df = pd.DataFrame(fsource_researcher)
    fsource_researcher_df = fsource_researcher_df.T
    fsource_researcher_df.columns = ["fb_source_researcher"]

    # get feedback source peer same age data
    fsource_peer_ssame_Age = get_data(fsource_peer_sameage_class)
    fsource_peer_ssame_Age_df = pd.DataFrame(fsource_peer_ssame_Age)
    fsource_peer_ssame_Age_df = fsource_peer_ssame_Age_df.T
    fsource_peer_ssame_Age_df.columns = ["fb_source_peer_sameage"]

    # get feedback source peer group data
    fsource_peer_group = get_data(fsource_peer_group)
    fsource_peer_group_df = pd.DataFrame(fsource_peer_group)
    fsource_peer_group_df = fsource_peer_group_df.T
    fsource_peer_group_df.columns = ["fb_source_peer_group"]

    # get feedback source peer older data
    fsource_peer_older = get_data(fsource_peer_older)
    fsource_peer_older_df = pd.DataFrame(fsource_peer_older)
    fsource_peer_older_df = fsource_peer_older_df.T
    fsource_peer_older_df.columns = ["fb_source_peer_older"]

    # get feedback source digital automated data
    fsource_digit_aut = get_data(fsource_dig_aut)
    fsource_digit_aut_df = pd.DataFrame(fsource_digit_aut)
    fsource_digit_aut_df = fsource_digit_aut_df.T
    fsource_digit_aut_df.columns = ["fb_source_dig_aut"]

    # get feedback source other non-human data
    fsource_non_human = get_data(fsource_other_nonhuman)
    fsource_non_human_df = pd.DataFrame(fsource_non_human)
    fsource_non_human_df = fsource_non_human_df.T
    fsource_non_human_df.columns = ["fb_source_non_human"]

    # get feedback source self data
    fsource_self = get_data(fsource_self)
    fsource_self_df = pd.DataFrame(fsource_self)
    fsource_self_df = fsource_self_df.T
    fsource_self_df.columns = ["fb_source_self"]

    # get feedback source other data
    fsource_other = get_data(fsource_other)
    fsource_other_df = pd.DataFrame(fsource_other)
    fsource_other_df = fsource_other_df.T
    fsource_other_df.columns = ["fb_source_other"]

    # FEEDBACK DIRECTED OUTPUT

    # get feedback directed data
    feedb_directed = get_data(feedback_directed_output)
    feedb_directed_df = pd.DataFrame(feedb_directed)
    feedb_directed_df = feedb_directed_df.T
    feedb_directed_df.columns = ["fb_directed"]

    # Get feedback directed highlighted text
    feedb_directed_df_HT = highlighted_text(feedback_directed_output)
    feedb_directed_df_HT_df = pd.DataFrame(feedb_directed_df_HT)
    feedb_directed_df_HT_df = feedb_directed_df_HT_df.T
    feedb_directed_df_HT_df.columns = ["fb_directed_ht"]

    # Get feedback directed user comments
    feedb_directed_Comments = comments(feedback_directed_output)
    feedb_directed_Comments_df = pd.DataFrame(feedb_directed_Comments)
    feedb_directed_Comments_df = feedb_directed_Comments_df.T
    feedb_directed_Comments_df.columns = ["fb_directed_info"]

    # FEEDBACK FORM OUTPUT

    # get feedback form data
    feedb_form = get_data(feedback_form_output)
    feedb_form_df = pd.DataFrame(feedb_form)
    feedb_form_df = feedb_form_df.T
    feedb_form_df.columns = ["fb_form"]

    # Get feedback form highlighted text
    feedb_form_HT = highlighted_text(feedback_form_output)
    feedb_form_HT_df = pd.DataFrame(feedb_form_HT)
    feedb_form_HT_df = feedb_form_HT_df.T
    feedb_form_HT_df.columns = ["fb_form_ht"]

    # Get feedback form user comments
    feedb_form_Comments = comments(feedback_form_output)
    feedb_form_Comments_df = pd.DataFrame(feedb_form_Comments)
    feedb_form_Comments_df = feedb_form_Comments_df.T
    feedb_form_Comments_df.columns = ["fb_form_info"]

    # FEEDBACK WHEN OUTPUT

    # get feedback when data
    feedb_when = get_data(feedback_when_output)
    feedb_when_df = pd.DataFrame(feedb_when)
    feedb_when_df = feedb_when_df.T
    feedb_when_df.columns = ["fb_when"]

    # Get feedback when highlighted text
    feedb_when_HT = highlighted_text(feedback_when_output)
    feedb_when_HT_df = pd.DataFrame(feedb_when_HT)
    feedb_when_HT_df = feedb_when_HT_df.T
    feedb_when_HT_df.columns = ["fb_when_ht"]

    # Get feedback when user comments
    feedb_when_Comments = comments(feedback_when_output)
    feedb_when_Comments_df = pd.DataFrame(feedb_when_Comments)
    feedb_when_Comments_df = feedb_when_Comments_df.T
    feedb_when_Comments_df.columns = ["fb_when_info"]

    # FEEDBACK KIND OUTPUT

    # get feedback kind data
    feedb_kind = get_data(feedback_kind_output)
    feedb_kind_df = pd.DataFrame(feedb_kind)
    feedb_kind_df = feedb_kind_df.T
    feedb_kind_df.columns = ["fb_kind"]

    # get feedback kind "about the outcome" nested data (correct / incorrect"
    feedb_kind_abt_outcome = get_data(feedback_about_outcome_output)
    feedb_kind_abt_outcome_df = pd.DataFrame(feedb_kind_abt_outcome)
    feedb_kind_abt_outcome_df = feedb_kind_abt_outcome_df.T
    feedb_kind_abt_outcome_df.columns = ["fb_kind_about_outcome"]

    # Get feedback kind highlighted text
    feedb_kind_HT = highlighted_text(feedback_kind_output)
    feedb_kind_HT_df = pd.DataFrame(feedb_kind_HT)
    feedb_kind_HT_df = feedb_kind_HT_df.T
    feedb_kind_HT_df.columns = ["fb_kind_ht"]

    # Get feedback kind user comments
    feedb_kind_Comments = comments(feedback_kind_output)
    feedb_kind_Comments_df = pd.DataFrame(feedb_kind_Comments)
    feedb_kind_Comments_df = feedb_kind_Comments_df.T
    feedb_kind_Comments_df.columns = ["fbkind_info"]

    # FEEDBACK EMOTIONAL TONE OUTPUT

    # get feedback emotional tone data
    feedb_emo_tone = get_data(feedback_emo_tone)
    feedb_emo_tone_df = pd.DataFrame(feedb_emo_tone)
    feedb_emo_tone_df = feedb_emo_tone_df.T
    feedb_emo_tone_df.columns = ["fb_emo_tone"]

    # Get feedback emotional tone highlighted text
    feedb_emo_tone_HT = highlighted_text(feedback_emo_tone)
    feedb_emo_tone_HT_df = pd.DataFrame(feedb_emo_tone_HT)
    feedb_emo_tone_HT_df = feedb_emo_tone_HT_df.T
    feedb_emo_tone_HT_df.columns = ["fb_emo_tone_ht"]

    # Get feedback emotional tone user comments
    feedb_emo_tone_Comments = comments(feedback_emo_tone)
    feedb_emo_tone_Comments_df = pd.DataFrame(feedb_emo_tone_Comments)
    feedb_emo_tone_Comments_df = feedb_emo_tone_Comments_df.T
    feedb_emo_tone_Comments_df.columns = ["fb_emo_tone_info"]

    # concatenate data frames
    feedback_ss_df = pd.concat([
        feedb_source_df,

        fsource_teacher_df,
        fsource_ta_df,
        fsource_volunteer_df,
        fsource_parent_df,
        fsource_researcher_df,
        fsource_peer_ssame_Age_df,
        fsource_peer_group_df,
        fsource_peer_older_df,
        fsource_digit_aut_df,
        fsource_non_human_df,
        fsource_self_df,
        fsource_other_df,

        feedb_directed_df,
        feedb_form_df,
        feedb_when_df,
        feedb_kind_df,
        feedb_kind_abt_outcome_df,
        feedb_emo_tone_df,
    ], axis=1, sort=False)

    # remove problematic text from outputs
    clean_up(feedback_ss_df)

    return feedback_ss_df

def homework_ss():
    from AttributeIDList import hw_dur_info_output
    from AttributeIDList import hw_total_time
    from AttributeIDList import hw_who_involved_output
    from AttributeIDList import hw_if_parents_describe_role_output
    from AttributeIDList import hw_completed_where_output
    from AttributeIDList import hw_mark_method_info_output

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

    return hw_ss_df

def indiv_instr_ss():
    from AttributeIDList import ii_approach_output
    from AttributeIDList import ii_also_included_output
    from AttributeIDList import ii_also_mentioned_output
    # get approach data
    ii_approach = get_data(ii_approach_output)
    ii_approach_df = pd.DataFrame(ii_approach)
    ii_approach_df = ii_approach_df.T
    ii_approach_df.columns = ["ii_approach"]

    # get also included data
    ii_also_included = get_data(ii_also_included_output)
    ii_also_included_df = pd.DataFrame(ii_also_included)
    ii_also_included_df = ii_also_included_df.T
    ii_also_included_df.columns = ["ii_elements_included"]

    # get also mentioned data
    ii_also_mentioned = get_data(ii_also_mentioned_output)
    ii_also_mentioned_df = pd.DataFrame(ii_also_mentioned)
    ii_also_mentioned_df = ii_also_mentioned_df.T
    ii_also_mentioned_df.columns = ["ii_programmes_mentioned"]

    ii_ss_df = pd.concat([
        ii_approach_df,
        ii_also_included_df,
        ii_also_mentioned_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    ii_ss_df.fillna("NA", inplace=True)

    return ii_ss_df

def mentoring_ss():

    from AttributeIDList import mentor_identity
    from AttributeIDList import mentor_paid_or_compensated
    from AttributeIDList import mentor_organisation
    from AttributeIDList import mentor_training
    from AttributeIDList import mentor_meeting_frequency
    from AttributeIDList import mentor_meeting_details_provided
    from AttributeIDList import mentor_meeting_location
    from AttributeIDList import mentoring_additional_experiences, mentoring_programme_focus
    # get Mentor identity data
    ment_ident = get_data(mentor_identity)
    ment_ident_df = pd.DataFrame(ment_ident)
    ment_ident_df = ment_ident_df.T
    ment_ident_df.columns = ["m_identity"]

    # Get Mentor identity highlighted text
    ment_ident_HT = highlighted_text(mentor_identity)
    ment_ident_HT_df = pd.DataFrame(ment_ident_HT)
    ment_ident_HT_df = ment_ident_HT_df.T
    ment_ident_HT_df.columns = ["m_identity_ht"]

    # Get Mentor identity user comments
    ment_ident_Comments = comments(mentor_identity)
    ment_ident_Comments_df = pd.DataFrame(ment_ident_Comments)
    ment_ident_Comments_df = ment_ident_Comments_df.T
    ment_ident_Comments_df.columns = ["m_identity_info"]

    # get Mentor pay data
    ment_pay = get_data(mentor_paid_or_compensated)
    ment_pay_df = pd.DataFrame(ment_pay)
    ment_pay_df = ment_pay_df.T
    ment_pay_df.columns = ["m_pay"]

    # Get Mentor pay highlighted text
    ment_pay_HT = highlighted_text(mentor_paid_or_compensated)
    ment_pay_HT_df = pd.DataFrame(ment_pay_HT)
    ment_pay_HT_df = ment_pay_HT_df.T
    ment_pay_HT_df.columns = ["m_pay_ht"]

    # Get Mentor pay user comments
    ment_pay_Comments = comments(mentor_paid_or_compensated)
    ment_pay_Comments_df = pd.DataFrame(ment_pay_Comments)
    ment_pay_Comments_df = ment_pay_Comments_df.T
    ment_pay_Comments_df.columns = ["m_pay_info"]

    # get Mentor org data
    ment_org = get_data(mentor_organisation)
    ment_org_df = pd.DataFrame(ment_org)
    ment_org_df = ment_org_df.T
    ment_org_df.columns = ["m_org"]

    # Get Mentor org highlighted text
    ment_org_HT = highlighted_text(mentor_organisation)
    ment_org_HT_df = pd.DataFrame(ment_org_HT)
    ment_org_HT_df = ment_org_HT_df.T
    ment_org_HT_df.columns = ["m_org_ht"]

    # Get Mentor org user comments
    ment_org_Comments = comments(mentor_organisation)
    ment_org_Comments_df = pd.DataFrame(ment_org_Comments)
    ment_org_Comments_df = ment_org_Comments_df.T
    ment_org_Comments_df.columns = ["m_org_info"]

    # get Mentor training data
    ment_training = get_data(mentor_training)
    ment_training_df = pd.DataFrame(ment_training)
    ment_training_df = ment_training_df.T
    ment_training_df.columns = ["m_training"]

    # Get Mentor training highlighted text
    ment_training_HT = highlighted_text(mentor_training)
    ment_training_HT_df = pd.DataFrame(ment_training_HT)
    ment_training_HT_df = ment_training_HT_df.T
    ment_training_HT_df.columns = ["m_training_ht"]

    # Get Mentor training user comments
    ment_training_Comments = comments(mentor_training)
    ment_training_Comments_df = pd.DataFrame(ment_training_Comments)
    ment_training_Comments_df = ment_training_Comments_df.T
    ment_training_Comments_df.columns = ["m_training_info"]

    # get Mentor meeting freq data
    ment_meeting_freq = get_data(mentor_meeting_frequency)
    ment_meeting_freq_df = pd.DataFrame(ment_meeting_freq)
    ment_meeting_freq_df = ment_meeting_freq_df.T
    ment_meeting_freq_df.columns = ["m_meeting_freq"]

    # Get Mentor meeting freq highlighted text
    ment_meeting_freq_HT = highlighted_text(mentor_meeting_frequency)
    ment_meeting_freq_HT_df = pd.DataFrame(ment_meeting_freq_HT)
    ment_meeting_freq_HT_df = ment_meeting_freq_HT_df.T
    ment_meeting_freq_HT_df.columns = ["m_meeting_freq_ht"]

    # Get Mentor meeting freq user comments
    ment_meeting_freq_Comments = comments(mentor_meeting_frequency)
    ment_meeting_freq_Comments_df = pd.DataFrame(ment_meeting_freq_Comments)
    ment_meeting_freq_Comments_df = ment_meeting_freq_Comments_df.T
    ment_meeting_freq_Comments_df.columns = ["m_meeting_freq_info"]

    # get Mentor meeting details data
    ment_meeting_details = get_data(mentor_meeting_details_provided)
    ment_meeting_details_df = pd.DataFrame(ment_meeting_details)
    ment_meeting_details_df = ment_meeting_details_df.T
    ment_meeting_details_df.columns = ["m_meeting_details"]

    # Get Mentor meeting details highlighted text
    ment_meeting_details_HT = highlighted_text(mentor_meeting_details_provided)
    ment_meeting_details_HT_df = pd.DataFrame(ment_meeting_details_HT)
    ment_meeting_details_HT_df = ment_meeting_details_HT_df.T
    ment_meeting_details_HT_df.columns = ["m_meeting_details_ht"]

    # Get Mentor meeting details user comments
    ment_meeting_details_Comments = comments(mentor_meeting_details_provided)
    ment_meeting_details_Comments_df = pd.DataFrame(ment_meeting_details_Comments)
    ment_meeting_details_Comments_df = ment_meeting_details_Comments_df.T
    ment_meeting_details_Comments_df.columns = ["m_meeting_details_info"]

    # get Mentor meeting location data
    ment_meeting_location = get_data(mentor_meeting_location)
    ment_meeting_location_df = pd.DataFrame(ment_meeting_location)
    ment_meeting_location_df = ment_meeting_location_df.T
    ment_meeting_location_df.columns = ["m_meeting_location"]

    # Get Mentor meeting location highlighted text
    ment_meeting_location_HT = highlighted_text(mentor_meeting_location)
    ment_meeting_location_HT_df = pd.DataFrame(ment_meeting_location_HT)
    ment_meeting_location_HT_df = ment_meeting_location_HT_df.T
    ment_meeting_location_HT_df.columns = ["m_meeting_location_ht"]

    # Get Mentor meeting location user comments
    ment_meeting_location_Comments = comments(mentor_meeting_location)
    ment_meeting_location_Comments_df = pd.DataFrame(ment_meeting_location_Comments)
    ment_meeting_location_Comments_df = ment_meeting_location_Comments_df.T
    ment_meeting_location_Comments_df.columns = ["m_meeting_location_info"]

    # get Mentor additional experiences data
    ment_addit_exp = get_data(mentoring_additional_experiences)
    ment_addit_exp_df = pd.DataFrame(ment_addit_exp)
    ment_addit_exp_df = ment_addit_exp_df.T
    ment_addit_exp_df.columns = ["m_addit_exp"]

    # Get Mentor additional experiences highlighted text
    ment_addit_exp_HT = highlighted_text(mentoring_additional_experiences)
    ment_addit_exp_HT_df = pd.DataFrame(ment_addit_exp_HT)
    ment_addit_exp_HT_df = ment_addit_exp_HT_df.T
    ment_addit_exp_HT_df.columns = ["m_addit_exp_ht"]

    # Get Mentor additional experiences user comments
    ment_addit_exp_Comments = comments(mentoring_additional_experiences)
    ment_addit_exp_Comments_df = pd.DataFrame(ment_addit_exp_Comments)
    ment_addit_exp_Comments_df = ment_addit_exp_Comments_df.T
    ment_addit_exp_Comments_df.columns = ["m_addit_exp_info"]

    # get Mentor prog focus data
    ment_prog_focus = get_data(mentoring_programme_focus)
    ment_prog_focus_df = pd.DataFrame(ment_prog_focus)
    ment_prog_focus_df = ment_prog_focus_df.T
    ment_prog_focus_df.columns = ["m_prog_focus"]

    # Get Mentor prog focus highlighted text
    ment_prog_focus_HT = highlighted_text(mentoring_programme_focus)
    ment_prog_focus_HT_df = pd.DataFrame(ment_prog_focus_HT)
    ment_prog_focus_HT_df = ment_prog_focus_HT_df.T
    ment_prog_focus_HT_df.columns = ["m_prog_focus_ht"]

    # Get Mentor prog focus user comments
    ment_prog_focus_Comments = comments(mentoring_programme_focus)
    ment_prog_focus_Comments_df = pd.DataFrame(ment_prog_focus_Comments)
    ment_prog_focus_Comments_df = ment_prog_focus_Comments_df.T
    ment_prog_focus_Comments_df.columns = ["m_prog_focus_info"]

    # concatenate data frames
    mentoring_ss_df = pd.concat([
        ment_ident_df,
        ment_pay_df,
        ment_org_df,
        ment_training_df,
        ment_meeting_freq_df,
        ment_meeting_details_df,
        ment_meeting_location_df,
        ment_addit_exp_df,
        ment_prog_focus_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    mentoring_ss_df.fillna("NA", inplace=True)

    return mentoring_ss_df

def mastery_learning_ss():
    from AttributeIDList import ml_theor_output
    from AttributeIDList import ml_age_group_output
    from AttributeIDList import ml_ability_group_output
    from AttributeIDList import ml_if_attain_what_grouping_type_output
    from AttributeIDList import ml_goal_level
    from AttributeIDList import ml_assess_detail
    from AttributeIDList import ml_fb_detail_prov
    from AttributeIDList import ml_mastery_level
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

    return ml_ss_df

def metacog_self_reg_ss():
    from AttributeIDList import msr_knowl_type_output
    from AttributeIDList import msr_task_stage_output
    from AttributeIDList import msr_strategy_type_output
    from AttributeIDList import msr_self_reg_mot_aspects_output
    from AttributeIDList import msr_teaching_approach_output
    from AttributeIDList import msr_digit_tech
    # get msr knowledge type data
    msr_knowl_type = get_data(msr_knowl_type_output)
    msr_knowl_type_df = pd.DataFrame(msr_knowl_type)
    msr_knowl_type_df = msr_knowl_type_df.T
    msr_knowl_type_df.columns = ["msr_knowl_type"]

    # get msr task stage data
    msr_task_stage = get_data(msr_task_stage_output)
    msr_task_stage_df = pd.DataFrame(msr_task_stage)
    msr_task_stage_df = msr_task_stage_df.T
    msr_task_stage_df.columns = ["msr_task_stage"]

    # get msr strategy type data
    msr_strategy = get_data(msr_strategy_type_output)
    msr_strategy_df = pd.DataFrame(msr_strategy)
    msr_strategy_df = msr_strategy_df.T
    msr_strategy_df.columns = ["msr_strategy"]

    # get msr motivational aspects data
    msr_motiv_aspects = get_data(msr_self_reg_mot_aspects_output)
    msr_motiv_aspects_df = pd.DataFrame(msr_motiv_aspects)
    msr_motiv_aspects_df = msr_motiv_aspects_df.T
    msr_motiv_aspects_df.columns = ["msr_motiv_aspects"]

    # get msr teaching approach data
    msr_teaching_approach = get_data(msr_teaching_approach_output)
    msr_teaching_approach_df = pd.DataFrame(msr_teaching_approach)
    msr_teaching_approach_df = msr_teaching_approach_df.T
    msr_teaching_approach_df.columns = ["msr_teaching_approach"]

    # get msr dig tech data
    msr_digit_tech = get_data(msr_digit_tech)
    msr_digit_tech_df = pd.DataFrame(msr_digit_tech)
    msr_digit_tech_df = msr_digit_tech_df.T
    msr_digit_tech_df.columns = ["msr_digit_tech"]

    msr_ss_df = pd.concat([
        msr_knowl_type_df,
        msr_task_stage_df,
        msr_strategy_df,
        msr_motiv_aspects_df,
        msr_teaching_approach_df,
        msr_digit_tech_df
    ], axis=1, sort=False)

    # fill blanks with NA
    msr_ss_df.fillna("NA", inplace=True)
    return msr_ss_df

def oral_lang_ss():
    from AttributeIDList import ol_focus
    from AttributeIDList import ol_target
    from AttributeIDList import ol_imp_comp_type
    from AttributeIDList import ol_activity_invol
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
    return ol_ss_df

def one_t_one_comp_ss():
    from AttributeIDList import comparisons_available
    # get one-to-one comparisons data
    comp_avail = get_data(comparisons_available)
    comp_avail_df = pd.DataFrame(comp_avail)
    comp_avail_df = comp_avail_df.T
    comp_avail_df.columns = ["1_1_comparisons_Available"]

    # Get one-to-one comparisons highlighted text
    comp_avail_HT = highlighted_text(comparisons_available)
    comp_avail_HT_df = pd.DataFrame(comp_avail_HT)
    comp_avail_HT_df = comp_avail_HT_df.T
    comp_avail_HT_df.columns = ["1_1_comparisons_Available_SS_ht"]

    # Get one-to-one comparisons user comments
    comp_avail_Comments = comments(comparisons_available)
    comp_avail_Comments_df = pd.DataFrame(comp_avail_Comments)
    comp_avail_Comments_df = comp_avail_Comments_df.T
    comp_avail_Comments_df.columns = ["1_1_comparisons_Available_SS_info"]

    # concatenate data frames
    one_to_one_ss_df = pd.concat([
        comp_avail_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    one_to_one_ss_df.fillna("NA", inplace=True)

    # remove problematic text from outputs
    clean_up(one_to_one_ss_df)

    return one_to_one_ss_df

def peer_tut():
    from AttributeIDList import tutor_age_output
    from AttributeIDList import tutor_same_age_output
    from AttributeIDList import tutor_cross_age_output
    from AttributeIDList import tutor_from_output
    from AttributeIDList import tutor_role_output
    from AttributeIDList import tutee_attainment_output
    from AttributeIDList import digit_tech_output
    from AttributeIDList import tutor_tutee_incentive_output
    from AttributeIDList import tutor_age_same, tutor_age_cross
    from AttributeIDList import tutor_age_cross

    # get tutor desc data
    tut_desc = get_data(tutor_age_output)
    tut_desc_df = pd.DataFrame(tut_desc)
    tut_desc_df = tut_desc_df.T
    tut_desc_df.columns = ["pt_tut_desc"]

    # split tutor desc components for ind col extraction

    # tutor same age
    tut_desc_same_age = get_data(tutor_age_same)
    tut_desc_same_age_df = pd.DataFrame(tut_desc_same_age)
    tut_desc_same_age_df = tut_desc_same_age_df.T
    tut_desc_same_age_df.columns = ["pt_tut_desc_same_age"]

    # tutor cross age
    tut_desc_cross_age = get_data(tutor_age_cross)
    tut_desc_cross_age_df = pd.DataFrame(tut_desc_cross_age)
    tut_desc_cross_age_df = tut_desc_cross_age_df.T
    tut_desc_cross_age_df.columns = ["pt_tut_desc_cross_age"]

    # nested tutor same age responses
    tut_same_age = get_data(tutor_same_age_output)
    tut_same_age_df = pd.DataFrame(tut_same_age)
    tut_same_age_df = tut_same_age_df.T
    tut_same_age_df.columns = ["pt_same_age_attainment"]

    # nested tutor cross age responses
    tut_cross_age = get_data(tutor_cross_age_output)
    tut_cross_age_df = pd.DataFrame(tut_cross_age)
    tut_cross_age_df = tut_cross_age_df.T
    tut_cross_age_df.columns = ["pt_cross_age_attainment"]

    # get tutor where from data
    tut_from = get_data(tutor_from_output)
    tut_from_df = pd.DataFrame(tut_from)
    tut_from_df = tut_from_df.T
    tut_from_df.columns = ["pt_tut_from"]

    # get tutor role data
    tut_role = get_data(tutor_role_output)
    tut_role_df = pd.DataFrame(tut_role)
    tut_role_df = tut_role_df.T
    tut_role_df.columns = ["pt_tut_role"]

    # get tutee attainment level data
    tut_tutee_attain_lev = get_data(tutee_attainment_output)
    tut_tutee_attain_lev_df = pd.DataFrame(tut_tutee_attain_lev)
    tut_tutee_attain_lev_df = tut_tutee_attain_lev_df.T
    tut_tutee_attain_lev_df.columns = ["pt_tutee_attain_level"]

    # get digit tech data
    digit_tech = get_data(digit_tech_output)
    digit_tech_df = pd.DataFrame(digit_tech)
    digit_tech_df = digit_tech_df.T
    digit_tech_df.columns = ["pt_digit_tech"]

    # get incentive data
    tut_incentive = get_data(tutor_tutee_incentive_output)
    tut_incentive_df = pd.DataFrame(tut_incentive)
    tut_incentive_df = tut_incentive_df.T
    tut_incentive_df.columns = ["pt_incentive"]

    peer_tut_ss_df = pd.concat([
        tut_desc_df,
        tut_desc_same_age_df,
        tut_desc_cross_age_df,

        tut_same_age_df,
        tut_cross_age_df,
        tut_from_df,
        tut_role_df,
        tut_tutee_attain_lev_df,
        digit_tech_df,
        tut_incentive_df,
    ], axis=1, sort=False)

    return peer_tut_ss_df

def phys_activity_ss():
    from AttributeIDList import pha_when_output
    from AttributeIDList import pha_lessons_included_output
    from AttributeIDList import pha_activity_type_output
    from AttributeIDList import pha_exercise_level_output
    # get when? data
    pha_when = get_data(pha_when_output)
    pha_when_df = pd.DataFrame(pha_when)
    pha_when_df = pha_when_df.T
    pha_when_df.columns = ["pa_when"]

    # get lessons included data
    pha_lessons = get_data(pha_lessons_included_output)
    pha_lessons_df = pd.DataFrame(pha_lessons)
    pha_lessons_df = pha_lessons_df.T
    pha_lessons_df.columns = ["pa_lessons"]

    # get activity type data
    pha_act_type = get_data(pha_activity_type_output)
    pha_act_type_df = pd.DataFrame(pha_act_type)
    pha_act_type_df = pha_act_type_df.T
    pha_act_type_df.columns = ["pa_act_type"]

    # get exercise level data
    pha_exer_level = get_data(pha_exercise_level_output)
    pha_exer_level_df = pd.DataFrame(pha_exer_level)
    pha_exer_level_df = pha_exer_level_df.T
    pha_exer_level_df.columns = ["pa_exer_level"]

    pha_ss_df = pd.concat([
        pha_when_df,
        pha_lessons_df,
        pha_act_type_df,
        pha_exer_level_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    pha_ss_df.fillna("NA", inplace=True)
    return pha_ss_df

def read_comprehension_ss():
    from AttributeIDList import rc_components_output
    from AttributeIDList import rc_strat_instruct_type_output
    from AttributeIDList import rc_instruct_components_output
    from AttributeIDList import rc_txt_type_output

    from AttributeIDList import rc_comp_strat_output
    from AttributeIDList import rc_comp_vocab_output
    from AttributeIDList import rc_comp_red_flu_output
    from AttributeIDList import rc_comp_phon_output
    from AttributeIDList import rc_comp_wri_output
    from AttributeIDList import rc_comp_other_output
    from AttributeIDList import rc_comp_unclear_output
    # get rc components data
    rc_comp = get_data(rc_components_output)
    rc_comp_df = pd.DataFrame(rc_comp)
    rc_comp_df = rc_comp_df.T
    rc_comp_df.columns = ["rc_comp"]

    # split rc components for ind col extraction

    # rc comp strat data
    rc_comp_strat = get_data(rc_comp_strat_output)
    rc_comp_strat_df = pd.DataFrame(rc_comp_strat)
    rc_comp_strat_df = rc_comp_strat_df.T
    rc_comp_strat_df.columns = ["rc_comp_strat"]

    # rc comp vocab data
    rc_comp_vocab = get_data(rc_comp_vocab_output)
    rc_comp_vocab_df = pd.DataFrame(rc_comp_vocab)
    rc_comp_vocab_df = rc_comp_vocab_df.T
    rc_comp_vocab_df.columns = ["rc_comp_vocab"]

    # rc comp reading fluency data
    rc_comp_red_flu = get_data(rc_comp_red_flu_output)
    rc_comp_red_flu_df = pd.DataFrame(rc_comp_red_flu)
    rc_comp_red_flu_df = rc_comp_red_flu_df.T
    rc_comp_red_flu_df.columns = ["rc_comp_red_flu"]

    # rc comp phonics fluency data
    rc_comp_phon = get_data(rc_comp_phon_output)
    rc_comp_phon_df = pd.DataFrame(rc_comp_phon)
    rc_comp_phon_df = rc_comp_phon_df.T
    rc_comp_phon_df.columns = ["rc_comp_phon"]

    # rc comp writing data
    rc_comp_wri = get_data(rc_comp_wri_output)
    rc_comp_wri_df = pd.DataFrame(rc_comp_wri)
    rc_comp_wri_df = rc_comp_wri_df.T
    rc_comp_wri_df.columns = ["rc_comp_wri"]

    # rc comp other data
    rc_comp_other = get_data(rc_comp_other_output)
    rc_comp_other_df = pd.DataFrame(rc_comp_other)
    rc_comp_other_df = rc_comp_other_df.T
    rc_comp_other_df.columns = ["rc_comp_other"]

    # rc comp unclear data
    rc_comp_unclear = get_data(rc_comp_unclear_output)
    rc_comp_unclear_df = pd.DataFrame(rc_comp_unclear)
    rc_comp_unclear_df = rc_comp_unclear_df.T
    rc_comp_unclear_df.columns = ["rc_comp_unclear"]

    # ^^ end of individual column extraction ^^*

    # get rc strategy instruction data
    rc_strat_instr = get_data(rc_strat_instruct_type_output)
    rc_strat_instr_df = pd.DataFrame(rc_strat_instr)
    rc_strat_instr_df = rc_strat_instr_df.T
    rc_strat_instr_df.columns = ["rc_strat_instruc"]

    # get rc instructional components data
    rc_instruc_comp = get_data(rc_comp_other_output)
    rc_instruc_comp_df = pd.DataFrame(rc_instruc_comp)
    rc_instruc_comp_df = rc_instruc_comp_df.T
    rc_instruc_comp_df.columns = ["rc_instruc_comp"]

    # get rc text type / reading materials data
    rc_txt_type = get_data(rc_txt_type_output)
    rc_txt_type_df = pd.DataFrame(rc_txt_type)
    rc_txt_type_df = rc_txt_type_df.T
    rc_txt_type_df.columns = ["rc_txt_type_red_mat"]

    rc_ss_df = pd.concat([
        rc_comp_df,
        rc_comp_strat_df,
        rc_comp_vocab_df,
        rc_comp_red_flu_df,
        rc_comp_phon_df,
        rc_comp_wri_df,
        rc_comp_other_df,
        rc_comp_unclear_df,

        rc_strat_instr_df,
        rc_instruc_comp_df,
        rc_txt_type_df,
    ], axis=1, sort=False)

    return rc_ss_df

def red_class_size_ss():
    from AttributeIDList import redc_avg_small_class_size_output
    from AttributeIDList import redc_avg_large_class_size_output
    from AttributeIDList import redc_small_class_teacher_number_output
    from AttributeIDList import redc_large_class_teacher_number_output
    from AttributeIDList import redc_large_class_adaption_output
    from AttributeIDList import redc_reduc_for_limited_num_sub_output
    from AttributeIDList import redc_impl_for_all_or_most_output
    # get typical or average small class size info
    redc_avg_small_class_size = comments(redc_avg_small_class_size_output)
    redc_avg_small_class_size_df = pd.DataFrame(redc_avg_small_class_size)
    redc_avg_small_class_size_df = redc_avg_small_class_size_df.T
    redc_avg_small_class_size_df.columns = ["redc_avg_small_class_size_info"]

    # get typical or average large class size info
    redc_avg_large_class_size = comments(redc_avg_large_class_size_output)
    redc_avg_large_class_size_df = pd.DataFrame(redc_avg_large_class_size)
    redc_avg_large_class_size_df = redc_avg_large_class_size_df.T
    redc_avg_large_class_size_df.columns = ["redc_avg_large_class_size_info"]

    # get small class teacher numb data
    redc_small_class_teach_num = get_data(redc_small_class_teacher_number_output)
    redc_small_class_teach_num_df = pd.DataFrame(redc_small_class_teach_num)
    redc_small_class_teach_num_df = redc_small_class_teach_num_df.T
    redc_small_class_teach_num_df.columns = ["redc_small_class_teach_num"]

    # get large class teacher numb data
    redc_large_class_teach_num = get_data(redc_large_class_teacher_number_output)
    redc_large_class_teach_num_df = pd.DataFrame(redc_large_class_teach_num)
    redc_large_class_teach_num_df = redc_large_class_teach_num_df.T
    redc_large_class_teach_num_df.columns = ["redc_large_class_teach_num"]

    # get large class adaption data
    redc_large_class_adapt = get_data(redc_large_class_adaption_output)
    redc_large_class_adapt_df = pd.DataFrame(redc_large_class_adapt)
    redc_large_class_adapt_df = redc_large_class_adapt_df.T
    redc_large_class_adapt_df.columns = ["redc_large_class_adapt"]

    # get limited number of subjects data
    redc_lim_num_subj = get_data(redc_reduc_for_limited_num_sub_output)
    redc_lim_num_subj_df = pd.DataFrame(redc_lim_num_subj)
    redc_lim_num_subj_df = redc_lim_num_subj_df.T
    redc_lim_num_subj_df.columns = ["redc_lim_num_subj"]

    # get reduction for all or most lessons across curriculum data
    redc_impl_all_or_most_lessons = get_data(redc_impl_for_all_or_most_output)
    redc_impl_all_or_most_lessons_df = pd.DataFrame(redc_impl_all_or_most_lessons)
    redc_impl_all_or_most_lessons_df = redc_impl_all_or_most_lessons_df.T
    redc_impl_all_or_most_lessons_df.columns = ["redc_impl_all_or_most_lessons"]

    redc_ss_df = pd.concat([
        redc_avg_small_class_size_df,
        redc_avg_large_class_size_df,
        redc_small_class_teach_num_df,
        redc_large_class_teach_num_df,
        redc_large_class_adapt_df,
        redc_lim_num_subj_df,
        redc_impl_all_or_most_lessons_df,
    ], axis=1, sort=False)

    return redc_ss_df

def repeat_year_ss():
    from AttributeIDList import ry_ret_stu_identify_output
    from AttributeIDList import ry_ret_stu_age_output
    from AttributeIDList import ry_ret_basis_output
    from AttributeIDList import ry_impact_measure_delay_output
    from AttributeIDList import ry_stu_ret_number_output
    from AttributeIDList import ry_ret_stud_compared_with_output
    from AttributeIDList import ry_prom_count_characteristics_output
    from AttributeIDList import ry_comparison
    from AttributeIDList import ry_comp_grp_school
    # get identify retained students data
    ry_identify_ret_stu = get_data(ry_ret_stu_identify_output)
    ry_identify_ret_stu_df = pd.DataFrame(ry_identify_ret_stu)
    ry_identify_ret_stu_df = ry_identify_ret_stu_df.T
    ry_identify_ret_stu_df.columns = ["ry_identify_ret_stu"]

    # get retained students age data
    ry_ret_stu_age = get_data(ry_ret_stu_age_output)
    ry_ret_stu_age_df = pd.DataFrame(ry_ret_stu_age)
    ry_ret_stu_age_df = ry_ret_stu_age_df.T
    ry_ret_stu_age_df.columns = ["ry_ret_stu_age"]

    # get retention basis data
    ry_ret_basis = get_data(ry_ret_basis_output)
    ry_ret_basis_df = pd.DataFrame(ry_ret_basis)
    ry_ret_basis_df = ry_ret_basis_df.T
    ry_ret_basis_df.columns = ["ry_ret_basis"]

    # get impact measure data
    ry_impact_meas = get_data(ry_impact_measure_delay_output)
    ry_impact_meas_df = pd.DataFrame(ry_impact_meas)
    ry_impact_meas_df = ry_impact_meas_df.T
    ry_impact_meas_df.columns = ["ry_impact_meas"]

    # get number of times students were retained data
    ry_stu_ret_num = get_data(ry_stu_ret_number_output)
    ry_stu_ret_num_df = pd.DataFrame(ry_stu_ret_num)
    ry_stu_ret_num_df = ry_stu_ret_num_df.T
    ry_stu_ret_num_df.columns = ["ry_stu_ret_num"]

    # get retained students compared with data
    ry_ret_stu_comparison = get_data(ry_ret_stud_compared_with_output)
    ry_ret_stu_comparison_df = pd.DataFrame(ry_ret_stu_comparison)
    ry_ret_stu_comparison_df = ry_ret_stu_comparison_df.T
    ry_ret_stu_comparison_df.columns = ["ry_ret_stud_comp"]

    # get promoted counterpart characteristics data
    ry_prom_count_char = get_data(ry_prom_count_characteristics_output)
    ry_prom_count_char_df = pd.DataFrame(ry_prom_count_char)
    ry_prom_count_char_df = ry_prom_count_char_df.T
    ry_prom_count_char_df.columns = ["ry_matching_char"]

    # get comparison data
    ry_comp = get_data(ry_comparison)
    ry_comp_df = pd.DataFrame(ry_comp)
    ry_comp_df = ry_comp_df.T
    ry_comp_df.columns = ["ry_comp"]

    # get comparison group same school as retained students data
    ry_comp_grp_school = get_data(ry_comp_grp_school)
    ry_comp_grp_school_df = pd.DataFrame(ry_comp_grp_school)
    ry_comp_grp_school_df = ry_comp_grp_school_df.T
    ry_comp_grp_school_df.columns = ["ry_comp_grp_school"]

    # concatenate data frames
    ry_ss_df = pd.concat([
        ry_identify_ret_stu_df,
        ry_ret_stu_age_df,
        ry_ret_basis_df,
        ry_impact_meas_df,
        ry_stu_ret_num_df,
        ry_ret_stu_comparison_df,
        ry_prom_count_char_df,
        ry_comp_df,
        ry_comp_grp_school_df,
    ], axis=1, sort=False)

    # remove problematic text from outputs
    clean_up(ry_ss_df)

    return ry_ss_df

def soc_emo_learning_ss():
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

    return sel_ss_df

def setting_streaming_ss():
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

    return sets_ss_df

def small_group_tuit_ss():
    from AttributeIDList import group_size_output
    from AttributeIDList import group_composition_output
    from AttributeIDList import group_teaching_lead_output

    # get group size data
    group_size = get_data(group_size_output)
    group_size_df = pd.DataFrame(group_size)
    group_size_df = group_size_df.T
    group_size_df.columns = ["sgt_group_size"]

    # Get group size highlighted text
    group_size_HT = highlighted_text(group_size_output)
    group_size_HT_df = pd.DataFrame(group_size_HT)
    group_size_HT_df = group_size_HT_df.T
    group_size_HT_df.columns = ["sgt_group_size_ht"]

    # Get group size user comments
    group_size_Comments = comments(group_size_output)
    group_size_Comments_df = pd.DataFrame(group_size_Comments)
    group_size_Comments_df = group_size_Comments_df.T
    group_size_Comments_df.columns = ["sgt_group_size_info"]

    # get group composition data
    group_composition = get_data(group_composition_output)
    group_composition_df = pd.DataFrame(group_composition)
    group_composition_df = group_composition_df.T
    group_composition_df.columns = ["sgt_group_composition"]

    # Get group composition highlighted text
    group_composition_HT = highlighted_text(group_composition_output)
    group_composition_HT_df = pd.DataFrame(group_composition_HT)
    group_composition_HT_df = group_composition_HT_df.T
    group_composition_HT_df.columns = ["sgt_group_composition_ht"]

    # Get group composition user comments
    group_composition_Comments = comments(group_composition_output)
    group_composition_Comments_df = pd.DataFrame(group_composition_Comments)
    group_composition_Comments_df = group_composition_Comments_df.T
    group_composition_Comments_df.columns = ["sgt_group_composition_info"]

    # get group composition data
    group_lead = get_data(group_teaching_lead_output)
    group_lead_df = pd.DataFrame(group_lead)
    group_lead_df = group_lead_df.T
    group_lead_df.columns = ["sgt_group_lead"]

    # Get group composition highlighted text
    group_lead_HT = highlighted_text(group_teaching_lead_output)
    group_lead_HT_df = pd.DataFrame(group_lead_HT)
    group_lead_HT_df = group_lead_HT_df.T
    group_lead_HT_df.columns = ["sgt_group_lead_ht"]

    # Get group composition user comments
    group_lead_Comments = comments(group_teaching_lead_output)
    group_lead_Comments_df = pd.DataFrame(group_lead_Comments)
    group_lead_Comments_df = group_lead_Comments_df.T
    group_lead_Comments_df.columns = ["sgt_group_lead_info"]

    sgt_ss_df = pd.concat([
        group_size_df,
        group_composition_df,
        group_lead_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    sgt_ss_df.fillna("NA", inplace=True)

    return sgt_ss_df

def summer_school_ss():
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
    return SS_ss_df

def teach_assistants_ss():

    from AttributeIDList import ta_description_output
    from AttributeIDList import ta_role_output
    from AttributeIDList import ta_group_size_output

    # get teaching assistants description data
    ta_desc = get_data(ta_description_output)
    ta_desc_df = pd.DataFrame(ta_desc)
    ta_desc_df = ta_desc_df.T
    ta_desc_df.columns = ["ta_desc"]

    # Get teaching assistants description highlighted text
    ta_desc_HT = highlighted_text(ta_description_output)
    ta_desc_HT_df = pd.DataFrame(ta_desc_HT)
    ta_desc_HT_df = ta_desc_HT_df.T
    ta_desc_HT_df.columns = ["ta_desc_ht"]

    # Get teaching assistants description user comments
    ta_desc_Comments = comments(ta_description_output)
    ta_desc_Comments_df = pd.DataFrame(ta_desc_Comments)
    ta_desc_Comments_df = ta_desc_Comments_df.T
    ta_desc_Comments_df.columns = ["ta_desc_info"]

    # TEACHING ASSISTANTS ROLE

    # get teaching assistants description data
    ta_role = get_data(ta_role_output)
    ta_role_df = pd.DataFrame(ta_role)
    ta_role_df = ta_role_df.T
    ta_role_df.columns = ["ta_role"]

    # Get teaching assistants description highlighted text
    ta_role_HT = highlighted_text(ta_role_output)
    ta_role_HT_df = pd.DataFrame(ta_role_HT)
    ta_role_HT_df = ta_role_HT_df.T
    ta_role_HT_df.columns = ["ta_role_ht"]

    # Get teaching assistants description user comments
    ta_role_Comments = comments(ta_role_output)
    ta_desc_Comments_df = pd.DataFrame(ta_role_Comments)
    ta_desc_Comments_df = ta_desc_Comments_df.T
    ta_desc_Comments_df.columns = ["ta_role_info"]

    # TEACHING GROUP SIZE

    # get teaching assistants group size data
    ta_group_size = get_data(ta_group_size_output)
    ta_group_size_df = pd.DataFrame(ta_group_size)
    ta_group_size_df = ta_group_size_df.T
    ta_group_size_df.columns = ["ta_group_size"]

    # get teaching assistants group size highlighted text
    ta_group_size_HT = highlighted_text(ta_group_size_output)
    ta_group_size_HT_df = pd.DataFrame(ta_group_size_HT)
    ta_group_size_HT_df = ta_group_size_HT_df.T
    ta_group_size_HT_df.columns = ["ta_group_size_ht"]

    # get teaching assistants group size user comments
    ta_group_size_Comments = comments(ta_group_size_output)
    ta_group_size_Comments_df = pd.DataFrame(ta_group_size_Comments)
    ta_group_size_Comments_df = ta_group_size_Comments_df.T
    ta_group_size_Comments_df.columns = ["ta_group_size_info"]

    # concatenate data frames
    ta_ss_df = pd.concat([
        ta_desc_df,
        ta_role_df,
        ta_group_size_df,

    ], axis=1, sort=False)

    # remove problematic text from outputs
    clean_up(ta_ss_df)
    
    return ta_ss_df

def parental_engagement():
    from AttributeIDList import pe_involved_output
    from AttributeIDList import pe_activity_location_output
    from AttributeIDList import pe_prog_training_output
    from AttributeIDList import pe_prog_support_output
    from AttributeIDList import pe_children_output
    from AttributeIDList import pe_focus_output
    # get who was involved data
    pe_involved = get_data(pe_involved_output)
    pe_involved_df = pd.DataFrame(pe_involved)
    pe_involved_df = pe_involved_df.T
    pe_involved_df.columns = ["pe_involved"]

    # get activiyt location data
    pe_act_loc = get_data(pe_activity_location_output)
    pe_act_loc_df = pd.DataFrame(pe_act_loc)
    pe_act_loc_df = pe_act_loc_df.T
    pe_act_loc_df.columns = ["pe_act_loc"]

    # get programme training data
    pe_prog_train = get_data(pe_prog_training_output)
    pe_prog_train_df = pd.DataFrame(pe_prog_train)
    pe_prog_train_df = pe_prog_train_df.T
    pe_prog_train_df.columns = ["pe_prog_training"]

    # get programme support data
    pe_prog_support = get_data(pe_prog_support_output)
    pe_prog_support_df = pd.DataFrame(pe_prog_support)
    pe_prog_support_df = pe_prog_support_df.T
    pe_prog_support_df.columns = ["pe_prog_support"]

    # get children data
    pe_children_work_with = get_data(pe_children_output)
    pe_children_work_with_df = pd.DataFrame(pe_children_work_with)
    pe_children_work_with_df = pe_children_work_with_df.T
    pe_children_work_with_df.columns = ["pe_children"]

    # get engagement focus data
    pe_focus = get_data(pe_focus_output)
    pe_focus_df = pd.DataFrame(pe_focus)
    pe_focus_df = pe_focus_df.T
    pe_focus_df.columns = ["pe_focus"]

    pe_ss_df = pd.concat([
        pe_involved_df,
        pe_act_loc_df,
        pe_prog_train_df,
        pe_prog_support_df,
        pe_children_work_with_df,
        pe_focus_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    pe_ss_df.fillna("NA", inplace=True)
    return pe_ss_df

def phonics():
    from AttributeIDList import ph_targ_pop_output
    from AttributeIDList import ph_constit_part_approach_output
    from AttributeIDList import ph_central_teach_lit_output
    from AttributeIDList import ph_par_invol_output
    from AttributeIDList import ph_digit_tech_output

    from AttributeIDList import ph_constit_part_approach_synth_ph
    from AttributeIDList import ph_constit_part_approach_syst_ph
    from AttributeIDList import ph_constit_part_approach_analyt_ph
    from AttributeIDList import ph_constit_part_approach_analog_ph
    from AttributeIDList import ph_constit_part_approach_emb_ph
    from AttributeIDList import ph_constit_part_approach_phon_aware
    from AttributeIDList import ph_constit_part_approach_phonol_aware
    from AttributeIDList import ph_constit_part_approach_onset_rime
    from AttributeIDList import ph_constit_part_approach_syll_instr
    from AttributeIDList import ph_constit_part_approach_sight_vocab
    from AttributeIDList import ph_constit_part_approach_whole_word

    # get phonics target population data
    ph_tar_pop = get_data(ph_targ_pop_output)
    ph_tar_pop_df = pd.DataFrame(ph_tar_pop)
    ph_tar_pop_df = ph_tar_pop_df.T
    ph_tar_pop_df.columns = ["ph_targ_pop"]

    # get phonics constituent part of approach data
    ph_const_part = get_data(ph_constit_part_approach_output)
    ph_const_part_df = pd.DataFrame(ph_const_part)
    ph_const_part_df = ph_const_part_df.T
    ph_const_part_df.columns = ["ph_constit_part"]

    # split constituent part (above) for individual column extraction

    # constituent part of approach: synthetic phonics
    ph_const_part_synth = get_data(ph_constit_part_approach_synth_ph)
    ph_const_part_synth_df = pd.DataFrame(ph_const_part_synth)
    ph_const_part_synth_df = ph_const_part_synth_df.T
    ph_const_part_synth_df.columns = ["ph_constit_part_synth_phon"]

    # constituent part of approach: systematic phonics
    ph_const_part_sys = get_data(ph_constit_part_approach_syst_ph)
    ph_const_part_sys_df = pd.DataFrame(ph_const_part_sys)
    ph_const_part_sys_df = ph_const_part_sys_df.T
    ph_const_part_sys_df.columns = ["ph_constit_part_sys_phon"]

    # constituent part of approach: analytic phonics
    ph_const_part_analyt = get_data(ph_constit_part_approach_analyt_ph)
    ph_const_part_analyt_df = pd.DataFrame(ph_const_part_analyt)
    ph_const_part_analyt_df = ph_const_part_analyt_df.T
    ph_const_part_analyt_df.columns = ["ph_constit_part_analyt_phon"]

    # constituent part of approach: analog phonics
    ph_const_part_analog = get_data(ph_constit_part_approach_analog_ph)
    ph_const_part_analog_df = pd.DataFrame(ph_const_part_analog)
    ph_const_part_analog_df = ph_const_part_analog_df.T
    ph_const_part_analog_df.columns = ["ph_constit_part_analog_phon"]

    # constituent part of approach: embedded phonics
    ph_const_part_emb = get_data(ph_constit_part_approach_emb_ph)
    ph_const_part_emb_df = pd.DataFrame(ph_const_part_emb)
    ph_const_part_emb_df = ph_const_part_emb_df.T
    ph_const_part_emb_df.columns = ["ph_constit_part_emb_phon"]

    # constituent part of approach: phonemic awareness
    ph_const_part_phon_aware = get_data(ph_constit_part_approach_phon_aware)
    ph_const_part_phon_aware_df = pd.DataFrame(ph_const_part_phon_aware)
    ph_const_part_phon_aware_df = ph_const_part_phon_aware_df.T
    ph_const_part_phon_aware_df.columns = ["ph_constit_part_phonem_aware"]

    # constituent part of approach: phonological awareness
    ph_const_part_phonol_aware = get_data(ph_constit_part_approach_phonol_aware)
    ph_const_part_phonol_aware_df = pd.DataFrame(ph_const_part_phonol_aware)
    ph_const_part_phonol_aware_df = ph_const_part_phonol_aware_df.T
    ph_const_part_phonol_aware_df.columns = ["ph_constit_part_phonol_aware"]

    # constituent part of approach: onset - rime
    ph_const_part_onset_rime = get_data(ph_constit_part_approach_onset_rime)
    ph_const_part_onset_rime_df = pd.DataFrame(ph_const_part_onset_rime)
    ph_const_part_onset_rime_df = ph_const_part_onset_rime_df.T
    ph_const_part_onset_rime_df.columns = ["ph_constit_part_onset_rime"]

    # constituent part of approach: syllable instruction
    ph_const_part_syll_instr = get_data(ph_constit_part_approach_syll_instr)
    ph_const_part_syll_instr_df = pd.DataFrame(ph_const_part_syll_instr)
    ph_const_part_syll_instr_df = ph_const_part_syll_instr_df.T
    ph_const_part_syll_instr_df.columns = ["ph_constit_part_syll_instr"]

    # constituent part of approach: sight vocab
    ph_const_part_sight_vocab = get_data(ph_constit_part_approach_sight_vocab)
    ph_const_part_sight_vocab_df = pd.DataFrame(ph_const_part_sight_vocab)
    ph_const_part_sight_vocab_df = ph_const_part_sight_vocab_df.T
    ph_const_part_sight_vocab_df.columns = ["ph_constit_part_sight_vocab"]

    # constituent part of approach: whole word
    ph_const_part_whole_word = get_data(ph_constit_part_approach_whole_word)
    ph_const_part_whole_word_df = pd.DataFrame(ph_const_part_whole_word)
    ph_const_part_whole_word_df = ph_const_part_whole_word_df.T
    ph_const_part_whole_word_df.columns = ["ph_constit_part_whole_word"]

    #^^ end of individual column extraction above ^^

    # get phonics central to approach data
    ph_central_to_approach = get_data(ph_central_teach_lit_output)
    ph_central_to_approach_df = pd.DataFrame(ph_central_to_approach)
    ph_central_to_approach_df = ph_central_to_approach_df.T
    ph_central_to_approach_df.columns = ["ph_central_to_approach"]

    # get phonics parental involvement data
    ph_par_invol = get_data(ph_par_invol_output)
    ph_par_invol_df = pd.DataFrame(ph_par_invol)
    ph_par_invol_df = ph_par_invol_df.T
    ph_par_invol_df.columns = ["ph_par_invol"]

    # get phonics parental involvement data
    ph_dig_tech = get_data(ph_digit_tech_output)
    ph_dig_tech_df = pd.DataFrame(ph_dig_tech)
    ph_dig_tech_df = ph_dig_tech_df.T
    ph_dig_tech_df.columns = ["ph_dig_tech"]

    ph_ss_df = pd.concat([
        ph_tar_pop_df,
        ph_const_part_df,

        ph_const_part_synth_df,
        ph_const_part_sys_df,
        ph_const_part_analyt_df,
        ph_const_part_analog_df,
        ph_const_part_emb_df,
        ph_const_part_phon_aware_df,
        ph_const_part_phonol_aware_df,
        ph_const_part_onset_rime_df,
        ph_const_part_syll_instr_df,
        ph_const_part_sight_vocab_df,
        ph_const_part_whole_word_df,

        ph_central_to_approach_df,
        ph_par_invol_df,
        ph_dig_tech_df
    ], axis=1, sort=False)

    # fill blanks with NA
    ph_ss_df.fillna("NA", inplace=True)

    return ph_ss_df

def performance_pay():
    from AttributeIDList import pp_incentive_criteria_output
    from AttributeIDList import pp_reward_recipient_output
    from AttributeIDList import pp_incentive_timing_output
    from AttributeIDList import pp_incentive_type_output
    from AttributeIDList import pp_incentive_amount_output
    from AttributeIDList import pp_teacher_eval_period_output

    # get incentive criteria data
    pp_incent_crit = get_data(pp_incentive_criteria_output)
    pp_incent_crit_df = pd.DataFrame(pp_incent_crit)
    pp_incent_crit_df = pp_incent_crit_df.T
    pp_incent_crit_df.columns = ["pp_incent_criteria"]

    # get reward recipient data
    pp_reward_recip = get_data(pp_reward_recipient_output)
    pp_reward_recip_df = pd.DataFrame(pp_reward_recip)
    pp_reward_recip_df = pp_reward_recip_df.T
    pp_reward_recip_df.columns = ["pp_reward_recip"]

    # get incentive timing data
    pp_incent_timing = get_data(pp_incentive_timing_output)
    pp_incent_timing_df = pd.DataFrame(pp_incent_timing)
    pp_incent_timing_df = pp_incent_timing_df.T
    pp_incent_timing_df.columns = ["pp_incent_timing"]

    # get incentive type data
    pp_incent_type= get_data(pp_incentive_type_output)
    pp_incent_type_df = pd.DataFrame(pp_incent_type)
    pp_incent_type_df = pp_incent_type_df.T
    pp_incent_type_df.columns = ["pp_incent_type"]

    # get incentive amount data
    pp_incent_amount = comments(pp_incentive_amount_output)
    pp_incent_amount_df = pd.DataFrame(pp_incent_amount)
    pp_incent_amount_df = pp_incent_amount_df.T
    pp_incent_amount_df.columns = ["pp_incent_amount"]

    # get teacher evaluation period data
    pp_teach_eval_per = get_data(pp_teacher_eval_period_output)
    pp_teach_eval_per_df = pd.DataFrame(pp_teach_eval_per)
    pp_teach_eval_per_df = pp_teach_eval_per_df.T
    pp_teach_eval_per_df.columns = ["pp_teach_eval_per"]

    pp_ss_df = pd.concat([
        pp_incent_crit_df,
        pp_reward_recip_df,
        pp_incent_timing_df,
        pp_incent_type_df,
        pp_incent_amount_df,
        pp_teach_eval_per_df,
    ], axis=1, sort=False)

    # fill blanks with NA
    pp_ss_df.fillna("NA", inplace=True)

    return pp_ss_df

def within_class_grouping():
    from AttributeIDList import wcg_dir_grouping_change_output
    from AttributeIDList import wcg_curr_taught_attain_grp_output
    from AttributeIDList import wcg_pupils_affected_by_wcg_output
    from AttributeIDList import wcg_attain_grouping_level
    from AttributeIDList import wcg_follow_same_curr
    from AttributeIDList import wcg_approach_name
    from AttributeIDList import wcg_pupil_assignment

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
    clean_up(wc_ss_df)

    return wc_ss_df