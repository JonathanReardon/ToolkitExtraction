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
from Main import load_json
from Main import getOutcomeData
from Main import verbose_display
from Main import save_dataframe

# local imports
from ind_var_functions import ind_var_gen
from ind_var_functions import ind_var_ss

load_json()

# Accept datafile name from user as argument 1
datafile = sys.argv[1]

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
strand_specific_option = int(input("Eenter a number from the list corresponding to the a strand specific data option from the list above: "))

match strand_specific_option:
    # MAIN TOOLKIT
    case 1: 
        print("- Strand specific datraframe selection: Arts Participation")
        ap_ss_df = ind_var_ss.arts_participation_ss()
        ss_df = ap_ss_df
    case 2: 
        print("- Strand specific datraframe selection: Behaviour Interventions")
        bi_ss_df = ind_var_ss.behaviour_int_ss()
        ss_df = bi_ss_df
    case 3:
        print("- Strand specific datraframe selection: Collaborative Learning")
        cl_ss_df = ind_var_ss.collab_learning_ss()
        ss_df = cl_ss_df
    case 4: 
        print("- Strand specific datraframe selection: Extending School Time")
        est_ss_df = ind_var_ss.ext_school_time_ss()
        ss_df = est_ss_df
    case 5: 
        print("- Strand specific datraframe selection: Feedback")
        feedback_ss_df = ind_var_ss.feedback_ss()
        ss_df = feedback_ss_df
    case 6:
        print("- Strand specific datraframe selection: Homework")
        hw_ss_df = ind_var_ss.homework_ss()
        ss_df = hw_ss_df
    case 7: 
        print("- Strand specific datraframe selection: Individualised Instruction")
        ii_ss_df = ind_var_ss.indiv_instr_ss()
        ss_df = ii_ss_df
    case 8: 
        print("- Strand specific datraframe selection: Mentoring")
        mentoring_ss_df = ind_var_ss.mentoring_ss()
        ss_df = mentoring_ss_df
    case 9:
        print("- Strand specific datraframe selection: Mastery Learning")
        ml_ss_df = ind_var_ss.mastery_learning_ss()
        ss_df = ml_ss_df
    case 10: 
        print("- Strand specific datraframe selection: Metacognition & Self Regulation")
        msr_ss_df = ind_var_ss.metacog_self_reg_ss()
        ss_df = msr_ss_df
    case 11:
        print("- Strand specific datraframe selection: One to One Tuition")
        one_to_one_ss_df = ind_var_ss.one_t_one_comp_ss()
        ss_df = one_to_one_ss_df
    case 12: 
        print("- Strand specific datraframe selection: Oral Language")
        ol_ss_df = ind_var_ss.oral_lang_ss()
        ss_df = ol_ss_df
    case 13:
        print("- Strand specific datraframe selection: Physical Activity")
        pha_ss_df = ind_var_ss.phys_activity_ss()
        ss_df = pha_ss_df
    case 14: 
        print("- Strand specific datraframe selection: Parentel Engagement")
        pe_ss_df = ind_var_ss.parental_engagement()
        ss_df = pe_ss_df
    case 15: 
        print("- Strand specific datraframe selection: Phonics")
        ph_ss_df = ind_var_ss.phonics()
        ss_df = ph_ss_df
    case 16:
        print("- Strand specific datraframe selection: Performance Pay")
        pp_ss_df = ind_var_ss.performance_pay()
        ss_df = pp_ss_df
    case 17: 
        print("- Strand specific datraframe selection: Peer Tutoring")
        peer_tut_ss_df = ind_var_ss.peer_tut()
        ss_df = peer_tut_ss_df
    case 18: 
        print("- Strand specific datraframe selection: Reading Comprehension")
        rc_ss_df = ind_var_ss.read_comprehension_ss()
        ss_df = rc_ss_df
    case 19:
        print("- Strand specific datraframe selection: Reducing Class Size")
        redc_ss_df = ind_var_ss.red_class_size_ss()
        ss_df = redc_ss_df
    case 20: 
        print("- Strand specific datraframe selection: Repeating a Year")
        ry_ss_df = ind_var_ss.repeat_year_ss()
        ss_df = ry_ss_df
    case 21: 
        print("- Strand specific datraframe selection: Social & Emotional Learning")
        sel_ss_df = ind_var_ss.soc_emo_learning_ss()
        ss_df = sel_ss_df
    case 22: 
        print("- Strand specific datraframe selection: Setting/Streaming")
        sets_ss_df = ind_var_ss.setting_streaming_ss()
        ss_df = sets_ss_df
    case 23: 
        print("- Strand specific datraframe selection: Small Group Tuition")
        sgt_ss_df = ind_var_ss.small_group_tuit_ss()
        ss_df = sgt_ss_df
    case 24: 
        print("- Strand specific datraframe selection: Summer Schools")
        SS_ss_df = ind_var_ss.summer_school_ss()
        ss_df = SS_ss_df
    case 25: 
        print("- Strand specific datraframe selection: Teaching Assistants")
        ta_ss_df = ind_var_ss.teach_assistants_ss()
        ss_df = ta_ss_df
    case 26: 
        print("- Strand specific datraframe selection: Within-Class Grouping")
        wc_ss_df = ind_var_ss.within_class_grouping()
        ss_df = wc_ss_df
    # EARLY YEARS
    case 27: 
        print("- Strand specific datraframe selection: Early Years - Early Literacy Approaches")
        ela_ss_df = ind_var_ss.ey_early_lit_approaches_ss()
        ss_df = ela_ss_df
    case 28: 
        print("- Strand specific datraframe selection: Early Numeracy Approaches")
        ena_ss_df = ind_var_ss.ey_early_num_approaches_ss()
        ss_df = ena_ss_df
    case 29: 
        print("- Strand specific datraframe selection: Earlier Starting Age")
        ey_esa_df = ind_var_ss.ey_earlier_start_age_ss()
        ss_df = ey_esa_df
    case 30: 
        print("- Strand specific datraframe selection: Extra Hours")
        ey_eh_df = ind_var_ss.ey_extra_hours_ss()
        ss_df = ey_eh_df
    case 31: 
        print("- Strand specific datraframe selection: Play Based Learning")
        ey_pbl_df = ind_var_ss.ey_play_based_learning_ss()
        ss_df = ey_pbl_df

