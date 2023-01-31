#!/usr/bin/env python3

# Record details
from files import data_files

from ind_var_Gen.eppi_ID import eppiid_df
from ind_var_Gen.Author import author_df
from ind_var_Gen.Date import year_df
from ind_var_Gen.PublicationType import publicationtype_df
from ind_var_Gen.AdminStrand import adminstrand_df

# Outcome dataframes
from ind_var_Gen.ToolkitStrand import toolkitstrand_df
from ind_var_Gen.OutcomeType import outcometype_df
from ind_var_Gen.smd import smd_df
from ind_var_Gen.sesmd import sesmd_df
from ind_var_Gen.OutcomeTitle import outcome_title_df
from ind_var_Gen.OutcomeType import outcometype_df
from ind_var_Gen.Outcome import outcome_df
from ind_var_Gen.Sample import sample_df
from ind_var_Gen.OutcomeComparison import out_comp_df
from ind_var_Gen.EffectSizeType import effectsizetype_df
from ind_var_Gen.OutcomeMeasure import outcome_measure_df
from ind_var_Gen.Outcome_TestType import testtype_df
from ind_var_Gen.ToolkitStrand import toolkitstrand_df

# general dataframes
from ind_var_Gen.Country import country_df
from ind_var_Gen.InterventionTrainingProvided import InterventionTrainingProvided_df
from ind_var_Gen.InterventionTeachingApproach import InterventionTeachingApproach_df
from ind_var_Gen.InterventionInclusion import DigitalTechnology_df
from ind_var_Gen.InterventionInclusion import Parents_or_Community_Volunteers_df
from ind_var_Gen.InterventionTime import InterventionTime_df
from ind_var_Gen.InterventionDelivery import interventiondelivery_df
from ind_var_Gen.InterventionDuration import InterventionDuration_Comments_df
from ind_var_Gen.InterventionFrequency import InterventionFrequency_Comments_df
from ind_var_Gen.InterventionSessionLength import InterventionSessionLength_Comments_df
from ind_var_Gen.EducationalSetting import edusetting_df
from ind_var_Gen.Age import student_age_df
from ind_var_Gen.NumberofSchools import number_of_schools_total_Comments_df
from ind_var_Gen.NumberofClasses import number_of_classes_total_Comments_df
from ind_var_Gen.StudyDesign import studydesign_df
from ind_var_Gen.SampleSize import sample_size_Comments_df
from ind_var_Gen.ses_fsm import low_ses_percentage_Comments_df

import pandas as pd
import numpy as np
from toolz import interleave

# strand specific addition
from ind_var_SS.ML_strand_specific import ml_ss_df

