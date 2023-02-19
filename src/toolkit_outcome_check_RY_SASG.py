from eppi_ID import eppiid_df
from OutcomeType import outcometype_df
from Outcome import outcome_df
from OutcomeTitle import outcome_title_df
from smd import smd_df

import numpy as np
from toolz import interleave

import pandas as pd


from Author import author_df
from Date import year_df
from PublicationType import publicationtype_df
from AdminStrand import adminstrand_df

# [STANDARD] Outcome dataframes
from ToolkitStrand import toolkitstrand_df
from sesmd import sesmd_df
from Sample import sample_df
from OutcomeComparison import out_comp_df
from EffectSizeType import effectsizetype_df
from OutcomeMeasure import outcome_measure_df
from Outcome_TestType import testtype_df
from ToolkitStrand import toolkitstrand_df

# [STANDARD] general dataframes
from Country import country_df
from InterventionTrainingProvided import InterventionTrainingProvided_df
from InterventionTeachingApproach import InterventionTeachingApproach_df
from InterventionInclusion import DigitalTechnology_df
from InterventionInclusion import Parents_or_Community_Volunteers_df
from InterventionTime import InterventionTime_df
from InterventionDelivery import interventiondelivery_df
from InterventionDuration import InterventionDuration_Comments_df
from InterventionFrequency import InterventionFrequency_Comments_df
from InterventionSessionLength import InterventionSessionLength_Comments_df
from EducationalSetting import edusetting_df
from Age import student_age_df
from NumberofSchools import number_of_schools_total_Comments_df
from NumberofClasses import number_of_classes_total_Comments_df
from StudyDesign import studydesign_df
from SampleSize import sample_size_Comments_df
from ses_fsm import low_ses_percentage_Comments_df


record_details_df = pd.concat([
    eppiid_df,
    author_df,
    year_df,
    publicationtype_df
], axis=1)

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


""" all_variables = pd.concat([
    eppiid_df,
    outcometype_df,
    outcome_df,
    smd_df
], axis=1, sort=False) """

