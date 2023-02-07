#!/usr/bin/env python3

# standard imports
import os
import sys
import pandas as pd
import re
from toolz import interleave

# lcoal imports - core extraction functions
from Main import verbose_display
from Main import save_dataframe

# local imports - individual variables
from ind_var_Gen import eppiid_df
from ind_var_Gen import author_df
from ind_var_Gen import year_df
from ind_var_Gen import admin_strand_df
from ind_var_Gen import abstract_df
from ind_var_Gen import pubtype_eppi_df

datafile = sys.argv[1]

def make_dataframe_1(save_file=True, clean_cols=True, verbose=True):

    from ind_var_Gen import publication_type_df
    from ind_var_Gen import country_df
    from ind_var_Gen import educational_setting_df
    from ind_var_Gen import study_realism_df
    from ind_var_Gen import student_age
    from ind_var_Gen import number_of_schools_df
    from ind_var_Gen import number_of_classes_df
    from ind_var_Gen import treatment_group_df
    from ind_var_Gen import participant_assignment_df
    from ind_var_Gen import level_of_assignment_df
    from ind_var_Gen import study_design_df
    from ind_var_Gen import randomisation_df
    from ind_var_Gen import other_outcomes_df

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
    all_variables.replace('\r', ' ', regex=True, inplace=True)
    all_variables.replace('\n', ' ', regex=True, inplace=True)
    all_variables.replace(':', ' ',  regex=True, inplace=True)
    all_variables.replace(';', ' ',  regex=True, inplace=True)

    if verbose:
        verbose_display(all_variables)

    if save_file:
        save_dataframe(all_variables, "_DataFrame1.csv")


def make_dataframe_2(save_file=True, clean_cols=True, verbose=True):

    from ind_var_Gen import intervention_name_df
    from ind_var_Gen import intervention_description_df
    from ind_var_Gen import intervention_objectives_df
    from ind_var_Gen import intervention_training_provided_df
    from ind_var_Gen import intervention_org_type
    from ind_var_Gen import intervention_focus_df
    from ind_var_Gen import intervention_teaching_approach_df
    from ind_var_Gen import intervention_inclusion_df
    from ind_var_Gen import intervention_time_df
    from ind_var_Gen import intervention_delivery_df
    from ind_var_Gen import intervention_duration_df
    from ind_var_Gen import intervention_frequency_df
    from ind_var_Gen import intervention_session_length_df
    from ind_var_Gen import intervention_detail_df
    from ind_var_Gen import intervention_costs_df
    from ind_var_Gen import intervention_evaluation_df
    from ind_var_Gen import baseline_differences_df
    from ind_var_Gen import comparability_df
    from ind_var_Gen import comparability_vars_reported_df
    from ind_var_Gen import clustering_df

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
    all_variables.replace('\r', ' ', regex=True, inplace=True)
    all_variables.replace('\n', ' ', regex=True, inplace=True)
    all_variables.replace(':', ' ',  regex=True, inplace=True)
    all_variables.replace(';', ' ',  regex=True, inplace=True)
    all_variables.replace(r'^\s*$', "NA", regex=True)

    if verbose:
        verbose_display(all_variables)

    if save_file:
        save_dataframe(all_variables, "_DataFrame2.csv")
        
def make_dataframe_3(save_file=True, clean_cols=True, verbose=True):

    from ind_var_Gen.SampleSize import sample_size_df
    from ind_var_Gen.Gender import gender_df
    from ind_var_Gen.ses_fsm import ses_fsm_df
    from ind_var_Gen.Sample_Size_Initial import initial_sample_size_df
    from ind_var_Gen.Sample_Size_Analyzed import analyzed_sample_size_df
    from ind_var_Gen.Attrition import attrition_df

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

    from ind_var_Gen import DescStatsOutcomeReported_df
    from ind_var_Gen import DescStatsPrimaryOutcomeReported_Intervention_df
    from ind_var_Gen import DescStatsPrimaryOutcomeReported_Control_df
    from ind_var_Gen import DescStatsPrimaryOutcomeReported_Intervention_TWO_df
    from ind_var_Gen import DescStatsPrimaryOutcomeReported_Control_TWO_df

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

    all_variables.replace('\r', ' ', regex=True, inplace=True)
    all_variables.replace('\n', ' ', regex=True, inplace=True)
    all_variables.replace(':', ' ',  regex=True, inplace=True)
    all_variables.replace(';', ' ',  regex=True, inplace=True)

    if verbose:
        verbose_display(all_variables)

    if save_file:
        save_dataframe(all_variables, "_Effect_Size_A.csv")


