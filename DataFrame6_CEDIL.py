#!/usr/bin/env python3

# Record details
from files import data_files

# for CEDIL Cash Transfer strand specific data
#from CEDIL_CT_SS.CEDIL_CT_SS import CT_CEDIL_ss_df

# for CEDIL Menstual Hygiene strand specific data
from CEDIL_CT_SS.CEDIL_MH_SS import CT_CEDIL_MH_SS_df

from ind_var_Gen.eppi_ID import eppiid_df
from ind_var_Gen.Author import author_df
from ind_var_Gen.Date import year_df
from ind_var_CEDIL.PublicationType_CEDIL import publication_type_df
from ind_var_Gen.AdminStrand import adminstrand_df

# [CEDIL] Outcome dataframes
from ind_var_Gen.OutcomeType import outcometype_df
from ind_var_Gen.smd import smd_df
from ind_var_Gen.sesmd import sesmd_df
from ind_var_Gen.OutcomeTitle import outcome_title_df
from ind_var_Gen.OutcomeType import outcometype_df
from ind_var_Gen.Outcome import outcome_df
from ind_var_CEDIL.out_samp_CEDIL import sample_df
from ind_var_Gen.OutcomeComparison import out_comp_df
from ind_var_CEDIL.out_es_type_CEDIL import effectsizetype_df
from ind_var_Gen.OutcomeMeasure import outcome_measure_df
from ind_var_CEDIL.out_test_type_CEDIL import testtype_outcome_df
from ind_var_Gen.ToolkitStrand import toolkitstrand_df

# [CEDIL] general dataframes
from ind_var_CEDIL.Country_CEDIL import country_df
from ind_var_CEDIL.InterventionTrainingProvided_CEDIL import InterventionTrainingProvided_df
from ind_var_CEDIL.InterventionTeachingApproach_CEDIL import InterventionTeachingApproach_df
from ind_var_CEDIL.InterventionInclusion_CEDIL import DigitalTechnology_df
from ind_var_CEDIL.InterventionInclusion_CEDIL import Parents_or_Community_Volunteers_df
from ind_var_CEDIL.InterventionTime_CEDIL import InterventionTime_df
from ind_var_CEDIL.InterventionDelivery_CEDIL import interventiondelivery_df
from ind_var_CEDIL.InterventionDuration_CEDIL import InterventionDuration_Comments_df
from ind_var_CEDIL.InterventionFrequency_CEDIL import InterventionFrequency_Comments_df
from ind_var_CEDIL.InterventionSessionLength_CEDIL import InterventionSessionLength_Comments_df
from ind_var_CEDIL.EducationalSetting_CEDIL import edusetting_df
from ind_var_CEDIL.Age_CEDIL import student_age_df
from ind_var_CEDIL.NumberofSchools_CEDIL import number_of_schools_total_Comments_df
from ind_var_CEDIL.NumberofClasses_CEDIL import number_of_classes_total_Comments_df
from ind_var_CEDIL.StudyDesign_CEDIL import studydesign_df
from ind_var_CEDIL.SampleSize_CEDIL import sample_size_Comments_df
from ind_var_CEDIL.ses_fsm_CEDIL import low_ses_percentage_Comments_df

# standard imports
import os
import pandas as pd
import numpy as np
from toolz import interleave

#################################
# REFACTOR STRAND FILTERING CODE
#################################

