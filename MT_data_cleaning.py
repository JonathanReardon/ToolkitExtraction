#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Jonathan Reardon
"""

# standard imports
import os
import sys
import pandas as pd
from toolz import interleave

# local imports - core extraction functions
from Main import verbose_display
from Main import save_dataframe
from Main import clean_up

# local imports - individual variables
from ind_var import ind_var_gen

datafile = sys.argv[1]

def make_dataframe_1(save_file=True, clean_cols=True, verbose=True):

    eppiid_df = ind_var_gen.eppi()
    author_df = ind_var_gen.author()
    year_df = ind_var_gen.date()
    abstract_df = ind_var_gen.abstract()
    admin_strand_df = ind_var_gen.admin_strand()
    pubtype_eppi_df = ind_var_gen.pubeppi()
    publication_type_df = ind_var_gen.pub_type()
    country_df = ind_var_gen.country()
    educational_setting_df = ind_var_gen.edu_setting()
    study_realism_df = ind_var_gen.study_realism()
    student_age = ind_var_gen.student_age()
    number_of_schools_df = ind_var_gen.number_of_schools()
    number_of_classes_df = ind_var_gen.number_of_classes()
    treatment_group_df = ind_var_gen.treat_group()
    participant_assignment_df = ind_var_gen.part_assign()
    level_of_assignment_df = ind_var_gen.level_assign()
    study_design_df = ind_var_gen.study_design()
    randomisation_df = ind_var_gen.randomisation()
    other_outcomes_df = ind_var_gen.other_outcomes()

    all_variables = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        abstract_df,
        admin_strand_df,
        pubtype_eppi_df,
        publication_type_df,
        country_df,
        educational_setting_df,
        study_realism_df,
        student_age,
        number_of_schools_df,
        number_of_classes_df,
        treatment_group_df,
        participant_assignment_df,
        level_of_assignment_df,
        study_design_df,
        randomisation_df,
        other_outcomes_df
    ], axis=1, sort=False)

    if clean_cols:
        # Insert empty columns for each variable for data 
        # checkers to log errors prior to main analysis
        all_variables.insert(6, 'strand_CLEAN', '')
        all_variables.insert(8, 'pub_eppi_CLEAN', '')
        all_variables.insert(12, 'pub_type_CLEAN', '')
        all_variables.insert(14, 'loc_country_CLEAN', '')
        all_variables.insert(18, 'int_Setting_CLEAN', '')
        all_variables.insert(22, 'eco_valid_CLEAN', '')
        all_variables.insert(26, 'part_age_CLEAN', '')
        # school cols
        all_variables.insert(29, 'school_treat_CLEAN', '')
        all_variables.insert(32, 'school_cont_CLEAN', '')
        all_variables.insert(35, 'school_total_CLEAN', '')
        all_variables.insert(39, 'school_na_CLEAN', '')
        # class cols
        all_variables.insert(42, 'class_treat_CLEAN', '')
        all_variables.insert(45, 'class_cont_CLEAN',  '')
        all_variables.insert(48, 'class_total_CLEAN', '')
        all_variables.insert(52, 'class_na_CLEAN', '')
        all_variables.insert(56, 'treat_group_CLEAN', '')
        all_variables.insert(60, 'part_assig_CLEAN', '')
        all_variables.insert(64, 'level_assig_CLEAN', '')
        all_variables.insert(68, 'int_design_CLEAN', '')
        all_variables.insert(72, 'rand_CLEAN', '')
        all_variables.insert(76, 'out_other_CLEAN', '')
        all_variables.insert(80, 'out_info_CLEAN', '')
        all_variables.insert(83, 'part_other_CLEAN', '')

    # remove problematic text from outputs
    clean_up(all_variables)

    if verbose:
        verbose_display(all_variables)

    if save_file:
        save_dataframe(all_variables, "_DataFrame1.csv")

def make_dataframe_2(save_file=True, clean_cols=True, verbose=True):

    eppiid_df = ind_var_gen.eppi()
    author_df = ind_var_gen.author()
    year_df = ind_var_gen.date()
    admin_strand_df = ind_var_gen.admin_strand()
    intervention_name_df = ind_var_gen.intervention_name()
    intervention_description_df = ind_var_gen.intervention_desc()
    intervention_objectives_df = ind_var_gen.intervention_objec()
    intervention_org_type = ind_var_gen.int_org_type()
    intervention_training_provided_df = ind_var_gen.int_train_prov()
    intervention_focus_df = ind_var_gen.intervention_focus()
    intervention_teaching_approach_df = ind_var_gen.int_teach_appr()
    intervention_inclusion_df = ind_var_gen.int_inclusion()
    intervention_time_df = ind_var_gen.int_time()
    intervention_delivery_df = ind_var_gen.int_delivery()
    intervention_duration_df = ind_var_gen.int_duration()
    intervention_frequency_df = ind_var_gen.int_frequency()
    intervention_session_length_df = ind_var_gen.int_sess_len()
    intervention_detail_df = ind_var_gen.int_detail()
    intervention_costs_df = ind_var_gen.int_costs()
    intervention_evaluation_df = ind_var_gen.int_eval()
    baseline_differences_df = ind_var_gen.baseline_diff()
    comparability_df = ind_var_gen.comparability()
    comparability_vars_reported_df = ind_var_gen.com_var_rep()
    clustering_df = ind_var_gen.clustering()

    all_variables = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        admin_strand_df,
        intervention_name_df,
        intervention_description_df,
        intervention_objectives_df,
        intervention_org_type,
        intervention_training_provided_df,
        intervention_focus_df,
        intervention_teaching_approach_df,
        intervention_inclusion_df,
        intervention_time_df,
        intervention_delivery_df,
        intervention_duration_df,
        intervention_frequency_df,
        intervention_session_length_df,
        intervention_detail_df,
        intervention_costs_df,
        intervention_evaluation_df, # out eval then clean, eef eval then clean
        baseline_differences_df,
        comparability_df,
        comparability_vars_reported_df,
        clustering_df,
    ], axis=1, sort=False)

    if clean_cols:
        # insert empty columns per variable for data checkers to log changes
        all_variables.insert(5, 'strand_CLEAN', '')
        all_variables.insert(8, 'int_name_CLEAN', '')
        all_variables.insert(11, 'int_desc_CLEAN', '')
        all_variables.insert(14, 'int_objec_CLEAN', '')
        all_variables.insert(18, 'int_prov_CLEAN', '')
        all_variables.insert(22, 'int_training_CLEAN', '')
        all_variables.insert(26, 'int_part_CLEAN', '')
        all_variables.insert(30, 'int_approach_CLEAN', '')
        all_variables.insert(34, 'digital_tech_CLEAN', '')
        all_variables.insert(38, 'parent_partic_CLEAN', '')
        all_variables.insert(42, 'int_when_CLEAN', '')
        all_variables.insert(46, 'int_who_CLEAN', '')
        all_variables.insert(49, 'int_dur_CLEAN', '')
        all_variables.insert(52, 'int_freq_CLEAN', '')
        all_variables.insert(55, 'int_leng_CLEAN', '')
        all_variables.insert(59, 'int_fidel_CLEAN', '')
        all_variables.insert(63, 'int_cost_CLEAN', '')
        all_variables.insert(67, 'out_eval_CLEAN', '')
        all_variables.insert(69, 'eef_eval_CLEAN', '')
        all_variables.insert(73, 'base_diff_CLEAN', '')
        all_variables.insert(77, 'comp_anal_CLEAN', '')
        all_variables.insert(81, 'comp_var_rep_CLEAN', '')
        all_variables.insert(85, 'comp_var_CLEAN', '')
        all_variables.insert(89, 'clust_anal_CLEAN', '')

    # remove problematic text from outputs
    clean_up(all_variables)
    all_variables.replace(r'^\s*$', "NA", regex=True)

    if verbose:
        verbose_display(all_variables)

    if save_file:
        save_dataframe(all_variables, "_DataFrame2.csv")
        
def make_dataframe_3(save_file=True, clean_cols=True, verbose=True):

    eppiid_df = ind_var_gen.eppi()
    author_df = ind_var_gen.author()
    year_df = ind_var_gen.date()
    admin_strand_df = ind_var_gen.admin_strand()
    sample_size_df = ind_var_gen.samp_size()
    gender_df = ind_var_gen.gender()
    ses_fsm_df = ind_var_gen.ses_fm()
    initial_sample_size_df = ind_var_gen.samp_size_init()
    analyzed_sample_size_df = ind_var_gen.samp_size_anal()
    attrition_df = ind_var_gen.attrition()

    all_variables = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        admin_strand_df,
        sample_size_df,
        gender_df,
        ses_fsm_df,
        initial_sample_size_df,
        analyzed_sample_size_df,
        attrition_df
    ], axis=1, sort=False)

    if clean_cols:
        # insert empty columns per variable for data checkers to log changes
        all_variables.insert(5, 'strand_CLEAN', '')
        all_variables.insert(8, 'sample_analysed_CLEAN', '')
        all_variables.insert(12, 'part_gen_CLEAN', '')
        all_variables.insert(15, 'fsm_perc_CLEAN', '')
        all_variables.insert(18, 'fsm_info_CLEAN', '')
        all_variables.insert(21, 'fsm_na_CLEAN', '')
        all_variables.insert(24, 'base_n_treat_CLEAN', '')
        all_variables.insert(27, 'base_n_cont_CLEAN', '')
        all_variables.insert(30, 'base_n_treat2_CLEAN', '')
        all_variables.insert(33, 'base_n_treat3_CLEAN', '')
        all_variables.insert(36, 'n_treat_CLEAN', '')
        all_variables.insert(39, 'n_cont_CLEAN', '')
        all_variables.insert(42, 'n_treat2_CLEAN', '')
        all_variables.insert(45, 'n_cont2_CLEAN', '')
        all_variables.insert(49, 'attri_CLEAN', '')
        all_variables.insert(52, 'attri_treat_CLEAN', '')
        all_variables.insert(55, 'attri_perc_CLEAN', '')

    all_variables.replace('\r', ' ', regex=True, inplace=True)
    all_variables.replace('\n', ' ', regex=True, inplace=True)
    all_variables.replace(':', ' ',  regex=True, inplace=True)
    all_variables.replace(';', ' ',  regex=True, inplace=True)

    if verbose:
        verbose_display(all_variables)

    if save_file:
        save_dataframe(all_variables, "_DataFrame3_Sample_Size.csv")

def make_dataframe_4(save_file=True, clean_cols=True, verbose=True):

    eppiid_df = ind_var_gen.eppi()
    author_df = ind_var_gen.author()
    year_df = ind_var_gen.date()
    admin_strand_df = ind_var_gen.admin_strand()
    DescStatsOutcomeReported_df = ind_var_gen.desc_s_out_rep()
    DescStatsPrimaryOutcomeReported_Intervention_df = ind_var_gen.desc_s_p_out_rep_interv()
    DescStatsPrimaryOutcomeReported_Control_df = ind_var_gen.desc_s_p_out_rep_contr()
    DescStatsPrimaryOutcomeReported_Intervention_TWO_df = ind_var_gen.desc_s_o_out_rep_interv_2()
    DescStatsPrimaryOutcomeReported_Control_TWO_df = ind_var_gen.desc_s_prim_out_rep_c_two()

    all_variables = pd.concat([
        eppiid_df, 
        author_df, 
        year_df, 
        admin_strand_df, 
        DescStatsOutcomeReported_df,
        DescStatsPrimaryOutcomeReported_Intervention_df, 
        DescStatsPrimaryOutcomeReported_Control_df,
        DescStatsPrimaryOutcomeReported_Intervention_TWO_df, 
        DescStatsPrimaryOutcomeReported_Control_TWO_df
    ], axis=1, sort=False)

    if clean_cols:
        # insert empty columns per variable for data checkers to log changes
        all_variables.insert(8, 'desc_stats_CLEAN', '')
        all_variables.insert(11, 'n_treat_CLEAN', '')
        all_variables.insert(14, 'pre_t_mean_CLEAN', '')
        all_variables.insert(17, 'pre_t_sd_CLEAN', '')
        all_variables.insert(20, 'post_t_mean_CLEAN', '')
        all_variables.insert(23, 'post_t_sd_CLEAN', '')
        all_variables.insert(26, 'gain_t_mean_CLEAN', '')
        all_variables.insert(29, 'gain_t_sd_CLEAN', '')
        all_variables.insert(32, 'out_t_other_CLEAN', '')
        all_variables.insert(35, 'n_cont_ht_CLEAN', '')
        all_variables.insert(38, 'pre_c_mean_CLEAN', '')
        all_variables.insert(41, 'pre_c_sd_CLEAN', '')
        all_variables.insert(44, 'post_c_mean_CLEAN', '')
        all_variables.insert(47, 'post_c_sd_CLEAN', '')
        all_variables.insert(50, 'gain_c_mean_CLEAN', '')
        all_variables.insert(53, 'gain_c_sd_CLEAN', '')
        all_variables.insert(56, 'out_c_other_CLEAN', '')
        all_variables.insert(59, 'n_treat2_CLEAN', '')
        all_variables.insert(62, 'pre_t2_mean_CLEAN', '')
        all_variables.insert(65, 'pre_t2_sd_CLEAN', '')
        all_variables.insert(68, 'post_t2_mean_CLEAN', '')
        all_variables.insert(71, 'post_t2_sd_CLEAN', '')
        all_variables.insert(74, 'gain_t2_mean_CLEAN', '')
        all_variables.insert(77, 'gain_t2_sd_CLEAN', '')
        all_variables.insert(80, 'out_t2_other_CLEAN', '')
        all_variables.insert(83, 'n_cont2_CLEAN', '')
        all_variables.insert(86, 'pre_c2_mean_CLEAN', '')
        all_variables.insert(89, 'pre_c2_sd_CLEAN', '')
        all_variables.insert(92, 'post_c2_mean_CLEAN', '')
        all_variables.insert(95, 'post_c2_sd_CLEAN', '')
        all_variables.insert(98, 'gain_c2_mean_CLEAN', '')
        all_variables.insert(101, 'gain_c2_sd_CLEAN', '')
        all_variables.insert(104, 'out_c2_other_CLEAN', '')
        all_variables.insert(108, 'follow_up_CLEAN', '')

    clean_up(all_variables)

    if verbose:
        verbose_display(all_variables)

    if save_file:
        save_dataframe(all_variables, "_Effect_Size_A.csv")

def make_dataframe_5(save_file=True, clean_cols=True, verbose=True):

    global toolkit_test_type, toolkit_es_type
    from Toolkit_Outcome_Check import outcome_num

    eppiid_df = ind_var_gen.eppi()
    author_df = ind_var_gen.author()
    year_df = ind_var_gen.date()
    admin_strand_df = ind_var_gen.admin_strand()
    outcometype_df = ind_var_gen.out_type()
    smd_df = ind_var_gen.smd()
    sesmd_df = ind_var_gen.ses_md()
    cilowersmd_df = ind_var_gen.cilower()
    ciuppersmd_df = ind_var_gen.ciupper()
    outcome_df = ind_var_gen.outcome()
    sample_df = ind_var_gen.sample()
    out_comp_df = ind_var_gen.out_comp()
    effectsizetype_df = ind_var_gen.es_type()
    outcome_measure_df = ind_var_gen.out_measure()
    outcome_title_df = ind_var_gen.out_tit()
    group1N_df = ind_var_gen.group1_n()
    group2N_df = ind_var_gen.group2_n()
    group1mean_df = ind_var_gen.group1_mean()
    group2mean_df = ind_var_gen.group2_mean()
    group1sd_df = ind_var_gen.group1_sd()
    group2sd_df = ind_var_gen.group2_sd()
    outcome_description_df = ind_var_gen.out_desc()
    testtype_outcome_df = ind_var_gen.test_type()

    # concatenate record detail data frames
    record_details_df = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        admin_strand_df
    ], axis=1)

    # concatenate all main dataframes
    df = pd.concat([
        outcometype_df,
        smd_df,
        sesmd_df,
        cilowersmd_df,
        ciuppersmd_df,
        outcome_df,
        sample_df,
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
        sample_df,
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
    toolkit_prim = []
    toolkit_prim_smd = []
    toolkit_prim_se = []
    toolkit_prim_ci_lower = []
    toolkit_prim_ci_upper = []
    toolkit_prim_outcome = []
    toolkit_prim_sample = []
    toolkit_prim_outcomp = []
    toolkit_es_type = []
    toolkit_out_measure = []
    toolkit_out_tit = []
    toolkit_g1_n = []
    toolkit_g2_n = []
    toolkit_g1_mean = []
    toolkit_g2_mean = []
    toolkit_g1_sd = []
    toolkit_g2_sd = []
    toolkit_out_desc = []
    toolkit_test_type = []

    toolkit_holders = [
        toolkit_prim,
        toolkit_prim_smd,
        toolkit_prim_se,
        toolkit_prim_ci_lower,
        toolkit_prim_ci_upper,
        toolkit_prim_outcome,
        toolkit_prim_sample,
        toolkit_prim_outcomp,
        toolkit_es_type,
        toolkit_out_measure,
        toolkit_out_tit,
        toolkit_g1_n,
        toolkit_g2_n,
        toolkit_g1_mean,
        toolkit_g2_mean,
        toolkit_g1_sd,
        toolkit_g2_sd,
        toolkit_out_desc,
        toolkit_test_type
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
            if 'Toolkit primary outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(toolkit_holders):
                    holder.append(df[outcome_vars[counter2] +f"{outcome_n}"][counter])
                break
        else:
            for holder in toolkit_holders:
                holder.append("NA")

    reading_prim = []
    reading_prim_smd = []
    reading_prim_se = []
    reading_prim_ci_lower = []
    reading_prim_ci_upper = []
    reading_prim_outcome = []
    reading_prim_sample = []
    reading_prim_outcomp = []
    reading_prim_es_type = []
    reading_prim_out_measure = []
    reading_prim_out_tit = []
    reading_prim_g1_n = []
    reading_prim_g2_n = []
    reading_prim_g1_mean = []
    reading_prim_g2_mean = []
    reading_prim_g1_sd = []
    reading_prim_g2_sd = []
    reading_prim_out_desc = []
    reading_test_type = []

    reading_holders = [
        reading_prim,
        reading_prim_smd,
        reading_prim_se,
        reading_prim_ci_lower,
        reading_prim_ci_upper,
        reading_prim_outcome,
        reading_prim_sample,
        reading_prim_outcomp,
        reading_prim_es_type,
        reading_prim_out_measure,
        reading_prim_out_tit,
        reading_prim_g1_n,
        reading_prim_g2_n,
        reading_prim_g1_mean,
        reading_prim_g2_mean,
        reading_prim_g1_sd,
        reading_prim_g2_sd,
        reading_prim_out_desc,
        reading_test_type
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Reading primary outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(reading_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in reading_holders:
                holder.append("NA")

    Writing_and_spelling_prim = []
    Writing_and_spelling_prim_smd = []
    Writing_and_spelling_prim_se = []
    Writing_and_spelling_prim_ci_lower = []
    Writing_and_spelling_prim_ci_upper = []
    Writing_and_spelling_prim_outcome = []
    Writing_and_spelling_prim_sample = []
    Writing_and_spelling_prim_outcomp = []
    Writing_and_spelling_prim_es_type = []
    Writing_and_spelling_prim_out_measure = []
    Writing_and_spelling_prim_out_tit = []
    Writing_and_spelling_prim_g1_n = []
    Writing_and_spelling_prim_g2_n = []
    Writing_and_spelling_prim_g1_mean = []
    Writing_and_spelling_prim_g2_mean = []
    Writing_and_spelling_prim_g1_sd = []
    Writing_and_spelling_prim_g2_sd = []
    Writing_and_spelling_prim_out_desc = []
    Writing_and_spelling_test_type = []

    writing_holders = [
        Writing_and_spelling_prim,
        Writing_and_spelling_prim_smd,
        Writing_and_spelling_prim_se,
        Writing_and_spelling_prim_ci_lower,
        Writing_and_spelling_prim_ci_upper,
        Writing_and_spelling_prim_outcome,
        Writing_and_spelling_prim_sample,
        Writing_and_spelling_prim_outcomp,
        Writing_and_spelling_prim_es_type,
        Writing_and_spelling_prim_out_measure,
        Writing_and_spelling_prim_out_tit,
        Writing_and_spelling_prim_g1_n,
        Writing_and_spelling_prim_g2_n,
        Writing_and_spelling_prim_g1_mean,
        Writing_and_spelling_prim_g2_mean,
        Writing_and_spelling_prim_g1_sd,
        Writing_and_spelling_prim_g2_sd,
        Writing_and_spelling_prim_out_desc,
        Writing_and_spelling_test_type
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Writing and spelling primary outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(writing_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in writing_holders:
                holder.append("NA")

    Mathematics_prim = []
    Mathematics_prim_smd = []
    Mathematics_prim_se = []
    Mathematics_prim_ci_lower = []
    Mathematics_prim_ci_upper = []
    Mathematics_prim_outcome = []
    Mathematics_prim_sample = []
    Mathematics_prim_outcomp = []
    Mathematics_prim_es_type = []
    Mathematics_prim_out_measure = []
    Mathematics_prim_out_tit = []
    Mathematics_prim_g1_n = []
    Mathematics_prim_g2_n = []
    Mathematics_prim_g1_mean = []
    Mathematics_prim_g2_mean = []
    Mathematics_prim_g1_sd = []
    Mathematics_prim_g2_sd = []
    Mathematics_prim_out_desc = []
    Mathematics_test_type = []

    mathematics_holders = [
        Mathematics_prim,
        Mathematics_prim_smd,
        Mathematics_prim_se,
        Mathematics_prim_ci_lower,
        Mathematics_prim_ci_upper,
        Mathematics_prim_outcome,
        Mathematics_prim_sample,
        Mathematics_prim_outcomp,
        Mathematics_prim_es_type,
        Mathematics_prim_out_measure,
        Mathematics_prim_out_tit,
        Mathematics_prim_g1_n,
        Mathematics_prim_g2_n,
        Mathematics_prim_g1_mean,
        Mathematics_prim_g2_mean,
        Mathematics_prim_g1_sd,
        Mathematics_prim_g2_sd,
        Mathematics_prim_out_desc,
        Mathematics_test_type
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Mathematics primary outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(mathematics_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in mathematics_holders:
                holder.append("NA")

    Science_prim = []
    Science_prim_smd = []
    Science_prim_se = []
    Science_prim_ci_lower = []
    Science_prim_ci_upper = []
    Science_prim_outcome = []
    Science_prim_sample = []
    Science_prim_outcomp = []
    Science_prim_es_type = []
    Science_prim_out_measure = []
    Science_prim_out_tit = []
    Science_prim_g1_n = []
    Science_prim_g2_n = []
    Science_prim_g1_mean = []
    Science_prim_g2_mean = []
    Science_prim_g1_sd = []
    Science_prim_g2_sd = []
    Science_prim_out_desc = []
    Science_test_type = []

    science_holders = [
        Science_prim,
        Science_prim_smd,
        Science_prim_se,
        Science_prim_ci_lower,
        Science_prim_ci_upper,
        Science_prim_outcome,
        Science_prim_sample,
        Science_prim_outcomp,
        Science_prim_es_type,
        Science_prim_out_measure,
        Science_prim_out_tit,
        Science_prim_g1_n,
        Science_prim_g2_n,
        Science_prim_g1_mean,
        Science_prim_g2_mean,
        Science_prim_g1_sd,
        Science_prim_g2_sd,
        Science_prim_out_desc,
        Science_test_type
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'Science primary outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(science_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in science_holders:
                holder.append("NA")

    FSM_prim = []
    FSM_prim_smd = []
    FSM_prim_se = []
    FSM_prim_ci_lower = []
    FSM_prim_ci_upper = []
    FSM_prim_outcome = []
    FSM_prim_sample = []
    FSM_prim_outcomp = []
    FSM_prim_es_type = []
    FSM_prim_out_measure = []
    FSM_prim_out_tit = []
    FSM_prim_g1_n = []
    FSM_prim_g2_n = []
    FSM_prim_g1_mean = []
    FSM_prim_g2_mean = []
    FSM_prim_g1_sd = []
    FSM_prim_g2_sd = []
    FSM_prim_out_desc = []
    FSM_test_type = []

    fsm_holders = [
        FSM_prim,
        FSM_prim_smd,
        FSM_prim_se,
        FSM_prim_ci_lower,
        FSM_prim_ci_upper,
        FSM_prim_outcome,
        FSM_prim_sample,
        FSM_prim_outcomp,
        FSM_prim_es_type,
        FSM_prim_out_measure,
        FSM_prim_out_tit,
        FSM_prim_g1_n,
        FSM_prim_g2_n,
        FSM_prim_g1_mean,
        FSM_prim_g2_mean,
        FSM_prim_g1_sd,
        FSM_prim_g2_sd,
        FSM_prim_out_desc,
        FSM_test_type
    ]

    for counter, row in enumerate(df['out_type_1']):
        for outcome_n in range(1, outcome_num+1):
            if 'SES/FSM outcome' in df[f'out_type_{outcome_n}'][counter]:
                for counter2, holder in enumerate(fsm_holders):
                    holder.append(
                        df[outcome_vars[counter2] + f"{outcome_n}"][counter])
                break
        else:
            for holder in fsm_holders:
                holder.append("NA")

    df_zip = list(zip(
        toolkit_out_tit,
        toolkit_out_desc,
        toolkit_prim,
        toolkit_prim_smd,
        toolkit_prim_se,
        toolkit_out_measure,
        toolkit_g1_n,
        toolkit_g1_mean,
        toolkit_g1_sd,
        toolkit_g2_n,
        toolkit_g2_mean,
        toolkit_g2_sd,
        toolkit_prim_ci_lower,
        toolkit_prim_ci_upper,
        toolkit_prim_outcome,
        toolkit_prim_sample,
        toolkit_prim_outcomp,
        toolkit_es_type,
        toolkit_test_type,

        reading_prim_out_tit,
        reading_prim_out_desc,
        reading_prim,
        reading_prim_smd,
        reading_prim_se,
        reading_prim_out_measure,
        reading_prim_g1_n,
        reading_prim_g1_mean,
        reading_prim_g1_sd,
        reading_prim_g2_n,
        reading_prim_g2_mean,
        reading_prim_g2_sd,
        reading_prim_ci_lower,
        reading_prim_ci_upper,
        reading_prim_outcome,
        reading_prim_sample,
        reading_prim_outcomp,
        reading_prim_es_type,
        reading_test_type,

        Writing_and_spelling_prim_out_tit,
        Writing_and_spelling_prim_out_desc,
        Writing_and_spelling_prim,
        Writing_and_spelling_prim_smd,
        Writing_and_spelling_prim_se,
        Writing_and_spelling_prim_out_measure,
        Writing_and_spelling_prim_g1_n,
        Writing_and_spelling_prim_g1_mean,
        Writing_and_spelling_prim_g1_sd,
        Writing_and_spelling_prim_g2_n,
        Writing_and_spelling_prim_g2_mean,
        Writing_and_spelling_prim_g2_sd,
        Writing_and_spelling_prim_ci_lower,
        Writing_and_spelling_prim_ci_upper,
        Writing_and_spelling_prim_outcome,
        Writing_and_spelling_prim_sample,
        Writing_and_spelling_prim_outcomp,
        Writing_and_spelling_prim_es_type,
        Writing_and_spelling_test_type,

        Mathematics_prim_out_tit,
        Mathematics_prim_out_desc,
        Mathematics_prim,
        Mathematics_prim_smd,
        Mathematics_prim_se,
        Mathematics_prim_out_measure,
        Mathematics_prim_g1_n,
        Mathematics_prim_g1_mean,
        Mathematics_prim_g1_sd,
        Mathematics_prim_g2_n,
        Mathematics_prim_g2_mean,
        Mathematics_prim_g2_sd,
        Mathematics_prim_ci_lower,
        Mathematics_prim_ci_upper,
        Mathematics_prim_outcome,
        Mathematics_prim_sample,
        Mathematics_prim_outcomp,
        Mathematics_prim_es_type,
        Mathematics_test_type,

        Science_prim_out_tit,
        Science_prim_out_desc,
        Science_prim,
        Science_prim_smd,
        Science_prim_se,
        Science_prim_out_measure,
        Science_prim_g1_n,
        Science_prim_g1_mean,
        Science_prim_g1_sd,
        Science_prim_g2_n,
        Science_prim_g2_mean,
        Science_prim_g2_sd,
        Science_prim_ci_lower,
        Science_prim_ci_upper,
        Science_prim_outcome,
        Science_prim_sample,
        Science_prim_outcomp,
        Science_prim_es_type,
        Science_test_type,

        FSM_prim_out_tit,
        FSM_prim_out_desc,
        FSM_prim,
        FSM_prim_smd,
        FSM_prim_se,
        FSM_prim_out_measure,
        FSM_prim_g1_n,
        FSM_prim_g1_mean,
        FSM_prim_g1_sd,
        FSM_prim_g2_n,
        FSM_prim_g2_mean,
        FSM_prim_g2_sd,
        FSM_prim_ci_lower,
        FSM_prim_ci_upper,
        FSM_prim_outcome,
        FSM_prim_sample,
        FSM_prim_outcomp,
        FSM_prim_es_type,
        FSM_test_type
    ))

    df = pd.DataFrame(df_zip)

    df.rename(columns={
        0: "out_tit_tool",
        1: "out_desc_tool",
        2: "out_type_tool",
        3: "smd_tool",
        4: "se_tool",
        5: "out_measure_tool",
        6: "out_g1_n_tool",
        7: "out_g1_mean_tool",
        8: "out_g1_sd_tool",
        9: "out_g2_n_tool",
        10: "out_g2_mean_tool",
        11: "out_g2_sd_tool",
        12: "ci_lower_tool",
        13: "ci_upper_tool",
        14: "out_label_tool",
        15: "out_samp_tool",
        16: "out_comp_tool",
        17: "out_es_type_tool",
        18: "out_test_type_raw_tool",

        19: "out_tit_red",
        20: "out_desc_red",
        21: "out_type_red",
        22: "smd_red",
        23: "se_red",
        24: "out_measure_red",
        25: "out_g1_n_red",
        26: "out_g1_mean_red",
        27: "out_g1_sd_red",
        28: "out_g2_n_red",
        29: "out_g2_mean_red",
        30: "out_g2_sd_red",
        31: "ci_lower_red",
        32: "ci_upper_red",
        33: "out_label_red",
        34: "out_samp_red",
        35: "out_comp_red",
        36: "out_es_type_red",
        37: "out_test_type_raw_red",

        38: "out_tit_wri",
        39: "out_desc_wri",
        40: "out_type_wri",
        41: "smd_wri",
        42: "se_wri",
        43: "out_measure_wri",
        44: "out_g1_n_wri",
        45: "out_g1_mean_wri",
        46: "out_g1_sd_wri",
        47: "out_g2_n_wri",
        48: "out_g2_mean_wri",
        49: "out_g2_sd_wri",
        50: "ci_lower_wri",
        51: "ci_upper_wri",
        52: "out_label_wri",
        53: "out_samp_wri",
        54: "out_comp_wri",
        55: "out_es_type_wri",
        56: "out_test_type_raw_wri",

        57: "out_tit_math",
        58: "out_desc_math",
        59: "out_type_math",
        60: "smd_math",
        61: "se_math",
        62: "out_measure_math",
        63: "out_g1_n_math",
        64: "out_g1_mean_math",
        65: "out_g1_sd_math",
        66: "out_g2_n_math",
        67: "out_g2_mean_math",
        68: "out_g2_sd_math",
        69: "ci_lower_math",
        70: "ci_upper_math",
        71: "out_label_math",
        72: "out_samp_math",
        73: "out_comp_math",
        74: "out_es_type_math",
        75: "out_test_type_raw_math",

        76: "out_tit_sci",
        77: "out_desc_sci",
        78: "out_type_sci",
        79: "smd_sci",
        80: "se_sci",
        81: "out_measure_sci",
        82: "out_g1_n_sci",
        83: "out_g1_mean_sci",
        84: "out_g1_sd_sci",
        85: "out_g2_n_sci",
        86: "out_g2_mean_sci",
        87: "out_g2_sd_sci",
        88: "ci_lower_sci",
        89: "ci_upper_sci",
        90: "out_label_sci",
        91: "out_samp_sci",
        92: "out_comp_sci",
        93: "out_es_type_sci",
        94: "out_test_type_raw_sci",

        95: "out_tit_fsm",
        96: "out_desc_fsm",
        97: "out_type_fsm",
        98: "smd_fsm",
        99: "se_fsm",
        100: "out_measure_fsm",
        101: "out_g1_n_fsm",
        102: "out_g1_mean_fsm",
        103: "out_g1_sd_fsm",
        104: "out_g2_n_fsm",
        105: "out_g2_mean_fsm",
        106: "out_g2_sd_fsm",
        107: "ci_lower_fsm",
        108: "ci_upper_fsm",
        109: "out_label_fsm",
        110: "out_samp_fsm",
        111: "out_comp_fsm",
        112: "out_es_type_fsm",
        113: "out_test_type_raw_fsm"

    }, inplace=True)

    # concatenate record details and main dataframes
    all_variables = pd.concat([record_details_df, df], axis=1, sort=False)

    if clean_cols:
        new_cols = [
        "out_tit_tool",
        'out_tit_tool_CLEAN',
        "out_desc_tool",
        'out_desc_tool_CLEAN', 
        "out_type_tool",
        'out_type_tool_CLEAN',
        "smd_tool",
        'smd_tool_CLEAN',
        "se_tool",
        'se_tool_CLEAN',
        "out_measure_tool",
        'out_measure_tool_CLEAN',
        "out_g1_n_tool",
        'out_g1_n_tool_CLEAN',
        "out_g1_mean_tool",
        'out_g1_mean_tool_CLEAN',
        "out_g1_sd_tool",
        'out_g1_sd_tool_CLEAN',
        "out_g2_n_tool",
        'out_g2_n_tool_CLEAN',
        "out_g2_mean_tool",
        'out_g2_mean_tool_CLEAN',
        "out_g2_sd_tool",
        'out_g2_sd_tool_CLEAN',
        "ci_lower_tool",
        'ci_lower_tool_CLEAN', 
        "ci_upper_tool",
        'ci_upper_tool_CLEAN',
        "out_label_tool",
        'out_label_tool_CLEAN',
        "out_samp_tool",
        'out_samp_tool_CLEAN',
        "out_comp_tool",
        'out_comp_tool_CLEAN', 
        "out_es_type_tool",
        'out_es_type_tool_CLEAN',
        "out_test_type_raw_tool",
        'out_test_type_raw_tool_CLEAN'
        ]

        all_variables = df.reindex(columns=new_cols, fill_value='')

        all_variables = pd.concat([record_details_df, all_variables], axis=1, sort=False)

    if verbose:
        verbose_display(all_variables)

    if save_file:
        save_dataframe(all_variables, "_Effect_Size_B.csv")

print('''
      ============================================
      *     Data Cleaning Dataframe Selection    * 
      ============================================

      ------------------
      *  Main Toolkit  *
      ------------------

      1. Dataframe 1   [Study, Research and Design Variables]
      2. Dataframe 2   [Intervention Details]
      3. Sample Size   [Sample Size Variables]
      4. Effect Size A [Descriptive Statistics]
      5. Effect Size B [Outcome Details]
      6. All 5 dataframes
      '''
)

# Get user selection for strand specific dataframe (if needed)
data_cleaning_option = int(input("Enter the number corresponding to the dataframe(s) you want: "))

match data_cleaning_option:
    # MAIN TOOLKIT
    case 1:
        print("- Data cleaning selection: Dataframe 1 - Study, Research and Design Variables")
        make_dataframe_1(save_file=True, clean_cols=True, verbose=False)
    case 2: 
        print("- Data cleaning selection: Dataframe 2 - Intervention Details")
        make_dataframe_2(save_file=True, clean_cols=True, verbose=False)
    case 3:
        print("- Data cleaning selection: Sample Size - Sample Size Variables")
        make_dataframe_3(save_file=True, clean_cols=True, verbose=False)
    case 4:
        print("- Data cleaning selection: Effect Size A - Descriptive Statistics")
        make_dataframe_4(save_file=True, clean_cols=True, verbose=False)
    case 5:
        print("- Data cleaning selection: Effect Size B - Outcome Details")
        make_dataframe_5(save_file=True, clean_cols=True, verbose=False)
    case 6:
        print('''- Data cleaning selection: 

            All 5 dataframes

            1) Dataframe 1 - Study, Research and Design Variables
            2) Dataframe 2 - Intervention Details
            3) Sample Size - Sample Size Variables
            4) Effect Size A - Descriptive Statistics
            5) Effect Size B - Outcome Details
        ''')

        make_dataframe_1(save_file=True, clean_cols=True, verbose=False)
        make_dataframe_2(save_file=True, clean_cols=True, verbose=False)
        make_dataframe_3(save_file=True, clean_cols=True, verbose=False)
        make_dataframe_4(save_file=True, clean_cols=True, verbose=False)
        make_dataframe_5(save_file=True, clean_cols=True, verbose=False)