def make_dataframe_5(save_file=True, clean_cols=True, verbose=True):

    global toolkit_test_type, toolkit_es_type

    from ind_var_Gen.OutcomeType import outcometype_df
    from ind_var_Gen.smd import smd_df
    from ind_var_Gen.sesmd import sesmd_df
    from ind_var_Gen.OutcomeDescription import outcome_description_df
    from ind_var_Gen.OutcomeTitle import outcome_title_df
    from ind_var_Gen.CIlowerSMD import cilowersmd_df
    from ind_var_Gen.CIupperSMD import ciuppersmd_df
    from ind_var_Gen.Sample import sample_df
    from ind_var_Gen.Outcome import outcome_df
    from ind_var_Gen.EffectSizeType import effectsizetype_df
    from ind_var_Gen.OutcomeComparison import out_comp_df
    from ind_var_Gen.OutcomeMeasure import outcome_measure_df
    from ind_var_Gen.Group1_N import group1N_df
    from ind_var_Gen.Group2_N import group2N_df
    from ind_var_Gen.Group1_Mean import group1mean_df
    from ind_var_Gen.Group2_Mean import group2mean_df
    from ind_var_Gen.Group1_SD import group1sd_df
    from ind_var_Gen.Group2_SD import group2sd_df
    from ind_var_Gen.TestType import testtype_outcome_df

    from Toolkit_Outcome_Check import outcome_num

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
        # insert empty columns per variable for data checkers to log changes
        all_variables.insert(6, 'out_tit_tool_CLEAN', '')
        all_variables.insert(8, 'out_desc_tool_CLEAN', '')
        all_variables.insert(10, 'out_type_tool_CLEAN', '')
        all_variables.insert(12, 'smd_tool_CLEAN', '')
        all_variables.insert(14, 'se_tool_CLEAN', '')
        all_variables.insert(16, 'out_measure_tool_CLEAN', '')
        all_variables.insert(18, 'out_g1_n_tool_CLEAN', '')
        all_variables.insert(20, 'out_g1_mean_tool_CLEAN', '')
        all_variables.insert(22, 'out_g1_sd_tool_CLEAN', '')
        all_variables.insert(24, 'out_g2_n_tool_CLEAN', '')
        all_variables.insert(26, 'out_g2_mean_tool_CLEAN', '')
        all_variables.insert(28, 'out_g2_sd_tool_CLEAN', '')
        all_variables.insert(30, 'ci_lower_tool_CLEAN', '')
        all_variables.insert(32, 'ci_upper_tool_CLEAN', '')
        all_variables.insert(34, 'out_label_tool_CLEAN', '')
        all_variables.insert(36, 'out_samp_tool_CLEAN', '')
        all_variables.insert(38, 'out_comp_tool_CLEAN', '')
        all_variables.insert(40, 'out_es_type_tool_CLEAN', '')
        all_variables.insert(42, 'out_test_type_raw_tool_CLEAN', '')

        all_variables.insert(44, 'out_tit_red_CLEAN', '')
        all_variables.insert(46, 'out_desc_red_CLEAN', '')
        all_variables.insert(48, 'out_type_red_CLEAN', '')
        all_variables.insert(50, 'smd_red_CLEAN', '')
        all_variables.insert(52, 'se_red_CLEAN', '')
        all_variables.insert(54, 'out_measure_red_CLEAN', '')
        all_variables.insert(56, 'out_g1_n_red_CLEAN', '')
        all_variables.insert(58, 'out_g1_mean_red_CLEAN', '')
        all_variables.insert(60, 'out_g1_sd_red_CLEAN', '')
        all_variables.insert(62, 'out_g2_n_red_CLEAN', '')
        all_variables.insert(64, 'out_g2_mean_red_CLEAN', '')
        all_variables.insert(66, 'out_g2_sd_red_CLEAN', '')
        all_variables.insert(68, 'ci_lower_red_CLEAN', '')
        all_variables.insert(70, 'ci_upper_red_CLEAN', '')
        all_variables.insert(72, 'out_label_red_CLEAN', '')
        all_variables.insert(74, 'out_samp_red_CLEAN', '')
        all_variables.insert(76, 'out_comp_red_CLEAN', '')
        all_variables.insert(78, 'out_es_type_red_CLEAN', '')
        all_variables.insert(80, 'out_test_type_raw_red_CLEAN', '')

        all_variables.insert(82, 'out_tit_wri_CLEAN', '')
        all_variables.insert(84, 'out_desc_wri_CLEAN', '')
        all_variables.insert(86, 'out_type_wri_CLEAN', '')
        all_variables.insert(88, 'smd_wri_CLEAN', '')
        all_variables.insert(90, 'se_wri_CLEAN', '')
        all_variables.insert(92, 'out_measure_wri_CLEAN', '')
        all_variables.insert(94, 'out_g1_n_wri_CLEAN', '')
        all_variables.insert(96, 'out_g1_mean_wri_CLEAN', '')
        all_variables.insert(98, 'out_g1_sd_wri_CLEAN', '')
        all_variables.insert(100, 'out_g2_n_wri_CLEAN', '')
        all_variables.insert(102, 'out_g2_mean_wri_CLEAN', '')
        all_variables.insert(104, 'out_g2_sd_wri_CLEAN', '')
        all_variables.insert(106, 'ci_lower_wri_CLEAN', '')
        all_variables.insert(108, 'ci_upper_wri_CLEAN', '')
        all_variables.insert(110, 'out_label_wri_CLEAN', '')
        all_variables.insert(112, 'out_samp_wri_CLEAN', '')
        all_variables.insert(114, 'out_comp_wri_CLEAN', '')
        all_variables.insert(116, 'out_es_type_wri_CLEAN', '')
        all_variables.insert(118, 'out_test_type_wri_CLEAN', '')

        all_variables.insert(120, 'out_tit_math_CLEAN', '')
        all_variables.insert(122, 'out_desc_math_CLEAN', '')
        all_variables.insert(124, 'out_type_math_CLEAN', '')
        all_variables.insert(126, 'smd_math_CLEAN', '')
        all_variables.insert(128, 'se_math_CLEAN', '')
        all_variables.insert(130, 'out_measure_math_CLEAN', '')
        all_variables.insert(132, 'out_g1_n_math_CLEAN', '')
        all_variables.insert(134, 'out_g1_mean_math_CLEAN', '')
        all_variables.insert(136, 'out_g1_sd_math_CLEAN', '')
        all_variables.insert(138, 'out_g2_n_math_CLEAN', '')
        all_variables.insert(140, 'out_g2_mean_math_CLEAN', '')
        all_variables.insert(142, 'out_g2_sd_math_CLEAN', '')
        all_variables.insert(144, 'ci_lower_math_CLEAN', '')
        all_variables.insert(146, 'ci_upper_math_CLEAN', '')
        all_variables.insert(148, 'out_label_math_CLEAN', '')
        all_variables.insert(150, 'out_samp_math_CLEAN', '')
        all_variables.insert(152, 'out_comp_math_CLEAN', '')
        all_variables.insert(154, 'out_es_type_math_CLEAN', '')
        all_variables.insert(156, 'out_test_type_math_CLEAN', '')

        all_variables.insert(158, 'out_tit_sci_CLEAN', '')
        all_variables.insert(160, 'out_desc_sci_CLEAN', '')
        all_variables.insert(162, 'out_type_sci_CLEAN', '')
        all_variables.insert(164, 'smd_sci_CLEAN', '')
        all_variables.insert(166, 'se_sci_CLEAN', '')
        all_variables.insert(168, 'out_measure_sci_CLEAN', '')
        all_variables.insert(170, 'out_g1_n_sci_CLEAN', '')
        all_variables.insert(172, 'out_g1_mean_sci_CLEAN', '')
        all_variables.insert(174, 'out_g1_sd_sci_CLEAN', '')
        all_variables.insert(176, 'out_g2_n_sci_CLEAN', '')
        all_variables.insert(178, 'out_g2_mean_sci_CLEAN', '')
        all_variables.insert(180, 'out_g2_sd_sci_CLEAN', '')
        all_variables.insert(182, 'ci_lower_sci_CLEAN', '')
        all_variables.insert(184, 'ci_upper_sci_CLEAN', '')
        all_variables.insert(186, 'out_label_sci_CLEAN', '')
        all_variables.insert(188, 'out_samp_sci_CLEAN', '')
        all_variables.insert(190, 'out_comp_sci_CLEAN', '')
        all_variables.insert(192, 'out_es_type_sci_CLEAN', '')
        all_variables.insert(194, 'out_test_type_sci_CLEAN', '')

        all_variables.insert(196, 'out_tit_fsm_CLEAN', '')
        all_variables.insert(198, 'out_desc_fsm_CLEAN', '')
        all_variables.insert(200, 'out_type_fsm_CLEAN', '')
        all_variables.insert(202, 'smd_fsm_CLEAN', '')
        all_variables.insert(204, 'se_fsm_CLEAN', '')
        all_variables.insert(206, 'out_measure_fsm_CLEAN', '')
        all_variables.insert(208, 'out_g1_n_fsm_CLEAN', '')
        all_variables.insert(210, 'out_g1_mean_fsm_CLEAN', '')
        all_variables.insert(212, 'out_g1_sd_fsm_CLEAN', '')
        all_variables.insert(214, 'out_g2_n_fsm_CLEAN', '')
        all_variables.insert(216, 'out_g2_mean_fsm_CLEAN', '')
        all_variables.insert(218, 'out_g2_sd_fsm_CLEAN', '')
        all_variables.insert(220, 'ci_lower_fsm_CLEAN', '')
        all_variables.insert(222, 'ci_upper_fsm_CLEAN', '')
        all_variables.insert(224, 'out_label_fsm_CLEAN', '')
        all_variables.insert(226, 'out_samp_fsm_CLEAN', '')
        all_variables.insert(228, 'out_comp_fsm_CLEAN', '')
        all_variables.insert(230, 'out_es_type_fsm_CLEAN', '')
        all_variables.insert(232, 'out_test_type_fsm_CLEAN', '')

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

      1.  Dataframe 1
      2.  Dataframe 2
      3.  Dataframe 3 - Sample Size
      4.  Dataframe 4 - Effect Size A
      5.  Dataframe 5 - Effect Size B
      6.  All 5 dataframes
      '''
)

# Get user selection for strand specific dataframe (if needed)
data_cleaning_option = int(input("Enter the number corresponding to the dataframe(s) you want: "))

match data_cleaning_option:
    # MAIN TOOLKIT
    case 1: 
        print("-  Data cleaning datraframe selection: Dataframe 1")
        make_dataframe_1(save_file=True, clean_cols=True, verbose=True)
    case 2: 
        print("-  Data cleaning datraframe selection: Dataframe 2")
        make_dataframe_2(save_file=True, clean_cols=True, verbose=True)
    case 3:
        print("-  Data cleaning datraframe selection: Dataframe 3 - Sample Size")
        make_dataframe_3(save_file=True, clean_cols=True, verbose=True)
    case 4:
        print("-  Data cleaning datraframe selection: Dataframe 4 - Effect Size A")
        make_dataframe_4(save_file=True, clean_cols=True, verbose=True)
    case 5:
        print("-  Data cleaning datraframe selection: Dataframe 5 - Effect Size B")
        make_dataframe_5(save_file=True, clean_cols=True, verbose=False)
    case 6:
        print("-  Data cleaning datraframe selection: All 5 dataframes")
        make_dataframe_1(save_file=True, clean_cols=True, verbose=True)
        make_dataframe_2(save_file=True, clean_cols=True, verbose=True)
        make_dataframe_3(save_file=True, clean_cols=True, verbose=True)
        make_dataframe_4(save_file=True, clean_cols=True, verbose=True)
        make_dataframe_5(save_file=True, clean_cols=True, verbose=False)


