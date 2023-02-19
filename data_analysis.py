#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Author__ = "Jonathan Reardon"

# Standard imports
import os
import sys

# Third party imports
import pandas as pd
import numpy as np
from toolz import interleave

# Local imports
from src.funcs import *
from src.attributeIDs import *

# Accept datafile from user
datafile = sys.argv[1]

load_json()

def make_dataframe_6(save_file=True, verbose=True):
    """
    """
    eppiid_df = retrieve_metadata("ItemId", "id")
    author_df = retrieve_metadata("ShortTitle", "pub_author")
    year_df = retrieve_metadata("Year", "pub_year")
    pub_type_data = retrieve_data(publication_type_output, "pub_type_raw")
    toolkitstrand_df = get_outcome_data_lvl2(toolkit_strand_codes, "out_strand_")
    smd_df = get_outcome_data_lvl1("SMD", "smd_")
    sesmd_df = get_outcome_data_lvl1("SESMD", "se_")
    out_title_df = get_outcome_data_lvl1("Title", "out_tit_")
    out_type_df = get_outcome_data_lvl2(outcome_type_codes, "out_type_")
    sample_df = get_outcome_data_lvl2(sample_output, "out_samp_")
    out_comp_df = get_outcome_data_lvl1("ControlText", "out_comp_")
    effectsizetype_df = get_outcome_data_lvl2(es_type_output, "out_es_type_")
    out_measure_df = get_outcome_data_lvl1("InterventionText", "out_measure_")
    testtype_df = get_outcome_data_lvl2(test_type_output, "out_test_type_raw_")
    admin_strand_data = retrieve_data(admin_strand_output, "strand_raw")
    admin_strand_info = retrieve_info(admin_strand_output, "strand_info")
    country_df = retrieve_data(countries, "loc_country_raw")
    intervention_training_prov_data = retrieve_data(int_training_provided_output, "int_training_raw")
    intervention_training_prov_ht = retrieve_ht(int_training_provided_output, "int_training_ht")
    intervention_training_prov_info = retrieve_info(int_training_provided_output, "int_training_info")
    intervention_teaching_app_data = retrieve_data(intervention_teaching_approach, "int_approach_raw")
    intervention_teaching_app_ht = retrieve_ht(intervention_teaching_approach, "int_approach_ht")
    intervention_teaching_app_info = retrieve_info(intervention_teaching_approach, "int_approach_info")
    digit_tech_data = retrieve_data(int_appr_dig_tech, "digit_tech_raw")
    digit_tech_ht = retrieve_ht(int_appr_dig_tech, "digit_tech_ht")
    digit_tech_info = retrieve_info(int_appr_dig_tech, "digit_tech_info")
    par_eng_data = retrieve_data(int_appr_par_or_comm_vol, "parent_partic_raw")
    par_eng_ht= retrieve_ht(int_appr_par_or_comm_vol, "parent_partic_ht")
    par_eng_info = retrieve_info(int_appr_par_or_comm_vol, "parent_partic_info")
    intervention_time_data = retrieve_data(intervention_time_output, "int_when_raw")
    intervention_time_ht = retrieve_ht(intervention_time_output, "int_when_ht")
    intervention_time_info = retrieve_info(intervention_time_output, "int_when_info")
    intervention_delivery_data = retrieve_data(intervention_delivery_output, "int_who_raw")
    intervention_delivery_ht = retrieve_ht(intervention_delivery_output, "int_who_ht")
    intervention_delivery_info = retrieve_info(intervention_delivery_output, "int_who_info")
    intervention_duration_info = retrieve_info(int_dur_output, "int_dur_info")
    intervention_frequency_info = retrieve_info(inte_freq_output, "int_freq_info")
    intervention_sess_length_info = retrieve_info(intervention_session_length_output, "int_leng_info")
    edu_setting_data = retrieve_data(edu_setting_output, "int_setting_raw")
    edu_setting_ht = retrieve_ht(edu_setting_output, "int_setting_ht")
    edu_setting_info = retrieve_info(edu_setting_output, "int_setting_info")
    student_age_data = retrieve_data(student_age_output, "part_age_raw")
    student_age_ht = retrieve_ht(student_age_output, "part_age_ht")
    student_age_info = retrieve_info(student_age_output, "part_age_info")
    number_of_school_total_info = retrieve_info(number_of_schools_total_output, "school_total_info")
    number_of_classes_total_info = retrieve_info(num_of_class_tot_output, "class_total_info")
    study_design_data = retrieve_data(study_design_output, "int_desig_raw")
    study_design_ht = retrieve_ht(study_design_output, "int_design_ht")
    study_design_info = retrieve_info(study_design_output, "int_design_info")
    sample_size_comments_df = retrieve_info(sample_size_output, "sample_analysed_info")
    low_ses_percentage_Comments_df = retrieve_info(percentage_low_fsm_output, "fsm_perc_info")

    record_details_df = pd.concat([
            eppiid_df,
            author_df,
            year_df,
            pub_type_data
    ], axis=1)

    df = pd.concat([
            toolkitstrand_df,
            smd_df,
            sesmd_df,
            out_title_df,
            out_type_df,
            sample_df,
            out_comp_df,
            effectsizetype_df,
            out_measure_df,
            testtype_df
        ], axis=1, sort=False)

    df = df[list(interleave([
            toolkitstrand_df,
            smd_df,
            sesmd_df,
            out_title_df,
            out_type_df,
            sample_df,
            out_comp_df,
            effectsizetype_df,
            out_measure_df,
            testtype_df
        ]))]

    general_df = pd.concat([
            admin_strand_data,
            admin_strand_info,
            country_df,
            intervention_training_prov_data,
            intervention_training_prov_ht,
            intervention_training_prov_info,
            intervention_teaching_app_data,
            intervention_teaching_app_ht,
            intervention_teaching_app_info,
            digit_tech_data,
            digit_tech_ht,
            digit_tech_info,
            par_eng_data,
            par_eng_ht,
            par_eng_info,
            intervention_time_data,
            intervention_time_ht,
            intervention_time_info,
            intervention_delivery_data,
            intervention_delivery_ht,
            intervention_delivery_info,
            intervention_duration_info,
            intervention_frequency_info,
            intervention_sess_length_info,
            edu_setting_data,
            edu_setting_ht,
            edu_setting_info,
            student_age_data,
            student_age_ht,
            student_age_info,
            number_of_school_total_info,
            number_of_classes_total_info,
            study_design_data,
            study_design_ht,
            study_design_info,
            sample_size_comments_df,
            low_ses_percentage_Comments_df
    ], axis=1)

    toolkit_lists = [[] for _ in range(10)]

    (toolkit_prim, 
     toolkit_prim_smd, 
     toolkit_prim_se, 
     toolkit_out_tit, 
     toolkit_prim_sample, 
     toolkit_prim_outcomp, 
     toolkit_es_type, 
     toolkit_out_measure, 
     toolkit_out_testtype, 
     toolkit_out_strand) = toolkit_lists

    outcome_vars = (
        "out_type_",
        "smd_",
        "se_",
        "out_tit_",
        "out_samp_",
        "out_comp_",
        "out_es_type_",
        "out_measure_",
        "out_test_type_raw_",
        "out_strand_",
    )

    getOutcomeData(df, 'Toolkit primary outcome', toolkit_lists, outcome_vars)

    reading_lists = [[] for _ in range(3)]

    (reading_prim, 
     reading_prim_smd, 
     reading_prim_se) = reading_lists

    getOutcomeData(df, 'Reading primary outcome', reading_lists, outcome_vars)

    writing_lists = [[] for _ in range(3)]

    (Writing_and_spelling_prim,
     Writing_and_spelling_prim_smd,
     Writing_and_spelling_prim_se) = writing_lists

    getOutcomeData(df, 'Writing and spelling primary outcome', writing_lists, outcome_vars)

    mathematics_lists = [[] for _ in range(3)]

    (Mathematics_prim,
     Mathematics_prim_smd,
     Mathematics_prim_se) = mathematics_lists

    getOutcomeData(df, 'Mathematics primary outcome', mathematics_lists, outcome_vars)

    science_lists = [[] for _ in range(3)]

    (Science_prim, Science_prim_smd, Science_prim_se) = science_lists

    getOutcomeData(df, 'Science primary outcome', science_lists, outcome_vars)

    fsm_lists = [[] for _ in range(3)]

    (fsm_prim, fsm_prim_smd, fsm_prim_se) = fsm_lists

    getOutcomeData(df, 'FSM primary outcome', fsm_lists, outcome_vars)

    df_zip = list(zip(
        toolkit_out_strand,
        toolkit_prim_smd,
        toolkit_prim_se,
        toolkit_out_tit,
        toolkit_prim,
        toolkit_prim_sample,
        toolkit_prim_outcomp,
        toolkit_es_type,
        toolkit_out_measure,
        toolkit_out_testtype,
        reading_prim,
        reading_prim_smd,
        reading_prim_se,
        Writing_and_spelling_prim,
        Writing_and_spelling_prim_smd,
        Writing_and_spelling_prim_se,
        Mathematics_prim,
        Mathematics_prim_smd,
        Mathematics_prim_se,
        Science_prim,
        Science_prim_smd,
        Science_prim_se,
        fsm_prim,
        fsm_prim_smd,
        fsm_prim_se
    ))

    df = pd.DataFrame(df_zip)

    df = df.rename(columns={
        0: "out_strand",
        1: "smd_tool",
        2: "se_tool",
        3: "out_tit",
        4: "out_out_type_tool",
        5: "out_samp",
        6: "out_comp",
        7: "out_es_type",
        8: "out_measure",
        9: "out_test_type_raw",
        10: "out_out_type_red",
        11: "smd_red",
        12: "se_red",
        13: "out_out_type_wri",
        14: "smd_wri",
        15: "se_wri",
        16: "out_out_type_math",
        17: "smd_math",
        18: "se_math",
        19: "out_out_type_sci",
        20: "smd_sci",
        21: "se_sci",
        22: "out_out_type_fsm",
        23: "smd_fsm",
        24: "se_fsm"
    })

    df_all = pd.concat([record_details_df, df, general_df], axis=1, sort=False)

    # add fsm_50 TRUE/FALSE column
    df_all["fsm_perc_info"] = (df_all["fsm_perc_info"].str.strip('%'))
    df_all["fsm_perc_info"] = pd.to_numeric(df_all["fsm_perc_info"], errors='coerce')

    # percentage taught by research staff only
    conditions = [
        df_all["fsm_perc_info"] > 49,
        df_all["fsm_perc_info"] < 50,
    ]
    values = ['TRUE', 'FALSE']

    df_all['fsm_50'] = np.select(conditions, values)

    df_all["fsm_perc_info"] = df_all["fsm_perc_info"].replace(
        to_replace=np.nan, value="NA", regex=True
    )

    df_all['fsm_50'] = df_all['fsm_50'].replace("0", "NA", regex=True)

    df_all = df_all[[
        'id',
        'pub_author',
        'pub_year',
        'pub_type_raw',
        'strand_raw',
        'out_out_type_tool',
        'smd_tool',
        'se_tool',
        'out_es_type',
        'out_tit',
        'out_comp',
        'out_samp',
        'out_measure',
        'out_test_type_raw',
        'out_out_type_red',
        'smd_red',
        'se_red',
        'out_out_type_wri',
        'smd_wri',
        'se_wri',
        'out_out_type_math',
        'smd_math',
        'se_math',
        'out_out_type_sci',
        'smd_sci',
        'se_sci',
        'out_out_type_fsm',
        'smd_fsm',
        'se_fsm',
        'sample_analysed_info',
        'school_total_info',
        'class_total_info',
        'int_setting_raw',
        'part_age_raw',
        'fsm_50',
        'fsm_perc_info',
        'loc_country_raw',
        'int_desig_raw',
        'int_approach_raw',
        'int_training_raw',
        'digit_tech_raw',
        'parent_partic_raw',
        'int_when_raw',
        'int_who_raw',
        'int_dur_info',
        'int_freq_info',
        'int_leng_info',
        'out_strand'
    ]]

    df_all_SS = pd.concat([df_all, ss_df], axis=1, sort=False)

    replacements = [('\r', ' '), ('\n', ' '), (':', ' '), (';', ' ')]
    for old, new in replacements:
        df_all_SS.replace(old, new, regex=True, inplace=True)

    if verbose:
        verbose_display(df_all_SS)

    if save_file:
        save_dataframe(df_all_SS, "_Main_Analysis_SS.csv")

