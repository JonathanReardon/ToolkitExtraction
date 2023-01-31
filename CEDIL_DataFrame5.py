#!/usr/bin/python3

from files import data_files

# for CEDIL Cash Transfer strand specific data
#from CEDIL_CT_SS.CEDIL_CT_SS import CT_CEDIL_ss_df

# for CEDIL Menstual Hygiene strand specific data
from CEDIL_CT_SS.CEDIL_MH_SS import CT_CEDIL_MH_SS_df

# local imports
from ind_var_CEDIL.eppi_ID_CEDIL import eppiid_df
from ind_var_CEDIL.Author_CEDIL import author_df
from ind_var_CEDIL.Date_CEDIL import year_df

from ind_var_CEDIL.out_edu_CEDIL import out_edu_df
from ind_var_CEDIL.out_edu_type_CEDIL import out_edu_type_df
from ind_var_CEDIL.school_complete_level_CEDIL import sch_complete_level_df
from ind_var_CEDIL.out_unders_pop_CEDIL import out_unders_pop_df
from ind_var_CEDIL.out_unders_type_CEDIL import out_unders_type_df
from ind_var_CEDIL.out_teach_type_CEDIL import out_teach_type_df
from ind_var_CEDIL.follow_up_CEDIL import follow_up_df
#from ind_var_CEDIL.AdminStrand_CEDIL import admin_strand_df


from ind_var_CEDIL.out_out_type_CEDIL import outcometype_df
from ind_var_CEDIL.smd_CEDIL import smd_df
from ind_var_CEDIL.sesmd_CEDIL import sesmd_df
from ind_var_CEDIL.OutcomeDescription_CEDIL import outcome_description_df
from ind_var_CEDIL.OutcomeTitle_CEDIL import outcome_title_df
from ind_var_CEDIL.CIlowerSMD_CEDIL import cilowersmd_df
from ind_var_CEDIL.CIupperSMD_CEDIL import ciuppersmd_df
from ind_var_CEDIL.out_samp_CEDIL import out_samp
from ind_var_CEDIL.Outcome_CEDIL import outcome_df
from ind_var_CEDIL.out_es_type_CEDIL import effectsizetype_df
from ind_var_CEDIL.OutcomeComparison_CEDIL import out_comp_df
from ind_var_CEDIL.OutcomeMeasure_CEDIL import outcome_measure_df
from ind_var_CEDIL.Group1_N_CEDIL import group1N_df
from ind_var_CEDIL.Group2_N_CEDIL import group2N_df
from ind_var_CEDIL.Group1_Mean_CEDIL import group1mean_df
from ind_var_CEDIL.Group2_Mean_CEDIL import group2mean_df
from ind_var_CEDIL.Group1_SD_CEDIL import group1sd_df
from ind_var_CEDIL.Group2_SD_CEDIL import group2sd_df
from ind_var_CEDIL.out_test_type_CEDIL import testtype_outcome_df
from ind_var_CEDIL.out_teach_CEDIL import out_teach_df

# standard imports
import os
import pandas as pd
import numpy as np
from toolz import interleave
import re

# for getting number of outcomes
from toolkit_outcome_check import all_variables

# get number of outcomes
outcome_num = all_variables.shape[1]-1

#################################
# REFACTOR STRAND FILTERING CODE
#################################

