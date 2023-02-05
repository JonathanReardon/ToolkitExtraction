#!/usr/bin/env python3

# Standard libraries
import os
import sys

# Third party libraries
import pandas as pd
import numpy as np
from toolz import interleave

# Local libraries - Basic dataframes
from ind_var_Gen import eppiid_df
from ind_var_Gen import author_df
from ind_var_Gen import year_df
from ind_var_Gen import publicationtype_df
from ind_var_Gen import adminstrand_df

# Local libraries - Outcome dataframes
from ind_var_Gen import toolkitstrand_df
from ind_var_Gen import outcometype_df
from ind_var_Gen import smd_df
from ind_var_Gen import sesmd_df
from ind_var_Gen import outcome_title_df
from ind_var_Gen import outcometype_df
from ind_var_Gen import outcome_df
from ind_var_Gen import sample_df
from ind_var_Gen import out_comp_df
from ind_var_Gen import effectsizetype_df
from ind_var_Gen import outcome_measure_df
from ind_var_Gen import testtype_df
from ind_var_Gen import toolkitstrand_df

# Local libraries - Intervention dataframes
from ind_var_Gen import country_df
from ind_var_Gen import InterventionTrainingProvided_df
from ind_var_Gen import InterventionTeachingApproach_df
from ind_var_Gen import DigitalTechnology_df
from ind_var_Gen import Parents_or_Community_Volunteers_df
from ind_var_Gen import InterventionTime_df
from ind_var_Gen import interventiondelivery_df
from ind_var_Gen import InterventionDuration_Comments_df
from ind_var_Gen import InterventionFrequency_Comments_df
from ind_var_Gen import InterventionSessionLength_Comments_df
from ind_var_Gen import edusetting_df

# Local libraries - Sample dataframes
from ind_var_Gen import student_age_df
from ind_var_Gen import number_of_schools_total_Comments_df
from ind_var_Gen import number_of_classes_total_Comments_df
from ind_var_Gen import studydesign_df
from ind_var_Gen import sample_size_Comments_df
from ind_var_Gen import low_ses_percentage_Comments_df

# strand specific addition
from ind_var_SS.AP_strand_specific import ap_ss_df

# for getting number of outcomes
from Toolkit_Outcome_Check import outcome_num

def getOutcomeData(dataframe, out_label, out_container, var_names):
    for counter, row in enumerate(dataframe['out_type_1']):
            found = False
            for outcome_n in range(1, outcome_num + 1):
                if out_label in dataframe[f'out_type_{outcome_n}'][counter]:
                    found = True
                    for counter2, holder in enumerate(out_container):
                        holder.append(dataframe[var_names[counter2] + f"{outcome_n}"][counter])
                    break
            if not found:
                for holder in out_container:
                    holder.append("NA")

datafile = sys.argv[1]

#################################
# REFACTOR STRAND FILTERING CODE
#################################

def make_dataframe(save_file=True, verbose=True):

    record_details_df = pd.concat([
        eppiid_df,
        author_df,
        year_df,
        publicationtype_df
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
    ], axis=1)[list(interleave([
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

    outcome_vars = [
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
    ]

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

    df.rename(columns={
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
    }, inplace=True)

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
        np.nan, "NA", regex=True)

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

    df_all_ap_SS = pd.concat([df_all, ap_ss_df], axis=1, sort=False)

    replacements = [('\r', ' '), ('\n', ' '), (':', ' '), (';', ' ')]
    for old, new in replacements:
        df_all_ap_SS.replace(old, new, regex=True, inplace=True)

    # replace NaN with NA
    #df_all_ap_SS = df_all_ap_SS.replace('NaN', 'NA', regex=True)

    if verbose:
        # print dataframe
        print(df_all_ap_SS)
        print("\n")
        # list column names and position
        for counter, i in enumerate(df_all_ap_SS):
            print(counter, i)
        print("\n")
        # print dataframe info
        print("Columns:", df_all_ap_SS.shape[1])
        print("Rows:", df_all_ap_SS.shape[0])
        print("Datapoints:", df_all_ap_SS.shape[0] * df_all_ap_SS.shape[1])
        print("\n")

    if save_file:
        # get current wd
        cw = os.getcwd() + "/Extractions"
        # get file name for output
        outfile_name_pre = datafile.rsplit('/')[-1]
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]
        outfile_name = outfile_name_mid + "_Main_Analysis_SS.csv"
        outfile = os.path.join(cw + "/" + outfile_name_mid, outfile_name)
        # create dir
        try:
            os.mkdir("Extractions/" + outfile_name_mid)
        except OSError:
            print("Create {} dir fail, check if it already exists or permissions".format("Extractions/" + outfile_name_mid))
        else:
            print("Successfully created {} directory".format("Extractions/" + outfile_name_mid))
        # write to disk
        print("Input file: {}".format(datafile))
        print("Saving extracted output to: {}".format(outfile))
        df_all_ap_SS.to_csv(outfile, index=False, header=True)

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