def make_dataframe(save_file=True, verbose=True):

    eppiid_df = ind_var_gen.eppi()
    author_df = ind_var_gen.author()
    year_df = ind_var_gen.date()
    publication_type_df = ind_var_gen.pub_type()
    toolkitstrand_df = ind_var_gen.toolkit_strand()
    smd_df = ind_var_gen.smd()
    sesmd_df = ind_var_gen.ses_md()
    outcome_title_df = ind_var_gen.out_tit()
    outcometype_df = ind_var_gen.out_type()
    sample_df = ind_var_gen.sample()
    out_comp_df = ind_var_gen.out_comp()
    effectsizetype_df = ind_var_gen.es_type()
    outcome_measure_df = ind_var_gen.out_measure()
    testtype_df = ind_var_gen.test_type()
    adminstrand_df = ind_var_gen.get_admin_strand_data()
    country_df = ind_var_gen.country()
    InterventionTrainingProvided_df = ind_var_gen.int_train_prov()
    InterventionTeachingApproach_df = ind_var_gen.int_teach_appr()
    DigitalTechnology_df = ind_var_gen.int_inclusion_digit_tech()
    Parents_or_Community_Volunteers_df = ind_var_gen.int_inclusion_par_vol()
    InterventionTime_df = ind_var_gen.int_time()
    interventiondelivery_df = ind_var_gen.int_delivery()
    InterventionDuration_Comments_df = ind_var_gen.int_duration_comm()
    InterventionFrequency_Comments_df = ind_var_gen.int_frequency_comms()
    InterventionSessionLength_Comments_df = ind_var_gen.int_sess_len_comm()
    edusetting_df = ind_var_gen.edu_setting()
    student_age_df = ind_var_gen.get_student_age_data()
    number_of_schools_total_Comments_df = ind_var_gen.number_of_schools_total_comm()
    number_of_classes_total_Comments_df = ind_var_gen.number_of_classes_total_comm()
    studydesign_df = ind_var_gen.study_design()
    sample_size_Comments_df = ind_var_gen.samp_size_comm()
    low_ses_percentage_Comments_df = ind_var_gen.low_ses_pc_comm()

    record_details_df = pd.concat([
            eppiid_df,
            author_df,
            year_df,
            publication_type_df
    ], axis=1)

    df = pd.concat([
            toolkitstrand_df,
            smd_df,
            sesmd_df,
            outcome_title_df,
            outcometype_df,
            sample_df,
            out_comp_df,
            effectsizetype_df,
            outcome_measure_df,
            testtype_df
        ], axis=1, sort=False)

    df = df[list(interleave([
            toolkitstrand_df,
            smd_df,
            sesmd_df,
            outcome_title_df,
            outcometype_df,
            sample_df,
            out_comp_df,
            effectsizetype_df,
            outcome_measure_df,
            testtype_df
        ]))]

    general_df = pd.concat([
            adminstrand_df,
            country_df,
            InterventionTrainingProvided_df,
            InterventionTeachingApproach_df,
            DigitalTechnology_df,
            Parents_or_Community_Volunteers_df,
            InterventionTime_df,
            interventiondelivery_df,
            InterventionDuration_Comments_df,
            InterventionFrequency_Comments_df,
            InterventionSessionLength_Comments_df,
            edusetting_df,
            student_age_df,
            number_of_schools_total_Comments_df,
            number_of_classes_total_Comments_df,
            studydesign_df,
            sample_size_Comments_df,
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

    """ col = (
        ('id', 'Unique identifier for the publication'),
        ('pub_author', 'Author(s) of the publication'),
        ('pub_year', 'Year of publication'),
        ('pub_type_raw', 'Raw publication type'),
        ('strand_raw', 'Raw strand'),
        ('out_out_type_tool', 'Outcome type for tool'),
        ('smd_tool', 'Standard mean difference for tool'),
        ('se_tool', 'Standard error for tool'),
        ('out_es_type', 'Type of effect size for tool'),
        ('out_tit', 'Outcome for technology in the classroom'),
        ('out_comp', 'Outcome for computer use'),
        ('out_samp', 'Outcome for sample'),
        ('out_measure', 'Outcome measurement'),
        ('out_test_type_raw', 'Raw test type for outcome'),
        ('out_out_type_red', 'Outcome type for reading'),
        ('smd_red', 'Standard mean difference for reading'),
        ('se_red', 'Standard error for reading'),
        ('out_out_type_wri', 'Outcome type for writing'),
        ('smd_wri', 'Standard mean difference for writing'),
        ('se_wri', 'Standard error for writing'),
        ('out_out_type_math', 'Outcome type for mathematics'),
        ('smd_math', 'Standard mean difference for mathematics'),
        ('se_math', 'Standard error for mathematics'),
        ('out_out_type_sci', 'Outcome type for science'),
        ('smd_sci', 'Standard mean difference for science'),
        ('se_sci', 'Standard error for science'),
        ('out_out_type_fsm', 'Outcome type for free school meal eligibility'),
        ('smd_fsm', 'Standard mean difference for free school meal eligibility'),
        ('se_fsm', 'Standard error for free school meal eligibility'),
        ('sample_analysed_info', 'Information about the sample analyzed'),
        ('school_total_info', 'Total number of schools'),
        ('class_total_info', 'Total number of classes'),
        ('int_setting_raw', 'Raw setting for the intervention'),
        ('part_age_raw', 'Raw age range of participants'),
        ('fsm_50', 'Indicator of free school meal eligibility'),
        ('fsm_perc_info', 'Percentage of participants eligible for free school meals'),
        ('loc_country_raw', 'Raw location country'),
        ('int_desig_raw', 'Raw design of the intervention'),
        ('int_approach_raw', 'Raw approach of the intervention'),
        ('int_training_raw', 'Raw training for the intervention'),
        ('digit_tech_raw', 'Raw technology used in the intervention'),
        ('parent_partic_raw', 'Raw level of parent participation'),
        ('int_when_raw', 'Raw timing of the intervention'),
        ('int_who_raw', 'Raw person(s) responsible for the intervention'),
        ('int_dur_info', 'Duration of the intervention'),
        ('int_freq_info', 'Frequency of the intervetion'),
        ('int_leng_info', 'Length of the intervetion'),
        ('out_strand', 'Length of the intervetion'),
    ) """

    """ df_all.columns = [col[0] for col in col] """

    df_all_SS = pd.concat([df_all, ss_df], axis=1, sort=False)

    replacements = [('\r', ' '), ('\n', ' '), (':', ' '), (';', ' ')]
    for old, new in replacements:
        df_all_SS.replace(old, new, regex=True, inplace=True)

    if verbose:
        verbose_display(df_all_SS)

    if save_file:
        save_dataframe(df_all_SS, "_Main_Analysis_SS.csv")

make_dataframe(save_file=True, verbose=False)































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