def make_dataframe(save_file=True, clean_cols=True, verbose=True):

    global toolkit_test_type, toolkit_es_type

    # concatenate record detail data frames
    record_details_df = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        out_edu_df,
        out_edu_type_df,
        sch_complete_level_df,
        out_unders_pop_df,
        out_unders_type_df,
        out_teach_df,
        out_teach_type_df,
        follow_up_df,
    ], axis=1)

    # concatenate all main dataframes
    df = pd.concat([
        outcometype_df,
        smd_df,
        sesmd_df,
        cilowersmd_df,
        ciuppersmd_df,
        outcome_df,
        out_samp,
        out_comp_df,
        effectsizetype_df,
        outcome_measure_df,
        outcome_title_df,
        group1N_df,
        group2N_df,
        group1mean_df,
        group2mean_df,
        group1sd_df,
        group2sd_df,
        outcome_description_df,
        testtype_outcome_df
    ], axis=1)[list(interleave([
        outcometype_df,
        smd_df,
        sesmd_df,
        cilowersmd_df,
        ciuppersmd_df,
        outcome_df,
        out_samp,
        out_comp_df,
        effectsizetype_df,
        outcome_measure_df,
        outcome_title_df,
        group1N_df,
        group2N_df,
        group1mean_df,
        group2mean_df,
        group1sd_df,
        group2sd_df,
        outcome_description_df,
        testtype_outcome_df
    ]))]

    # empty lists to hold data
    schl_enrol_prim = []
    schl_enrol_prim_smd = []
    schl_enrol_prim_se = []
    schl_enrol_prim_ci_lower = []
    schl_enrol_prim_ci_upper = []
    schl_enrol_prim_outcome = []
    schl_enrol_prim_sample = []
    schl_enrol_prim_outcomp = []
    schl_enrol_es_type = []
    schl_enrol_out_measure = []
    schl_enrol_out_tit = []
    schl_enrol_g1_n = []
    schl_enrol_g2_n = []
    schl_enrol_g1_mean = []
    schl_enrol_g2_mean = []
    schl_enrol_g1_sd = []
    schl_enrol_g2_sd = []
    schl_enrol_out_desc = []
    schl_enrol_test_type = []

    schl_enrol_holders = [
        schl_enrol_prim,
        schl_enrol_prim_smd,
        schl_enrol_prim_se,
        schl_enrol_prim_ci_lower,
        schl_enrol_prim_ci_upper,
        schl_enrol_prim_outcome,
        schl_enrol_prim_sample,
        schl_enrol_prim_outcomp,
        schl_enrol_es_type,
        schl_enrol_out_measure,
        schl_enrol_out_tit,
        schl_enrol_g1_n,
        schl_enrol_g2_n,
        schl_enrol_g1_mean,
        schl_enrol_g2_mean,
        schl_enrol_g1_sd,
        schl_enrol_g2_sd,
        schl_enrol_out_desc,
        schl_enrol_test_type
    ]

    outcome_vars = [
        "out_type_",
        "smd_",
        "se_",
        "ci_lower_",
        "ci_upper_",
        "out_label_",
        "out_samp_",
        "out_comp_",
        "out_es_type_",
        "out_measure_",
        "out_tit_",
        "out_g1_n_",
        "out_g2_n_",
        "out_g1_mean_",
        "out_g2_mean_",
        "out_g1_sd_",
        "out_g2_sd_",
        "out_desc_",
        "out_test_type_raw_"
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'School enrolment outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(schl_enrol_holders):
                    holder.append(df[outcome_vars[counter2] +f"{outcome_n}"][counter])
                break
        else:
            for holder in schl_enrol_holders:
                holder.append("NA")

    ret_ed_prim = []
    ret_ed_prim_smd = []
    ret_ed_prim_se = []
    ret_ed_prim_ci_lower = []
    ret_ed_prim_ci_upper = []
    ret_ed_prim_outcome = []
    ret_ed_prim_sample = []
    ret_ed_prim_outcomp = []
    ret_ed_prim_es_type = []
    ret_ed_prim_out_measure = []
    ret_ed_prim_out_tit = []
    ret_ed_prim_g1_n = []
    ret_ed_prim_g2_n = []
    ret_ed_prim_g1_mean = []
    ret_ed_prim_g2_mean = []
    ret_ed_prim_g1_sd = []
    ret_ed_prim_g2_sd = []
    ret_ed_prim_out_desc = []
    ret_ed_test_type = []

    ret_ed_holders = [
        ret_ed_prim,
        ret_ed_prim_smd,
        ret_ed_prim_se,
        ret_ed_prim_ci_lower,
        ret_ed_prim_ci_upper,
        ret_ed_prim_outcome,
        ret_ed_prim_sample,
        ret_ed_prim_outcomp,
        ret_ed_prim_es_type,
        ret_ed_prim_out_measure,
        ret_ed_prim_out_tit,
        ret_ed_prim_g1_n,
        ret_ed_prim_g2_n,
        ret_ed_prim_g1_mean,
        ret_ed_prim_g2_mean,
        ret_ed_prim_g1_sd,
        ret_ed_prim_g2_sd,
        ret_ed_prim_out_desc,
        ret_ed_test_type
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Return to education outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(ret_ed_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in ret_ed_holders:
                holder.append("NA")

    attendance_prim = []
    attendance_prim_smd = []
    attendance_prim_se = []
    attendance_prim_ci_lower = []
    attendance_prim_ci_upper = []
    attendance_prim_outcome = []
    attendance_prim_sample = []
    attendance_prim_outcomp = []
    attendance_prim_es_type = []
    attendance_prim_out_measure = []
    attendance_prim_out_tit = []
    attendance_prim_g1_n = []
    attendance_prim_g2_n = []
    attendance_prim_g1_mean = []
    attendance_prim_g2_mean = []
    attendance_prim_g1_sd = []
    attendance_prim_g2_sd = []
    attendance_prim_out_desc = []
    attendance_test_type = []

    attendance_holders = [
        attendance_prim,
        attendance_prim_smd,
        attendance_prim_se,
        attendance_prim_ci_lower,
        attendance_prim_ci_upper,
        attendance_prim_outcome,
        attendance_prim_sample,
        attendance_prim_outcomp,
        attendance_prim_es_type,
        attendance_prim_out_measure,
        attendance_prim_out_tit,
        attendance_prim_g1_n,
        attendance_prim_g2_n,
        attendance_prim_g1_mean,
        attendance_prim_g2_mean,
        attendance_prim_g1_sd,
        attendance_prim_g2_sd,
        attendance_prim_out_desc,
        attendance_test_type
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Attendance outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(attendance_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in attendance_holders:
                holder.append("NA")

    abs_out_prim = []
    abs_out_prim_smd = []
    abs_out_prim_se = []
    abs_out_prim_ci_lower = []
    abs_out_prim_ci_upper = []
    abs_out_prim_outcome = []
    abs_out_prim_sample = []
    abs_out_prim_outcomp = []
    abs_out_prim_es_type = []
    abs_out_prim_out_measure = []
    abs_out_prim_out_tit = []
    abs_out_prim_g1_n = []
    abs_out_prim_g2_n = []
    abs_out_prim_g1_mean = []
    abs_out_prim_g2_mean = []
    abs_out_prim_g1_sd = []
    abs_out_prim_g2_sd = []
    abs_out_prim_out_desc = []
    abs_out_test_type = []

    abs_out_holders = [
        abs_out_prim,
        abs_out_prim_smd,
        abs_out_prim_se,
        abs_out_prim_ci_lower,
        abs_out_prim_ci_upper,
        abs_out_prim_outcome,
        abs_out_prim_sample,
        abs_out_prim_outcomp,
        abs_out_prim_es_type,
        abs_out_prim_out_measure,
        abs_out_prim_out_tit,
        abs_out_prim_g1_n,
        abs_out_prim_g2_n,
        abs_out_prim_g1_mean,
        abs_out_prim_g2_mean,
        abs_out_prim_g1_sd,
        abs_out_prim_g2_sd,
        abs_out_prim_out_desc,
        abs_out_test_type
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Absence outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(abs_out_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in abs_out_holders:
                holder.append("NA")

    time_in_school_prim = []
    time_in_school_prim_smd = []
    time_in_school_prim_se = []
    time_in_school_prim_ci_lower = []
    time_in_school_prim_ci_upper = []
    time_in_school_prim_outcome = []
    time_in_school_prim_sample = []
    time_in_school_prim_outcomp = []
    time_in_school_prim_es_type = []
    time_in_school_prim_out_measure = []
    time_in_school_prim_out_tit = []
    time_in_school_prim_g1_n = []
    time_in_school_prim_g2_n = []
    time_in_school_prim_g1_mean = []
    time_in_school_prim_g2_mean = []
    time_in_school_prim_g1_sd = []
    time_in_school_prim_g2_sd = []
    time_in_school_prim_out_desc = []
    time_in_school_test_type = []

    time_in_school_holders = [
        time_in_school_prim,
        time_in_school_prim_smd,
        time_in_school_prim_se,
        time_in_school_prim_ci_lower,
        time_in_school_prim_ci_upper,
        time_in_school_prim_outcome,
        time_in_school_prim_sample,
        time_in_school_prim_outcomp,
        time_in_school_prim_es_type,
        time_in_school_prim_out_measure,
        time_in_school_prim_out_tit,
        time_in_school_prim_g1_n,
        time_in_school_prim_g2_n,
        time_in_school_prim_g1_mean,
        time_in_school_prim_g2_mean,
        time_in_school_prim_g1_sd,
        time_in_school_prim_g2_sd,
        time_in_school_prim_out_desc,
        time_in_school_test_type,
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Time in school outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(time_in_school_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in time_in_school_holders:
                holder.append("NA")

    dropout_prim = []
    dropout_prim_smd = []
    dropout_prim_se = []
    dropout_prim_ci_lower = []
    dropout_prim_ci_upper = []
    dropout_prim_outcome = []
    dropout_prim_sample = []
    dropout_prim_outcomp = []
    dropout_prim_es_type = []
    dropout_prim_out_measure = []
    dropout_prim_out_tit = []
    dropout_prim_g1_n = []
    dropout_prim_g2_n = []
    dropout_prim_g1_mean = []
    dropout_prim_g2_mean = []
    dropout_prim_g1_sd = []
    dropout_prim_g2_sd = []
    dropout_prim_out_desc = []
    dropout_test_type = []

    dropout_holders = [
        dropout_prim,
        dropout_prim_smd,
        dropout_prim_se,
        dropout_prim_ci_lower,
        dropout_prim_ci_upper,
        dropout_prim_outcome,
        dropout_prim_sample,
        dropout_prim_outcomp,
        dropout_prim_es_type,
        dropout_prim_out_measure,
        dropout_prim_out_tit,
        dropout_prim_g1_n,
        dropout_prim_g2_n,
        dropout_prim_g1_mean,
        dropout_prim_g2_mean,
        dropout_prim_g1_sd,
        dropout_prim_g2_sd,
        dropout_prim_out_desc,
        dropout_test_type,
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Drop-out outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(dropout_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in dropout_holders:
                holder.append("NA")

    retention_prim = []
    retention_prim_smd = []
    retention_prim_se = []
    retention_prim_ci_lower = []
    retention_prim_ci_upper = []
    retention_prim_outcome = []
    retention_prim_sample = []
    retention_prim_outcomp = []
    retention_prim_es_type = []
    retention_prim_out_measure = []
    retention_prim_out_tit = []
    retention_prim_g1_n = []
    retention_prim_g2_n = []
    retention_prim_g1_mean = []
    retention_prim_g2_mean = []
    retention_prim_g1_sd = []
    retention_prim_g2_sd = []
    retention_prim_out_desc = []
    retention_test_type = []

    retention_holders = [
        retention_prim,
        retention_prim_smd,
        retention_prim_se,
        retention_prim_ci_lower,
        retention_prim_ci_upper,
        retention_prim_outcome,
        retention_prim_sample,
        retention_prim_outcomp,
        retention_prim_es_type,
        retention_prim_out_measure,
        retention_prim_out_tit,
        retention_prim_g1_n,
        retention_prim_g2_n,
        retention_prim_g1_mean,
        retention_prim_g2_mean,
        retention_prim_g1_sd,
        retention_prim_g2_sd,
        retention_prim_out_desc,
        retention_test_type,
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Retention outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(retention_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in retention_holders:
                holder.append("NA")

    grad_comp_prim = []
    grad_comp_prim_smd = []
    grad_comp_prim_se = []
    grad_comp_prim_ci_lower = []
    grad_comp_prim_ci_upper = []
    grad_comp_prim_outcome = []
    grad_comp_prim_sample = []
    grad_comp_prim_outcomp = []
    grad_comp_prim_es_type = []
    grad_comp_prim_out_measure = []
    grad_comp_prim_out_tit = []
    grad_comp_prim_g1_n = []
    grad_comp_prim_g2_n = []
    grad_comp_prim_g1_mean = []
    grad_comp_prim_g2_mean = []
    grad_comp_prim_g1_sd = []
    grad_comp_prim_g2_sd = []
    grad_comp_prim_out_desc = []
    grad_comp_test_type = []

    grad_comp_holders = [
        grad_comp_prim,
        grad_comp_prim_smd,
        grad_comp_prim_se,
        grad_comp_prim_ci_lower,
        grad_comp_prim_ci_upper,
        grad_comp_prim_outcome,
        grad_comp_prim_sample,
        grad_comp_prim_outcomp,
        grad_comp_prim_es_type,
        grad_comp_prim_out_measure,
        grad_comp_prim_out_tit,
        grad_comp_prim_g1_n,
        grad_comp_prim_g2_n,
        grad_comp_prim_g1_mean,
        grad_comp_prim_g2_mean,
        grad_comp_prim_g1_sd,
        grad_comp_prim_g2_sd,
        grad_comp_prim_out_desc,
        grad_comp_test_type,
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Grade completion outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(grad_comp_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in grad_comp_holders:
                holder.append("NA")

    school_comp_prim = []
    school_comp_prim_smd = []
    school_comp_prim_se = []
    school_comp_prim_ci_lower = []
    school_comp_prim_ci_upper = []
    school_comp_prim_outcome = []
    school_comp_prim_sample = []
    school_comp_prim_outcomp = []
    school_comp_prim_es_type = []
    school_comp_prim_out_measure = []
    school_comp_prim_out_tit = []
    school_comp_prim_g1_n = []
    school_comp_prim_g2_n = []
    school_comp_prim_g1_mean = []
    school_comp_prim_g2_mean = []
    school_comp_prim_g1_sd = []
    school_comp_prim_g2_sd = []
    school_comp_prim_out_desc = []
    school_comp_test_type = []

    school_comp_holders = [
        school_comp_prim,
        school_comp_prim_smd,
        school_comp_prim_se,
        school_comp_prim_ci_lower,
        school_comp_prim_ci_upper,
        school_comp_prim_outcome,
        school_comp_prim_sample,
        school_comp_prim_outcomp,
        school_comp_prim_es_type,
        school_comp_prim_out_measure,
        school_comp_prim_out_tit,
        school_comp_prim_g1_n,
        school_comp_prim_g2_n,
        school_comp_prim_g1_mean,
        school_comp_prim_g2_mean,
        school_comp_prim_g1_sd,
        school_comp_prim_g2_sd,
        school_comp_prim_out_desc,
        school_comp_test_type,
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'School completion outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(school_comp_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in school_comp_holders:
                holder.append("NA")

    next_grade_prim = []
    next_grade_prim_smd = []
    next_grade_prim_se = []
    next_grade_prim_ci_lower = []
    next_grade_prim_ci_upper = []
    next_grade_prim_outcome = []
    next_grade_prim_sample = []
    next_grade_prim_outcomp = []
    next_grade_prim_es_type = []
    next_grade_prim_out_measure = []
    next_grade_prim_out_tit = []
    next_grade_prim_g1_n = []
    next_grade_prim_g2_n = []
    next_grade_prim_g1_mean = []
    next_grade_prim_g2_mean = []
    next_grade_prim_g1_sd = []
    next_grade_prim_g2_sd = []
    next_grade_prim_out_desc = []
    next_grade_test_type = []

    next_grade_holders = [
        next_grade_prim,
        next_grade_prim_smd,
        next_grade_prim_se,
        next_grade_prim_ci_lower,
        next_grade_prim_ci_upper,
        next_grade_prim_outcome,
        next_grade_prim_sample,
        next_grade_prim_outcomp,
        next_grade_prim_es_type,
        next_grade_prim_out_measure,
        next_grade_prim_out_tit,
        next_grade_prim_g1_n,
        next_grade_prim_g2_n,
        next_grade_prim_g1_mean,
        next_grade_prim_g2_mean,
        next_grade_prim_g1_sd,
        next_grade_prim_g2_sd,
        next_grade_prim_out_desc,
        next_grade_test_type,
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Next grade outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(next_grade_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in next_grade_holders:
                holder.append("NA")

    grade_rep_prim = []
    grade_rep_prim_smd = []
    grade_rep_prim_se = []
    grade_rep_prim_ci_lower = []
    grade_rep_prim_ci_upper = []
    grade_rep_prim_outcome = []
    grade_rep_prim_sample = []
    grade_rep_prim_outcomp = []
    grade_rep_prim_es_type = []
    grade_rep_prim_out_measure = []
    grade_rep_prim_out_tit = []
    grade_rep_prim_g1_n = []
    grade_rep_prim_g2_n = []
    grade_rep_prim_g1_mean = []
    grade_rep_prim_g2_mean = []
    grade_rep_prim_g1_sd = []
    grade_rep_prim_g2_sd = []
    grade_rep_prim_out_desc = []
    grade_rep_test_type = []

    grade_rep_holders = [
        grade_rep_prim,
        grade_rep_prim_smd,
        grade_rep_prim_se,
        grade_rep_prim_ci_lower,
        grade_rep_prim_ci_upper,
        grade_rep_prim_outcome,
        grade_rep_prim_sample,
        grade_rep_prim_outcomp,
        grade_rep_prim_es_type,
        grade_rep_prim_out_measure,
        grade_rep_prim_out_tit,
        grade_rep_prim_g1_n,
        grade_rep_prim_g2_n,
        grade_rep_prim_g1_mean,
        grade_rep_prim_g2_mean,
        grade_rep_prim_g1_sd,
        grade_rep_prim_g2_sd,
        grade_rep_prim_out_desc,
        grade_rep_test_type,
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Grade repetition outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(grade_rep_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in grade_rep_holders:
                holder.append("NA")

    other_outcome_prim = []
    other_outcome_prim_smd = []
    other_outcome_prim_se = []
    other_outcome_prim_ci_lower = []
    other_outcome_prim_ci_upper = []
    other_outcome_prim_outcome = []
    other_outcome_prim_sample = []
    other_outcome_prim_outcomp = []
    other_outcome_prim_es_type = []
    other_outcome_prim_out_measure = []
    other_outcome_prim_out_tit = []
    other_outcome_prim_g1_n = []
    other_outcome_prim_g2_n = []
    other_outcome_prim_g1_mean = []
    other_outcome_prim_g2_mean = []
    other_outcome_prim_g1_sd = []
    other_outcome_prim_g2_sd = []
    other_outcome_prim_out_desc = []
    other_outcome_test_type = []

    other_outcome_holders = [
        other_outcome_prim,
        other_outcome_prim_smd,
        other_outcome_prim_se,
        other_outcome_prim_ci_lower,
        other_outcome_prim_ci_upper,
        other_outcome_prim_outcome,
        other_outcome_prim_sample,
        other_outcome_prim_outcomp,
        other_outcome_prim_es_type,
        other_outcome_prim_out_measure,
        other_outcome_prim_out_tit,
        other_outcome_prim_g1_n,
        other_outcome_prim_g2_n,
        other_outcome_prim_g1_mean,
        other_outcome_prim_g2_mean,
        other_outcome_prim_g1_sd,
        other_outcome_prim_g2_sd,
        other_outcome_prim_out_desc,
        other_outcome_test_type,
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Other outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(other_outcome_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in other_outcome_holders:
                holder.append("NA")

    df_zip = list(zip(
        schl_enrol_out_tit,
        schl_enrol_out_desc,
        schl_enrol_prim,
        schl_enrol_prim_smd,
        schl_enrol_prim_se,
        schl_enrol_out_measure,
        schl_enrol_g1_n,
        schl_enrol_g2_n,
        schl_enrol_g1_mean,
        schl_enrol_g2_mean,
        schl_enrol_g1_sd,
        schl_enrol_g2_sd,
        schl_enrol_prim_ci_lower,
        schl_enrol_prim_ci_upper,
        schl_enrol_prim_outcome,
        schl_enrol_prim_sample,
        schl_enrol_prim_outcomp,
        schl_enrol_es_type,
        schl_enrol_test_type,
        
        ret_ed_prim_out_tit,
        ret_ed_prim_out_desc,
        ret_ed_prim,
        ret_ed_prim_smd,
        ret_ed_prim_se,
        ret_ed_prim_out_measure,
        ret_ed_prim_g1_n,
        ret_ed_prim_g2_n,
        ret_ed_prim_g1_mean,
        ret_ed_prim_g2_mean,
        ret_ed_prim_g1_sd,
        ret_ed_prim_g2_sd,
        ret_ed_prim_ci_lower,
        ret_ed_prim_ci_upper,
        ret_ed_prim_outcome,
        ret_ed_prim_sample,
        ret_ed_prim_outcomp,
        ret_ed_prim_es_type,
        ret_ed_test_type,
        
        attendance_prim_out_tit,
        attendance_prim_out_desc,
        attendance_prim,
        attendance_prim_smd,
        attendance_prim_se,
        attendance_prim_out_measure,
        attendance_prim_g1_n,
        attendance_prim_g2_n,
        attendance_prim_g1_mean,
        attendance_prim_g2_mean,
        attendance_prim_g1_sd,
        attendance_prim_g2_sd,
        attendance_prim_ci_lower,
        attendance_prim_ci_upper,
        attendance_prim_outcome,
        attendance_prim_sample,
        attendance_prim_outcomp,
        attendance_prim_es_type,
        attendance_test_type,

        abs_out_prim_out_tit,
        abs_out_prim_out_desc,
        abs_out_prim,
        abs_out_prim_smd,
        abs_out_prim_se,
        abs_out_prim_out_measure,
        abs_out_prim_g1_n,
        abs_out_prim_g2_n,
        abs_out_prim_g1_mean,
        abs_out_prim_g2_mean,
        abs_out_prim_g1_sd,
        abs_out_prim_g2_sd,
        abs_out_prim_ci_lower,
        abs_out_prim_ci_upper,
        abs_out_prim_outcome,
        abs_out_prim_sample,
        abs_out_prim_outcomp,
        abs_out_prim_es_type,
        abs_out_test_type,

        time_in_school_prim_out_tit,
        time_in_school_prim_out_desc,
        time_in_school_prim,
        time_in_school_prim_smd,
        time_in_school_prim_se,
        time_in_school_prim_out_measure,
        time_in_school_prim_g1_n,
        time_in_school_prim_g2_n,
        time_in_school_prim_g1_mean,
        time_in_school_prim_g2_mean,
        time_in_school_prim_g1_sd,
        time_in_school_prim_g2_sd,
        time_in_school_prim_ci_lower,
        time_in_school_prim_ci_upper,
        time_in_school_prim_outcome,
        time_in_school_prim_sample,
        time_in_school_prim_outcomp,
        time_in_school_prim_es_type,
        time_in_school_test_type,

        dropout_prim_out_tit,
        dropout_prim_out_desc,
        dropout_prim,
        dropout_prim_smd,
        dropout_prim_se,
        dropout_prim_out_measure,
        dropout_prim_g1_n,
        dropout_prim_g2_n,
        dropout_prim_g1_mean,
        dropout_prim_g2_mean,
        dropout_prim_g1_sd,
        dropout_prim_g2_sd,
        dropout_prim_ci_lower,
        dropout_prim_ci_upper,
        dropout_prim_outcome,
        dropout_prim_sample,
        dropout_prim_outcomp,
        dropout_prim_es_type,
        dropout_test_type,

        retention_prim_out_tit,
        retention_prim_out_desc,
        retention_prim,
        retention_prim_smd,
        retention_prim_se,
        retention_prim_out_measure,
        retention_prim_g1_n,
        retention_prim_g2_n,
        retention_prim_g1_mean,
        retention_prim_g2_mean,
        retention_prim_g1_sd,
        retention_prim_g2_sd,
        retention_prim_ci_lower,
        retention_prim_ci_upper,
        retention_prim_outcome,
        retention_prim_sample,
        retention_prim_outcomp,
        retention_prim_es_type,
        retention_test_type,

        grad_comp_prim_out_tit,
        grad_comp_prim_out_desc,
        grad_comp_prim,
        grad_comp_prim_smd,
        grad_comp_prim_se,
        grad_comp_prim_out_measure,
        grad_comp_prim_g1_n,
        grad_comp_prim_g2_n,
        grad_comp_prim_g1_mean,
        grad_comp_prim_g2_mean,
        grad_comp_prim_g1_sd,
        grad_comp_prim_g2_sd,
        grad_comp_prim_ci_lower,
        grad_comp_prim_ci_upper,
        grad_comp_prim_outcome,
        grad_comp_prim_sample,
        grad_comp_prim_outcomp,
        grad_comp_prim_es_type,
        grad_comp_test_type,

        school_comp_prim_out_tit,
        school_comp_prim_out_desc,
        school_comp_prim,
        school_comp_prim_smd,
        school_comp_prim_se,
        school_comp_prim_out_measure,
        school_comp_prim_g1_n,
        school_comp_prim_g2_n,
        school_comp_prim_g1_mean,
        school_comp_prim_g2_mean,
        school_comp_prim_g1_sd,
        school_comp_prim_g2_sd,
        school_comp_prim_ci_lower,
        school_comp_prim_ci_upper,
        school_comp_prim_outcome,
        school_comp_prim_sample,
        school_comp_prim_outcomp,
        school_comp_prim_es_type,
        school_comp_test_type,

        next_grade_prim_out_tit,
        next_grade_prim_out_desc,
        next_grade_prim,
        next_grade_prim_smd,
        next_grade_prim_se,
        next_grade_prim_out_measure,
        next_grade_prim_g1_n,
        next_grade_prim_g2_n,
        next_grade_prim_g1_mean,
        next_grade_prim_g2_mean,
        next_grade_prim_g1_sd,
        next_grade_prim_g2_sd,
        next_grade_prim_ci_lower,
        next_grade_prim_ci_upper,
        next_grade_prim_outcome,
        next_grade_prim_sample,
        next_grade_prim_outcomp,
        next_grade_prim_es_type,
        next_grade_test_type,

        grade_rep_prim_out_tit,
        grade_rep_prim_out_desc,
        grade_rep_prim,
        grade_rep_prim_smd,
        grade_rep_prim_se,
        grade_rep_prim_out_measure,
        grade_rep_prim_g1_n,
        grade_rep_prim_g2_n,
        grade_rep_prim_g1_mean,
        grade_rep_prim_g2_mean,
        grade_rep_prim_g1_sd,
        grade_rep_prim_g2_sd,
        grade_rep_prim_ci_lower,
        grade_rep_prim_ci_upper,
        grade_rep_prim_outcome,
        grade_rep_prim_sample,
        grade_rep_prim_outcomp,
        grade_rep_prim_es_type,
        grade_rep_test_type,

        other_outcome_prim_out_tit,
        other_outcome_prim_out_desc,
        other_outcome_prim,
        other_outcome_prim_smd,
        other_outcome_prim_se,
        other_outcome_prim_out_measure,
        other_outcome_prim_g1_n,
        other_outcome_prim_g2_n,
        other_outcome_prim_g1_mean,
        other_outcome_prim_g2_mean,
        other_outcome_prim_g1_sd,
        other_outcome_prim_g2_sd,
        other_outcome_prim_ci_lower,
        other_outcome_prim_ci_upper,
        other_outcome_prim_outcome,
        other_outcome_prim_sample,
        other_outcome_prim_outcomp,
        other_outcome_prim_es_type,
        other_outcome_test_type,
    ))

    df = pd.DataFrame(df_zip)

    df.rename(columns={
        0: "out_tit_schl_enrol",
        1: "out_desc_schl_enrol",
        2: "out_type_schl_enrol",
        3: "smd_schl_enrol",
        4: "se_schl_enrol",
        5: "out_measure_schl_enrol",
        6: "out_g1_n_schl_enrol",
        7: "out_g1_mean_schl_enrol",
        8: "out_g1_sd_schl_enrol",
        9: "out_g2_n_schl_enrol",
        10: "out_g2_mean_schl_enrol",
        11: "out_g2_sd_schl_enrol",
        12: "ci_lower_schl_enrol",
        13: "ci_upper_schl_enrol",
        14: "out_label_schl_enrol",
        15: "out_samp_schl_enrol",
        16: "out_comp_schl_enrol",
        17: "out_es_type_schl_enrol",
        18: "out_test_type_raw_schl_enrol",

        19: "out_tit_ret_ed",
        20: "out_desc_ret_ed",
        21: "out_type_ret_ed",
        22: "smd_ret_ed",
        23: "se_ret_ed",
        24: "out_measure_ret_ed",
        25: "out_g1_n_ret_ed",
        26: "out_g1_mean_ret_ed",
        27: "out_g1_sd_ret_ed",
        28: "out_g2_n_ret_ed",
        29: "out_g2_mean_ret_ed",
        30: "out_g2_sd_ret_ed",
        31: "ci_lower_ret_ed",
        32: "ci_upper_ret_ed",
        33: "out_label_ret_ed",
        34: "out_samp_ret_ed",
        35: "out_comp_ret_ed",
        36: "out_es_type_ret_ed",
        37: "out_test_type_raw_red_ed",

        38: "out_tit_attend",
        39: "out_desc_attend",
        40: "out_type_attend",
        41: "smd_attend",
        42: "se_attendance",
        43: "out_measure_attend",
        44: "out_g1_n_attend",
        45: "out_g1_mean_attend",
        46: "out_g1_sd_attend",
        47: "out_g2_n_attend",
        48: "out_g2_mean_attend",
        49: "out_g2_sd_attend",
        50: "ci_lower_attend",
        51: "ci_upper_attend",
        52: "out_label_attend",
        53: "out_samp_attend",
        54: "out_comp_attend",
        55: "out_es_type_attend",
        56: "out_test_type_raw_attend",

        57: "out_tit_abs",
        58: "out_desc_abs",
        59: "out_type_abs",
        60: "smd_abs",
        61: "se_abs",
        62: "out_measure_abs",
        63: "out_g1_n_abs",
        64: "out_g1_mean_abs",
        65: "out_g1_sd_abs",
        66: "out_g2_n_abs",
        67: "out_g2_mean_abs",
        68: "out_g2_sd_abs",
        69: "ci_lower_abs",
        70: "ci_upper_abs",
        71: "out_label_abs",
        72: "out_samp_abs",
        73: "out_comp_abs",
        74: "out_es_type_abs",
        75: "out_test_type_raw_abs",

        76: "out_tit_time_schl",
        77: "out_desc_time_schl",
        78: "out_type_time_schl",
        79: "smd_time_schl",
        80: "se_time_schl",
        81: "out_measure_time_schl",
        82: "out_g1_n_time_schl",
        83: "out_g1_mean_time_schl",
        84: "out_g1_sd_time_schl",
        85: "out_g2_n_time_schl",
        86: "out_g2_mean_time_schl",
        87: "out_g2_sd_time_schl",
        88: "ci_lower_time_schl",
        89: "ci_upper_time_schl",
        90: "out_label_time_schl",
        91: "out_samp_time_schl",
        92: "out_comp_time_schl",
        93: "out_es_type_time_schl",
        94: "out_test_type_raw_time_schl",

        95: "out_tit_dropout",
        96: "out_desc_dropout",
        97: "out_type_dropout",
        98: "smd_dropout",
        99: "se_dropout",
        100: "out_measure_dropout",
        101: "out_g1_n_dropout",
        102: "out_g1_mean_dropout",
        103: "out_g1_sd_dropout",
        104: "out_g2_n_dropout",
        105: "out_g2_mean_dropout",
        106: "out_g2_sd_dropout",
        107: "ci_lower_dropout",
        108: "ci_upper_dropout",
        109: "out_label_dropout",
        110: "out_samp_dropout",
        111: "out_comp_dropout",
        112: "out_es_type_dropout",
        113: "out_test_type_raw_dropout",

        114: "out_tit_ret",
        115: "out_desc_ret",
        116: "out_type_ret",
        117: "smd_ret",
        118: "se_ret",
        119: "out_measure_ret",
        120: "out_g1_n_ret",
        121: "out_g1_mean_ret",
        122: "out_g1_sd_ret",
        123: "out_g2_n_ret",
        124: "out_g2_mean_ret",
        125: "out_g2_sd_ret",
        126: "ci_lower_ret",
        127: "ci_upper_ret",
        128: "out_label_ret",
        129: "out_samp_ret",
        130: "out_comp_ret",
        131: "out_es_type_ret",
        132: "out_test_type_raw_ret",

        133: "out_tit_grad_comp",
        134: "out_desc_grad_comp",
        135: "out_type_grad_comp",
        136: "smd_grad_comp",
        137: "se_grad_comp",
        138: "out_measure_grad_comp",
        139: "out_g1_n_grad_comp",
        140: "out_g1_mean_grad_comp",
        141: "out_g1_sd_grad_comp",
        142: "out_g2_n_grad_comp",
        143: "out_g2_mean_grad_comp",
        144: "out_g2_sd_grad_comp",
        145: "ci_lower_grad_comp",
        146: "ci_upper_grad_comp",
        147: "out_label_grad_comp",
        148: "out_samp_grad_comp",
        149: "out_comp_grad_comp",
        150: "out_es_type_grad_comp",
        151: "out_test_type_raw_grad_comp",

        152: "out_tit_school_comp",
        153: "out_desc_school_comp",
        154: "out_type_school_comp",
        155: "smd_school_comp",
        156: "se_school_comp",
        157: "out_measure_school_comp",
        158: "out_g1_n_school_comp",
        159: "out_g1_mean_school_comp",
        160: "out_g1_sd_school_comp",
        161: "out_g2_n_school_comp",
        162: "out_g2_mean_school_comp",
        163: "out_g2_sd_school_comp",
        164: "ci_lower_school_comp",
        165: "ci_upper_school_comp",
        166: "out_label_school_comp",
        167: "out_samp_school_comp",
        168: "out_comp_school_comp",
        169: "out_es_type_school_comp",
        170: "out_test_type_raw_school_comp",

        171: "out_tit_next_grade",
        172: "out_desc_next_grade",
        173: "out_type_next_grade",
        174: "smd_next_grade",
        175: "se_next_grade",
        176: "out_measure_next_grade",
        177: "out_g1_n_next_grade",
        178: "out_g1_mean_next_grade",
        179: "out_g1_sd_next_grade",
        180: "out_g2_n_next_grade",
        181: "out_g2_mean_next_grade",
        182: "out_g2_sd_next_grade",
        183: "ci_lower_next_grade",
        184: "ci_upper_next_grade",
        185: "out_label_next_grade",
        186: "out_samp_next_grade",
        187: "out_comp_next_grade",
        188: "out_es_type_next_grade",
        189: "out_test_type_raw_next_grade",

        190: "out_tit_grade_rep",
        191: "out_desc_grade_rep",
        192: "out_type_grade_rep",
        193: "smd_grade_rep",
        194: "se_grade_rep",
        195: "out_measure_grade_rep",
        196: "out_g1_n_grade_rep",
        197: "out_g1_mean_grade_rep",
        198: "out_g1_sd_grade_rep",
        199: "out_g2_n_grade_rep",
        200: "out_g2_mean_grade_rep",
        201: "out_g2_sd_grade_rep",
        202: "ci_lower_grade_rep",
        203: "ci_upper_grade_rep",
        204: "out_label_grade_rep",
        205: "out_samp_grade_rep",
        206: "out_comp_grade_rep",
        207: "out_es_type_grade_rep",
        208: "out_test_type_raw_grade_rep",

        209: "out_tit_other_outcome",
        210: "out_desc_other_outcome",
        211: "out_type_other_outcome",
        212: "smd_other_outcome",
        213: "se_other_outcome",
        214: "out_measure_other_outcome",
        215: "out_g1_n_other_outcome",
        216: "out_g1_mean_other_outcome",
        217: "out_g1_sd_other_outcome",
        218: "out_g2_n_other_outcome",
        219: "out_g2_mean_other_outcome",
        220: "out_g2_sd_other_outcome",
        221: "ci_lower_other_outcome",
        222: "ci_upper_other_outcome",
        223: "out_label_other_outcome",
        224: "out_samp_other_outcome",
        225: "out_comp_other_outcome",
        226: "out_es_type_other_outcome",
        227: "out_test_type_raw_other_outcome",

    }, inplace=True)

    # concatenate record details and main dataframes
    df = pd.concat([record_details_df, df, CT_CEDIL_MH_SS_df],axis=1, sort=False)

    if clean_cols:
        # insert empty columns per variable for data checkers to log changes
        df.insert(6, 'out_tit_tool_CLEAN', '')
        df.insert(8, 'out_desc_tool_CLEAN', '')
        df.insert(10, 'out_type_tool_CLEAN', '')
        df.insert(12, 'smd_tool_CLEAN', '')
        df.insert(14, 'se_tool_CLEAN', '')
        df.insert(16, 'out_measure_tool_CLEAN', '')
        df.insert(18, 'out_g1_n_tool_CLEAN', '')
        df.insert(20, 'out_g1_mean_tool_CLEAN', '')
        df.insert(22, 'out_g1_sd_tool_CLEAN', '')
        df.insert(24, 'out_g2_n_tool_CLEAN', '')
        df.insert(26, 'out_g2_mean_tool_CLEAN', '')
        df.insert(28, 'out_g2_sd_tool_CLEAN', '')
        df.insert(30, 'ci_lower_tool_CLEAN', '')
        df.insert(32, 'ci_upper_tool_CLEAN', '')
        df.insert(34, 'out_label_tool_CLEAN', '')
        df.insert(36, 'out_samp_tool_CLEAN', '')
        df.insert(38, 'out_comp_tool_CLEAN', '')
        df.insert(40, 'out_es_type_tool_CLEAN', '')
        df.insert(42, 'out_test_type_raw_tool_CLEAN', '')

        df.insert(44, 'out_tit_red_CLEAN', '')
        df.insert(46, 'out_desc_red_CLEAN', '')
        df.insert(48, 'out_type_red_CLEAN', '')
        df.insert(50, 'smd_red_CLEAN', '')
        df.insert(52, 'se_red_CLEAN', '')
        df.insert(54, 'out_measure_red_CLEAN', '')
        df.insert(56, 'out_g1_n_red_CLEAN', '')
        df.insert(58, 'out_g1_mean_red_CLEAN', '')
        df.insert(60, 'out_g1_sd_red_CLEAN', '')
        df.insert(62, 'out_g2_n_red_CLEAN', '')
        df.insert(64, 'out_g2_mean_red_CLEAN', '')
        df.insert(66, 'out_g2_sd_red_CLEAN', '')
        df.insert(68, 'ci_lower_red_CLEAN', '')
        df.insert(70, 'ci_upper_red_CLEAN', '')
        df.insert(72, 'out_label_red_CLEAN', '')
        df.insert(74, 'out_samp_red_CLEAN', '')
        df.insert(76, 'out_comp_red_CLEAN', '')
        df.insert(78, 'out_es_type_red_CLEAN', '')
        df.insert(80, 'out_test_type_raw_red_CLEAN', '')

        df.insert(82, 'out_tit_attendance_CLEAN', '')
        df.insert(84, 'out_desc_attendance_CLEAN', '')
        df.insert(86, 'out_type_attendance_CLEAN', '')
        df.insert(88, 'smd_attendance_CLEAN', '')
        df.insert(90, 'se_attendance_CLEAN', '')
        df.insert(92, 'out_measure_attendance_CLEAN', '')
        df.insert(94, 'out_g1_n_attendance_CLEAN', '')
        df.insert(96, 'out_g1_mean_attendance_CLEAN', '')
        df.insert(98, 'out_g1_sd_attendance_CLEAN', '')
        df.insert(100, 'out_g2_n_attendance_CLEAN', '')
        df.insert(102, 'out_g2_mean_attendance_CLEAN', '')
        df.insert(104, 'out_g2_sd_attendance_CLEAN', '')
        df.insert(106, 'ci_lower_attendance_CLEAN', '')
        df.insert(108, 'ci_upper_attendance_CLEAN', '')
        df.insert(110, 'out_label_attendance_CLEAN', '')
        df.insert(112, 'out_samp_attendance_CLEAN', '')
        df.insert(114, 'out_comp_attendance_CLEAN', '')
        df.insert(116, 'out_es_type_attendance_CLEAN', '')
        df.insert(118, 'out_test_type_attendance_CLEAN', '')

        df.insert(120, 'out_tit_math_CLEAN', '')
        df.insert(122, 'out_desc_math_CLEAN', '')
        df.insert(124, 'out_type_math_CLEAN', '')
        df.insert(126, 'smd_math_CLEAN', '')
        df.insert(128, 'se_math_CLEAN', '')
        df.insert(130, 'out_measure_math_CLEAN', '')
        df.insert(132, 'out_g1_n_math_CLEAN', '')
        df.insert(134, 'out_g1_mean_math_CLEAN', '')
        df.insert(136, 'out_g1_sd_math_CLEAN', '')
        df.insert(138, 'out_g2_n_math_CLEAN', '')
        df.insert(140, 'out_g2_mean_math_CLEAN', '')
        df.insert(142, 'out_g2_sd_math_CLEAN', '')
        df.insert(144, 'ci_lower_math_CLEAN', '')
        df.insert(146, 'ci_upper_math_CLEAN', '')
        df.insert(148, 'out_label_math_CLEAN', '')
        df.insert(150, 'out_samp_math_CLEAN', '')
        df.insert(152, 'out_comp_math_CLEAN', '')
        df.insert(154, 'out_es_type_math_CLEAN', '')
        df.insert(156, 'out_test_type_math_CLEAN', '')

        df.insert(158, 'out_tit_sci_CLEAN', '')
        df.insert(160, 'out_desc_sci_CLEAN', '')
        df.insert(162, 'out_type_sci_CLEAN', '')
        df.insert(164, 'smd_sci_CLEAN', '')
        df.insert(166, 'se_sci_CLEAN', '')
        df.insert(168, 'out_measure_sci_CLEAN', '')
        df.insert(170, 'out_g1_n_sci_CLEAN', '')
        df.insert(172, 'out_g1_mean_sci_CLEAN', '')
        df.insert(174, 'out_g1_sd_sci_CLEAN', '')
        df.insert(176, 'out_g2_n_sci_CLEAN', '')
        df.insert(178, 'out_g2_mean_sci_CLEAN', '')
        df.insert(180, 'out_g2_sd_sci_CLEAN', '')
        df.insert(182, 'ci_lower_sci_CLEAN', '')
        df.insert(184, 'ci_upper_sci_CLEAN', '')
        df.insert(186, 'out_label_sci_CLEAN', '')
        df.insert(188, 'out_samp_sci_CLEAN', '')
        df.insert(190, 'out_comp_sci_CLEAN', '')
        df.insert(192, 'out_es_type_sci_CLEAN', '')
        df.insert(194, 'out_test_type_sci_CLEAN', '')

        df.insert(196, 'out_tit_fsm_CLEAN', '')
        df.insert(198, 'out_desc_fsm_CLEAN', '')
        df.insert(200, 'out_type_fsm_CLEAN', '')
        df.insert(202, 'smd_fsm_CLEAN', '')
        df.insert(204, 'se_fsm_CLEAN', '')
        df.insert(206, 'out_measure_fsm_CLEAN', '')
        df.insert(208, 'out_g1_n_fsm_CLEAN', '')
        df.insert(210, 'out_g1_mean_fsm_CLEAN', '')
        df.insert(212, 'out_g1_sd_fsm_CLEAN', '')
        df.insert(214, 'out_g2_n_fsm_CLEAN', '')
        df.insert(216, 'out_g2_mean_fsm_CLEAN', '')
        df.insert(218, 'out_g2_sd_fsm_CLEAN', '')
        df.insert(220, 'ci_lower_fsm_CLEAN', '')
        df.insert(222, 'ci_upper_fsm_CLEAN', '')
        df.insert(224, 'out_label_fsm_CLEAN', '')
        df.insert(226, 'out_samp_fsm_CLEAN', '')
        df.insert(228, 'out_comp_fsm_CLEAN', '')
        df.insert(230, 'out_es_type_fsm_CLEAN', '')
        df.insert(232, 'out_test_type_fsm_CLEAN', '')

    if verbose:
        # print dataframe
        print(df)
        print("\n")

        # list column names and position
        for counter, i in enumerate(df):
            print(counter, i)
        print("\n")

        # print dataframe info
        print("Columns: {}".format(df.shape[1]))
        print("Rows: {}".format(df.shape[0]))
        print("Datapoints: {}".format(df.shape[0] * df.shape[1]))
        print("\n")

    if save_file:
        # get current wd
        cw = os.getcwd()

        # get file name for output
        outfile_name_pre = data_files.rsplit('/')[-1]
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]  # use for dir name
        outfile_name = outfile_name_mid + "_Educational_Outcome.csv"
        outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)

        # create dir (filename)
        try:
            os.mkdir(outfile_name_mid)
        except OSError:
            print("Create {} dir fail, already exists or permission error".format(outfile_name_mid))
        else:
            print("Successfully created {} directory".format(outfile_name_mid))

        # write to disk
        print("Input file: {}".format(data_files))
        print("Saving extracted output to: {}".format(outfile))
        df.to_csv(outfile, index=False)

make_dataframe(save_file=True, clean_cols=False, verbose=False)