df = pd.concat([
    outcome_df,
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
    outcome_df,
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


# SUBSET OUTCOME 1 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_1 for 'Secondary outcome(s) label
conditions = [df["out_label_1"].str.startswith("Sec")]
choices = [True]
df["SEC_check_1"] = np.select(conditions, choices, default=False)

# remove out_label_1 based on out_label_1 boolean
df["out_label_1"].iloc[(df["SEC_check_1"] == False).values] = 'NA'

# remove out_tit_1 values based if out_label_1 are Primary outcomes
df["out_tit_1"].iloc[(df["SEC_check_1"] == False).values] = 'NA'

# remove smd values where out_tut_1 is not TE
df["smd_1"].iloc[(df["SEC_check_1"] == False).values] = 'NA' """


# check out_tit_1 for 'TE_SUB' or 'TE_PRI' prefix
conditions = [df["out_tit_1"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_1"] = np.select(conditions, choices, default=False)

# remove out_label_1 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# remove out_tit_1 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_1"].iloc[(df['TE_check_1'] == False).values] = 'NA'

# SUBSET OUTCOME 2 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_2 for 'Secondary outcome(s) label
conditions = [df["out_label_2"].str.startswith("Sec")]
choices = [True]
df["SEC_check_2"] = np.select(conditions, choices, default=False)

# remove out_label_2 based on out_label_2 boolean
df["out_label_2"].iloc[(df["SEC_check_2"] == False).values] = 'NA'

# remove out_tit_2 values based if out_label_2 are Primary outcomes
df["out_tit_2"].iloc[(df["SEC_check_2"] == False).values] = 'NA'

# remove smd values where out_tut_2 is not TE
df["smd_2"].iloc[(df["SEC_check_2"] == False).values] = 'NA' """


# check out_tit_2 for 'TE' prefix
conditions = [df["out_tit_2"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_2"] = np.select(conditions, choices, default=False)

# remove out_label_2 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# remove out_tit_2 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_2"].iloc[(df['TE_check_2'] == False).values] = 'NA'

# SUBSET OUTCOME 3 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_3 for 'Secondary outcome(s) label
conditions = [df["out_label_3"].str.startswith("Sec")]
choices = [True]
df["SEC_check_3"] = np.select(conditions, choices, default=False)

# remove out_label_3 based on out_label_3 boolean
df["out_label_3"].iloc[(df["SEC_check_3"] == False).values] = 'NA'

# remove out_tit_3 values based if out_label_3 are Primary outcomes
df["out_tit_3"].iloc[(df["SEC_check_3"] == False).values] = 'NA'

# remove smd values where out_tut_3 is not TE
df["smd_3"].iloc[(df["SEC_check_3"] == False).values] = 'NA' """

# check out_tit_3 for 'TE' prefix


conditions = [df["out_tit_3"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_3"] = np.select(conditions, choices, default=False)

# remove out_label_3 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# remove out_tit_3 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_3"].iloc[(df['TE_check_3'] == False).values] = 'NA'

# SUBSET OUTCOME 4 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_4 for 'Secondary outcome(s) label
conditions = [df["out_label_4"].str.startswith("Sec")]
choices = [True]
df["SEC_check_4"] = np.select(conditions, choices, default=False)

# remove out_label_4 based on out_label_4 boolean
df["out_label_4"].iloc[(df["SEC_check_4"] == False).values] = 'NA'

# remove out_tit_4 values based if out_label_3 are Primary outcomes
df["out_tit_4"].iloc[(df["SEC_check_4"] == False).values] = 'NA'

# remove smd values where out_tut_4 is not TE
df["smd_4"].iloc[(df["SEC_check_4"] == False).values] = 'NA' """


# check out_tit_4 for 'TE' prefix
conditions = [df["out_tit_4"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_4"] = np.select(conditions, choices, default=False)

# remove out_label_4 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'

# remove out_tit_4 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_4"].iloc[(df['TE_check_4'] == False).values] = 'NA'


# SUBSET OUTCOME 5 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_5 for 'Secondary outcome(s) label
conditions = [df["out_label_5"].str.startswith("Sec")]
choices = [True]
df["SEC_check_5"] = np.select(conditions, choices, default=False)

# remove out_label_5 based on out_label_5 boolean
df["out_label_5"].iloc[(df["SEC_check_5"] == False).values] = 'NA'

# remove out_tit_5 values based if out_label_3 are Primary outcomes
df["out_tit_5"].iloc[(df["SEC_check_5"] == False).values] = 'NA'

# remove smd values where out_tut_5 is not TE
df["smd_5"].iloc[(df["SEC_check_5"] == False).values] = 'NA' """


# check out_tit_5 for 'TE' prefix
conditions = [df["out_tit_5"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_5"] = np.select(conditions, choices, default=False)

# remove out_label_5 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# remove out_tit_5 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_5"].iloc[(df['TE_check_5'] == False).values] = 'NA'

# SUBSET OUTCOME 6 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_6 for 'Secondary outcome(s) label
conditions = [df["out_label_6"].str.startswith("Sec")]
choices = [True]
df["SEC_check_6"] = np.select(conditions, choices, default=False)

# remove out_label_6 based on out_label_6 boolean
df["out_label_6"].iloc[(df["SEC_check_6"] == False).values] = 'NA'

# remove out_tit_6 values based if out_label_3 are Primary outcomes
df["out_tit_6"].iloc[(df["SEC_check_6"] == False).values] = 'NA'

# remove smd values where out_tut_6 is not TE
df["smd_6"].iloc[(df["SEC_check_6"] == False).values] = 'NA' """


# check out_tit_6 for 'TE' prefix
conditions = [df["out_tit_6"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_6"] = np.select(conditions, choices, default=False)

# remove out_label_6 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# remove out_tit_6 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_6"].iloc[(df['TE_check_6'] == False).values] = 'NA'

# SUBSET OUTCOME 7 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_7 for 'Secondary outcome(s) label
conditions = [df["out_label_7"].str.startswith("Sec")]
choices = [True]
df["SEC_check_7"] = np.select(conditions, choices, default=False)

# remove out_label_7 based on out_label_7 boolean
df["out_label_7"].iloc[(df["SEC_check_7"] == False).values] = 'NA'

# remove out_tit_7 values based if out_label_3 are Primary outcomes
df["out_tit_7"].iloc[(df["SEC_check_7"] == False).values] = 'NA'

# remove smd values where out_tut_7 is not TE
df["smd_7"].iloc[(df["SEC_check_7"] == False).values] = 'NA' """


# check out_tit_7 for 'TE' prefix
conditions = [df["out_tit_7"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_7"] = np.select(conditions, choices, default=False)

# remove out_label_7 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# remove out_tit_7 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_7"].iloc[(df['TE_check_7'] == False).values] = 'NA'

# SUBSET OUTCOME 8 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_8 for 'Secondary outcome(s) label
conditions = [df["out_label_8"].str.startswith("Sec")]
choices = [True]
df["SEC_check_8"] = np.select(conditions, choices, default=False)

# remove out_label_8 based on out_label_8 boolean
df["out_label_8"].iloc[(df["SEC_check_8"] == False).values] = 'NA'

# remove out_tit_8 values based if out_label_3 are Primary outcomes
df["out_tit_8"].iloc[(df["SEC_check_8"] == False).values] = 'NA'

# remove smd values where out_tut_8 is not TE
df["smd_8"].iloc[(df["SEC_check_8"] == False).values] = 'NA' """


# check out_tit_8 for 'TE' prefix
conditions = [df["out_tit_8"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_8"] = np.select(conditions, choices, default=False)

# remove out_label_8 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'

# remove out_tit_8 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_8"].iloc[(df['TE_check_8'] == False).values] = 'NA'


# SUBSET OUTCOME 9 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_9 for 'Secondary outcome(s) label
conditions = [df["out_label_9"].str.startswith("Sec")]
choices = [True]
df["SEC_check_9"] = np.select(conditions, choices, default=False)

# remove out_label_9 based on out_label_9 boolean
df["out_label_9"].iloc[(df["SEC_check_9"] == False).values] = 'NA'

# remove out_tit_9 values based if out_label_3 are Primary outcomes
df["out_tit_9"].iloc[(df["SEC_check_9"] == False).values] = 'NA'

# remove smd values where out_tut_9 is not TE
df["smd_9"].iloc[(df["SEC_check_9"] == False).values] = 'NA' """


# check out_tit_9 for 'TE' prefix
conditions = [df["out_tit_9"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_9"] = np.select(conditions, choices, default=False)

# remove out_label_9 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# remove out_tit_9 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_9"].iloc[(df['TE_check_9'] == False).values] = 'NA'

# SUBSET OUTCOME 10 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_10 for 'Secondary outcome(s) label
conditions = [df["out_label_10"].str.startswith("Sec")]
choices = [True]
df["SEC_check_10"] = np.select(conditions, choices, default=False)

# remove out_label_10 based on out_label_10 boolean
df["out_label_10"].iloc[(df["SEC_check_10"] == False).values] = 'NA'

# remove out_tit_10 values based if out_label_3 are Primary outcomes
df["out_tit_10"].iloc[(df["SEC_check_10"] == False).values] = 'NA'

# remove smd values where out_tut_10 is not TE
df["smd_10"].iloc[(df["SEC_check_10"] == False).values] = 'NA' """


# check out_tit_10 for 'TE' prefix
conditions = [df["out_tit_10"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_10"] = np.select(conditions, choices, default=False)

# remove out_label_10 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# remove out_tit_10 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_10"].iloc[(df['TE_check_10'] == False).values] = 'NA'

# SUBSET OUTCOME 11 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_11 for 'Secondary outcome(s) label
conditions = [df["out_label_11"].str.startswith("Sec")]
choices = [True]
df["SEC_check_11"] = np.select(conditions, choices, default=False)

# remove out_label_11 based on out_label_11 boolean
df["out_label_11"].iloc[(df["SEC_check_11"] == False).values] = 'NA'

# remove out_tit_11 values based if out_label_3 are Primary outcomes
df["out_tit_11"].iloc[(df["SEC_check_11"] == False).values] = 'NA'

# remove smd values where out_tut_11 is not TE
df["smd_11"].iloc[(df["SEC_check_11"] == False).values] = 'NA' """


# check out_tit_11 for 'TE' prefix
conditions = [df["out_tit_11"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_11"] = np.select(conditions, choices, default=False)

# remove out_label_11 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'

# remove out_tit_11 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_11"].iloc[(df['TE_check_11'] == False).values] = 'NA'











# SUBSET OUTCOME 12 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_11 for 'Secondary outcome(s) label
conditions = [df["out_label_11"].str.startswith("Sec")]
choices = [True]
df["SEC_check_11"] = np.select(conditions, choices, default=False)

# remove out_label_11 based on out_label_11 boolean
df["out_label_11"].iloc[(df["SEC_check_11"] == False).values] = 'NA'

# remove out_tit_11 values based if out_label_3 are Primary outcomes
df["out_tit_11"].iloc[(df["SEC_check_11"] == False).values] = 'NA'

# remove smd values where out_tut_11 is not TE
df["smd_11"].iloc[(df["SEC_check_11"] == False).values] = 'NA' """


# check out_tit_11 for 'TE' prefix
conditions = [df["out_tit_12"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_12"] = np.select(conditions, choices, default=False)

# remove out_label_11 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_11"].iloc[(df['TE_check_12'] == False).values] = 'NA'

# remove out_tit_11 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_12"].iloc[(df['TE_check_12'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_12"].iloc[(df['TE_check_12'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_12"].iloc[(df['TE_check_12'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_12"].iloc[(df['TE_check_12'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_12"].iloc[(df['TE_check_12'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_12"].iloc[(df['TE_check_12'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_12"].iloc[(df['TE_check_12'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_12"].iloc[(df['TE_check_12'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_12"].iloc[(df['TE_check_12'] == False).values] = 'NA'


# SUBSET OUTCOME 12 BASED ON SECONDARY OUTCOMES AND TE OUTCOME TITLES

""" # check out_label_11 for 'Secondary outcome(s) label
conditions = [df["out_label_11"].str.startswith("Sec")]
choices = [True]
df["SEC_check_11"] = np.select(conditions, choices, default=False)

# remove out_label_11 based on out_label_11 boolean
df["out_label_11"].iloc[(df["SEC_check_11"] == False).values] = 'NA'

# remove out_tit_11 values based if out_label_3 are Primary outcomes
df["out_tit_11"].iloc[(df["SEC_check_11"] == False).values] = 'NA'

# remove smd values where out_tut_11 is not TE
df["smd_11"].iloc[(df["SEC_check_11"] == False).values] = 'NA' """


# check out_tit_13 for 'TE' prefix
conditions = [df["out_tit_13"].str.startswith(("SA", "SG"))]
choices = [True]
df["TE_check_13"] = np.select(conditions, choices, default=False)

# remove out_label_11 for 'TE_SUB' or 'TE_PRI' prefix
df["out_label_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'

# remove out_tit_11 for 'TE_SUB' or 'TE_PRI' prefix
df["out_tit_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'

# remove smd for 'TE_SUB' or 'TE_PRI' prefix
df["smd_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'

# remove se for 'TE_SUB' or 'TE_PRI' prefix
df["se_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'

# remove out_type for 'TE_SUB' or 'TE_PRI' prefix
df["out_type_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'

# remove out sample for 'TE_SUB' or 'TE_PRI' prefix
df["out_samp_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'

# remove out comp for 'TE_SUB' or 'TE_PRI' prefix
df["out_comp_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'

# remove out es type for 'TE_SUB' or 'TE_PRI' prefix
df["out_es_type_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'

# remove out measure type for 'TE_SUB' or 'TE_PRI' prefix
df["out_measure_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'

# remove out teset type raw for 'TE_SUB' or 'TE_PRI' prefix
df["out_test_type_raw_13"].iloc[(df['TE_check_13'] == False).values] = 'NA'










df_all = pd.concat([record_details_df, df, general_df], axis=1, sort=False)

""" print(df_all[0:10])

df_all.to_csv("toolkit_outcome_check_RY_SASG.csv", index=False, header=True) """