def make_dataframe(save_file=True, verbose=True):

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
        testtype_outcome_df
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
        testtype_outcome_df
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

    toolkit_prim = []
    toolkit_prim_smd = []
    toolkit_prim_se = []
    toolkit_out_tit = []
    toolkit_prim_sample = []
    toolkit_prim_outcomp = []
    toolkit_es_type = []
    toolkit_out_measure = []
    toolkit_out_testtype = []
    toolkit_out_strand = []

    for counter, row in enumerate(df['out_type_1']):
        if 'Toolkit primary outcome' in row:
            toolkit_prim.append(row)
            toolkit_out_strand.append(df['out_strand_1'][counter])
            toolkit_prim_smd.append(df['smd_1'][counter])
            toolkit_prim_se.append(df['se_1'][counter])
            toolkit_out_tit.append(df['out_tit_1'][counter])
            toolkit_prim_sample.append(df['out_samp_1'][counter])
            toolkit_prim_outcomp.append(df['out_comp_1'][counter])
            toolkit_es_type.append(df['out_es_type_1'][counter])
            toolkit_out_measure.append(df['out_measure_1'][counter])
            toolkit_out_testtype.append(df['out_test_type_raw_1'][counter])
        elif 'Toolkit primary outcome' in df['out_type_2'][counter]:
            toolkit_prim.append(df['out_type_2'][counter])
            toolkit_out_strand.append(df['out_strand_2'][counter])
            toolkit_prim_smd.append(df['smd_2'][counter])
            toolkit_prim_se.append(df['se_2'][counter])
            toolkit_out_tit.append(df['out_tit_2'][counter])
            toolkit_prim_sample.append(df['out_samp_2'][counter])
            toolkit_prim_outcomp.append(df['out_comp_2'][counter])
            toolkit_es_type.append(df['out_es_type_2'][counter])
            toolkit_out_measure.append(df['out_measure_2'][counter])
            toolkit_out_testtype.append(df['out_test_type_raw_2'][counter])
        elif 'Toolkit primary outcome' in df['out_type_3'][counter]:
            toolkit_prim.append(df['out_type_3'][counter])
            toolkit_out_strand.append(df['out_strand_3'][counter])
            toolkit_prim_smd.append(df['smd_3'][counter])
            toolkit_prim_se.append(df['se_3'][counter])
            toolkit_out_tit.append(df['out_tit_3'][counter])
            toolkit_prim_sample.append(df['out_samp_3'][counter])
            toolkit_prim_outcomp.append(df['out_comp_3'][counter])
            toolkit_es_type.append(df['out_es_type_3'][counter])
            toolkit_out_measure.append(df['out_measure_3'][counter])
            toolkit_out_testtype.append(df['out_test_type_raw_3'][counter])



        else:
            toolkit_prim.append("NA")
            toolkit_out_strand.append("NA")
            toolkit_prim_smd.append("NA")
            toolkit_prim_se.append("NA")
            toolkit_out_tit.append("NA")
            toolkit_prim_sample.append("NA")
            toolkit_prim_outcomp.append("NA")
            toolkit_es_type.append("NA")
            toolkit_out_measure.append("NA")
            toolkit_out_testtype.append("NA")


    reading_prim = []
    reading_prim_smd = []
    reading_prim_se = []

    for counter, row in enumerate(df['out_type_1']):
        if 'Reading primary outcome' in row:
            reading_prim.append(row)
            reading_prim_smd.append(df['smd_1'][counter])
            reading_prim_se.append(df['se_1'][counter])
        elif 'Reading primary outcome' in df['out_type_2'][counter]:
            reading_prim.append(df['out_type_2'][counter])
            reading_prim_smd.append(df['smd_2'][counter])
            reading_prim_se.append(df['se_2'][counter])
        elif 'Reading primary outcome' in df['out_type_3'][counter]:
            reading_prim.append(df['out_type_3'][counter])
            reading_prim_smd.append(df['smd_3'][counter])
            reading_prim_se.append(df['se_3'][counter])


        else:
            reading_prim.append("NA")
            reading_prim_smd.append("NA")
            reading_prim_se.append("NA")

    Writing_and_spelling_prim = []
    Writing_and_spelling_prim_smd = []
    Writing_and_spelling_prim_se = []

    for counter, row in enumerate(df['out_type_1']):
        if 'Writing and spelling primary outcome' in row:
            Writing_and_spelling_prim.append(df['out_type_1'][counter])
            Writing_and_spelling_prim_smd.append(df['smd_1'][counter])
            Writing_and_spelling_prim_se.append(df['se_1'][counter])
        elif 'Writing and spelling primary outcome' in df['out_type_2'][counter]:
            Writing_and_spelling_prim.append(df['out_type_2'][counter])
            Writing_and_spelling_prim_smd.append(df['smd_2'][counter])
            Writing_and_spelling_prim_se.append(df['se_2'][counter])
        elif 'Writing and spelling primary outcome' in df['out_type_3'][counter]:
            Writing_and_spelling_prim.append(df['out_type_3'][counter])
            Writing_and_spelling_prim_smd.append(df['smd_3'][counter])
            Writing_and_spelling_prim_se.append(df['se_3'][counter])

        else:
            Writing_and_spelling_prim.append("NA")
            Writing_and_spelling_prim_smd.append("NA")
            Writing_and_spelling_prim_se.append("NA")

    Mathematics_prim = []
    Mathematics_prim_smd = []
    Mathematics_prim_se = []

    for counter, row in enumerate(df['out_type_1']):
        if 'Mathematics primary outcome' in row:
            Mathematics_prim.append(row)
            Mathematics_prim_smd.append(df['smd_1'][counter])
            Mathematics_prim_se.append(df['se_1'][counter])
        elif 'Mathematics primary outcome' in df['out_type_2'][counter]:
            Mathematics_prim.append(df['out_type_2'][counter])
            Mathematics_prim_smd.append(df['smd_2'][counter])
            Mathematics_prim_se.append(df['se_2'][counter])
        elif 'Mathematics primary outcome' in df['out_type_3'][counter]:
            Mathematics_prim.append(df['out_type_3'][counter])
            Mathematics_prim_smd.append(df['smd_3'][counter])
            Mathematics_prim_se.append(df['se_3'][counter])




        else:
            Mathematics_prim.append("NA")
            Mathematics_prim_smd.append("NA")
            Mathematics_prim_se.append("NA")

    Science_prim = []
    Science_prim_smd = []
    Science_prim_se = []

    for counter, row in enumerate(df['out_type_1']):
        if 'Science primary outcome' in row:
            Science_prim.append(row)
            Science_prim_smd.append(df['smd_1'][counter])
            Science_prim_se.append(df['se_1'][counter])
        elif 'Science primary outcome' in df['out_type_2'][counter]:
            Science_prim.append(df['out_type_2'][counter])
            Science_prim_smd.append(df['smd_2'][counter])
            Science_prim_se.append(df['se_2'][counter])
        elif 'Science primary outcome' in df['out_type_3'][counter]:
            Science_prim.append(df['out_type_3'][counter])
            Science_prim_smd.append(df['smd_3'][counter])
            Science_prim_se.append(df['se_3'][counter])


        else:
            Science_prim.append("NA")
            Science_prim_smd.append("NA")
            Science_prim_se.append("NA")

    fsm_prim = []
    fsm_prim_smd = []
    fsm_prim_se = []

    for counter, row in enumerate(df['out_type_1']):
        if 'SES/FSM outcome' in row:
            fsm_prim.append(row)
            fsm_prim_smd.append(df['smd_1'][counter])
            fsm_prim_se.append(df['se_1'][counter])
        elif 'SES/FSM outcome' in df['out_type_2'][counter]:
            fsm_prim.append(df['out_type_2'][counter])
            fsm_prim_smd.append(df['smd_2'][counter])
            fsm_prim_se.append(df['se_2'][counter])
        elif 'SES/FSM outcome' in df['out_type_3'][counter]:
            fsm_prim.append(df['out_type_3'][counter])
            fsm_prim_smd.append(df['smd_3'][counter])
            fsm_prim_se.append(df['se_3'][counter])


        else:
            fsm_prim.append("NA")
            fsm_prim_smd.append("NA")
            fsm_prim_se.append("NA")

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

    #df_all = pd.concat([record_details_df, df, general_df], axis=1, sort=False)

    # remove problematic text from outputs
    df_all.replace('\r', ' ', regex=True, inplace=True)
    df_all.replace('\n', ' ', regex=True, inplace=True)
    df_all.replace(':', ' ',  regex=True, inplace=True)
    df_all.replace(';', ' ',  regex=True, inplace=True)

    # replace NaN with NA
    df_all = df_all.replace('NaN', 'NA', regex=True)

    df_all = pd.concat([df_all, CT_CEDIL_MH_SS_df], axis=1, sort=False)

    if verbose:
        # print dataframe
        print(df_all)
        # list column names and position
        for counter, i in enumerate(df_all):
            print(counter, i)

        # print dataframe info
        print("Columns:", df_all.shape[1])
        print("Rows:", df_all.shape[0])
        print("Datapoints:", df_all.shape[0] * df_all.shape[1])

    if save_file:
        # get current wd
        cw = os.getcwd()

        # get file name for output
        outfile_name_pre = data_files.rsplit('/')[-1]
        outfile_name_mid = outfile_name_pre.rsplit('.')[0]
        outfile_name = outfile_name_mid + "_CEDIL_Main_Analysis_SS.csv"
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
        df_all.to_csv(outfile, index=False)


make_dataframe(save_file=True, verbose=True)










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