# Command line strand specific options display
print('''
      ============================================
      *    Strand Specific Dataframe Selection   * 
      ============================================

      ------------------
      *  Main Toolkit  *
      ------------------

      1.  Arts Participation
      2.  Behaviour Interventions
      3.  Collaborative Learning
      4.  Extending School Time
      5.  Feedback
      6.  Homework
      7.  Individualised Instruction
      8.  Mentoring
      9.  Mastery Learning
      10. Metacognition & Self Regulation
      11. One to One Tution
      12. Oral Language
      13. Physical Activity
      14. Parentel Engagement
      15. Phonics
      16. Performance Pay
      17. Peer Tutoring
      18. Reading Comprehension
      19. Reducing Class Size
      20. Repeating a Year
      21. Social & Emotional Learning
      22. Setting/Streaming
      23. Small Group Tuition
      24. Summer Schools
      25. Teaching Assistants
      26. Within-Class Grouping

      ------------------
      *   Early Years  *
      ------------------

      27. Early Years - Early Literacy Approaches
      28. Early Years - Early Numeracy Approaches
      29. Early Years - Earlier Starting Age
      30. Early Years - Extra Hours
      31. Early Years - Play Based Learning
      '''
)

# Get user selection for strand specific dataframe (if needed)
strand_specific_option = int(input("Enter a number from the list corresponding to the a strand specific data option from the list above: "))