#################################
# REFACTOR STRAND FILTERING CODE
#################################

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
    elif 'Toolkit primary outcome' in df['out_type_4'][counter]:
        toolkit_prim.append(df['out_type_4'][counter])
        toolkit_out_strand.append(df['out_strand_4'][counter])
        toolkit_prim_smd.append(df['smd_4'][counter])
        toolkit_prim_se.append(df['se_4'][counter])
        toolkit_out_tit.append(df['out_tit_4'][counter])
        toolkit_prim_sample.append(df['out_samp_4'][counter])
        toolkit_prim_outcomp.append(df['out_comp_4'][counter])
        toolkit_es_type.append(df['out_es_type_4'][counter])
        toolkit_out_measure.append(df['out_measure_4'][counter])
        toolkit_out_testtype.append(df['out_test_type_raw_4'][counter])
    elif 'Toolkit primary outcome' in df['out_type_5'][counter]:
        toolkit_prim.append(df['out_type_5'][counter])
        toolkit_out_strand.append(df['out_strand_5'][counter])
        toolkit_prim_smd.append(df['smd_5'][counter])
        toolkit_prim_se.append(df['se_5'][counter])
        toolkit_out_tit.append(df['out_tit_5'][counter])
        toolkit_prim_sample.append(df['out_samp_5'][counter])
        toolkit_prim_outcomp.append(df['out_comp_5'][counter])
        toolkit_es_type.append(df['out_es_type_5'][counter])
        toolkit_out_measure.append(df['out_measure_5'][counter])
        toolkit_out_testtype.append(df['out_test_type_raw_5'][counter])
    elif 'Toolkit primary outcome' in df['out_type_6'][counter]:
        toolkit_prim.append(df['out_type_6'][counter])
        toolkit_out_strand.append(df['out_strand_6'][counter])
        toolkit_prim_smd.append(df['smd_6'][counter])
        toolkit_prim_se.append(df['se_6'][counter])
        toolkit_out_tit.append(df['out_tit_6'][counter])
        toolkit_prim_sample.append(df['out_samp_6'][counter])
        toolkit_prim_outcomp.append(df['out_comp_6'][counter])
        toolkit_es_type.append(df['out_es_type_6'][counter])
        toolkit_out_measure.append(df['out_measure_6'][counter])
        toolkit_out_testtype.append(df['out_test_type_raw_6'][counter])
    elif 'Toolkit primary outcome' in df['out_type_7'][counter]:
        toolkit_prim.append(df['out_type_7'][counter])
        toolkit_out_strand.append(df['out_strand_7'][counter])
        toolkit_prim_smd.append(df['smd_7'][counter])
        toolkit_prim_se.append(df['se_7'][counter])
        toolkit_out_tit.append(df['out_tit_7'][counter])
        toolkit_prim_sample.append(df['out_samp_7'][counter])
        toolkit_prim_outcomp.append(df['out_comp_7'][counter])
        toolkit_es_type.append(df['out_es_type_7'][counter])
        toolkit_out_measure.append(df['out_measure_7'][counter])
        toolkit_out_testtype.append(df['out_test_type_raw_7'][counter])
    elif 'Toolkit primary outcome' in df['out_type_8'][counter]:
        toolkit_prim.append(df['out_type_8'][counter])
        toolkit_out_strand.append(df['out_strand_8'][counter])
        toolkit_prim_smd.append(df['smd_8'][counter])
        toolkit_prim_se.append(df['se_8'][counter])
        toolkit_out_tit.append(df['out_tit_8'][counter])
        toolkit_prim_sample.append(df['out_samp_8'][counter])
        toolkit_prim_outcomp.append(df['out_comp_8'][counter])
        toolkit_es_type.append(df['out_es_type_8'][counter])
        toolkit_out_measure.append(df['out_measure_8'][counter])
        toolkit_out_testtype.append(df['out_test_type_raw_8'][counter])



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
    elif 'Reading primary outcome' in df['out_type_4'][counter]:
        reading_prim.append(df['out_type_4'][counter])
        reading_prim_smd.append(df['smd_4'][counter])
        reading_prim_se.append(df['se_4'][counter])
    elif 'Reading primary outcome' in df['out_type_5'][counter]:
        reading_prim.append(df['out_type_5'][counter])
        reading_prim_smd.append(df['smd_5'][counter])
        reading_prim_se.append(df['se_5'][counter])
    elif 'Reading primary outcome' in df['out_type_6'][counter]:
        reading_prim.append(df['out_type_6'][counter])
        reading_prim_smd.append(df['smd_6'][counter])
        reading_prim_se.append(df['se_6'][counter])
    elif 'Reading primary outcome' in df['out_type_7'][counter]:
        reading_prim.append(df['out_type_7'][counter])
        reading_prim_smd.append(df['smd_7'][counter])
        reading_prim_se.append(df['se_7'][counter])
    elif 'Reading primary outcome' in df['out_type_8'][counter]:
        reading_prim.append(df['out_type_8'][counter])
        reading_prim_smd.append(df['smd_8'][counter])
        reading_prim_se.append(df['se_8'][counter])



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
    elif 'Writing and spelling primary outcome' in df['out_type_4'][counter]:
        Writing_and_spelling_prim.append(df['out_type_4'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_4'][counter])
        Writing_and_spelling_prim_se.append(df['se_4'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_5'][counter]:
        Writing_and_spelling_prim.append(df['out_type_5'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_5'][counter])
        Writing_and_spelling_prim_se.append(df['se_5'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_6'][counter]:
        Writing_and_spelling_prim.append(df['out_type_6'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_6'][counter])
        Writing_and_spelling_prim_se.append(df['se_6'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_7'][counter]:
        Writing_and_spelling_prim.append(df['out_type_7'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_7'][counter])
        Writing_and_spelling_prim_se.append(df['se_7'][counter])
    elif 'Writing and spelling primary outcome' in df['out_type_8'][counter]:
        Writing_and_spelling_prim.append(df['out_type_8'][counter])
        Writing_and_spelling_prim_smd.append(df['smd_8'][counter])
        Writing_and_spelling_prim_se.append(df['se_8'][counter])



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
    elif 'Mathematics primary outcome' in df['out_type_4'][counter]:
        Mathematics_prim.append(df['out_type_4'][counter])
        Mathematics_prim_smd.append(df['smd_4'][counter])
        Mathematics_prim_se.append(df['se_4'][counter])
    elif 'Mathematics primary outcome' in df['out_type_5'][counter]:
        Mathematics_prim.append(df['out_type_5'][counter])
        Mathematics_prim_smd.append(df['smd_5'][counter])
        Mathematics_prim_se.append(df['se_5'][counter])
    elif 'Mathematics primary outcome' in df['out_type_6'][counter]:
        Mathematics_prim.append(df['out_type_6'][counter])
        Mathematics_prim_smd.append(df['smd_6'][counter])
        Mathematics_prim_se.append(df['se_6'][counter])
    elif 'Mathematics primary outcome' in df['out_type_7'][counter]:
        Mathematics_prim.append(df['out_type_7'][counter])
        Mathematics_prim_smd.append(df['smd_7'][counter])
        Mathematics_prim_se.append(df['se_7'][counter])
    elif 'Mathematics primary outcome' in df['out_type_8'][counter]:
        Mathematics_prim.append(df['out_type_8'][counter])
        Mathematics_prim_smd.append(df['smd_8'][counter])
        Mathematics_prim_se.append(df['se_8'][counter])



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
    elif 'Science primary outcome' in df['out_type_4'][counter]:
        Science_prim.append(df['out_type_4'][counter])
        Science_prim_smd.append(df['smd_4'][counter])
        Science_prim_se.append(df['se_4'][counter])
    elif 'Science primary outcome' in df['out_type_5'][counter]:
        Science_prim.append(df['out_type_5'][counter])
        Science_prim_smd.append(df['smd_5'][counter])
        Science_prim_se.append(df['se_5'][counter])
    elif 'Science primary outcome' in df['out_type_6'][counter]:
        Science_prim.append(df['out_type_6'][counter])
        Science_prim_smd.append(df['smd_6'][counter])
        Science_prim_se.append(df['se_6'][counter])
    elif 'Science primary outcome' in df['out_type_7'][counter]:
        Science_prim.append(df['out_type_7'][counter])
        Science_prim_smd.append(df['smd_7'][counter])
        Science_prim_se.append(df['se_7'][counter])
    elif 'Science primary outcome' in df['out_type_8'][counter]:
        Science_prim.append(df['out_type_8'][counter])
        Science_prim_smd.append(df['smd_8'][counter])
        Science_prim_se.append(df['se_8'][counter])



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
    elif 'SES/FSM outcome' in df['out_type_4'][counter]:
        fsm_prim.append(df['out_type_4'][counter])
        fsm_prim_smd.append(df['smd_4'][counter])
        fsm_prim_se.append(df['se_4'][counter])
    elif 'SES/FSM outcome' in df['out_type_5'][counter]:
        fsm_prim.append(df['out_type_5'][counter])
        fsm_prim_smd.append(df['smd_5'][counter])
        fsm_prim_se.append(df['se_5'][counter])
    elif 'SES/FSM outcome' in df['out_type_6'][counter]:
        fsm_prim.append(df['out_type_6'][counter])
        fsm_prim_smd.append(df['smd_6'][counter])
        fsm_prim_se.append(df['se_6'][counter])
    elif 'SES/FSM outcome' in df['out_type_7'][counter]:
        fsm_prim.append(df['out_type_7'][counter])
        fsm_prim_smd.append(df['smd_7'][counter])
        fsm_prim_se.append(df['se_7'][counter])
    elif 'SES/FSM outcome' in df['out_type_8'][counter]:
        fsm_prim.append(df['out_type_8'][counter])
        fsm_prim_smd.append(df['smd_8'][counter])
        fsm_prim_se.append(df['se_8'][counter])



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

df_all_ml_SS = pd.concat([df_all, ml_ss_df], axis=1, sort=False)

# remove problematic text from outputs
df_all_ml_SS.replace('\r', ' ', regex=True, inplace=True)
df_all_ml_SS.replace('\n', ' ', regex=True, inplace=True)
df_all_ml_SS.replace(':', ' ',  regex=True, inplace=True)
df_all_ml_SS.replace(';', ' ',  regex=True, inplace=True)

# replace NaN with NA
df_all_ml_SS = df_all_ml_SS.replace('NaN', 'NA', regex=True)

# list column names and position
for counter, i in enumerate(df_all_ml_SS):
    print(counter, i)

# useful info
print("Columns:", df_all_ml_SS.shape[1])
print("Rows:", df_all_ml_SS.shape[0])
print("Datapoints:", df_all_ml_SS.shape[0] * df_all_ml_SS.shape[1])

# get file name for output
outfile_name = data_files.rsplit('/')[-1]
outfile_name = outfile_name.rsplit('.')[0]
outfile_name = outfile_name + "_Main_Analysis_SS.csv"

# write to disk
print("saving {}".format(outfile_name))
df_all_ml_SS.to_csv(outfile_name, index=False, header=True)

print(df_all_ml_SS)































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