match strand_specific_option:
    # MAIN TOOLKIT
    case 1: 
        print("- Strand specific datraframe selection: Arts Participation")
        ss_df = arts_participation_ss()
    case 2: 
        print("- Strand specific datraframe selection: Behaviour Interventions")
        ss_df = behaviour_int_ss()
    case 3:
        print("- Strand specific datraframe selection: Collaborative Learning")
        ss_df = collab_learning_ss()
    case 4: 
        print("- Strand specific datraframe selection: Extending School Time")
        ss_df = ext_school_time_ss()
    case 5: 
        print("- Strand specific datraframe selection: Feedback")
        ss_df = feedback_ss()
    case 6:
        print("- Strand specific datraframe selection: Homework")
        ss_df = homework_ss()
    case 7: 
        print("- Strand specific datraframe selection: Individualised Instruction")
        ss_df = indiv_instr_ss()
    case 8: 
        print("- Strand specific datraframe selection: Mentoring")
        ss_df = mentoring_ss()
    case 9:
        print("- Strand specific datraframe selection: Mastery Learning")
        ss_df = mastery_learning_ss()
    case 10: 
        print("- Strand specific datraframe selection: Metacognition & Self Regulation")
        ss_df = metacog_self_reg_ss()
    case 11:
        print("- Strand specific datraframe selection: One to One Tuition")
        ss_df = one_t_one_comp_ss()
    case 12: 
        print("- Strand specific datraframe selection: Oral Language")
        ss_df = oral_lang_ss()
    case 13:
        print("- Strand specific datraframe selection: Physical Activity")
        ss_df = phys_activity_ss()
    case 14: 
        print("- Strand specific datraframe selection: Parentel Engagement")
        ss_df = parental_engagement()
    case 15: 
        print("- Strand specific datraframe selection: Phonics")
        ss_df = phonics()
    case 16:
        print("- Strand specific datraframe selection: Performance Pay")
        ss_df = performance_pay()
    case 17: 
        print("- Strand specific datraframe selection: Peer Tutoring")
        ss_df = peer_tut()
    case 18: 
        print("- Strand specific datraframe selection: Reading Comprehension")
        ss_df = read_comprehension_ss()
    case 19:
        print("- Strand specific datraframe selection: Reducing Class Size")
        ss_df = red_class_size_ss()
    case 20: 
        print("- Strand specific datraframe selection: Repeating a Year")
        ss_df = repeat_year_ss()
    case 21: 
        print("- Strand specific datraframe selection: Social & Emotional Learning")
        ss_df = soc_emo_learning_ss()
    case 22: 
        print("- Strand specific datraframe selection: Setting/Streaming")
        ss_df = setting_streaming_ss()
    case 23: 
        print("- Strand specific datraframe selection: Small Group Tuition")
        ss_df = small_group_tuit_ss()
    case 24: 
        print("- Strand specific datraframe selection: Summer Schools")
        ss_df = summer_school_ss()
    case 25: 
        print("- Strand specific datraframe selection: Teaching Assistants")
        ss_df = teach_assistants_ss()
    case 26: 
        print("- Strand specific datraframe selection: Within-Class Grouping")
        ss_df = within_class_grouping()
    # EARLY YEARS
    case 27: 
        print("- Strand specific datraframe selection: Early Years - Early Literacy Approaches")
        ss_df = ey_early_lit_approaches_ss()
    case 28: 
        print("- Strand specific datraframe selection: Early Numeracy Approaches")
        ss_df = ey_early_num_approaches_ss()
    case 29: 
        print("- Strand specific datraframe selection: Earlier Starting Age")
        ss_df = ey_earlier_start_age_ss()
    case 30: 
        print("- Strand specific datraframe selection: Extra Hours")
        ss_df = ey_extra_hours_ss()
    case 31: 
        print("- Strand specific datraframe selection: Play Based Learning")
        ss_df = ey_play_based_learning_ss()

make_dataframe_6(save_file=True, verbose=False)































""" ################
## for percipio
################

percipio = df_all[[
    'id',
    'int_setting_raw',
    'loc_country_raw',
    'digit_tech_raw',
    'out_out_type_tool',
    'out_measure'
]]

# remove problematic text from outputs
percipio.replace('\r', ' ', regex=True, inplace=True)
percipio.replace('\n', ' ', regex=True, inplace=True)
percipio.replace(':', ' ',  regex=True, inplace=True)
percipio.replace(';', ' ',  regex=True, inplace=True)

# replace NaN with NA
percipio = percipio.replace('NaN', 'NA', regex=True)

# get file name for output
outfile_name = "dummy_filters_website.csv"

# write to disk
print("saving {}".format(outfile_name))
percipio.to_csv(outfile_name, index=False, header=True) """
